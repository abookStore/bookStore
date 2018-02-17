SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

CREATE TABLE IF NOT EXISTS `account_consume` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `user_id` int(11) NOT NULL COMMENT '用户id',
  `amount` decimal(10,3) NOT NULL DEFAULT '0.000' COMMENT '金额',
  `current_balance` decimal(11,3) NOT NULL DEFAULT '0.000' COMMENT '当前余额',
  `day` int(11) NOT NULL COMMENT '日期',
  `month` int(11) NOT NULL COMMENT '月份',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `day` (`day`),
  KEY `month` (`month`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;