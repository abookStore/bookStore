SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE IF NOT EXISTS `order_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` bigint(20) NOT NULL COMMENT '订单id',
  `consignee` varchar(255) NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `address` varchar(255) DEFAULT NULL COMMENT '收货地址',
  `phone` bigint(20) DEFAULT NULL COMMENT '收货人联系电话',
  `post_code` int(11) DEFAULT NULL COMMENT '收货地址邮编',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;