/*
 Navicat Premium Dump SQL

 Source Server         : msyql
 Source Server Type    : MySQL
 Source Server Version : 80039 (8.0.39)
 Source Host           : localhost:3306
 Source Schema         : sakila

 Target Server Type    : MySQL
 Target Server Version : 80039 (8.0.39)
 File Encoding         : 65001

 Date: 13/12/2024 10:59:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for invoice
-- ----------------------------
DROP TABLE IF EXISTS `invoice`;
CREATE TABLE `invoice`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `invoice_code` bigint NULL DEFAULT NULL,
  `invoice_number` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `invoice_date` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `verification_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `buyer_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `buyer_tax_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password_zone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `tax_rate` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `tax_amount` decimal(10, 2) NULL DEFAULT NULL,
  `total_amount` decimal(10, 2) NULL DEFAULT NULL,
  `total_tax_amount` decimal(10, 2) NULL DEFAULT NULL,
  `seller_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `seller_tax_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `seller_address_phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `seller_bank_account` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `file_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 59 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of invoice
-- ----------------------------
INSERT INTO `invoice` VALUES (53, 51001700112, '30469015', '2020年12月23日', '02207 35144 10620 180', '四川三足科技有限公司', '91510903MA6260NF1E', '0377/2967554353352+854>+1799\n27<*+054/604<0157<8>36>92827\n-6*2/3>78/+<24714*7737992>1+', '3%', 0.57, 9.07, 19.60, '四川成渝高速公路股份有限公司成仁分公司', '91510000689919120D', '四川省成都市高新区科园2路10号航利研发中心2幢2单元12楼028-85525911', '中信银行高升路支行7411210182200180646', '../out/20241016140504_20201223__3/91510000689919120D_f3c17dea5202450daa1d6b293390644c.pdf');
INSERT INTO `invoice` VALUES (54, 51001700112, '99748157', '2020年12月23日', '14112 19741 26393 612', '四川三足科技有限公司', '91510903MA6260NF1E', '0385/6430*812*86*2>3741<6892\n/1>67>91+67027**>2246>12/-76\n708>255991-56*44>75+583453**', '3%', 0.17, 5.71, 5.88, '四川成南高速公路有限责任公司', '91510000709155317M', '成都市武侯区武侯祠大街180号028-84121625', '成都建设银行股份有限公司成都南郊支行51001875136050366310', '../out/20241016140504_20201223__3/91510000709155317M_05fc60ecab6343deb5d96fb6b94e61f4.pdf');
INSERT INTO `invoice` VALUES (55, 51001900212, '10023131', '2020年12月23日', '13869 62520 49101 473', '四川三足科技有限公司', '91510903MA6260NF1E', '0389-+6*89073><3<<0+10-><80>\n*4/9>76625138*<274//*3<*>7>8\n<3*5++2*/5<>492/06/48092481>', '3%', 0.28, 9.22, 9.50, '成都机场高速公路有限责任公司', '91510100633168022E', '四川省双流县西航港街道成都航空港机场高速公路收费站028-85963366', '建行成都西月城支行51001416139059600168', '../out/20241016140504_20201223__3/91510100633168022E_140d21c2dcd3468eaf56816d9190eb5e.pdf');
INSERT INTO `invoice` VALUES (56, 51001900212, '10023130', '2020年12月23日', '16777 61342 17939 496', '四川三足科技有限公司', '91510903MA6260NF1E', '03--8/556727/33/03161>7-+653\n</9<8*215-/9/62*7*/-811039/*\n//>-8-533*6*>-+872373<5///46', '3%', 0.28, 9.22, 9.50, '成都机场高速公路有限责任公司', '91510100633168022E', '四川省双流县西航港街道成都航空港机场高速公路收费站028-85963366', '建行成都西月城支行51001416139059600168', '../out/20241017140555_20201223__1/91510100633168022E_937083446ff948eba0b1f6a46a88ed52.pdf');
INSERT INTO `invoice` VALUES (57, 51001700112, '30161374', '2020年12月23日', '14073 14653 13521 967', '四川三足科技有限公司', '91510903MA6260NF1E', '033<743+*0-/</73+24122*0<553\n0>*<79<70>4-9<099/943-6-718+\n<4>+/+98048760+76-187<-6/2>*', '3%', 0.31, 0.39, 10.70, '四川成德南高速公路有限责任公司', '91510000689940624C', '四川省成都市武侯区二环路西一段90号四川高速大厦028-84921905', '中国建设银行股份有限公司成都双楠支行51001875436051505182', '../out/20241017140603_20201223__2/91510000689940624C_97ca15ecff3a4e9b853c62001dc0db55.pdf');
INSERT INTO `invoice` VALUES (58, 51001700112, '98778004', '2020年12月23日', '14255 62520 86354 833', '四川三足科技有限公司', '91510903MA6260NF1E', '0395*4+7264391/3*7894-90*>*<\n7*0/<98742508<11342/05+566<-\n-+9-83><<98/2079811430/-9*<7', '3%', 0.56, 8.66, 19.20, '四川成南高速公路有限责任公司', '91510000709155317M', '成都市武侯区武侯祠大街180号028-84121625', '成都建设银行股份有限公司成都南郊支行51001875136050366310', '../out/20241017140603_20201223__2/91510000709155317M_44308ed89a5c467e9ede236eb1efd8bc.pdf');

SET FOREIGN_KEY_CHECKS = 1;
