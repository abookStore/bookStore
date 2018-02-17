SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE `address_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '收货人姓名',
  `address` varchar(255) NOT NULL DEFAULT '' COMMENT '收货地址',
  `post_code` int(11) NOT NULL COMMENT '邮编',
  `phone` bigint(20) NOT NULL COMMENT '联系电话',
  `is_default` int(11) NOT NULL COMMENT '是否默认地址 1: 是 0: 否',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_uid` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;