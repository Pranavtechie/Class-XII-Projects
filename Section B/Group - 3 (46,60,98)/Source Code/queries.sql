-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: rough
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `125430668_trans`
--

DROP TABLE IF EXISTS `125430668_trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `125430668_trans` (
  `date` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `125430668_trans`
--

LOCK TABLES `125430668_trans` WRITE;
/*!40000 ALTER TABLE `125430668_trans` DISABLE KEYS */;
INSERT INTO `125430668_trans` VALUES ('2020-11-26','11:06:31',5000,'TRANSFERED TO YOUR ACCOUNT BY PRANAV'),('2020-11-28','11:01:46',20000,'TRANSFERED TO YOUR ACCOUNT BY PRANAV');
/*!40000 ALTER TABLE `125430668_trans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `874687473_trans`
--

DROP TABLE IF EXISTS `874687473_trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `874687473_trans` (
  `date` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `874687473_trans`
--

LOCK TABLES `874687473_trans` WRITE;
/*!40000 ALTER TABLE `874687473_trans` DISABLE KEYS */;
INSERT INTO `874687473_trans` VALUES ('2020-11-25','17:11:29',900000,'CREDITED TO YOURSELF'),('2020-11-26','10:27:43',3000,'DEBITED BY YOURSELF'),('2020-11-26','11:06:31',5000,'TRANSFERED FROM YOUR ACCOUNT TO PRUDHVI'),('2020-11-26','11:12:33',50000,'DEBITED BY YOURSELF'),('2020-11-28','11:01:46',20000,'TRANSFERED FROM YOUR ACCOUNT TO PRUDHVI'),('2020-11-28','11:02:13',100000,'CREDITED TO YOURSELF'),('2020-11-28','11:56:44',3000,'DEBITED BY YOURSELF'),('2020-11-28','11:57:12',3000,'CREDITED TO YOURSELF'),('2020-12-01','10:05:22',500000,'CREDITED BY BANK ON LOAN');
/*!40000 ALTER TABLE `874687473_trans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `977035007_trans`
--

DROP TABLE IF EXISTS `977035007_trans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `977035007_trans` (
  `date` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `977035007_trans`
--

LOCK TABLES `977035007_trans` WRITE;
/*!40000 ALTER TABLE `977035007_trans` DISABLE KEYS */;
/*!40000 ALTER TABLE `977035007_trans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_password`
--

DROP TABLE IF EXISTS `employee_password`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_password` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_password`
--

LOCK TABLES `employee_password` WRITE;
/*!40000 ALTER TABLE `employee_password` DISABLE KEYS */;
INSERT INTO `employee_password` VALUES ('pranav@1','letmeinbank2','pranav'),('prudhvi@1','letmeinbank','prudhvi'),('sandeep@1','letmeinbank1','sandeep');
/*!40000 ALTER TABLE `employee_password` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_code`
--

DROP TABLE IF EXISTS `loan_code`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_code` (
  `loan_code` varchar(5) NOT NULL,
  `rate` int DEFAULT NULL,
  `loan_name` varchar(50) NOT NULL,
  PRIMARY KEY (`loan_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_code`
--

LOCK TABLES `loan_code` WRITE;
/*!40000 ALTER TABLE `loan_code` DISABLE KEYS */;
INSERT INTO `loan_code` VALUES ('bs15',15,'BUSSINESS LOAN'),('hm10',10,'HOME LOAN'),('pl11',11,'PERSONAL LOAN'),('vc09',9,'VEHICLE LOAN');
/*!40000 ALTER TABLE `loan_code` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_details`
--

DROP TABLE IF EXISTS `loan_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_details` (
  `account_num` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `time` int DEFAULT NULL,
  `loan_name` varchar(20) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`account_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_details`
--

LOCK TABLES `loan_details` WRITE;
/*!40000 ALTER TABLE `loan_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_balance`
--

DROP TABLE IF EXISTS `user_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_balance` (
  `account_num` int NOT NULL,
  `balance` int DEFAULT NULL,
  PRIMARY KEY (`account_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_balance`
--

LOCK TABLES `user_balance` WRITE;
/*!40000 ALTER TABLE `user_balance` DISABLE KEYS */;
INSERT INTO `user_balance` VALUES (125430668,525000),(874687473,1427000),(977035007,500000);
/*!40000 ALTER TABLE `user_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_details` (
  `account_num` int NOT NULL,
  `username` varchar(10) NOT NULL,
  `MIDDLE_NAME` varchar(20) DEFAULT NULL,
  `date_opened` varchar(10) NOT NULL,
  `aadhar_num` varchar(12) NOT NULL,
  `pan_num` varchar(10) NOT NULL,
  `phone_num` varchar(10) NOT NULL,
  `address` varchar(300) NOT NULL,
  `SUR_NAME` varchar(20) DEFAULT NULL,
  `LAST_NAME` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`account_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
INSERT INTO `user_details` VALUES (125430668,'prudhvi@60','PRUDHVI','2020-11-26','385176092954','AAADA6754G','9444286710','SAINIK SCHOOL KALIKIRI, KALIKIRI, CHITOOR DIST, PIN - 517234','BYLLA','RAJ'),(874687473,'pranav@098','PRANAV','2020-11-25','123456789123','AAAAA1209N','8639129148','SAINIK SCHOOL KALIKIRI, KALIKIRI, CHITOOR DISTRICT, PIN - 517234','MAKKENA','SAI'),(977035007,'sandeep@46','SANDEEP','2020-11-26','389110347865','ASAAD8709C','9848621345','SAINIK SCHOOL KALIKIRI, KALIKIRI, CHITOOR DIST, PIN - 517234','GONTU','KUMAR');
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_password`
--

DROP TABLE IF EXISTS `user_password`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_password` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `account_num` int NOT NULL,
  PRIMARY KEY (`account_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_password`
--

LOCK TABLES `user_password` WRITE;
/*!40000 ALTER TABLE `user_password` DISABLE KEYS */;
INSERT INTO `user_password` VALUES ('prudhvi@60','enterbank','PRUDHVI',125430668),('pranav@098','letme','PRANAV',874687473),('sandeep@46','letme,in@bank','SANDEEP',977035007);
/*!40000 ALTER TABLE `user_password` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-02  9:19:37
