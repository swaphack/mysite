/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : webchat

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2017-05-24 17:34:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for shop_mommodity
-- ----------------------------
DROP TABLE IF EXISTS `shop_mommodity`;
CREATE TABLE `shop_mommodity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `price` decimal(11,2) NOT NULL,
  `num` int(11) NOT NULL,
  `detail` longtext NOT NULL,
  `piture` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shop_mommodity
-- ----------------------------
INSERT INTO `shop_mommodity` VALUES ('1', '水库', '100.00', '1', '存水', 'images/items/1.png');
INSERT INTO `shop_mommodity` VALUES ('2', '矿场', '10.00', '1', '生产矿石', 'images/items/1_4.png');
INSERT INTO `shop_mommodity` VALUES ('3', '商店', '100.00', '1', '购买和销售物品', 'images/items/1_25.png');
INSERT INTO `shop_mommodity` VALUES ('4', '铁匠铺', '100.00', '1', '生产装备', 'images/items/1_26.png');
