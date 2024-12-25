import random

def rock_paper_scissor(y,c):
        if c == y:
            print(f"Its a draw both picked {y}.")
        else:
            if c == "rock" and y == "paper":
                print(f"You won computer picked {c}.")
            elif c == "rock" and y == "scissor":
                print(f"You lose computer picked {c}.")
            elif c == "paper" and y == "rock":
                print(f"You lose computer picked {c}.")
            elif c == "paper" and y == "scissor":
                print(f"You won computer picked {c}.")
            elif c == "scissor" and y == "paper":
                print(f"You lose computer picked {c}.")
            elif c == "scissor" and y == "rock":
                print(f"You won computer picked {c}.")
            else:
                print("Error.")

play=True
while play:
    computer = random.choice(["rock", "paper", "scissor"])
    user = input("Enter your choice: ").lower()
    rock_paper_scissor(c=computer, y=user)
    a=True
    while a:
        try_again= input("Wanna play again(y/n): ").lower()
        if try_again == "n" :
            play = False
            a=False
        elif try_again == "y":
            computer = random.choice(["rock", "paper", "scissor"])
            user = input("Enter your choice: ").lower()
            rock_paper_scissor(y=user, c=computer)
        else:
            print("Invalid choice.")
