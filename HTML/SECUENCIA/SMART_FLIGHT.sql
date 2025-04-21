-- ANTES DE EJECUTAR ESTE SCRIPT ES NECESARIO CREAR EL ESQUEMA
-- CREAR TABLA VUELO

CREATE TABLE vuelo (
    id_vuelo INT AUTO_INCREMENT,
    origen VARCHAR(45),
    destino VARCHAR(45),
    estado VARCHAR(45),
    tiempo_vuelo INT,
    avion VARCHAR(45),
    PRIMARY KEY (id_vuelo)
)