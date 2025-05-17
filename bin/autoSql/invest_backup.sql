-- MySQL dump 10.13  Distrib 8.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: book_keeping
-- ------------------------------------------------------
-- Server version	8.2.0

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
-- Table structure for table `invest`
--

DROP TABLE IF EXISTS `invest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invest` (
  `vest_id` int NOT NULL AUTO_INCREMENT COMMENT '投资ID',
  `prd_channel` char(20) DEFAULT NULL COMMENT '产品购买渠道',
  `prd_name` char(80) DEFAULT NULL COMMENT '产品名称',
  `prd_rate` float(10,2) DEFAULT NULL COMMENT '产品预期收益',
  `prd_status` char(1) DEFAULT NULL COMMENT '产品状态（未赎回N,已赎回Y）',
  `buy_amt` float(10,2) DEFAULT NULL COMMENT '购买金额',
  `buy_date` date DEFAULT NULL COMMENT '购买日',
  `ma_date` date DEFAULT NULL COMMENT '到期日',
  `ac_date` date DEFAULT NULL COMMENT '会计日',
  `current_amt` float(10,2) DEFAULT NULL COMMENT '记账日总金额',
  `profit` float(10,2) DEFAULT NULL COMMENT '当前收益金额',
  `days` int DEFAULT NULL COMMENT '相差天数',
  `real_rate` float DEFAULT NULL COMMENT '真实年化',
  `isnew` char(1) DEFAULT NULL COMMENT '是否最新记录（Y,N）',
  `ts` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '时间戳',
  PRIMARY KEY (`vest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COMMENT='投资信息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invest`
--

LOCK TABLES `invest` WRITE;
/*!40000 ALTER TABLE `invest` DISABLE KEYS */;
INSERT INTO `invest` VALUES (1,'网商银行','信银理财安盈象固收精选日开25号（90天持有期）理财产品B',NULL,'N',30000.00,'2025-04-22','2025-07-22','2025-05-08',30032.40,32.40,16,2.46,'N','2025-05-17 08:00:03'),(2,'网商银行','信银理财安盈象固收精选日开25号（90天持有期）理财产品B',NULL,'N',30000.00,'2025-04-22','2025-07-22','2025-05-17',30053.01,53.01,25,2.58,'Y','2025-05-17 08:00:03'),(3,'网商银行','交银理财稳享固收精选日开25号（90天持有期）理财产品B',NULL,'N',20000.00,'2025-04-16','2025-07-16','2025-05-08',20019.14,19.14,22,1.59,'N','2025-05-17 08:19:21'),(4,'网商银行','信银理财安盈象固收稳健六个月持有期42号理财产品',NULL,'N',10000.00,'2025-04-16','2025-10-15','2025-05-08',10007.87,7.87,22,1.31,'N','2025-05-17 08:20:09'),(5,'网商银行','建信理财惠众（日申月赎）固收类产品（中旬）第1期',NULL,'N',10000.00,'2025-04-16','2025-05-14','2025-05-08',10016.32,16.32,22,2.71,'N','2025-05-17 08:20:22'),(6,'网商银行','交银理财稳享固收精选日开25号（90天持有期）理财产品B',NULL,'N',20000.00,'2025-04-16','2025-07-16','2025-05-17',20036.38,36.38,31,2.14,'Y','2025-05-17 08:19:21'),(7,'网商银行','信银理财安盈象固收稳健六个月持有期42号理财产品',NULL,'N',10000.00,'2025-04-16','2025-10-15','2025-05-17',10012.79,12.79,31,1.51,'Y','2025-05-17 08:20:09'),(8,'网商银行','建信理财惠众（日申月赎）固收类产品（中旬）第1期',NULL,'N',10000.00,'2025-04-16','2025-05-14','2025-05-17',10023.50,23.50,31,2.77,'Y','2025-05-17 08:20:22'),(9,'网商银行','平安理财新卓越指数增强日开180天持有1号固收类理财产品A',NULL,'N',20000.00,'2025-04-22','2025-10-20','2025-05-08',20013.80,13.80,16,1.57,'N','2025-05-17 08:22:06'),(10,'网商银行','平安理财新卓越指数增强日开180天持有1号固收类理财产品A',NULL,'N',20000.00,'2025-04-22','2025-10-20','2025-05-17',20029.57,29.57,25,2.16,'Y','2025-05-17 08:29:12');
/*!40000 ALTER TABLE `invest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-17 17:07:30
