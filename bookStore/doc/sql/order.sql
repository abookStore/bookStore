CREATE TABLE `order` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `order_id` int(20) DEFAULT NULL COMMENT '订单编号',
  `user_id` int(11) DEFAULT NULL COMMENT '用户编号',
  `quantity` int(11) DEFAULT NULL COMMENT '数量',
  `origin_cost` decimal(11,2) DEFAULT NULL COMMENT '定价总费用',
  `actual_cost` decimal(11,2) DEFAULT NULL COMMENT '实际总费用',
  `order_status` int(5) DEFAULT NULL COMMENT '订单状态',
  `delivery_status` int(5) DEFAULT NULL COMMENT '发货状态',
  `pay_status` int(5) DEFAULT NULL COMMENT '付款状态',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_id` (`order_id`),
  KEY `created_at` (`created_at`),
  KEY `updated_at` (`updated_at`),
  KEY `order_id_2` (`order_id`),
  KEY `pay_status` (`pay_status`),
  KEY `delivery_status` (`delivery_status`),
  KEY `order_status` (`order_status`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;