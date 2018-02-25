# 表结构, 数据更新
mysql.data:
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/user.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/order.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/order_info.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/order_detail.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/book.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/address_info.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/account_refund.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/account_consume.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/account_prepay.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/account.sql
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/shopping_cart.sql

	mysql -f -h127.0.0.1 -P3306 -uroot < sql/mock_data.sql

mysql.rebuild:
	mysql -f -h127.0.0.1 -P3306 -uroot < sql/drop.sql

	make mysql.data
