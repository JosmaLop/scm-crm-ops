-- 1. Creamos la base de datos
CREATE DATABASE IF NOT EXISTS crm_importaciones;
USE crm_importaciones;

-- 2. Creamos la tabla de Clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    perfil_uso VARCHAR(50) -- Ej: Gaming, Diseño, Oficina
);

-- 3. Creamos la tabla de Proveedores
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(100), -- Ej: Miami, La Paz
    contacto_principal VARCHAR(100)
);

-- 4. Creamos la tabla de Cotizaciones (Leads)
CREATE TABLE cotizaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    descripcion_equipo TEXT NOT NULL,
    estado VARCHAR(50) DEFAULT 'Pendiente', -- Pendiente, En Tránsito, Entregado
    precio_estimado DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- 5. Insertamos unos datos de prueba
INSERT INTO proveedores (nombre_empresa, ubicacion, contacto_principal) 
VALUES ('Tech Miami Wholesale', 'Miami, USA', 'John Doe');

INSERT INTO clientes (nombre_completo, telefono, email, perfil_uso) 
VALUES ('Carlos Perez', '71234567', 'carlos@email.com', 'Diseño');