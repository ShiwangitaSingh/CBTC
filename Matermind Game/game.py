# Important library
import maskpass

# Functions
# function for setting the secret number
def setting():
    s = maskpass.askpass(prompt="Set the number: ")
    l = len(s)
    return s,l

# Play function
def play():
    s,l = setting()
    hint = list("*"*l)
    atempt = 0
    while True:
        g = input("guess : ")
        atempt +=1
        count = 0
        for i in s:
            if i in g:
                try:
                    if s[count] == g[count]:
                        hint[count] = i
                except:
                    print(f'enter {len(s)} digit number')
            count += 1
        print(x:="".join(hint))
        if x == s:
            print("You guessed it!!!")
            return atempt
            break

print("\nPlayer 1 TURN\n")
p1 = play()
print("\nPlayer 2 TURN\n")
p2 = play()

if p1==p2:
    print("\nIt's a tie")
elif p1>p2:
    print(f"\nPlayer 1 won by {p1-p2} attempts")
elif p2>p1:
    print(f"\nPlayer 2 won by {p2-p1} attempts")