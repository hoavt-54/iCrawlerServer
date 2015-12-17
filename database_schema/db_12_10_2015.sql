SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `iii_news_db` DEFAULT CHARACTER SET utf8 ;
USE `iii_news_db` ;

-- -----------------------------------------------------
-- Table `iii_news_db`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`categories` (
  `category_id` VARCHAR(20) NOT NULL,
  `category_name` VARCHAR(45) NOT NULL,
  `category_weight` FLOAT NULL DEFAULT '0',
  PRIMARY KEY (`category_id`),
  INDEX `category_index` (`category_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`sources`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`sources` (
  `source_id` VARCHAR(20) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `url` VARCHAR(45) NOT NULL,
  `reputation` FLOAT NULL DEFAULT '0',
  `avatar_url` VARCHAR(200) NULL DEFAULT NULL,
  `fb_page_id` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`source_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`articles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`articles` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `url` VARCHAR(2000) NOT NULL,
  `title` VARCHAR(255) NULL DEFAULT NULL,
  `facebook_id` VARCHAR(40) NULL DEFAULT NULL,
  `source_id` VARCHAR(20) NOT NULL,
  `category_id` VARCHAR(20) NULL DEFAULT NULL,
  `comment_count` INT(10) NULL DEFAULT '0',
  `share_count` INT(10) NULL DEFAULT '0',
  `like_count` INT(10) NULL DEFAULT '0',
  `hot_point` FLOAT NULL DEFAULT '0',
  `is_top_story_on_their_site` TINYINT(1) NULL DEFAULT '0',
  `is_on_home_page` TINYINT(1) NULL DEFAULT NULL,
  `updated_time` BIGINT(20) NULL DEFAULT NULL,
  `thumbnail_url` VARCHAR(300) NULL DEFAULT NULL,
  `short_description` VARCHAR(300) NULL DEFAULT NULL,
  `country` VARCHAR(10) NULL DEFAULT 'us',
  `facebook_plugin_id` VARCHAR(40) NULL DEFAULT NULL,
  `twitter_count` INT(10) NULL DEFAULT '0',
  `text_html` TEXT NULL DEFAULT NULL,
  `text` VARCHAR(10000) NULL DEFAULT NULL,
  `is_duplicated` TINYINT(1) NULL DEFAULT '0',
  `last_update_statistic` INT(11) NULL DEFAULT '0',
  `category_weight` FLOAT NULL DEFAULT '0',
  `reputation` FLOAT NULL DEFAULT '0',
  `normalized_title` VARCHAR(255) NULL DEFAULT NULL,
  `fb_thumbnail_id` VARCHAR(45) NULL DEFAULT NULL,
  `thumbnail_fb_urls` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `url_UNIQUE` (`url`(250) ASC),
  UNIQUE INDEX `fb_id_unix` (`facebook_plugin_id` ASC),
  INDEX `fk_articles_sources_idx` (`source_id` ASC),
  INDEX `fk_articles_categories1_idx` (`category_id` ASC),
  INDEX `con_index` (`country` ASC),
  INDEX `duplicated_content` (`is_duplicated` ASC),
  INDEX `updated_time_index` (`updated_time` ASC),
  CONSTRAINT `fk_articles_categories`
    FOREIGN KEY (`category_id`)
    REFERENCES `iii_news_db`.`categories` (`category_id`)
    ON DELETE SET NULL
    ON UPDATE SET NULL,
  CONSTRAINT `fk_articles_sources`
    FOREIGN KEY (`source_id`)
    REFERENCES `iii_news_db`.`sources` (`source_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2372496
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`comments` (
  `comment_id` VARCHAR(20) NOT NULL,
  `source_id` VARCHAR(10) NOT NULL,
  `article_id` INT(11) NOT NULL,
  `content` VARCHAR(5000) NULL DEFAULT NULL,
  `like_count` INT(11) NULL DEFAULT '0',
  `dislike_count` INT(11) NULL DEFAULT '0',
  `is_repliable` TINYINT(1) NULL DEFAULT '0',
  `datetime` BIGINT(20) NULL DEFAULT NULL,
  `insert_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_name` VARCHAR(100) NULL DEFAULT NULL,
  `user_avatar_url` VARCHAR(250) NULL DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  INDEX `fk_comments_sources1_idx` (`source_id` ASC),
  INDEX `fk_comments_articles1_idx` (`article_id` ASC),
  CONSTRAINT `fk_comments_articles1`
    FOREIGN KEY (`article_id`)
    REFERENCES `iii_news_db`.`articles` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_comments_sources1`
    FOREIGN KEY (`source_id`)
    REFERENCES `iii_news_db`.`sources` (`source_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`likes` (
  `user_id` INT(10) UNSIGNED NOT NULL,
  `article_id` INT(11) NOT NULL,
  `time` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `article_id`),
  INDEX `article_fk_idx` (`article_id` ASC),
  CONSTRAINT `article_fk`
    FOREIGN KEY (`article_id`)
    REFERENCES `iii_news_db`.`articles` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`users` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `fbId` VARCHAR(45) NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  `twitterId` VARCHAR(45) NULL DEFAULT NULL,
  `reg_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `user_email_index` (`email` ASC),
  INDEX `user_fbid_index` (`fbId` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 1191
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `iii_news_db`.`users2`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `iii_news_db`.`users2` (
  `id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `fbId` VARCHAR(45) NULL DEFAULT NULL,
  `name` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_email_index` (`email` ASC),
  INDEX `user_fbid_index` (`fbId` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
USE `iii_news_db`;

DELIMITER $$
USE `iii_news_db`$$
CREATE
DEFINER=`root`@`%`
TRIGGER `iii_news_db`.`update_reputation_category`
BEFORE INSERT ON `iii_news_db`.`articles`
FOR EACH ROW
BEGIN
		DECLARE source_reputation FLOAT;
        DECLARE cate_weight FLOAT;
        SET source_reputation = (SELECT reputation FROM iii_news_db.sources WHERE source_id = NEW.source_id LIMIT 1);
        SET cate_weight = (SELECT category_weight FROM iii_news_db.categories WHERE category_id = NEW.category_id LIMIT 1);
        SET NEW.reputation = source_reputation;        
        SET NEW.category_weight = cate_weight;
    END$$


DELIMITER ;
