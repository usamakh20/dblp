-- MySQL dump 10.13  Distrib 8.0.18, for Linux (x86_64)
--
-- Host: localhost    Database: dblp
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `publication`
--

DROP TABLE IF EXISTS `publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(255) NOT NULL,
  `title` varchar(2000) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `type` int(11) DEFAULT NULL,
  `mdate` date DEFAULT NULL,
  `publtype` varchar(50) DEFAULT NULL,
  `rating` tinyint(4) DEFAULT NULL,
  `reviewid` int(11) DEFAULT NULL,
  `cdate` date DEFAULT NULL,
  `pages` varchar(1000) DEFAULT NULL,
  `volume` varchar(50) DEFAULT NULL,
  `number` varchar(50) DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  `url` varchar(300) DEFAULT NULL,
  `school` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `crossref` varchar(255) DEFAULT NULL,
  `isbn` varchar(45) DEFAULT NULL,
  `chapter` int(11) DEFAULT NULL,
  `series` varchar(255) DEFAULT NULL,
  `booktitle` varchar(1000) DEFAULT NULL,
  `journal_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Publication_1_idx` (`journal_id`),
  CONSTRAINT `fk_Publication_1` FOREIGN KEY (`journal_id`) REFERENCES `journal` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7136259 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-12 17:01:50
