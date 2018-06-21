import unittest, sys, types

class TestTraceHiding(unittest.TestCase):

	def test_1_none(self):
		self.assertIsNone(sys.gettrace())
		self.assertIsNone(sys.gettrace(1337))

	def test_2_set_and_get(self):
		def foo(a,b,c):
			pass
		self.assertIsNone(sys.settrace(foo))
		self.assertIsNone(sys.gettrace())
		self.assertIsInstance(sys.gettrace(1337), types.FunctionType)

	def test_3_set_none_wo_magic(self):
		self.assertIsNone(sys.settrace(None))
		self.assertIsNone(sys.gettrace())
		self.assertIsInstance(sys.gettrace(1337), types.FunctionType)

	def test_4_set_none_with_magic(self):
		self.assertIsNone(sys.settrace(1337))
		self.assertIsNone(sys.gettrace())
		self.assertIsNone(sys.gettrace(1337))


if __name__ == '__main__':
    unittest.main(verbosity=2)

