# Preguntas de revisión y refutación sustentada

Selecciona lo que pueda cambiar la conclusión. No conviertas esta guía en un cuestionario obligatorio ni traslades al usuario comprobaciones que puedes realizar.

## Formular preguntas que permitan descubrir un error

| Riesgo | Pregunta comprobable |
| --- | --- |
| Complacencia o anclaje | ¿La evidencia justificaría el mismo juicio si el usuario defendiera lo contrario o la respuesta fuera de otro autor? |
| Afirmación ambigua | ¿Qué significa exactamente «mejor», «funciona» o «rentable» en este caso y frente a qué alternativa? |
| Supuesto oculto | ¿Qué condición tiene que cumplirse para que la conclusión sea válida y qué dato mostraría que falla? |
| Falsa autoridad | ¿Qué pasaje o resultado de la fuente respalda esta afirmación, con las mismas condiciones? |
| Fuentes repetidas | ¿Son observaciones independientes o todas repiten un mismo informe o dato? |
| Datos incompletos | ¿Cambian el resultado el denominador, el tamaño de muestra, los casos excluidos o la tasa de referencia? |
| Causalidad apresurada | ¿Qué explicación alternativa produciría el mismo resultado y qué observación las distinguiría? |
| Comparación injusta | ¿Se comparan las mismas funciones, costos totales, plazos, población y condiciones? |
| Transferencia indebida | ¿El resultado sigue siendo aplicable a esta fecha, versión, lugar o grupo? |
| Exceso de certeza | ¿Se ha demostrado la afirmación o solo es compatible con lo observado? |

Responde primero la pregunta factual con los datos pertinentes y después contrástala con la respuesta original. Si delegas una comprobación autorizada, proporciona la pregunta neutral y las fuentes necesarias; evita inducir el veredicto esperado. Esto reduce el anclaje, pero no garantiza independencia ni exactitud.

## Ajustar la revisión al caso

- **Negocio:** distingue interés declarado, intención de compra y compra observada. Comprueba ingresos frente a margen, costos omitidos, adquisición, retención y capacidad de operación solo si afectan la decisión. Una lista de interesados no demuestra rentabilidad.
- **Idea:** identifica para quién resuelve qué problema y qué alternativa utiliza hoy. Una idea novedosa no demuestra demanda; que exista competencia tampoco demuestra que vaya a fracasar. Busca una prueba pequeña que pueda cambiar la decisión.
- **Investigación:** contrasta la conclusión con el diseño, la medición, la muestra y la incertidumbre reportada. Separa asociación de causalidad y resultados exploratorios de confirmaciones. No infieras un efecto inexistente solo porque no se demostró uno.
- **Diagnóstico:** separa observación, hipótesis de causa y causa confirmada. Contrasta la explicación principal con una alternativa plausible y propone o realiza una comprobación que las diferencie. Respeta lo que las herramientas y el tipo de diagnóstico permiten concluir; no ejecutes intervenciones ajenas al alcance de revisión.

## Cómo sustentar «esta afirmación es falsa»

Para cada falsedad importante, conserva una cadena breve y comprobable:

1. **Afirmación delimitada:** qué frase o dato estás refutando y bajo qué condiciones.
2. **Evidencia obtenida:** documento original y ubicación, observación verificable, cálculo reproducible o contraejemplo válido.
3. **Contradicción:** por qué esa evidencia es incompatible con la afirmación, en lugar de simplemente no apoyarla.
4. **Corrección y alcance:** qué puede afirmarse ahora y qué parte de la conclusión original sigue siendo válida o incierta.

Para refutar una afirmación universal basta un contraejemplo dentro de su alcance. Un caso adverso aislado no refuta por sí solo una afirmación probabilística; comprueba la frecuencia, las condiciones y la incertidumbre pertinentes. Una predicción no se vuelve falsa por no haberse comprobado todavía; evalúa su fundamento y sus supuestos.

Una cita que no contiene el dato contradice la atribución a esa fuente, pero no necesariamente el dato en sí. Una página inaccesible no demuestra que una fuente sea inventada. No atribuyas intención de engañar a partir de un error factual.

**Ejemplo sintético:** «Pasar del 40 % al 52 % equivale a subir 12 % en términos relativos». Los valores difieren en 12 puntos porcentuales; el incremento relativo es `(52 − 40) / 40 = 0,30`, es decir, 30 %. Se refuta ese cálculo, sin inferir por ello la causa del cambio ni que todo el análisis sea incorrecto.

## Criterios de diseño y fuentes

Estas son adaptaciones prácticas para este skill; los estudios no prueban que este conjunto de instrucciones elimine errores o complacencia. Su eficacia debe comprobarse con casos de uso, incluyendo respuestas correctas y evidencia insuficiente.

- [Sharma y colaboradores, 2023: Towards Understanding Sycophancy in Language Models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models). Documenta respuestas que favorecen la postura del usuario frente a la exactitud. Motiva comprobar que el juicio no dependa de a quién se atribuye una afirmación.
- [Dhuliawala y colaboradores, ACL 2024: Chain-of-Verification](https://aclanthology.org/2024.findings-acl.212/). Estudia preguntas de verificación respondidas por separado antes de corregir una respuesta; motiva separar preguntas y comprobaciones de la conclusión inicial.
- [Kamoi y colaboradores, TACL 2024: When Can LLMs Actually Correct Their Own Mistakes?](https://aclanthology.org/2024.tacl-1.78/). Revisa límites de la autocorrección y condiciones donde ayuda la retroalimentación externa fiable; motiva buscar comprobaciones externas y declarar lo que no se verificó.
- [Dubois y colaboradores, 2026: Ask don't tell, versión 4](https://arxiv.org/abs/2602.23971v4). Este preprint encuentra reducciones de complacencia al reformular declaraciones como preguntas en sus experimentos. Motiva neutralizar la petición antes de evaluarla, sin prometer el mismo resultado en cualquier modelo o tarea.
