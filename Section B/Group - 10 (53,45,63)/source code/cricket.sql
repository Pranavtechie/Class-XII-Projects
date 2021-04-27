-- MySQL dump 10.13  Distrib 5.1.73, for Win32 (ia32)
--
-- Host: localhost    Database: cricket
-- ------------------------------------------------------
-- Server version	5.1.73-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `odibatsmen`
--

DROP TABLE IF EXISTS `odibatsmen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `odibatsmen` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `runsScored` int(11) DEFAULT NULL,
  `strikeRate` decimal(5,2) DEFAULT NULL,
  `average` decimal(5,2) DEFAULT NULL,
  `halfCenturies` int(11) DEFAULT NULL,
  `centuries` int(11) DEFAULT NULL,
  `highestScore` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `odibatsmen`
--

LOCK TABLES `odibatsmen` WRITE;
/*!40000 ALTER TABLE `odibatsmen` DISABLE KEYS */;
INSERT INTO `odibatsmen` VALUES ('aaron finch','17 nov 1986',119,4559,'89.50','40.35',24,15,153),('ab devilliers','12 dec 1987',307,7000,'136.85','47.99',84,28,184),('chris gayle','21 sep 1979',300,10480,'87.20','37.70',54,25,215),('david warner','27 oct 1986',116,4990,'95.56','45.36',20,17,179),('k l rahul','18 apr 1992',28,997,'80.48','40.60',5,4,111),('kane williamson','08 aug 1990',149,6133,'81.84','47.91',39,13,148),('m s dhoni','07 jul 1981',350,10773,'87.56','50.58',73,10,183),('rohit sharma','30 apr 1987',224,9115,'88.58','48.53',43,29,264),('sachin tendulkar','02 jun 1989',463,18426,'86.24','44.83',96,49,200),('shikhar dhawan','05 dec 1985',115,5688,'94.02','44.50',29,17,143),('steven smith','02 jun 1989',118,3810,'86.32','41.41',23,8,164),('virat kohli','05 nov 1988',245,11791,'93.21','60.31',57,43,183);
/*!40000 ALTER TABLE `odibatsmen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `odibowlers`
--

DROP TABLE IF EXISTS `odibowlers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `odibowlers` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `wicketsTaken` int(11) DEFAULT NULL,
  `economy` decimal(5,2) DEFAULT NULL,
  `5wicketsInAMatch` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `odibowlers`
--

LOCK TABLES `odibowlers` WRITE;
/*!40000 ALTER TABLE `odibowlers` DISABLE KEYS */;
INSERT INTO `odibowlers` VALUES ('bhuvaneshwar kumar','05 feb 1990',114,132,'5.02',1),('dale steyn','27 jun 1983',125,196,'4.88',3),('imran tahir','08 aug 1990',107,173,'4.65',3),('jasprit bumrah','06 dec 1993',61,104,'4.49',1),('lasith malinga','29 aug 1983',226,338,'5.35',8),('mitchell starc','30 jan 1990',85,172,'5.02',7),('mohammed shami','03 sep 1990',78,148,'5.48',1),('rangana herath','18 feb 1980',287,483,'5.43',12),('ravichandran ashwin','17 sep 1986',111,150,'4.92',0),('trent boult','22 jul 1989',89,164,'5.05',5),('yuzvendra chahal','23 jul 1990',58,85,'5.07',2);
/*!40000 ALTER TABLE `odibowlers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t20batsmen`
--

DROP TABLE IF EXISTS `t20batsmen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t20batsmen` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `runsScored` int(11) DEFAULT NULL,
  `strikeRate` decimal(5,2) DEFAULT NULL,
  `average` decimal(5,2) DEFAULT NULL,
  `halfCenturies` int(11) DEFAULT NULL,
  `centuries` int(11) DEFAULT NULL,
  `highestScore` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t20batsmen`
--

