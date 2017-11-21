class descriptiveItem(object):
	def __init__(self,name,price,quantity):
		self.name = name
		self.price = price
		self.quantity = quantity

milk = descriptiveItem('Milk','1.50','3')
soda = descriptiveItem('Sprite','1.25','2')
fish = descriptiveItem('Salmon','4.25','1')
paper = descriptiveItem('Brawny','10.50','1')
napkins = descriptiveItem('Vanity Fair','1','5')
plate = descriptiveItem('Dixie','1.50','4')
chicken = descriptiveItem('Tyson','9.50','1')
beef = descriptiveItem('National Beef','4.25','2')
sugar = descriptiveItem('Domino Sugar','1.50','1')
salt = descriptiveItem('Morton','1.50','1')
pepper = descriptiveItem('McCormick','1','1')
honey = descriptiveItem('Busy Bee','2.50','1')


class groceryStore(object):
	def __init__(self,name):
		self.name = name
		self.list = []

# Defining Grocery Stores in "name" of groceryStore


fiesta = groceryStore('Fiesta')
listing1 = ('Milk, Soda, Fish')
fiesta.list.append(listing1)
print("My " + fiesta.name + " grocery list is \n " + str(fiesta.list))

print("\n\n\n")

walmart = groceryStore('Walmart')
listing2 = ('Paper, Napkins, Plate, Chips')
walmart.list.append(listing2)
print("My " + walmart.name + " grocery list is\n " + str(walmart.list))

print("\n\n\n")

samsClub = groceryStore('Sams Club')
listing3 = ('Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey')
samsClub.list.append(listing3)
print("My " + samsClub.name + " is grocery list is \n" + str(samsClub.list))


