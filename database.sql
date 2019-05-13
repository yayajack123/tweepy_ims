/*
SQLyog Ultimate v12.4.1 (64 bit)
MySQL - 10.1.35-MariaDB : Database - db_tweepy
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_tweepy` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_tweepy`;

/*Table structure for table `tb_chat` */

DROP TABLE IF EXISTS `tb_chat`;

CREATE TABLE `tb_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text_get` varchar(255) DEFAULT NULL,
  `text_send` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_chat` */

insert  into `tb_chat`(`id`,`text_get`,`text_send`) values 
(1,'halo','halo juga'),
(2,'hai','hai juga'),
(3,'selamat pagi','selamat pagi juga');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
