import random
import testModule

print("Rock, Paper, Scissors. Will you win?")
player = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
cpu = random.randint(0,2)
if player == 0:
    print("Player chose:")
    print(testModule.options[player])
    print("CPU chose:")
    print(testModule.options[cpu])
    if cpu == 0:
        print("Tie!")
    elif cpu == 1:
        print("CPU wins!")
    else:
        print("Player wins!")
elif player == 1:
    print("Player chose:")
    print(testModule.options[player])
    print("CPU chose:")
    print(testModule.options[cpu])
    if cpu == 0:
        print("Player wins!")
    elif cpu == 1:
        print("Tie!")
    else:
        print("CPU wins!")
elif player == 2:
    print("Player chose:")
    print(testModule.options[player])
    print("CPU chose:")
    print(testModule.options[cpu])
    if cpu == 0:
        print("CPU wins!")
    elif cpu == 1:
        print("Player wins!")
    else:
        print("Tie!")

else:
    print("Select a valid option")




