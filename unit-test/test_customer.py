import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

	def setUp(self):
		self.customer_1 = Customer('Emem', 'Etim', 3000)
		self.customer_2 = Customer('Nancy', 'Rufus', 5000)

	def test_customer_mail(self):
		self.assertEqual(self.customer_1.customer_mail, 'Emem.Etim@email.com')
		self.assertEqual(self.customer_2.customer_mail, 'Nancy.Rufus@email.com')

	def test_customer_fullname(self):
		self.assertEqual(self.customer_1.customer_fullname, 'Emem Etim')
		self.assertEqual(self.customer_2.customer_fullname, 'Nancy Rufus')

	def test_apply_discount(self):
		self.customer_1.apply_discount()
		self.customer_2.apply_discount()

		self.assertEqual(self.customer_1.purchase, 2850)
		self.assertEqual(self.customer_2.purchase, 4750)

if __name__ == '__main__':
	unittest.main()
