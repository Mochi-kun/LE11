from Tkinter import*
import model

class CC:
	def __init__(self):
		self.ing_list = {}
		self.food_list = {}
		self.ing_avi = {}
		self.food_avi = {}
		self.order_f = {}
		self.order_i = {}
		self.cookOrder = {}
		self.data = model.Data()
	def giveMenu(self):
		print "-" #get info from self.giveAviFood then format to string then send to gui
	def getIng(self):
		self.ing_list = self.data.inglist
	def getFood(self):
		self.food_list = self.data.foodlist
	def giveAviFood(self):
		print "-" #if food_list value not 0 then add to list
	def giveAviIng(self):
		print "-" #if ing_list value not 0 then add to list
	def buyIng(self):
		self.data.addIng(self.order_i.get("Ingredient"), self.order_i.get("Amount"))
	def cook(self):
		print "-" #fix this with classes of food later
	def update_resto(self):
		self.getIng()
		self.getFood()
		self.update_ing()
		self.giveMenu()
	def update_ing(self):
		keys = {}
		keys = self.ing_list.keys()
		f = open("ing.txt", "w")
		for i in keys:
			a = i + " = " + self.ing_list.get(i) + "\n"
			f.write(a)
		f.close()
	def open_ing(ing, fin):
		curr = 1
		file = open("Inventory.txt","r")
		for x in file:
			if x == '\n':
				curr = 2
			elif curr == 1:
				ing[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
			elif curr == 2:
				fin[x.split(":")[0].strip()] = int(x.split(":")[1].strip())
		file.close()

cc = CC()