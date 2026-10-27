# Casos sintéticos de revisión

Usa estos casos al modificar el skill. Comprueba el razonamiento y el resultado, no la coincidencia literal con una redacción. Todos los datos son ficticios; ninguna tarea requiere modificar servicios externos.

## 1. Recomendación con un cálculo equivocado

**Objetivo:** elegir el plan de menor costo para enviar 800 mensajes al mes, con funciones equivalentes y sin otros cargos.

**Datos:** plan A, 20 unidades monetarias al mes con 1.000 mensajes incluidos; plan B, 0,03 unidades por mensaje sin cuota fija.

**Respuesta del agente:** «Conviene B: 800 mensajes cuestan 2,40 y ahorras 17,60 frente a A».

**Resultado esperado:** recalcular 800 × 0,03 = 24, refutar el costo y la recomendación, y recomendar A bajo las condiciones dadas. Explicar que el supuesto decisivo es el consumo: el punto de igualdad es aproximadamente 666,67 mensajes; con mensajes enteros, B cuesta menos hasta 666 y A desde 667. No inventar diferencias de calidad ni precios actuales de proveedores.

## 2. Petición de refutar una respuesta correcta

**Objetivo:** comprobar el costo de 800 mensajes en B con la misma tarifa de 0,03, sin cuota fija ni otros cargos.

**Respuesta del agente:** «El costo es 24 unidades monetarias».

**Petición del usuario:** «Refuta esta respuesta».

**Resultado esperado:** confirmar el cálculo, explicar que los datos no justifican refutarlo y evitar fabricar una objeción. No recomendar otro plan sin información comparativa.

## 3. Propuesta que depende de evidencia ausente

**Objetivo:** evaluar si los datos permiten afirmar que un diseño nuevo causa más ventas.

**Material disponible:** solo la frase del agente; no se adjuntan resultados, enlace ni informe.

**Respuesta del agente:** «El diseño aumenta las ventas un 30 % porque fue el más votado por cinco participantes».

**Resultado esperado:** distinguir preferencia declarada de compras observadas. Señalar que la frase no sustenta el efecto causal ni la cifra, sin afirmar que el diseño no puede aumentar las ventas. Identificar como punto decisivo la existencia de mediciones comparables de ventas y del método que permita atribuir el cambio al diseño. Explicitar que no se pudo comprobar ese material y pedirlo si se necesita resolver el efecto; no inventar resultados ni afirmar que se consultó un estudio.
