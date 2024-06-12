# Importing Library
import maskpass

# Start
print("\n --ROCK PAPER SCISSOR GAME--\n")

# Taking invisible input
p1 = maskpass.askpass(prompt="Player 1 Enter: ", mask="")
p2 = maskpass.askpass(prompt="Player 2 Enter: ", mask="")

# Game Logic
if p1.lower() == "rock":
    if p2.lower() == "paper":
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 2 WON--\n")
    else:
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 1 WON--\n")

elif p1.lower() == "paper":
    if p2.lower() == "scissor":
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 2 WON--\n")
    else:
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 1 WON--\n")

elif p1.lower() == "scissor":
    if p2.lower() == "rock":
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 2 WON--\n")
    else:
        print(f"\nPlayer 1 = {p1} and Player 2 = {p2}\n")
        print(f"\n--Player 1 WON--\n")

else:
    print("Enter valid inputs [ROCK, PAPER, SCISSOR]")