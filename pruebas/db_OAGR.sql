
CREATE SCHEMA IF NOT EXISTS `db_OAGR` DEFAULT CHARACTER SET utf8mb4 ;
USE `db_OAGR` ;
-- -----------------------------------------------------
-- Table `db_OAGR`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`admin` (
  `id` INT() PRIMARY KEY AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(10) NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`almacen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`almacen` (
  `id` INT() PRIMARY KEY AUTO_INCREMENT NOT NULL,
  `producto` VARCHAR(100) NOT NULL,
  `descripcion` VARCHAR(200) NULL DEFAULT NULL,
  `imagen` VARCHAR() NULL DEFAULT NULL,
  `cantidad` INT() NOT NULL,
  `precio` INT() NOT NULL);
-- -----------------------------------------------------
-- Table `db_OAGR`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_OAGR`.`cliente` (
  `id` INT() PRIMARY KEY  AUTO_INCREMENT NOT NULL,
  `nombre` VARCHAR(50) NOT NULL,
  `correo` VARCHAR(100) NOT NULL,
  `contra` VARCHAR(50) NOT NULL);

--admin predeterminado  
insert into admin(nombre, correo, contrasenia) values ('mayrin', 'mayrinreyes1707@gmail.com', '12345');

--Productos
