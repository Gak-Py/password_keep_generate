import csv
from tkinter import *
from tkinter import messagebox
import random
import string
window = Tk()
window.minsize(width=300, height=300)
window.config(pady=50, padx=50)
window.title("Password Keeper")

canvas = Canvas(width=400, height=270)
pass_img = PhotoImage(file="logo.png")
bc_image = canvas.create_image(200,120, image=pass_img)
canvas.grid(row=0, column=0, columnspan=3)

def gen_pass():
    gened_str = random.choices(string.ascii_letters, k=random.randint(7,10))
    gened_num = random.choices(string.digits, k=random.randint(3,6))
    gened_kigou = random.choices(string.punctuation, k=random.randint(3, 5))
    gened_pass = gened_str + gened_kigou + gened_num
    random.shuffle(gened_pass)
    pass_input.delete(0, END)
    pass_input.insert(END, "".join(gened_pass))

def pass_add():
    website = website_input.get()
    user = user_input.get()
    password = pass_input.get()
    if website == "" or user == "" or password =="":
        messagebox.showinfo("Alert", "Fill All Input!")

    else:
        with open("pass_list.csv", mode="a") as data:
            writer = csv.writer(data)
            writer.writerow([website, user, password])
        messagebox.showinfo("Alert", "Password Added!")
        website_input.delete(0, END)
        pass_input.delete(0, END)
        user_input.delete(0, END)
        website_input.focus()

website_area = Label(text="website", font=("Futura", 15, "italic"),anchor="w")
website_area.grid(row=1, column=0)

website_input = Entry(textvariable="website url", width=40)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")

user_area = Label(text="user/email", font=("Futura", 15, "italic"),anchor="w")
user_area.grid(row=2, column=0)

user_input = Entry(textvariable="user", width=40)
user_input.grid(row=2, column=1, columnspan=2, sticky="w")


pass_area = Label(text="password", font=("Futura", 15, "italic"),anchor="w")
pass_area.grid(row=3, column=0)

pass_gen_btn = Button(text="generate", command=gen_pass)
pass_gen_btn.grid(row=3, column=2, sticky="w")

pass_input = Entry(width=25)
pass_input.grid(row=3, column=1, sticky="w")

add_btn = Button(text="add", command=pass_add)
add_btn.config(width=37)
add_btn.grid(row=4, column=1, columnspan=2, pady=5)

website_input.focus()
window.mainloop()

