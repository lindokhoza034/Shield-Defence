from tkinter import *
import customtkinter
from tkinter import messagebox
import subprocess
import ast


window = Tk()

window_width = 925
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)

window.title("Sign In")
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
window.configure(bg="#fff")
window.resizable(False, False)


# sign up function
def signin():
    username = user.get()
    password = passw.get()

    with open("users.txt", "r") as file:
        data = file.read()
        users = ast.literal_eval(data)

        if username in users and users[username] == password:
            # Execute block.py in a new process
            subprocess.Popen(["python", "block.py"])

            # Close the login.py window
            window.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")


def signup():
    subprocess.Popen(["python", "register.py"])
    window.destroy()


image = PhotoImage(file="images//1.png")
Label(window, image=image, border=0, bg="white").place(x=0, y=0)

# frame with the input box and sign up button
frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=538, y=50)

# Sign In Heading --------------------------------------------------------
heading = Label(
    frame,
    text="Sign In",
    fg="black",
    bg="white",
    font=("Microsoft Yahei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)


# Username Input ---------------------------------------------------------
def on_enter(e):
    if user.get() != "" and user.get() == "Username":
        user.delete(0, "end")
        user.configure(show="")


def on_leave(e):
    if user.get() == "":
        user.insert(0, "Username")
        user.configure(show="")


user = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft Yahei UI Light", 11),
)
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# Password Input ---------------------------------------------------------
def on_enter(e):
    if passw.get() != "" and passw.get() == "Password":
        passw.delete(0, "end")
        passw.configure(show="*")
    elif passw.get() != "":
        passw.configure(show="*")


def on_leave(e):
    if passw.get() == "":
        passw.insert(0, "Password")
        passw.configure(show="")


passw = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft Yahei UI Light", 11),
)
passw.place(x=30, y=150)
passw.insert(0, "Password")
passw.bind("<FocusIn>", on_enter)
passw.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

# Sign Ip Button ------------------------------------------------------
Button(
    frame,
    width=39,
    pady=7,
    text="Sign In",
    bg="black",
    fg="white",
    border=0,
    command=signin,
).place(x=35, y=204)

# I don't have an account text ----------------------------------------------
label = Label(
    frame,
    text="Don't have an account?",
    fg="black",
    bg="white",
    font=("Microsoft Yahei UI Light", 9),
)
label.place(x=90, y=270)

# Sign Up --------------------------------------------------------------------

signup = Button(
    frame,
    width=6,
    text="Sign Up",
    border=0,
    bg="white",
    cursor="hand2",
    fg="black",
    command=signup,
)
signup.place(x=225, y=270)

window.mainloop()
