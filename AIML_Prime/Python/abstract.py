from abc import abstractmethod


class Animal:
    @abstractmethod
    def speak(self):
      pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
print(Dog().speak())