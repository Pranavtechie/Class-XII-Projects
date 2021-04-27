-- MySQL dump 10.13  Distrib 5.1.73, for Win32 (ia32)
--
-- Host: localhost    Database: hospital_management
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
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor` (
  `Slno` varchar(30) NOT NULL,
  `Doctor_Name` varchar(30) DEFAULT NULL,
  `Doctor_ID` varchar(30) DEFAULT NULL,
  `Sex` varchar(30) DEFAULT NULL,
  `Age` varchar(30) DEFAULT NULL,
  `Department` varchar(30) DEFAULT NULL,
  `Available_Days` varchar(30) DEFAULT NULL,
  `Salary` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('1','RAJGOPAL VERMA','12005','M','48','VIROLOGY','ALL DAYS','80000');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inpatient_management`
--

DROP TABLE IF EXISTS `inpatient_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inpatient_management` (
  `Slno` varchar(30) NOT NULL,
  `Patient_Name` varchar(30) DEFAULT NULL,
  `Patient_ID` varchar(30) DEFAULT NULL,
  `Sex` varchar(30) DEFAULT NULL,
  `Age` varchar(30) DEFAULT NULL,
  `Illness` varchar(30) DEFAULT NULL,
  `Consulting_Doctor` varchar(30) DEFAULT NULL,
  `Room_No` varchar(30) DEFAULT NULL,
  `Date_of_Admission` varchar(30) DEFAULT NULL,
  `Payment` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inpatient_management`
--

LOCK TABLES `inpatient_management` WRITE;
/*!40000 ALTER TABLE `inpatient_management` DISABLE KEYS */;
INSERT INTO `inpatient_management` VALUES ('1','abhishek','13003','m','18','fever','ram','23','2021-03-15','12000'),('2','DINKAR','0031','M','18','CORONA','RAMGOPAL VERMA','31','2020-12-13','1200'),('ryh','truy','yrjy','yhujy','yj','','yjuy','yruj','yuj','yyuj'),('yguy','yti','yt','ytjiu','yj','gyj','gyju','ygj','gfyj','jy');
/*!40000 ALTER TABLE `inpatient_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `medicine` (
  `Slno` int(10) NOT NULL,
  `Medicine_ID` int(10) DEFAULT NULL,
  `Medicine_Name` varchar(30) DEFAULT NULL,
  `Cost` int(6) DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (1,1,'bandage',50);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outpatient_management`
--

DROP TABLE IF EXISTS `outpatient_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outpatient_management` (
  `Slno` varchar(30) NOT NULL,
  `Patient_Name` varchar(30) DEFAULT NULL,
  `PatientID` varchar(30) DEFAULT NULL,
  `Sex` varchar(30) DEFAULT NULL,
  `Age` varchar(30) DEFAULT NULL,
  `Illness` varchar(30) DEFAULT NULL,
  `Date_of_Visiting` varchar(30) DEFAULT NULL,
  `Payment` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Slno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outpatient_management`
--

LOCK TABLES `outpatient_management` WRITE;
/*!40000 ALTER TABLE `outpatient_management` DISABLE KEYS */;
INSERT INTO `outpatient_management` VALUES ('rey','truy','rtgujh','ryjuy','yj','jfyhf','yjf','yj'),('tyiuyt','tuki','uk','uk','ghki','yuk','yuki','kj');
/*!40000 ALTER TABLE `outpatient_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay`
--

DROP TABLE IF EXISTS `pay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pay` (
  `Slno` varchar(30) DEFAULT NULL,
  `Patient_ID` varchar(30) DEFAULT NULL,
  `Patient_Name` varchar(30) DEFAULT NULL,
  `Room_Rent` varchar(30) DEFAULT NULL,
  `Scanning_Bill` varchar(30) DEFAULT NULL,
  `Medicine_Charges` varchar(30) DEFAULT NULL,
  `Other_Payments` varchar(30) DEFAULT NULL,
  `Total_Payments` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay`
--

LOCK TABLES `pay` WRITE;
/*!40000 ALTER TABLE `pay` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-13 17:43:53
