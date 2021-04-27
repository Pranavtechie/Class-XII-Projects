-- MySQL dump 10.13  Distrib 5.1.73, for Win32 (ia32)
--
-- Host: localhost    Database: shopie
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
-- Table structure for table `admin_users`
--

DROP TABLE IF EXISTS `admin_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin_users` (
  `name` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_users`
--

LOCK TABLES `admin_users` WRITE;
/*!40000 ALTER TABLE `admin_users` DISABLE KEYS */;
INSERT INTO `admin_users` VALUES ('Ranga Madhav','ranga','1234'),('Sandeep Masa','sandeep','1234'),('Vishnu Kumar','vishnu','1234'),('Anoop V S','anoop','1234');
/*!40000 ALTER TABLE `admin_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_request`
--

DROP TABLE IF EXISTS `customer_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `company` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_request`
--

LOCK TABLES `customer_request` WRITE;
/*!40000 ALTER TABLE `customer_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_users`
--

DROP TABLE IF EXISTS `customer_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_users` (
  `name` varchar(100) DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_users`
--

LOCK TABLES `customer_users` WRITE;
/*!40000 ALTER TABLE `customer_users` DISABLE KEYS */;
INSERT INTO `customer_users` VALUES ('sandeep','2020-09-26 04:28:57'),('sandeep','2020-09-26 05:37:00'),('sandeep','2020-09-26 05:39:37'),('sandeep','2020-09-26 05:40:57'),('sandeep','2020-09-26 05:41:40'),('sandeep','2020-09-26 05:43:26'),('sandeep','2020-09-26 06:35:32'),('sandeep','2020-09-26 06:38:55'),('sandeep','2020-09-26 06:39:51'),('ranga','2020-09-26 06:42:04'),('range','2020-09-26 06:43:12'),('ranga','2020-09-26 06:47:41'),('ranga','2020-09-26 06:54:05'),('ranga','2020-09-26 06:56:27'),('ranga','2020-09-26 07:02:42'),('vishnu','2020-09-26 07:07:13'),('ranga','2020-09-26 09:09:13'),('ranag','2020-09-26 09:10:09'),('suraj','2020-09-26 09:18:51'),('anurag','2020-09-26 09:20:57'),('customer','2020-09-26 09:32:36'),('c','2020-09-26 09:34:12'),('ranga','2020-09-27 10:50:45');
/*!40000 ALTER TABLE `customer_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direct_review`
--

DROP TABLE IF EXISTS `direct_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direct_review` (
  `name` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `mobile_review` varchar(1000) DEFAULT NULL,
  KEY `model` (`model`),
  CONSTRAINT `direct_review_ibfk_1` FOREIGN KEY (`model`) REFERENCES `phones` (`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direct_review`
--

LOCK TABLES `direct_review` WRITE;
/*!40000 ALTER TABLE `direct_review` DISABLE KEYS */;
INSERT INTO `direct_review` VALUES ('suraj','vivo V19','hi there i am the guy who is reviewing this product and this product is very good and I think this phones tops the budget list of the smartphones in the year of 2020');
/*!40000 ALTER TABLE `direct_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phones`
--

DROP TABLE IF EXISTS `phones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phones` (
  `company` varchar(100) DEFAULT NULL,
  `model` varchar(100) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `processor` varchar(100) DEFAULT NULL,
  `dimensions` varchar(100) DEFAULT NULL,
  `battery` varchar(100) DEFAULT NULL,
  `year` year(4) DEFAULT NULL,
  `camera` varchar(100) DEFAULT NULL,
  `special` varchar(100) DEFAULT NULL,
  `good_for` varchar(200) DEFAULT NULL,
  `display_spec` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `ram` varchar(100) DEFAULT NULL,
  `storage` int(4) DEFAULT NULL,
  PRIMARY KEY (`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phones`
--

LOCK TABLES `phones` WRITE;
/*!40000 ALTER TABLE `phones` DISABLE KEYS */;
INSERT INTO `phones` VALUES ('Samsung','Galaxy a10s',9700,'Samsung Exynos 7884','6.2 inches','4000mAh',2019,'13MP+2MP/8MP','Good battery','Budget phone','PLS TFT LCD','One UI 2.0','2',32),('Samsung','Galaxy m10s',8999,'Samsung Exynos 7884B','6.4 inches','4000mAh',2019,'13MP+5MP/8MP','Crisp display & good battery','Budget phone','AMOLED','One UI 2.0','3',32),('Samsung','Galaxy note 8',60000,'Samsung Exynos 8895','6.3 inches','3300mAh',2017,'12MP+12MP/8MP+2MP','Portrait mode&s pen','The most feature-rich android phone you can buy','Quad HD+ Super AMOLED','One UI 1.0','6',64),('Samsung','Galaxy note 9',63999,'Samsung Exynos 9810','6.4 inches','4000mAh',2018,'12MP+12MP/8MP+2MP','S pen and display','Headphone jack and iris scanner','Super AMOLED','One UI 2.0','6',128),('Samsung','Galaxy note10',73600,'Octa-Core Samsung Exynos 9825','6.3 inches','3500mAh',2019,'12MP+12MP+16MP/10MP','S pen ','Overall performer','Dynamic AMOLED','One UI 2.5','8',256),('Samsung','Galaxy s10',52999,'Samsung Exynos 9820','6.1 inches','4100mAh',2019,'12MP+12MP+16MP/10MP','Cam and performance','High quality optcs & overall performance','Dynamic AMOLED','One UI 2.1','8',128),('Samsung','Galaxy s10+',52999,'Samsung Exynos 9820','6.4 inches','4100mAh',2019,'12MP+12MP+16MP/10MP+8MP','Cam and performance','High quality optcs & overall performance','Dynamic AMOLED','One UI 2','8',128),('Samsung','Galaxy s10e',48500,'Samsung Exynos 9820','5.8 inches','3000mAh',2019,'12MP+16MP/10MP','Cam and performance','High quality optcs & overall performance','full-HD+Dynamic AMOLED','One UI 2','6',128),('Samsung','Galaxy s8',45990,'Samsung Exynos 8895','5.8 inches','3000mAh',2017,'12MP/8MP+2MP','Performance','Overall performer','OLED','One UI','4',64),('Samsung','Galaxy s8+',47900,'Samsung Exynos 8895','6.2 inches','3500mAh',2017,'12MP/8MP+2MP','Excellent display','It/\'s one of few phones so far to have been /\'Mobile HDR Premium/\' certified','Super AMOLED','One U','4',64),('Samsung','Galaxy s9',55999,'Samsung Exynos 9810','5.8 inches','3000mAh',2018,'12MP/8MP+2MP','Performance','Overall performer','Quad HD+ Super AMOLED','One UI 2.1','4',256),('Samsung','Galaxy s9+',55900,'Samsung Exynos 9810 SoC','6.2 inches','3500mAh',2018,'12MP+12MP/8MP+2MP','Performance','Solid specs & great screen','Quad HD+ Super AMOLED','One UI 2.1','6',128),('Apple','iPhone 11',66990,'Apple A13 Bionic (7 nm+)','6.1 inches','3110mAh',2019,'12MP+12MP/12MP','Powerful performer','Night mode for better low-light photography','Liquid Retina IPS LCD  & 16M colours','iOS 13 upgraded to iOS 14','4',64),('Apple','iPhone 11 Pro',99599,'Apple A13 Bionic (7 nm+)','5.8 inches','3046mAh',2019,'12MP+12MP+12MP/12MP','Good camera','Best-in-class photos and video from a variety of perspectives and good low light shots','Super Retina XDR OLED  & 16M colours','iOS 13 upgraded to iOS 14','4',64),('Apple','iPhone 11 Pro Max',99990,'Apple A13 Bionic (7 nm+)','6.5 inches','3969mAh',2019,'12MP+12MP+12MP/12MP','Good camera','Best in class photos and video from a variety of perspectives and good low light shots','Super Retina XDR OLED  & 16M colours','iOS 13 upgraded to iOS 14','4',64),('Apple','iPhone 7',29499,'Apple A10 Fusion (16 nm)','4.7 inches','1960mAh',2016,'12MP/7MP','Performance','Faster processors and improved water resistance implemented through a click-less haptic home button','Retina IPS LCD  & 16M colours','iOS 10.0.1 upgraded to iOS14','2',32),('Apple','iPhone 7 Plus',36999,'Apple A10 Fusion (16 nm)','5.5 inches','2900mAh',2016,'12MP+12MP/7MP','Performance','Faster processors and improved water resistance implemented through a click-less haptic home button','Retina IPS LCD  & 16M colours','iOS 10.0.1 upgraded to iOS14','3',32),('Apple','iPhone 8',38999,'Apple A11 Bionic (10 nm)','4.7 inches','1821mAh',2017,'12MP/7MP','Performance','Good product','Retina IPS LCD  & 16M colours','iOS 11 upgraded to iOS 14','2',128),('Apple','iPhone 8 Plus',41500,'Apple A11 Bionic (10 nm)','5.5 inches','2691mAh',2017,'12MP+12MP/7MP','Performance','Good product','Retina IPS LCD  & 16M colours','iOS 11 upgraded to iOS 14','3',64),('Apple','iPhone SE',37900,'Apple A13 Bionic (7 nm+)','4.7 inches','1821mAh',2020,'12MP/7MP','Performance','Best for portability.','Retina IPS LCD  & 16M colours','iOS 11 upgraded to iOS 14','3',64),('Apple','iPhone X',66990,'Apple A11 Bionic (10 nm)','5.8 inches','2716mAh',2017,'12MP+12MP/7MP','Performance ','Powerful performer','Super Retina OLED  & 16M colours','iOS 11.1.1 upgraded to iOS 14','3',64),('Apple','iPhone XR',49900,'Apple A12 Bionic (7 nm)','6.1 inches','2942mAh',2018,'12MP/7MP','Good for gaming','Best value iPhone','Liquid Retina IPS LCD  & 16M colours','iOS 12 upgraded to iOS 14','3',64),('Apple','iPhone XS',97900,'Apple A12 Bionic (7 nm)','5.8 inches','2658mAh',2018,'12MP+12MP/7MP','Performance','Powerful performer','Super Retina OLED  & 16M colours','iOS 12 upgraded to iOS 14','4',512),('Apple','iPhone XS Max',113900,'Apple A12 Bionic (7 nm)','6.5 inches','3174mAh',2018,'12MP+12MP/7MP','Performance','Powerful performer','Super Retina OLED  & 16M colours','iOS 12 upgraded to iOS 14','4',256),('OnePlus','OnePlus 6',34999,'Qualcomm  Snapdragon 845 (10nm)','6.28 inches','3300mAh',2018,'16MP+20MP/16MP','Performance','Overall performer','Optic AMOLED  & 16M colours','OxygenOS 10.3.1','6',64),('OnePlus','OnePlus 6T',27999,'Qualcomm  Snapdragon 845 (10nm)','6.41 inches','3700mAh',2018,'16MP+20MP/16MP','Performance',' One of the only phones with an android q beta available','Optic AMOLED  & 16M colours','OxygenOS 10.3.1','8',128),('OnePlus','OnePlus 7',27800,'Qualcomm  Snapdragon 855 (7nm)','6.41 inches','3700mAh',2019,'48MP+5MP/16MP','Performance','Overall performer and is still a flagship killer','Optic AMOLED  & 16M colours','OxygenOS 10.0.5','6',128),('OnePlus','OnePlus 7 Pro',39999,'Qualcomm Snapdragon 855 (7nm)','6.67 inches','4000mAh',2019,'48MP+8MP+16MP/16MP','Performance','Overall performance','Fluid AMOLED  & 16M colours','OxygenOS 10.0.5','6',128),('OnePlus','OnePlus 7T',37999,'Qualcomm Snapdragon 855+ (7nm)','6.55 inches','3800mAh',2019,'48MP+12MP+16MP/16MP','Good camera','Overall performance','Fluid AMOLED  & 16M colours','OxygenOS 10.0.7','8',256),('OnePlus','OnePlus 7T Pro',43999,'Qualcomm Snapdragon 855+ (7nm)','6.67 inches','4085mAh',2019,'48MP+8MP+16MP/16MP','Pop up selfie camera','Excellent display & good stereo sound','Fluid AMOLED  & 16M colours','OxygenOS 10.0.4 ','8',256),('OnePlus','OnePlus 8',41999,'Qualcomm Snapdragon 865+ (7nm)','6.55 inches','4300mAh',2020,'48MP+16MP+2MP/16MP','Overall performer ','Great display and a good enough battery life with 30w fast charging support','Fluid AMOLED  & 16M colours','OxygenOS 10.0','6',128),('OnePlus','OnePlus 8 Pro',54999,'Qualcomm Snapdragon 865 +(7nm)','6.78 inches','4510mAh',2020,'48MP+8MP+48MP+5MP/16MP','Camera','Overall performer','Fluid AMOLED  & 1B colours','OxygenOS 10.0','8',128),('OnePlus','OnePlus 8T',51700,'Qualcomm Snapdragon 865 +(7nm)','6.55 inches','4500mAh',2021,'48MP+16MP+5MP+2MP/32MP','Good camera','Overall performer','Fluid AMOLED  & 16M colours','OxygenOS 11','8',128),('OnePlus','OnePlus Nord',27999,'Qualcomm Snapdragon 765G (7nm)','6.44 inches','4115mAh',2020,'48MP+8MP+5MP+2MP/32MP+8MP','Overall performer ','Least among other and one of the best to go for it','Fluid AMOLED  & 16M colours','OxygenOS 10.5.4','8',128),('Realme','Realme 6',15000,'Media Tek Helio G90T','6.50 inches','4300mAh',2020,'64MP+8MP+2MP+2/16MP','perfo and camera','Good product','IPS LCD','Realme UI','4',64),('Realme','Realme 6 Pro ',17000,'Snapdragon 720G','6.60 inches ','4300mAh',2020,'64MP+8MP+12MP+2/16MP','camera and perfo','good camera and good product','IPS LCD','Realme UI','6',64),('Realme','Realme 6I',13000,'Media Tek Helio G90T','6.5 inches','4300mAh',2020,'48MP+8MP+2MP+2/17MP','camera','good perduct','IPS LCD','Realme UI','4',64),('Realme','Realme 7 ',17000,'Media Tek Helio G95','6.5 inches','5000mAh',2020,'64MP+8MP+2MP+2/16MP','perfo ','Good product','IPS LCD','Realme UI','6',128),('Realme','Realme 7 Pro',20000,'Snapdragon 720','6.4 inches','4500mAh',2020,'64MP+8MP+2MP+2/32MP','perfo ','Good product','Super AMOLED','Realme UI','6',128),('Realme','Realme C12',9000,'Media Tek Helio G35','6.52 inches','6000mAh',2020,'13MP+2MP+2/5MP','battery','budget phone and powerful battery','IPS LCD','Realme UI','3',32),('Realme','Realme Narzo 10',14000,'Media Tek Helio G80','6.5 inches','5000mAh',2020,'48MP+8MP+2MP+2/16MP','battery','powerful battery and good product','IPS LCD','Realme UI','4',128),('Realme','Realme X2 Pro',30000,'Snapdragon 855+','6.50 inches','4000mAh',2020,'64MP+13MP+8MP+2MP/16MP','perfo ','powerful performer','Super AMOLED','Realme UI','8',128),('Realme','Realme X3 Super Zoom',28000,'Snapdragon 855+','6.60 inches ','4200mAh',2020,'64MP+8MP+8MP+2/32MP+8MP','Good camera','overall performer and powerful processor','IPS LCD','Realme UI','12',256),('Realme','Realme X50PRO 5G',49000,'Snapdragon 865','6.44 inches','4200mAh',2020,'64MP+8MP+12MP+2/32MP+8MP','Good camera and perfo','powerful processor','Super AMOLED','Realme UI','6',128),('Redmi','Redmi K20 Pro',25000,'Snapdrogon 855','6.39 inches','4000mAh',2019,'48MP+13MP+8/20MP','camera','pop up camera','AMOLED','MIUI','8',128),('Redmi','Redmi Note 7 Pro',14000,'Snapdragon 675','6.30 inches','4000mAh',2019,'48MP+5/13MP','camera','good perduct','IPS LCD','MIUI','6',64),('Redmi','Redmi Note 7S',12000,'Snapdragon 660','6.3 inches','4000mAh',2019,'48MP+5/13MP','perfo','budget phone','IPS LCD','MIUI','3',32),('Redmi','Redmi Note 8 ',14000,'Snapdragon 665','6.3 inches','4000mAh',2019,'48MP+8MP+2MP+2/13MP','camera','Good product','IPS LCD','MIUI','4',64),('Redmi','Redmi Note 8 Pro',17000,'Media Tek Helio G90T','6.53 inches','4500mAh',2019,'68MP+8MP+2MP+2/20MP','camera','overall performer and camera','IPS LCD','MIUI','6',128),('Redmi','Redmi Note 9',15000,'Media Tek Helio G85','6.53 inches','5020mAh',2020,'48MP+8MP+2MP+2/13MP','perfo','overall performer','IPS LCD','MIUI','6',128),('Redmi','Redmi Note 9 Pro ',18500,'Snapdragon 720G','6.67 inches','5020mAh',2020,'48MP+8MP+5MP+2/16MP','screen and perfo','screen and good product','IPS LCD','MIUI','6',128),('Redmi','Redmi Note 9 Pro Max',20000,'Snapdragon 720G','6.67 inches','5020mAh',2020,'64MP+8MP+5MP+2/32MP','battery and screen','max screen and good product ','IPS LCD','MIUI','8',128),('Redmi','Redmi Poco X2 Pro',19000,'Snapdragon 730G','6.67 inches','4500mAh',2020,'64MP+18MP+2MP+2/20MP+2MP','good camera','large screen and good performer','IPS LCD','MIUI','8',128),('Redmi','Redmi10',47500,'Snapdragon 865','6.67 inches','4780mAh',2020,'108MP+13MP+2MP+2/20MP','Good camera and perfo','high processor and good product with overall features','AMOLED','MIUI','8',128),('Vivo','Vivo IQOO3',34990,'Snapdragon 865','6.44 inches','4440mAh',2020,'48MP+13MP+13MP+2/16MP','Good camera','Powerful performer','Super AMOLED','Fun Touch','8',128),('Vivo','Vivo S1 Pro',18500,'Snapdragon 665','6.38 inches','4500mAh',2020,'48MP+8MP+2MP+2/32MP','perfo ','Good camera','Super AMOLED','Fun Touch','8',128),('Vivo','Vivo V17 PRO',27700,'Snapdragon 675','6.44 inches','4100mAh',2020,'48MP+13MP+8MP+2/32MP+8MP','perfo ','good in low light photograps and wonderful camera','Super AMOLED','Fun Touch','8',128),('Vivo','vivo V19',24990,'Snapdragon 712','6.56 inches','4500mAh',2020,'48MP+8MP+8MP+2/32MP','Good camera','Good product','AMOLED','Fun Touch','8',128),('Vivo','Vivo Y11',9990,'Snapdragon 439','6.35 inches','5000mAh',2019,'13MP+2/8MP','perfo ','budget phone','IPS LCD','Fun Touch','4',64),('Vivo','Vivo Y15',12990,'Media Tek Helio P22','6.35 inches','5000mAh',2019,'13MP+8MP+2/16MP','perfo ','pop up camera','IPS LCD','Fun Touch','4',64),('Vivo','Vivo Y20',12990,'Snapdragon 460','6.51 inches','5000mAh',2020,'13MP+2MP+2/8MP','perfo ','budget phone','IPS LCD','Fun Touch','4',64),('Vivo','Vivo Y50',16990,'Snapdragon 665','6.53 inches','5000mAh',2020,'13MP+8MP+2MP+2/16MP','perfo ','powerful battery','IPS LCD','Fun Touch','8',128),('Vivo','Vivo Z1x',18490,'Snapdragon 713','6.38 inches','4500mAh',2020,'48MP+8MP+2/32MP','overall performer','pop up camera','Super AMOLED','Fun Touch','8',128),('Vivo','VivoX50',34990,'Snapdragon 730','6.56 inches','4200mAh',2020,'48MP+13MP+8MP+5/32MP','Good camera','Good product','AMOLED','Fun Touch','8',128);
/*!40000 ALTER TABLE `phones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phones_primary`
--

DROP TABLE IF EXISTS `phones_primary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phones_primary` (
  `company` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `battery` varchar(100) DEFAULT NULL,
  `camera` varchar(100) DEFAULT NULL,
  `ram` varchar(100) DEFAULT NULL,
  `os` varchar(100) DEFAULT NULL,
  `storage` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phones_primary`
--

LOCK TABLES `phones_primary` WRITE;
/*!40000 ALTER TABLE `phones_primary` DISABLE KEYS */;
INSERT INTO `phones_primary` VALUES ('Samsung','Galaxy a10s',9700,'4000mAh','13MP+2MP/8MP','2','One UI 2.0',32),('Samsung','Galaxy m10s',8999,'4000mAh','13MP+5MP/8MP','3','One UI 2.0',32),('Samsung','Galaxy note 8',60000,'3300mAh','12MP+12MP/8MP+2MP','6','One UI 1.0',64),('Samsung','Galaxy note 9',63999,'4000mAh','12MP+12MP/8MP+2MP','6','One UI 2.0',128),('Samsung','Galaxy note10',73600,'3500mAh','12MP+12MP+16MP/10MP','8','One UI 2.5',256),('Samsung','Galaxy s10',52999,'4100mAh','12MP+12MP+16MP/10MP','8','One UI 2.1',128),('Samsung','Galaxy s10+',52999,'4100mAh','12MP+12MP+16MP/10MP+8MP','8','One UI 2',128),('Samsung','Galaxy s10e',48500,'3000mAh','12MP+16MP/10MP','6','One UI 2',128),('Samsung','Galaxy s8',45990,'3000mAh','12MP/8MP+2MP','4','One UI',64),('Samsung','Galaxy s8+',47900,'3500mAh','12MP/8MP+2MP','4','One U',64),('Samsung','Galaxy s9',55999,'3000mAh','12MP/8MP+2MP','4','One UI 2.1',256),('Samsung','Galaxy s9+',55900,'3500mAh','12MP+12MP/8MP+2MP','6','One UI 2.1',128),('Apple','iPhone 11',66990,'3110mAh','12MP+12MP/12MP','4','iOS 13 upgraded to iOS 14',64),('Apple','iPhone 11 Pro',99599,'3046mAh','12MP+12MP+12MP/12MP','4','iOS 13 upgraded to iOS 14',64),('Apple','iPhone 11 Pro Max',99990,'3969mAh','12MP+12MP+12MP/12MP','4','iOS 13 upgraded to iOS 14',64),('Apple','iPhone 7',29499,'1960mAh','12MP/7MP','2','iOS 10.0.1 upgraded to iOS14',32),('Apple','iPhone 7 Plus',36999,'2900mAh','12MP+12MP/7MP','3','iOS 10.0.1 upgraded to iOS14',32),('Apple','iPhone 8',38999,'1821mAh','12MP/7MP','2','iOS 11 upgraded to iOS 14',128),('Apple','iPhone 8 Plus',41500,'2691mAh','12MP+12MP/7MP','3','iOS 11 upgraded to iOS 14',64),('Apple','iPhone SE',37900,'1821mAh','12MP/7MP','3','iOS 11 upgraded to iOS 14',64),('Apple','iPhone X',66990,'2716mAh','12MP+12MP/7MP','3','iOS 11.1.1 upgraded to iOS 14',64),('Apple','iPhone XR',49900,'2942mAh','12MP/7MP','3','iOS 12 upgraded to iOS 14',64),('Apple','iPhone XS',97900,'2658mAh','12MP+12MP/7MP','4','iOS 12 upgraded to iOS 14',512),('Apple','iPhone XS Max',113900,'3174mAh','12MP+12MP/7MP','4','iOS 12 upgraded to iOS 14',256),('OnePlus','OnePlus 6',34999,'3300mAh','16MP+20MP/16MP','6','OxygenOS 10.3.1',64),('OnePlus','OnePlus 6T',27999,'3700mAh','16MP+20MP/16MP','8','OxygenOS 10.3.1',128),('OnePlus','OnePlus 7',27800,'3700mAh','48MP+5MP/16MP','6','OxygenOS 10.0.5',128),('OnePlus','OnePlus 7 Pro',39999,'4000mAh','48MP+8MP+16MP/16MP','6','OxygenOS 10.0.5',128),('OnePlus','OnePlus 7T',37999,'3800mAh','48MP+12MP+16MP/16MP','8','OxygenOS 10.0.7',256),('OnePlus','OnePlus 7T Pro',43999,'4085mAh','48MP+8MP+16MP/16MP','8','OxygenOS 10.0.4 ',256),('OnePlus','OnePlus 8',41999,'4300mAh','48MP+16MP+2MP/16MP','6','OxygenOS 10.0',128),('OnePlus','OnePlus 8 Pro',54999,'4510mAh','48MP+8MP+48MP+5MP/16MP','8','OxygenOS 10.0',128),('OnePlus','OnePlus 8T',51700,'4500mAh','48MP+16MP+5MP+2MP/32MP','8','OxygenOS 11',128),('OnePlus','OnePlus Nord',27999,'4115mAh','48MP+8MP+5MP+2MP/32MP+8MP','8','OxygenOS 10.5.4',128),('Realme','Realme 6',15000,'4300mAh','64MP+8MP+2MP+2/16MP','4','Realme UI',64),('Realme','Realme 6 Pro ',17000,'4300mAh','64MP+8MP+12MP+2/16MP','6','Realme UI',64),('Realme','Realme 6I',13000,'4300mAh','48MP+8MP+2MP+2/17MP','4','Realme UI',64),('Realme','Realme 7 ',17000,'5000mAh','64MP+8MP+2MP+2/16MP','6','Realme UI',128),('Realme','Realme 7 Pro',20000,'4500mAh','64MP+8MP+2MP+2/32MP','6','Realme UI',128),('Realme','Realme C12',9000,'6000mAh','13MP+2MP+2/5MP','3','Realme UI',32),('Realme','Realme Narzo 10',14000,'5000mAh','48MP+8MP+2MP+2/16MP','4','Realme UI',128),('Realme','Realme X2 Pro',30000,'4000mAh','64MP+13MP+8MP+2MP/16MP','8','Realme UI',128),('Realme','Realme X3 Super Zoom',28000,'4200mAh','64MP+8MP+8MP+2/32MP+8MP','12','Realme UI',256),('Realme','Realme X50PRO 5G',49000,'4200mAh','64MP+8MP+12MP+2/32MP+8MP','6','Realme UI',128),('Redmi','Redmi K20 Pro',25000,'4000mAh','48MP+13MP+8/20MP','8','MIUI',128),('Redmi','Redmi Note 7 Pro',14000,'4000mAh','48MP+5/13MP','6','MIUI',64),('Redmi','Redmi Note 7S',12000,'4000mAh','48MP+5/13MP','3','MIUI',32),('Redmi','Redmi Note 8 ',14000,'4000mAh','48MP+8MP+2MP+2/13MP','4','MIUI',64),('Redmi','Redmi Note 8 Pro',17000,'4500mAh','68MP+8MP+2MP+2/20MP','6','MIUI',128),('Redmi','Redmi Note 9',15000,'5020mAh','48MP+8MP+2MP+2/13MP','6','MIUI',128),('Redmi','Redmi Note 9 Pro ',18500,'5020mAh','48MP+8MP+5MP+2/16MP','6','MIUI',128),('Redmi','Redmi Note 9 Pro Max',20000,'5020mAh','64MP+8MP+5MP+2/32MP','8','MIUI',128),('Redmi','Redmi Poco X2 Pro',19000,'4500mAh','64MP+18MP+2MP+2/20MP+2MP','8','MIUI',128),('Redmi','Redmi10',47500,'4780mAh','108MP+13MP+2MP+2/20MP','8','MIUI',128),('Vivo','Vivo IQOO3',34990,'4440mAh','48MP+13MP+13MP+2/16MP','8','Fun Touch',128),('Vivo','Vivo S1 Pro',18500,'4500mAh','48MP+8MP+2MP+2/32MP','8','Fun Touch',128),('Vivo','Vivo V17 PRO',27700,'4100mAh','48MP+13MP+8MP+2/32MP+8MP','8','Fun Touch',128),('Vivo','vivo V19',24990,'4500mAh','48MP+8MP+8MP+2/32MP','8','Fun Touch',128),('Vivo','Vivo Y11',9990,'5000mAh','13MP+2/8MP','4','Fun Touch',64),('Vivo','Vivo Y15',12990,'5000mAh','13MP+8MP+2/16MP','4','Fun Touch',64),('Vivo','Vivo Y20',12990,'5000mAh','13MP+2MP+2/8MP','4','Fun Touch',64),('Vivo','Vivo Y50',16990,'5000mAh','13MP+8MP+2MP+2/16MP','8','Fun Touch',128),('Vivo','Vivo Z1x',18490,'4500mAh','48MP+8MP+2/32MP','8','Fun Touch',128),('Vivo','VivoX50',34990,'4200mAh','48MP+13MP+8MP+5/32MP','8','Fun Touch',128);
/*!40000 ALTER TABLE `phones_primary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_review`
--

DROP TABLE IF EXISTS `purchase_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `purchase_review` (
  `model` varchar(100) DEFAULT NULL,
  `customer_name` varchar(100) DEFAULT NULL,
  `experience` varchar(1000) DEFAULT NULL,
  `mobile_review` varchar(1000) DEFAULT NULL,
  KEY `model` (`model`),
  CONSTRAINT `purchase_review_ibfk_1` FOREIGN KEY (`model`) REFERENCES `phones` (`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_review`
--

LOCK TABLES `purchase_review` WRITE;
/*!40000 ALTER TABLE `purchase_review` DISABLE KEYS */;
INSERT INTO `purchase_review` VALUES ('iPhone 11','ranga madhav','good','this is a great phone and very good to use '),('OnePlus 7 Pro','ranga','good','very good'),('VivoX50','shiva kumar','awesome','it is one of the best budget phones');
/*!40000 ALTER TABLE `purchase_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quantity`
--

DROP TABLE IF EXISTS `quantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quantity` (
  `company` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `quantity` int(3) DEFAULT NULL,
  KEY `model` (`model`),
  CONSTRAINT `quantity_ibfk_1` FOREIGN KEY (`model`) REFERENCES `phones` (`model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quantity`
--

LOCK TABLES `quantity` WRITE;
/*!40000 ALTER TABLE `quantity` DISABLE KEYS */;
INSERT INTO `quantity` VALUES ('Samsung','Galaxy a10s',10),('Samsung','Galaxy m10s',10),('Samsung','Galaxy note 8',10),('Samsung','Galaxy note 9',10),('Samsung','Galaxy note10',10),('Samsung','Galaxy s10',10),('Samsung','Galaxy s10+',10),('Samsung','Galaxy s10e',10),('Samsung','Galaxy s8',10),('Samsung','Galaxy s8+',10),('Samsung','Galaxy s9',10),('Samsung','Galaxy s9+',10),('Apple','iPhone 11',10),('Apple','iPhone 11 Pro',10),('Apple','iPhone 11 Pro Max',10),('Apple','iPhone 7',10),('Apple','iPhone 7 Plus',10),('Apple','iPhone 8',10),('Apple','iPhone 8 Plus',10),('Apple','iPhone SE',10),('Apple','iPhone X',10),('Apple','iPhone XR',10),('Apple','iPhone XS',10),('Apple','iPhone XS Max',10),('OnePlus','OnePlus 6',10),('OnePlus','OnePlus 6T',10),('OnePlus','OnePlus 7',10),('OnePlus','OnePlus 7 Pro',10),('OnePlus','OnePlus 7T',10),('OnePlus','OnePlus 7T Pro',10),('OnePlus','OnePlus 8',10),('OnePlus','OnePlus 8 Pro',10),('OnePlus','OnePlus 8T',10),('OnePlus','OnePlus Nord',10),('Realme','Realme 6',10),('Realme','Realme 6 Pro ',10),('Realme','Realme 6I',10),('Realme','Realme 7 ',10),('Realme','Realme 7 Pro',10),('Realme','Realme C12',10),('Realme','Realme Narzo 10',10),('Realme','Realme X2 Pro',10),('Realme','Realme X3 Super Zoom',10),('Realme','Realme X50PRO 5G',10),('Redmi','Redmi K20 Pro',10),('Redmi','Redmi Note 7 Pro',10),('Redmi','Redmi Note 7S',10),('Redmi','Redmi Note 8 ',10),('Redmi','Redmi Note 8 Pro',10),('Redmi','Redmi Note 9',10),('Redmi','Redmi Note 9 Pro ',10),('Redmi','Redmi Note 9 Pro Max',10),('Redmi','Redmi Poco X2 Pro',10),('Redmi','Redmi10',10),('Vivo','Vivo IQOO3',10),('Vivo','Vivo S1 Pro',10),('Vivo','Vivo V17 PRO',10),('Vivo','vivo V19',10),('Vivo','Vivo Y11',10),('Vivo','Vivo Y15',10),('Vivo','Vivo Y20',10),('Vivo','Vivo Y50',10),('Vivo','Vivo Z1x',10),('Vivo','VivoX50',10);
/*!40000 ALTER TABLE `quantity` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-27 22:22:20
