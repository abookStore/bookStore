SET NAMES utf8;

CREATE DATABASE IF NOT EXISTS bookstore;

USE bookstore;

# user
INSERT IGNORE INTO `user` (`id`, `username`, `nickname`, `realname`, `password`, `question`, `answer`, `gender`, `mail`, `phone`, `qq`, `created_at`, `updated_at`)
VALUES
	(4, 'bs', 'guest', '132', 'pwd', 'none', 'none', '23', 'xxx@xxx.com', '12321321', '1231223222', '2018-02-17 04:56:56', '2018-02-27 15:26:08'),
	(5, 'bsw', 'guest', '132', 'pwd', 'none', 'none', '23', 'xxx@xxx.com', '1231232', '12312', '2018-02-17 04:56:56', '2018-02-27 15:26:09'),
	(6, 'bsw2', 'guest', '132', 'pwd', 'none', 'none', '23', 'xxx@xxx.com', '123123212', '12312', '2018-02-17 04:56:56', '2018-02-27 15:26:10'),
	(7, 'test01', '测试账号01', '测试员1', '123456', '哈哈哈', '哈哈哈', 'male', 'test@bwyj.com', '13921212121', '12345', '2018-02-25 05:26:06', '2018-02-25 05:26:06');

# order
INSERT IGNORE INTO `order` (`id`, `order_id`, `user_id`, `quantity`, `origin_cost`, `actual_cost`, `order_status`, `delivery_status`, `pay_status`, `created_at`, `updated_at`)
VALUES
	(1, 12, 4, 1, 22.00, 22.00, 1, 1, 1, '2018-01-22 10:44:01', '2018-02-18 03:57:43'),
	(2, 231, 4, 1, 231.00, 2312.00, 1, 1, 1, '2018-01-22 11:19:05', '2018-02-18 03:57:44'),
	(23, 2018022401354909970, 4, 5, 10.00, 10.00, 1, 0, 1, '2018-02-23 17:35:49', '2018-03-05 15:38:34'),
	(26, 2018022510123557049, 4, 1, 0.00, 0.00, 1, 1, 1, '2018-02-25 02:12:35', '2018-03-09 14:30:31'),
	(27, 2018022515021241657, 7, 2, 0.00, 0.00, 1, 0, 0, '2018-02-25 07:02:12', '2018-02-25 07:02:12'),
	(28, 2018022515293327143, 7, 1, 0.00, 0.00, 1, 0, 0, '2018-02-25 07:29:33', '2018-02-25 07:29:33'),
	(29, 2018022515335078984, 7, 1, 0.00, 0.00, 1, 0, 1, '2018-02-25 07:33:50', '2018-02-25 07:33:50');

# order_detail
INSERT IGNORE INTO `order_detail` (`id`, `order_id`, `book_id`, `book_name`, `isbn`, `origin_price`, `actual_price`, `discount`, `order_quantity`, `deliveried_quantity`, `supplier_id`, `warehouse`, `created_at`, `updated_at`)
VALUES
	(1, 12, 1, '诗经', 12312321, 12.00, 123.00, 2.00, 11, 2, 5, '北京1', '2018-01-23 15:57:56', '2018-02-28 15:52:13'),
	(2, 12, 2, '论语', 12311233, 1.00, 22.00, 3.00, 42, 21, 5, '北京2', '2018-01-23 15:58:18', '2018-02-28 15:52:15'),
	(14, 2018022401231992113, 1, '论语', 9203204223, 12.15, 9.72, 0.80, 4, 4, 4, '供货商1', '2018-02-23 17:23:19', '2018-03-06 14:42:49'),
	(15, 2018022401235357943, 2, '诗经', 9820302123, 0.00, 0.00, 0.80, 4, 0, 4, '供货商2', '2018-02-23 17:23:53', '2018-02-27 15:18:50'),
	(21, 2018022401354909970, 2, '诗经', 9820302123, 0.00, 0.00, 0.80, 4, 0, 5, '供货商2', '2018-02-23 17:35:49', '2018-02-28 15:52:19'),
	(24, 2018022510123557049, 2, '诗经', 9820302123, 0.00, 0.00, 0.80, 1, 0, 4, '供货商2', '2018-02-25 02:12:35', '2018-02-27 15:18:51'),
	(25, 2018022515021241657, 2, '诗经', 9820302123123, 0.00, 0.00, 1.00, 2, 0, 5, '供货商2', '2018-02-25 07:02:12', '2018-02-28 15:52:17'),
	(26, 2018022515293327143, 2, '诗经', 9820302123123, 0.00, 0.00, 1.00, 1, 0, 5, '供货商2', '2018-02-25 07:29:33', '2018-02-28 15:52:18'),
	(27, 2018022515335078984, 2, '诗经', 9820302123123, 0.00, 0.00, 1.00, 1, 0, 5, '供货商2', '2018-02-25 07:33:50', '2018-02-28 15:52:19');

