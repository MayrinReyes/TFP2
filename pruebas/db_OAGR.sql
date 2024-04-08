
CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_OAGR` ;
-- -----------------------------------------------------
-- Table `db_OAGR`.`adminis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`adminis` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(50) NOT NULL);
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
  `nperson` int NOT NULL,
  `mesa` int NOT NULL,
   FOREIGN KEY (`id_cliente`) REFERENCES cliente(id));
   
-- -----------------------------------------------------
-- Table `db_OAGR`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`comentarios` (
  `id` INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `id_cliente` INT NOT NULL,
  `razon` VARCHAR(50) NOT NULL,
  `mensaje` VARCHAR(200) NOT NULL,
   FOREIGN KEY (`id_cliente`) REFERENCES cliente(id));
  
-- admin predeterminado  
insert into adminis(nombre, correo, contra) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');

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

insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Dorayaki', 'Postres', 'dorayaki.png', '234', '70');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Hanami Dango', 'Postres', 'hanami_dango.png', '564', '95');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mitarashi Dango', 'Postres', 'mitarashi_dango.png', '453', '85');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Mochis', 'Postres', 'mochis.png', '533', '60');

insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Hakata', 'Ramen', 'hakata.png', '676', '80');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Kyoto', 'Ramen', 'kyoto.png', '567', '70');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Sapporo', 'Ramen', 'sapporo.png', '645', '75');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Shio', 'Ramen', 'shio.png', '876', '90');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Tokyo', 'Ramen', 'tokyo.png', '545', '90');

insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Maki', 'Sushi', 'maki.png', '345', '80');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Nigiri', 'Sushi', 'nigiri.png', '564', '75');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Temaki', 'Sushi', 'temaki.png', '546', '50');
insert into almacen(producto, descripcion, imagen, cantidad, precio) values ('Uramaki', 'Sushi', 'uramaki.png', '265', '82');

insert into clientes (nombre, correo, contra, direccion, telefono) values ('alid',	'probanding@gmail.com',	'sepa si quedo bien',	'9878989034 5345',	'4494359680');
insert into clientes (nombre, correo, contra, direccion, telefono) values ('val', 'dkwoen@hotmail.com', 'ey eso', 'ttyfyjugb', '4495699410');
insert into reservas (id_cliente, hora, dia, nperson, mesa) values ('1', '10:00', '2024-04-17', '3', '5');
insert into comentarios (id_cliente, razon, mensaje) values ('1', 'prueba2', 'mensaje	');
insert into comentarios (id_cliente, razon, mensaje) values ('1', 'prueba', 'solo estoy probando que guarde mis comentarios');
insert into comentarios (id_cliente, razon, mensaje) values ('2', 'jala o no', 'me avente todo el disenio, falta la funcion');
insert into pedidos (id_cliente, id_producto, cantidad, total) values ('1', '1', '3', '60');