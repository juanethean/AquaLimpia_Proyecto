# Proyecto de Análisis de Datos: AquaLimpia S.A.

## Descripción General
Este proyecto implementa un ecosistema analítico reproducible orientado al procesamiento de datos operativos y físico-químicos de las plantas de tratamiento de aguas residuales de AquaLimpia S.A. El propósito central es diagnosticar e identificar las causas subyacentes de los incumplimientos intermitentes en la Demanda Biológica de Oxígeno (DBO) del efluente, facilitando la toma de decisiones basada en evidencia.

## Estructura del Repositorio
La arquitectura del proyecto sigue un paradigma de separación modular para garantizar la integridad de los datos fuente:
* `data/`: Contiene el *dataset* original y estructurado de los registros históricos de las plantas (`dataset_set_A_aguas_residuales.xlsx`).
* `src/`: Almacena el código fuente en Python, incluyendo el archivo principal (`main.py`) y los módulos de funciones (`funciones.py`) para las rutinas de limpieza y cálculo de eficiencia.
* `outputs/`: Directorio de destino para los reportes automatizados en formato tabular (.csv) y el almacenamiento de las vistas del *dashboard*.

## Objetivos del Proyecto
* **Procesar** rigurosamente los datos operativos y ambientales mediante flujos ETL (Extracción, Transformación y Carga) estandarizados.
* **Generar** reportes segmentados y automatizados para auditar el cumplimiento normativo (Gestión Ambiental) y la eficiencia del proceso (Operaciones).
* **Visualizar** el rendimiento comparativo de las plantas mediante un *dashboard* interactivo para la detección temprana de anomalías en los caudales y la DBO.

## Proceso Analítico
1. **Ingesta y Limpieza:** Carga del archivo Excel y eliminación de registros anómalos o valores nulos.
2. **Cálculo de Métricas:** Computación de la tasa de remoción de la DBO utilizando las variables de entrada y salida, cruzadas con los caudales y el consumo energético en aireación.
3. **Segmentación:** División del *DataFrame* matriz en dos reportes funcionales específicos para cada área de la empresa.

## Resultados Obtenidos
* Despliegue de un **Dashboard Exploratorio** funcional que correlaciona gráficamente picos de caudal con caídas en la eficiencia del tratamiento biológico.
* **Reporte Operativo (.csv):** Consolida métricas de caudal, DBO, energía y lodos, permitiendo ajustar los regímenes de aireación.
* **Reporte Ambiental (.csv):** Certifica el estado de cumplimiento normativo (DBO de salida frente a los umbrales legales), proveyendo evidencia auditable para los entes reguladores.
