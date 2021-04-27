-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: quiz
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `admin_user`
--

DROP TABLE IF EXISTS `admin_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_user` (
  `name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_user`
--

LOCK TABLES `admin_user` WRITE;
/*!40000 ALTER TABLE `admin_user` DISABLE KEYS */;
INSERT INTO `admin_user` VALUES ('Pallanti Asrith Vatsal','asrith','1234');
/*!40000 ALTER TABLE `admin_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assessment`
--

DROP TABLE IF EXISTS `assessment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assessment` (
  `question` varchar(500) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessment`
--

LOCK TABLES `assessment` WRITE;
/*!40000 ALTER TABLE `assessment` DISABLE KEYS */;
INSERT INTO `assessment` VALUES ('Which kind of fruit must have a large wedding ceremony with lots of people in attendance?','can\'t elope');
/*!40000 ALTER TABLE `assessment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mistakes`
--

DROP TABLE IF EXISTS `mistakes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mistakes` (
  `question` varchar(500) DEFAULT NULL,
  `given_answer` varchar(500) DEFAULT NULL,
  `correct_answer` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mistakes`
--

LOCK TABLES `mistakes` WRITE;
/*!40000 ALTER TABLE `mistakes` DISABLE KEYS */;
INSERT INTO `mistakes` VALUES ('who is the lt. governer of ladakh','r k mathur','rk mathur'),('who is the chief justice of india','justice sharad arvind bodbe','justice sharad arvind bobde'),('who is the founder of linux','denis richie','linus trovalds');
/*!40000 ALTER TABLE `mistakes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `question` varchar(500) NOT NULL,
  `answer` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`question`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES ('a','a'),('b','b'),('d','d'),('g','g'),('i','i'),('in which year sainik school kalikiri was founded','2014'),('j','j'),('l','l'),('n','n'),('o','o'),('p','p'),('q','q'),('r','r'),('s','s'),('u','u'),('v','v'),('what is the nearest star to earth','sun'),('who invented git','linus trovalds'),('who invented python','guido van rossum'),('who is  naval chief of staff of India','admiral karambir singh'),('who is the chief justice of india','justice sharad arvind bodbe'),('who is the current indian cricket team skipper','virat kohli'),('who is the first CDS of india','gen bipin rawat'),('who is the first indian women to join indian navy as a pilot','sub lt shivangi'),('who is the founder of linux','linus trovalds'),('who is the lt. governer of jammu and kashmir','g c murmu'),('who is the lt. governer of ladakh','r k mathur'),('x','x'),('y','y'),('z','z');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riddles`
--

DROP TABLE IF EXISTS `riddles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riddles` (
  `question` varchar(500) DEFAULT NULL,
  `answer` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riddles`
--

LOCK TABLES `riddles` WRITE;
/*!40000 ALTER TABLE `riddles` DISABLE KEYS */;
INSERT INTO `riddles` VALUES ('What 8 letter word can have consecutive letters taken out and still remain a word until only one letter is left?','starting'),('Born in an instant, I tell all stories. I can be lost, but I never die. What am I?','memories'),('123 = 0\n    4235 = 0\n    656 = 2\n    5390 = 2\n    8890 = 6\n    1001 = 2\n    19235 = 1\n    What is 123456789?','4'),('What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify greatness, while the entire world signifies a great woman.','heroine'),('What number has all its letters in alphabetical order when spelled out?','forty');
/*!40000 ALTER TABLE `riddles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_questions`
--

DROP TABLE IF EXISTS `user_questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_questions` (
  `question` varchar(500) CHARACTER SET latin1 NOT NULL,
  `answer` varchar(500) CHARACTER SET latin1 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_questions`
--

LOCK TABLES `user_questions` WRITE;
/*!40000 ALTER TABLE `user_questions` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-11 12:53:32
