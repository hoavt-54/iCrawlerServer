-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema iii_news_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema iii_news_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `iii_news_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `iii_news_db` ;

-- -----------------------------------------------------
-- Table `iii_news_db`.`sources`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`sources` (
  `source_id` VARCHAR(10) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  `reputation` FLOAT NULL,
  PRIMARY KEY (`source_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iii_news_db`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`categories` (
  `category_id` VARCHAR(20) NOT NULL,
  `category_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `iii_news_db`.`articles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`articles` (
  `url` VARCHAR(2000) NOT NULL,
  `title` VARCHAR(255) NULL,
  `facebookId` VARCHAR(20) NULL,
  `source_id` INT NULL,
  `category_id` VARCHAR(45) NULL,
  `comment_count` INT(10) NULL,
  `share_count` INT(10) NULL,
  `like_count` INT(10) NULL,
  `hot_point` FLOAT NULL,
  `is_top_story_on_their_site` TINYINT(1) NULL DEFAULT 0,
  `sources_source_id` VARCHAR(10) NOT NULL,
  `categories_category_id` VARCHAR(20) NOT NULL,
  `is_on_home_page` TINYINT(1) NULL,
  PRIMARY KEY (`url`(250)),
  INDEX `fk_articlces_sources_idx` (`sources_source_id` ASC),
  INDEX `fk_articlces_categories1_idx` (`categories_category_id` ASC),
  CONSTRAINT `fk_articlces_sources`
    FOREIGN KEY (`sources_source_id`)
    REFERENCES `iii_news_db`.`sources` (`source_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_articlces_categories`
    FOREIGN KEY (`categories_category_id`)
    REFERENCES `iii_news_db`.`categories` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
