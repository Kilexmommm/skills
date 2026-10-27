"""Validate portable skills and flag common private-data patterns without printing values."""

from pathlib import Path
import re
import subprocess
import sys

import yaml


PATTERNS = {
    "possible credential": re.compile(
        r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}"
        r"|sk-(?:proj-)?[A-Za-z0-9_-]{24,}|AKIA[A-Z0-9]{16}"
        r"|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)"
    ),
    "personal absolute path": re.compile(r"(?:/Users/|/home/|[A-Za-z]:\\Users\\)[\w.-]+"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b"),
}


def privacy_issues(content):
    issues = []
    for line_number, line in enumerate(content.splitlines(), 1):
        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(line):
                if label == "email" and match.group(1).lower() in {
                    "example.com", "example.org", "example.net"
                }:
                    continue
                issues.append(f"line {line_number}: {label}")
    return issues


def validate_skill(path):
    issues = []
    content = (path / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
    if not match:
        return ["missing or malformed YAML frontmatter"]
    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return ["invalid YAML frontmatter"]
    if not isinstance(metadata, dict):
        return ["frontmatter must be a mapping"]
    name = metadata.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        issues.append("invalid skill name")
    elif name != path.name:
        issues.append("name must match its directory")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        issues.append("description must contain 1–1024 characters")
    if re.search(r"\[TODO:|\[INSERT", content, re.I):
        issues.append("unfinished scaffold placeholder")
    ui_path = path / "agents" / "openai.yaml"
    if ui_path.exists():
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            interface = ui.get("interface", {}) if isinstance(ui, dict) else None
            if not isinstance(interface, dict):
                issues.append("UI metadata must be a mapping")
            else:
                short = interface.get("short_description")
                if short is not None and (not isinstance(short, str) or not 25 <= len(short) <= 64):
                    issues.append("UI short_description must contain 25–64 characters")
        except yaml.YAMLError:
            issues.append("invalid agents/openai.yaml")
    return issues


def main():
    root = Path(__file__).resolve().parents[1]
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root).decode().split("\0")
    skills = [root / item for item in tracked if item.endswith("/SKILL.md")]
    errors = []
    if not skills:
        errors.append("no tracked skills found")
    for skill in skills:
        for issue in validate_skill(skill.parent):
            errors.append(f"{skill.relative_to(root)}: {issue}")
    for item in filter(None, tracked):
        path = root / item
        if path.is_symlink():
            errors.append(f"{item}: symbolic link requires manual portability review")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"MANUAL REVIEW: {item} (binary file)")
            continue
        for issue in privacy_issues(content):
            errors.append(f"{item}: {issue}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(skills)} skills; tracked text checked for common private-data patterns.")
    print("Client names, identifying context, binaries and Git history still require manual review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
