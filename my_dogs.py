# my_dogs.py
from dog import Dog # we need to specify exactly what we want

my_dog = Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_third_dog = Dog("Krypto", "SuperDog")

my_other_dog.sit()

my_third_dog.roll_over()