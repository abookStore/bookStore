SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE IF NOT EXISTS `order_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `order_id` bigint(20) NOT NULL COMMENT '对应订单的id',
  `book_id` int(11) NOT NULL COMMENT '书目id',
  `book_name` varchar(255) NOT NULL DEFAULT '' COMMENT '书名',
  `isbn` bigint(20) NOT NULL COMMENT 'ISBN编号',
  `origin_price` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '定价',
  `actual_price` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '实价',
  `discount` decimal(5,2) NOT NULL DEFAULT '0.00' COMMENT '折扣',
  `order_quantity` int(5) NOT NULL DEFAULT '0' COMMENT '购买数',
  `deliveried_quantity` int(11) NOT NULL DEFAULT '0' COMMENT '配送数',
  `supplier_id` int(11) NOT NULL COMMENT '供货商编号',
  `warehouse` varchar(255) NOT NULL DEFAULT '' COMMENT '供货商',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;