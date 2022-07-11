# class подкласс (суперкласс):
# 	методы_подкласса

class Person: # В данном случае - суперкласс
	def __init__(self, name):
		self.__name = name

	@property
	def name(self):
		return self.__name

	def display_intro(self):
		print(f"Name is {self.__name}")

x = Person("Alina")
x.display_intro()

# class Employee:
# 	def __init__(self, name):
# 		self.__name = name # Имя работника
#
# 	@property
# 	def name(self):
# 		return self.__name
#
# 	def display_intro(self):
# 		print(f"Name is {self.__name}")
#
# 	def work(self):
# 		print(f"{self.name} works")
#
# x = Employee("Bob")
# x.work()


class Employee(Person): # В данном случае подкласс
	def work(self):
		print(f"{self.__name} works") # Ошибка, потому что name - приватный


tom = Employee("Tom")
tom.display_intro()
tom.work()