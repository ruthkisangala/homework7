# Task 1
animals = ["dog", "cat", "rabbit", "snake"]

# Task 2
def five_letters():
    for animal in animals: 
        if len(animal) < 5:
            print(animal)

print("Animals with less than 5 letters are:")
five_letters()

# Task 3
def letter_d():
    for animal in animals:
        if animal[0] == "d":
            print(animal)

print("\nAnimals starting with the letter \"d\" are:")
letter_d()

#Task 4
def detect():
    animal_input = input("Enter an animal: ").lower()
    if animal_input in animals:
        print(True)
    else:
        print(False)
    
detect()

#Task 5
def big_list():
    first_list = list(input("Enter the first list: ").split(","))
    second_list = list(input("Enter the second list: ").split(","))
    combined_list = list(first_list)
    for animal in second_list:
        if animal not in first_list:
            combined_list.append(animal)

    print(first_list)
    print(second_list)
    print(combined_list)

big_list()

# I don't understand how I can delete the white spaces.

#Task 6
def sort_alphabetically():
    animals = ["cat", "mouse", "rabbit", "horse", "giraffe", "elephant", "lion"]
    animals.sort()
    print(animals)

sort_alphabetically()

#Task 7
def sort_alphabetically_second():
    animals = ["cat", "mouse", "rabbit", "horse", "giraffe", "elephant", "lion"]
    animals_second = []
    for animal in animals: 
        animal = animal[1:] + animal[0]
        animals_second.append(animal)
    animals_second.sort()
    animals = []
    for animal in animals_second: 
        animal = animal[-1] + animal[:-1]
        animals.append(animal)
    print(animals)

sort_alphabetically_second()

#not the prettiest solution, but I couldn't think of another solution
    
#Task8

numbers = [11, 33, 50]

def single_int():
    single_integer = ""
    for number in numbers:
        single_integer += str(number)

    print(single_integer)

single_int()