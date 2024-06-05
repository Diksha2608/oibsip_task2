from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+550+150")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())

        # Convert height into meter
        m = h / 100
        bmi = round(float(w / m ** 2), 1)
        label1.config(text=bmi)

        # Category
        if bmi <= 18.5:
            label2.config(text="Underweight!")
            label3.config(text="You have lower weight than normal body!")
        elif 18.5 < bmi <= 25:
            label2.config(text="Normal!")
            label3.config(text="It indicates that you are healthy!")
        elif 25 < bmi <= 30:
            label2.config(text="Overweight!")
            label3.config(text="It indicates that a person is \n slightly overweight! \nA doctor may advise to lose some weight.")
        else:
            label2.config(text="Obese")
            label3.config(text="Health may be at risk if they do not lose weight!")
    except ValueError:
        label1.config(text="Error")
        label2.config(text="")
        label3.config(text="Please enter valid numbers for height and weight!")

# Icon
image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, image_icon)

# Top image
top = PhotoImage(file="images/top1.png")
top_image = Label(root, image=top, background="#b6addb")
top_image.place(x=10, y=-10)

# Bottom box
Label(root, width=72, height=18, bg="#b6addb").pack(side=BOTTOM)

# Two boxes
box = PhotoImage(file="Images/box.png")
Label(root, image=box).place(x=20, y=110)
Label(root, image=box).place(x=240, y=110)


# Slider 1
current_value = tk.DoubleVar(value=0.00)

def slider_changed(event):
    Height.set(f"{current_value.get():.2f}")

# Command to change background color of scale
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider 2
current_value2 = tk.DoubleVar(value=0.00)

def slider_changed2(event):
    Weight.set(f"{current_value2.get():.2f}")

# Command to change background color of scale
style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry box for Height
Height = StringVar(value="0.00")
Weight = StringVar(value="0.00")

def update_slider1(*args):
    value = Height.get()
    if value:
        current_value.set(float(value))

def update_slider2(*args):
    value = Weight.get()
    if value:
        current_value2.set(float(value))

Height.trace("w", update_slider1)
Weight.trace("w", update_slider2)

Label(root, text="Height (cm)", font='arial 18', bg="#d1cce6").place(x=65, y=130)
height = Entry(root, textvariable=Height, width=5, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=45, y=180)

Label(root, text="Weight (kg)", font='arial 18', bg="#d1cce6").place(x=285, y=130)
weight = Entry(root, textvariable=Weight, width=5, font='arial 40', bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=270, y=180)

# Calculate BMI button
Button(root, text="Calculate BMI", width=20, height=3, font="arial 10 bold", bg="#1f6e68", fg="white", command=BMI).place(x=150, y=330)

# Labels for BMI result
label4 = Label(root, text="Click here to know your BMI ", font="arial 16 bold", bg="#b6addb", fg="#fff")
label4.place(x=100, y=400)

label1 = Label(root, font="arial 30 bold", bg="#b6addb", fg="#fff")
label1.place(x=185, y=430)

label2 = Label(root, font="arial 20 bold", bg="#b6addb", fg="#3b3a3a", anchor='center')
label2.place(x=135, y=480, width=200)

label3 = Label(root, font="arial 10 bold", bg="#b6addb", anchor='center')
label3.place(x=85, y=520, width=300)

root.mainloop()
