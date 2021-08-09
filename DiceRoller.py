import random

def Diceroller():
    a_num = int(input("How many rolls do you need? -> "))
    side = int(input("How many sided die? -> "))
    listnum = [random.randint(1,side) for x in range(a_num) ]
    calcnum = sum(listnum)
    print(f"Your list of rolls are {listnum} which adds up too {calcnum}")
    again = input("Do you want to keep rolling? (Y/N) ->")
    if again == "Y" or "y":
        Diceroller()
    else:
        print("Goodbye")
Diceroller()