# order_info
INSERT IGNORE INTO `order_info` (`id`, `order_id`, `consignee`, `address`, `phone`, `post_code`, `created_at`, `updated_at`)
VALUES
	(1, 12, '哈哈', '北京市通州区xxxxxxx', 12323231223, 102302, '2018-02-16 14:09:22', '2018-02-16 14:16:36'),
	(2, 2018022201095491341, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-21 17:09:54', '2018-02-21 17:09:54'),
	(4, 2018022401031775597, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:03:17', '2018-02-23 17:03:17'),
	(5, 2018022401094848122, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:09:48', '2018-02-23 17:09:48'),
	(6, 2018022401120254913, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:12:02', '2018-02-23 17:12:02'),
	(7, 2018022401215071954, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:21:50', '2018-02-23 17:21:50'),
	(8, 2018022401231992113, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:23:19', '2018-02-23 17:23:19'),
	(9, 2018022401235357943, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:23:53', '2018-02-23 17:23:53'),
	(10, 2018022401354909970, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-23 17:35:49', '2018-02-23 17:35:49'),
	(13, 2018022510123557049, '大雄', '北京市海淀五路居西四环北路102号', 13212312321, 100101, '2018-02-25 02:12:35', '2018-02-25 02:12:35'),
	(14, 2018022515021241657, '测试员1', '福建省厦门市', 123123, 200323, '2018-02-25 07:02:12', '2018-02-25 07:02:12'),
	(15, 2018022515293327143, '测试员1', '福建省厦门市', 123123, 200323, '2018-02-25 07:29:33', '2018-02-25 07:29:33'),
	(16, 2018022515335078984, '测试员1', '福建省厦门市', 123123, 200323, '2018-02-25 07:33:50', '2018-02-25 07:33:50');

# account
INSERT IGNORE INTO `account` (`id`, `user_id`, `balance`, `bonus_point`, `discount`, `created_at`, `updated_at`)
VALUES
	(1, 4, 14180.00, 0, 1.00, '2018-01-27 12:01:25', '2018-02-17 05:01:08'),
	(2, 5, 9680.00, 0, 1.00, '2018-02-15 14:32:18', '2018-02-17 05:01:26'),
	(3, 6, 0.00, 0, 1.00, '2018-02-15 15:38:04', '2018-02-16 14:20:26');

# account_comsume
INSERT IGNORE INTO `account_consume` (`id`, `user_id`, `amount`, `current_balance`, `day`, `month`, `created_at`, `updated_at`)
VALUES
	(1, 4, 200.000, 14180.000, 20180202, 201802, '2018-02-17 04:51:01', '2018-02-17 04:55:43'),
	(2, 4, 150.000, 14030.000, 20180203, 201802, '2018-02-17 04:54:01', '2018-02-17 04:57:16'),
	(3, 5, 320.000, 9680.000, 20180202, 201802, '2018-02-17 04:56:56', '2018-02-17 04:58:35');

# account_prepay
INSERT IGNORE INTO `account_prepay` (`id`, `user_id`, `amount`, `current_balance`, `day`, `month`, `created_at`, `updated_at`)
VALUES
	(1, 4, 10000.000, 10000.000, 20180201, 201802, '2018-02-17 04:52:49', '2018-02-17 04:53:11'),
	(2, 5, 10000.000, 10000.000, 20180201, 201802, '2018-02-17 04:53:28', '2018-02-17 04:53:40'),
	(3, 4, 4380.000, 14380.000, 0, 0, '2018-02-17 04:54:30', '2018-02-17 04:54:38');

# account_refund
INSERT IGNORE INTO `account_refund` (`id`, `user_id`, `amount`, `current_balance`, `day`, `month`, `created_at`, `updated_at`)
VALUES
	(1, 4, 150.000, 14180.000, 20180203, 201802, '2018-02-17 04:58:41', '2018-02-17 04:59:26');

# address_info
INSERT IGNORE INTO `address_info` (`id`, `user_id`, `name`, `address`, `post_code`, `phone`, `is_default`, `created_at`, `updated_at`)
VALUES
	(1, 4, '大雄', '北京市海淀五路居西四环北路102号', 100101, 13212312321, 1, '2018-02-16 14:09:58', '2018-02-16 14:14:10'),
	(2, 4, '胖虎', '北京市朝阳区', 100201, 13212312312, 0, '2018-02-16 14:14:37', '2018-02-16 14:14:58'),
	(3, 6, 'haha', '天津市滨海新区', 234230, 18922302033, 1, '2018-02-16 14:15:02', '2018-02-17 04:43:35');

# book
INSERT IGNORE INTO `book` (`id`, `name`, `author`, `press`, `isbn`, `supplier_id`, `supplier`, `discount`, `quantity`, `description`, `price`, `is_active`, `created_at`, `updated_at`)
VALUES
	(1, '论语', '周杰伦', '北京教育出版社', 9203204223123, 5, '供货商1', 1.00, 79, NULL, 12.15, 1, '2018-03-05 16:11:04', '2018-03-05 16:11:04'),
	(2, '诗经', '王力宏', '北京机械工业出版社', 9820302123123, 5, '供货商2', 1.00, 1, NULL, 0.00, 1, '2018-03-05 16:11:05', '2018-03-05 16:11:05'),
	(3, '进击的巨人', 'yyf', '中国国家出版社', 8920340303123, 4, '供货商1', 1.00, 0, NULL, 0.00, 0, '2018-03-05 16:11:06', '2018-03-05 16:11:06'),
	(4, '论语', '12', '123', 9203204223123, 4, '1212', 1.00, 0, NULL, 0.00, 1, '2018-03-05 16:11:06', '2018-03-05 16:11:06');

# admin
INSERT IGNORE INTO `admin` (`id`, `user_id`, `auth`, `created_at`, `updated_at`)
VALUES
	(1, 4, 1, '2018-03-07 14:19:22', '2018-03-07 14:19:22');

