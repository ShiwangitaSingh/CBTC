# Importing required libraries
import tkinter  
from tkinter import *  
import customtkinter  
from customtkinter import *  


def play():
    try: 
        None
    except:
        # Handle any errors (e.g., if user inputs are invalid)
        result1.configure(text="Oh! It seems you entered some wrong values\nEnter valid details please !!!")


# Setting the appearance of the app to match the system's theme
customtkinter.set_appearance_mode("System")

# Creating the main app window
app = customtkinter.CTk()
app.geometry("720x480")  # Setting the window size
app.title("Mastermind Game")  # Setting the window title

# UI Elements
# Frame 1: Collecting user's first and last name
frame1 = CTkFrame(app)
frame1.pack(padx=10, pady=10)

label_1 = CTkLabel(frame1, text="Player 1 Set a multidigit number")
label_1.pack(side=LEFT, padx=10, pady=10)

Fname = StringVar()  # Variable to hold first name
num1 = CTkEntry(frame1, width=100, height=40, textvariable=Fname)
num1.pack(side=LEFT, padx=10, pady=10)



# Frame 2: Collecting user's birth year and date
frame2 = CTkFrame(app)
frame2.pack(padx=10, pady=10)

label_2 = CTkLabel(frame2, text="Player 2 guess the number")
label_2.pack(side=LEFT, padx=10, pady=10)

Lname = StringVar()  # Variable to hold last name
num2 = CTkEntry(frame2, width=100, height=40, textvariable=Lname)
num2.pack(side=RIGHT, padx=10, pady=10)



# Button to trigger password generation
button = CTkButton(master=app, text="Play", command=play)
button.pack(padx=10, pady=10)

# Frame 3: Display the generated password
frame3 = CTkFrame(app)
frame3.pack(padx=10, pady=5)

result1 = CTkLabel(frame3, text="Let's Go")
result1.pack(padx=10, pady=10)

# Running the app
app.mainloop()