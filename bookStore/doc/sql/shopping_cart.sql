SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE IF NOT EXISTS `shopping_cart` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL COMMENT '用户编号',
  `book_id` int(11) DEFAULT NULL COMMENT '书目id',
  `book_name` varchar(50) NOT NULL DEFAULT '' COMMENT '书目名称',
  `isbn` bigint(20) NOT NULL COMMENT 'ISBN编号',
  `supplier_id` int(11) NOT NULL COMMENT '供货商编号',
  `supplier` varchar(50) NOT NULL DEFAULT '' COMMENT '供货商',
  `origin_price` decimal(5,2) NOT NULL DEFAULT '0.00' COMMENT '定价',
  `actual_price` decimal(5,2) NOT NULL DEFAULT '0.00' COMMENT '实价',
  `total_price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '总价',
  `discount` decimal(5,2) NOT NULL DEFAULT '1.00' COMMENT '折扣',
  `order_quantity` int(5) NOT NULL DEFAULT '0' COMMENT '购买数',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`book_id`),
  UNIQUE KEY `uni_idx_shopping_cart` (`user_id`,`book_id`),
  KEY `idx_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;