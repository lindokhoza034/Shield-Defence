import subprocess
from tkinter import *
from tkinter import messagebox
import ast
import sys

window = Tk()

window_width = 925
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 2)

window.title("Sign Up")
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
window.configure(bg="#fff")
window.resizable(False, False)


# sign up function
def signup():
    username = user.get()
    password = passw.get()
    confirm_password = confirm_passw.get()

    if not username or username == "Username":
        messagebox.showerror("Invalid", "Username cannot be empty.")
        return

    if password == confirm_password:
        try:
            file = open("users.txt", "r+")
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username: password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open("users.txt", "w")
            w = file.write(str(r))

            messagebox.showinfo("Sign Up", "Sign Up Successful")
            subprocess.Popen(["python", "login.py"])
            window.destroy()

        except:
            file = open("users.txt", "w")
            pp = str({"username": "password"})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid", "Passwords do not match")


def signin():
    subprocess.Popen(["python", "login.py"])
    window.destroy()


image = PhotoImage(file="images//1.png")
Label(window, image=image, border=0, bg="white").place(x=0, y=0)

# frame with the input box and sign up button
frame = Frame(window, width=350, height=390, bg="white")
frame.place(x=538, y=50)

# Sign Up Heading
heading = Label(
    frame,
    text="Sign Up",
    fg="black",
    bg="white",
    font=("Microsoft Yahei UI Light", 23, "bold"),
)
heading.place(x=100, y=5)


# Username Input
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


# Password Input
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


# confirm password
def on_enter(e):
    if confirm_passw.get() != "" and confirm_passw.get() == "Confirm Password":
        confirm_passw.delete(0, "end")
        confirm_passw.configure(show="*")
    elif confirm_passw.get() != "":
        confirm_passw.configure(show="*")


def on_leave(e):
    if confirm_passw.get() == "":
        confirm_passw.insert(0, "Confirm Password")
        confirm_passw.configure(show="")


confirm_passw = Entry(
    frame,
    width=25,
    fg="black",
    border=0,
    bg="white",
    font=("Microsoft Yahei UI Light", 11),
)
confirm_passw.place(x=30, y=220)
confirm_passw.insert(0, "Confirm Password")
confirm_passw.bind("<FocusIn>", on_enter)
confirm_passw.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

# Sign Up Button
Button(
    frame,
    width=39,
    pady=7,
    text="Sign Up",
    bg="black",
    fg="white",
    border=0,
    command=signup,
).place(x=35, y=280)
# I have an account text
label = Label(
    frame,
    text="Have an account?",
    fg="black",
    bg="white",
    font=("Microsoft Yahei UI Light", 9),
)
label.place(x=90, y=340)

# sign in text

signin = Button(
    frame,
    width=6,
    text="Sign In",
    border=0,
    bg="white",
    cursor="hand2",
    fg="black",
    command=signin,
)
signin.place(x=192, y=340)

window.mainloop()
