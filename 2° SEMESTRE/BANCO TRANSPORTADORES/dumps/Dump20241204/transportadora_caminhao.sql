-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: transportadora
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `caminhao`
--

DROP TABLE IF EXISTS `caminhao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `caminhao` (
  `placaminhao` int NOT NULL,
  `modelo` varchar(25) NOT NULL,
  `manutencao` int DEFAULT NULL,
  `custo` int DEFAULT NULL,
  `codmercadoria` int DEFAULT NULL,
  `codfuncionario` int DEFAULT NULL,
  PRIMARY KEY (`placaminhao`),
  KEY `codmercadoria` (`codmercadoria`),
  KEY `fk_codfuncionario` (`codfuncionario`),
  CONSTRAINT `caminhao_ibfk_1` FOREIGN KEY (`codmercadoria`) REFERENCES `mercadoria` (`codigo`),
  CONSTRAINT `fk_codfuncionario` FOREIGN KEY (`codfuncionario`) REFERENCES `funcionario` (`codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caminhao`
--

LOCK TABLES `caminhao` WRITE;
/*!40000 ALTER TABLE `caminhao` DISABLE KEYS */;
INSERT INTO `caminhao` VALUES (1234567,'Mercedes 1113',20000,1500,1001,NULL),(2345678,'Volkswagen 17-230',25000,2000,1002,NULL),(3456789,'Scania P 310',30000,2500,1003,NULL),(4567890,'Volvo FH 540',35000,3000,1004,NULL),(5678901,'MAN TGX 18.440',40000,3500,1005,NULL);
/*!40000 ALTER TABLE `caminhao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-04 15:19:24
