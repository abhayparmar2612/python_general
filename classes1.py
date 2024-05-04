#classes in python :
#class Dog:
 #   def __init__(self,name,breed):
  #      self.name = name
   #     self.breed = breed
#
 #   def bark(self):
  #      print(f"{self.name} says: Woof!")


#my_dog= Dog("Buddy","Labrador")
#my_dog.bark()


# Python inheritance:
#class Animal:
 #   def __init__(self,name,food):
  #      self.name =name
   #     self.food = food
    #def speak(self):
     #   print(f"{self.name} makes a sound")
    #def food(self):
     #   print(f"{self.food} : is favouite food")

#class Dog(Animal):
 #   def speak(self):
  #      print(f"{self.name} says: woof!")
   # def food(self):
    #    print(f"{self.food } : is favourite food")

#my_animal = Animal("choti","roti")
#my_dog = Dog("choti","roti")
              
class BankAccount:
    def __init__(self,balance):
        self._balance = balance

    def deposit(self,amount):
        self._balance += amount
        print("amount deposit successfullY")
        print(f"total balance = {self._balance}")

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print("amount withdraw successfully")
            print(f"Remaining balance is {self._balance}")
        else:
            print("Insufficient funds")
            
        
        
