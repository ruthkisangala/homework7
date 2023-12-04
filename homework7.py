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
    first_list = ("").join(list(input("Enter the first list: ").split(",")))
    

    #second_list = list(input("Enter the second list: "))
    #combined_list = first_list + second_list
    print(first_list)
    #print(second_list)
    #print(combined_list)

big_list()