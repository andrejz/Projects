class Item():
	def __init__(self, id_no, price, quantity):
		"""Does the initialization"""
		self.i = id_no
		self.p = price
		self.q = quantity
		

	def update_quant(self, quant, operation = "add"):
		"""Updates the amount in the inventory. Adds by default but can subtract as well"""
		if operation == "subtract":
			self.q = self.q - quant
		else:
			self.q += quant
			
	def update_price(self, price):
		"""Updates a price with a new price"""
		self.p = price
	
	def print_product(self):
		"""Prints a single product"""
		print "Product: " + str(self.name) + "\tPrice: " + str(self.p) + "\tQuantity: " + str(self.q)
		
		

class Inventory():
	def __init__(self):
		"""Initializes the class"""
		self.product_list = [] #List to hold all products
		
	def add(self, product):
		"""Adds a product to the product list"""
		self.product_list.append(product)
		
	def i_printout(self):
		"""Prints out a full inventory together with its total value"""
		value = 0
		for i in self.product_list:
			print "item no{0}, for {1} euro, {2} items in stock".format(i.i, i.p, i.q)
			value += i.q * i.p
		print "\nTotal value of the stock is {0} euro.\n".format(value)
		
if __name__ == '__main__':	
	umbrella = Item(3131, 43, 6)
	potato = Item(4148, 2, 867)
	glass = Item(297, 15, 32)

	total = Inventory()
	total.add(umbrella)
	total.add(potato)
	total.add(glass)

	total.i_printout()

	umbrella.update_quant(19)
	glass.update_price(11)
	total.i_printout()
