-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dblp
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dblp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dblp` DEFAULT CHARACTER SET utf8 ;
USE `dblp` ;

-- -----------------------------------------------------
-- Table `dblp`.`authors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`authors` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `bibtex` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1274214
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dblp`.`journal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`journal` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1348
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dblp`.`publication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`publication` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `key` VARCHAR(255) NOT NULL,
  `title` VARCHAR(2000) NULL DEFAULT NULL,
  `address` VARCHAR(255) NULL DEFAULT NULL,
  `year` INT(11) NULL DEFAULT NULL,
  `type` INT(11) NULL DEFAULT NULL,
  `mdate` DATE NULL DEFAULT NULL,
  `publtype` VARCHAR(50) NULL DEFAULT NULL,
  `rating` TINYINT(4) NULL DEFAULT NULL,
  `reviewid` INT(11) NULL DEFAULT NULL,
  `cdate` DATE NULL DEFAULT NULL,
  `pages` VARCHAR(1000) NULL DEFAULT NULL,
  `volume` VARCHAR(50) NULL DEFAULT NULL,
  `number` VARCHAR(50) NULL DEFAULT NULL,
  `month` INT(11) NULL DEFAULT NULL,
  `url` VARCHAR(300) NULL DEFAULT NULL,
  `school` VARCHAR(255) NULL DEFAULT NULL,
  `publisher` VARCHAR(255) NULL DEFAULT NULL,
  `crossref` VARCHAR(255) NULL DEFAULT NULL,
  `isbn` VARCHAR(45) NULL DEFAULT NULL,
  `chapter` INT(11) NULL DEFAULT NULL,
  `series` VARCHAR(255) NULL DEFAULT NULL,
  `booktitle` VARCHAR(1000) NULL DEFAULT NULL,
  `journal_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Publication_1_idx` (`journal_id` ASC),
  CONSTRAINT `fk_Publication_1`
    FOREIGN KEY (`journal_id`)
    REFERENCES `dblp`.`journal` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1679424
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dblp`.`authors_publications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`authors_publications` (
  `author_id` INT(11) NOT NULL,
  `publ_id` INT(11) NOT NULL,
  PRIMARY KEY (`author_id`, `publ_id`),
  INDEX `fk_Authors_Publications_2_idx` (`publ_id` ASC),
  CONSTRAINT `fk_Authors_Publications_1`
    FOREIGN KEY (`author_id`)
    REFERENCES `dblp`.`authors` (`id`),
  CONSTRAINT `fk_Authors_Publications_2`
    FOREIGN KEY (`publ_id`)
    REFERENCES `dblp`.`publication` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dblp`.`cite`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`cite` (
  `publ_id` INT(11) NOT NULL,
  `cite_key` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`publ_id`, `cite_key`),
  CONSTRAINT `fk_Cite_1`
    FOREIGN KEY (`publ_id`)
    REFERENCES `dblp`.`publication` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dblp`.`ee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblp`.`ee` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(255) NULL DEFAULT NULL,
  `publ_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `publication_refrence_ee_idx` (`publ_id` ASC),
  CONSTRAINT `publication_refrence_ee`
    FOREIGN KEY (`publ_id`)
    REFERENCES `dblp`.`publication` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1945026
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
