from random import randint
from itertools import counter

# Basically, it prints 4 lists with random value, and every list should have technically bigger number
# But at the end it gives ValueError for some reason. I'll resolve it someday.
def ranlist():
    try:
        num = []
        for x in range(0, 100):
            for y in range(0, 100):
                res = randint(x, y)
                num.append(res)
                print(num)
                if len(num) > 4:
                    break
    # It shouldn't be an error. I don't how to fix it lol
    except ValueError:
        print("You created lists")
        input("Press ENTER to exit")
        exit()
        
# It will count values. I'll finish this ASAP
def data_couner(x, y):
    data_1 = [x]
    data_2 = [y]
    return data_1 + data_2

print("1. Output strange result")
print("2. Count data")
choice = ('1', '2')
user_choice = int(input("Write your choice: "))

try:
    if user_choice == 1:
      ranlist()
      if user_choice == 2:
            NUM1 = float(input("Type first number: "))
            NUM2 = float(input("Type second number: "))
            result = data_counter(NUM1, NUM2)
            print(result)
except ValueError:
    print("You had to write a number")
    input("Press ENTER to exit")
    exit()

# Function 1 - 11.11.2022
# Function 2 - 13.11.2022
