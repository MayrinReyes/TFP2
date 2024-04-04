

CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_OAGR` ;
-- -----------------------------------------------------
-- Table `db_OAGR`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`admin` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(10) NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`almacen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`almacen` (
  `id` INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `producto` VARCHAR(100) NOT NULL,
  `descripcion` VARCHAR(200) DEFAULT NULL,
  `imagen` VARCHAR(100) DEFAULT NULL,
  `cantidad` INT NOT NULL,
  `precio` INT NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`cliente` (
  `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(100) DEFAULT NULL,
  `telefono` VARCHAR(10) DEFAULT NULL);


-- -----------------------------------------------------
-- Table `db_OAGR`.`pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`pedidos` (
  `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `id_cliente` INT NOT NULL,
  `id_producto` INT NOT NULL,
  `cantidad` VARCHAR(100) NOT NULL,
  `total` VARCHAR(50) NOT NULL,
   FOREIGN KEY (`id_cliente`) REFERENCES cliente(id),
   FOREIGN KEY (`id_producto`) REFERENCES almacen(id));
   


-- -----------------------------------------------------
-- Table `db_OAGR`.`reservas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`reservas` (
  `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `id_cliente` INT NOT NULL,
  `hora` time NOT NULL,
  `dia` date NOT NULL,
  `nperson` VARCHAR(100) NOT NULL,
  `mesa` VARCHAR(50) NOT NULL,
   FOREIGN KEY (`id_cliente`) REFERENCES cliente(id));
 
-- admin predeterminado  
insert into admin(nombre, correo, contra) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');


-- Productos
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Agua', 'Bebidas', 'agua.png', '409', '20');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Boba', 'Bebidas', 'boba.png', '209', '30');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Coca', 'Bebidas', 'coca.png', '312', '20');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Frappe', 'Bebidas', 'frappe.png', '123', '30');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Limon', 'Bebidas', 'jugo_limon.png', '123', '25');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Naranja', 'Bebidas', 'jugo_naranja.png', '42', '25');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Jugo de Toronja', 'Bebidas', 'jugo_toronja.png', '34', '25');


insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Bombon', 'Cafe', 'bombon.png', '893', '40');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Capuchino', 'Cafe', 'capuchino.png', '213', '35');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Carajillo', 'Cafe', 'carajillo.png', '423', '30');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Cafe con Leche', 'Cafe', 'con_leche.png', '123', '30');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Espresso', 'Cafe', 'espresso.png', '124', '40');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Irlandes', 'Cafe', 'irlandes.png', '121', '45');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Latte Macchiato', 'Cafe', 'latte_macchiato.png', '321', '50');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Lungo', 'Cafe', 'lungo.png', '324', '45');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Macchiato', 'Cafe', 'macchiato.png', '145', '34');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mocca', 'Cafe', 'mocca.png', '221', '40');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Ristretto', 'Cafe', 'ristretto.png', '342', '55');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Vienes', 'Cafe', 'vienes.png', '532', '50');


insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Dorayaki', 'Comida', 'dorayaki.png', '234', '70');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Hanami Dango', 'Comida', 'hanami_dango.png', '564', '95');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Maki', 'Comida', 'maki.png', '345', '80');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mitarashi Dango', 'Comida', 'mitarashi_dango.png', '453', '85');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mochis', 'Comida', 'mochis.png', '533', '60');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Nigiri', 'Comida', 'nigiri.png', '564', '75');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Ramen', 'Comida', 'ramen.png', '676', '80');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Temaki', 'Comida', 'temaki.png', '546', '50');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Uramaki', 'Comida', 'uramaki.png', '265', '82');