LOCK TABLES `t20batsmen` WRITE;
/*!40000 ALTER TABLE `t20batsmen` DISABLE KEYS */;
INSERT INTO `t20batsmen` VALUES ('aaron finch','17 nov 1986',58,1878,'156.50','38.33',11,2,172),('ab devilliers','12 dec 1987',81,2054,'141.56','46.88',25,0,83),('chris gayle','21 sep 1979',58,1627,'142.84','32.54',13,2,117),('david warner','27 oct 1986',76,2079,'140.85','30.57',15,1,100),('k l rahul','18 apr 1992',34,1192,'146.46','43.77',9,2,110),('kane williamson','08 aug 1990',57,1505,'121.57','31.35',9,0,73),('m s dhoni','07 jul 1981',98,1617,'126.13','37.60',2,0,56),('rohit sharma','30 apr 1987',104,2633,'138.32','32.11',19,4,118),('sachin tendulkar','02 jun 1989',1,10,'83.33','10.00',0,0,10),('shikhar dhawan','05 dec 1985',58,1592,'128.22','27.85',10,0,92),('steven smith','02 jun 1989',36,577,'128.79','27.48',4,0,90),('virat kohli','05 nov 1988',75,2753,'138.07','52.66',25,0,94);
/*!40000 ALTER TABLE `t20batsmen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t20bowlers`
--

DROP TABLE IF EXISTS `t20bowlers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t20bowlers` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `wicketsTaken` int(11) DEFAULT NULL,
  `economy` decimal(5,2) DEFAULT NULL,
  `5wicketsInAMatch` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t20bowlers`
--

LOCK TABLES `t20bowlers` WRITE;
/*!40000 ALTER TABLE `t20bowlers` DISABLE KEYS */;
INSERT INTO `t20bowlers` VALUES ('bhuvaneshwar kumar','05 feb 1990',43,41,'7.05',1),('dale steyn','27 jun 1983',44,61,'6.80',0),('imran tahir','08 aug 1990',38,63,'6.73',2),('jasprit bumrah','06 dec 1993',42,51,'6.72',0),('lasith malinga','29 aug 1983',79,106,'7.24',2),('mitchell starc','30 jan 1990',28,39,'6.74',0),('mohammed shami','03 sep 1990',8,10,'9.94',0),('rangana herath','18 feb 1980',58,67,'7.12',0),('ravichandran ashwin','17 sep 1986',46,52,'6.98',0),('trent boult','22 jul 1989',27,39,'8.64',0),('yuzvendra chahal','23 jul 1990',36,52,'8.11',1);
/*!40000 ALTER TABLE `t20bowlers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testbatsmen`
--

DROP TABLE IF EXISTS `testbatsmen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testbatsmen` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `runsScored` int(11) DEFAULT NULL,
  `strikeRate` decimal(5,2) DEFAULT NULL,
  `average` decimal(5,2) DEFAULT NULL,
  `halfCenturies` int(11) DEFAULT NULL,
  `centuries` int(11) DEFAULT NULL,
  `highestScore` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testbatsmen`
--

LOCK TABLES `testbatsmen` WRITE;
/*!40000 ALTER TABLE `testbatsmen` DISABLE KEYS */;
INSERT INTO `testbatsmen` VALUES ('aaron finch','17 nov 1986',5,278,'443.98','27.80',2,0,62),('ab devilliers','12 dec 1987',180,3000,'80.54','38.98',70,18,202),('chris gayle','21 sep 1979',103,7215,'60.28','42.19',37,15,333),('david warner','27 oct 1986',82,7009,'73.21','48.34',30,23,335),('k l rahul','18 apr 1992',36,2006,'56.46','34.59',11,5,199),('kane williamson','08 aug 1990',77,6370,'51.57','52.21',31,21,242),('m s dhoni','07 jul 1981',90,4876,'59.12','38.09',33,6,224),('rohit sharma','30 apr 1987',32,2141,'59.26','46.54',10,6,212),('sachin tendulkar','25 apr 1973',200,15921,'54.08','53.79',68,51,248),('shikhar dhawan','05 dec 1985',34,2315,'66.95','40.61',5,7,190),('steven smith','02 jun 1989',71,7072,'55.98','63.14',27,26,239),('virat kohli','05 nov 1988',88,7202,'57.81','54.98',22,27,254);
/*!40000 ALTER TABLE `testbatsmen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testbowlers`
--

DROP TABLE IF EXISTS `testbowlers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testbowlers` (
  `name` varchar(100) NOT NULL,
  `DOB` varchar(100) DEFAULT NULL,
  `matchesPlayed` int(11) DEFAULT NULL,
  `wicketsTaken` int(11) DEFAULT NULL,
  `economy` decimal(5,2) DEFAULT NULL,
  `5wicketsInAMatch` int(11) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testbowlers`
--

LOCK TABLES `testbowlers` WRITE;
/*!40000 ALTER TABLE `testbowlers` DISABLE KEYS */;
INSERT INTO `testbowlers` VALUES ('bhuvaneshwar kumar','05 feb 1990',21,63,'2.95',4),('dale steyn','27 jun 1983',93,439,'3.25',26),('imran tahir','27 mar 1979',20,57,'3.51',2),('jasprit bumrah','06 dec 1993',12,62,'2.54',5),('lasith malinga','29 aug 1983',30,101,'3.86',3),('mitchell starc','30 jan 1990',55,238,'3.37',13),('mohammed shami','03 sep 1990',47,175,'3.31',5),('rangana herath','18 feb 1980',400,870,'3.24',38),('ravichandran ashwin','17 sep 1986',70,362,'2.84',27),('trent boult','22 jul 1989',64,255,'2.98',8),('yuzvendra chahal','23 jul 1990',0,0,'0.00',0);
/*!40000 ALTER TABLE `testbowlers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-09 19:49:20
