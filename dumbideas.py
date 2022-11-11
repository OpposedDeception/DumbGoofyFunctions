from random import randint

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

print("1. Output strange result")
choice = ('1')
user_choice = int(input("Write your choice: "))

try:
    if user_choice == 1:
      ranlist()
except ValueError:
    print("You had to write a number")
    input("Press ENTER to exit")
    exit()

# Function 1 - 11.11.2022