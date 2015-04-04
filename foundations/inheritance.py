class Parent():
	def __init__(self, last_name, eye_color):
		print("Parent Constructor Called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		print("Child constructor called")
		Parent.__init__(self,last_name, eye_color)
		self.number_of_toys = number_of_toys

#billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.number_of_toys)

select ordernames.name, count(*) as num from ordernames join taxonomy,
	 animals where ordernames.t_order = taxonomy.t_order group by ordernames.name order by num
'''

select ordernames.name, count(*) as num from animals, taxonomy, ordernames where animals.species = taxonomy.name and taxonomy.t_order = ordernames.t_order group by ordernames.name order by num desc

select ordernames.name, count(*) as num from ordernames, taxonomy, animals where ordernames.t_order = taxonomy.t_order and animals.species = taxonomy.name group by ordernames.name 