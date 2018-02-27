SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE IF NOT EXISTS `book` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL DEFAULT '' COMMENT '书目名称',
  `author` varchar(11) DEFAULT '' COMMENT '作者',
  `press` varchar(11) DEFAULT '' COMMENT '出版社',
  `isbn` bigint(20) NOT NULL COMMENT 'ISBN编号',
  `supplier_id` int(11) DEFAULT NULL COMMENT '供货商编号',
  `supplier` varchar(50) DEFAULT NULL COMMENT '供货商',
  `quantity` int(11) NOT NULL DEFAULT '0' COMMENT '库存数量',
  `description` varchar(200) DEFAULT NULL COMMENT '简介',
  `price` decimal(11,2) NOT NULL DEFAULT '0.00' COMMENT '定价',
  `is_active` int(11) NOT NULL DEFAULT '1' COMMENT '是否使用中 1:使用中 0: 停止使用',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `ux_name` (`name`),
  KEY `idx_isbn` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;