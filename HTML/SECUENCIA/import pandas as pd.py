import pandas as pd

# Crear una tabla extendida con 10 actividades del EDT, duración estimada, horas y roles
data = [
    # Fase de Planificación
    ["1", "Reunión de Inicio (Kick Off)", "Preparar presentación del caso", 1, 4, "Jefe de Proyecto"],
    ["1", "Reunión de Inicio (Kick Off)", "Reunión con stakeholders", 1, 2, "Jefe de Proyecto"],
    ["2", "Acta de Constitución", "Definir alcance del proyecto", 1, 4, "Jefe de Proyecto"],
    ["2", "Acta de Constitución", "Redactar y aprobar el acta", 1, 4, "Jefe de Proyecto"],
    ["3", "Análisis del Sistema Actual", "Revisión de arquitectura monolítica", 2, 8, "Arquitecto de Software"],
    ["3", "Análisis del Sistema Actual", "Identificación de problemas", 2, 6, "Arquitecto de Software"],
    # Fase de Análisis y Diseño
    ["4", "Diseño de Arquitectura Propuesta", "Definir microservicios", 3, 12, "Arquitecto de Software"],
    ["4", "Diseño de Arquitectura Propuesta", "Diseñar APIs y flujos", 3, 10, "Arquitecto de Software"],
    ["5", "Propuesta de Requisitos de Software", "Redactar ERS", 2, 8, "Analista de Sistemas"],
    ["5", "Propuesta de Requisitos de Software", "Validar ERS con cliente", 1, 3, "Jefe de Proyecto"],
]

# Crear el DataFrame
df = pd.DataFrame(data, columns=["Nº", "Actividad", "Subactividad", "Duración (días)", "Horas estimadas", "Rol Responsable"])
df
