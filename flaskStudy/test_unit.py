import unittest
import json
from login import app


# 单元测试 login.py

class LoginTest(unittest.TestCase):
	"""构造单元测试案例"""

	def setUp(self):
		"""自动先执行"""
		# 设置flask工作在测试模式下，能详细反馈更多系统信息
		# app.config["TESTING"] = True
		app.testing = True

		# 使用flask提供的，创建web请求的客户端
		self.client = app.test_client()

	def test_empty_user_password(self):
		"""测试用户名密码不完整的情况"""

		# 模拟发送web请求
		ret = self.client.post("/login", data={})

		# ret是视图返回的响应对象，data属性是响应体的属性
		resp = ret.data

		# 因login视图返回的是json字符串，需转为字典
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 1)

	def test_wrong_user_password(self):
		"""测试用户名密码错误的情况"""

		# 模拟发送web请求
		ret = self.client.post("/login", data={"user_name": "incas", "password": "incas"})

		# ret是视图返回的响应对象，data属性是响应体的属性
		resp = ret.data

		# 因login视图返回的是json字符串，需转为字典
		resp = json.loads(resp)

		# 拿到返回值后进行断言测试
		self.assertIn("code", resp)
		self.assertEqual(resp["code"], 2)

	# def tearDown(self):
	# 	"""在所有test函数执行完后执行的善后清理操作"""
	# 	db.session.remove()  # 清理数据库连接操作
	# 	db.drop_all()   # 清空数据库操作


if __name__ == '__main__':
	unittest.main()
