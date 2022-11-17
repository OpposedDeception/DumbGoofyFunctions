from random import randint
from itertools import counter
from colorama import Back, Fore, init

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
        
# Counter function is finished!
def counter(integer):
    for i in count(integer):
        print(i, end=' ')
        if i > limit():
            print()
            break
            
# Counter limit, to prevent from several issues.            
def limit(counter()):
    if len(counter()) > 104:
        print("Too big value")
        
def printOnNewLine(string):
   resultion = print(f'\n'.join
                      {string})
   if string != str:
       raise TypeError('You can only enter string values, such as "string" ')
   else:
       pass
   return resultion
            
init(convert=True)
    
print(Back.CYAN + Fore.BLACK + '1. Output strange result')
print(Back.CYAN + Fore.BLACK + '2. Count integers')
print(Back.CYAN + Fore.BLACK + '3. Print character on new line')
choice = ('1', '2', '3')
user_choice = int(input("Write your choice: "))

try:
    if user_choice in choice == 1:
      ranlist()
    elif user_choice in choice == 2:
            NUM1 = float(input("Type first number: "))
            result = counter(NUM1)
            print(result)
    elif user_choice in choice == 3:
       user_result = str(input("Write what string you want to input: "))
       result_of_the_user = printOnNewLine(user_result)
       print(result_of_the_user)        
except ValueError:
    print("You had to write a number")
    input("Press ENTER to exit")
    exit()

# Function 1 - 11.11.2022
# Function 2 - 13.11.2022
# Function 3, 4 and 5 - 14.11.2022
