from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## Setup ##

redLed = LED(15)

greenLed = LED(17)

yellowLed = LED(18)

## GUI SET UP ##

win = Tk()
win.title("Task5.1p - LED GUI")
win.geometry("800x600")


win.configure(bg = 'grey50')
myFont = tkinter.font.Font(family = 'Helvetica', size = 14, weight = "bold")

## Button Events ##

def ledToggle(led, button_id):
        print(button_id)
        if led.is_lit:
                led.off()
                buttons[button_id].config(text = "Off")
        else:
                led.on()
                buttons[button_id].config(text = "On")

def controlLed(color):
        if color.lower() in buttons:
                buttons[color.lower()].invoke()
        else:
                textLabel.config(text = "Please enter a valid color")

def onEnter(event):
        color = textBox.get()
        controlLed(color)

def close():
        RPi.GPIO.cleanup()
        win.destroy()

## Buttons / Widgets ##

buttons = {}

redButton = Button(win, text = "Off", font = myFont, command = lambda: ledToggle(redLed, "red"), bg = 'red2', height = 2, width = 12, borderwidth = 4, highlightthickness = 2)
redButton.place(relx=0.2, rely=0.5, anchor = CENTER)
buttons["red"] = redButton

greenButton = Button(win, text = "Off", font = myFont, command = lambda: ledToggle(greenLed, "green"), bg = 'lawn green', height = 2, width = 12, borderwidth = 4, highlightthickness = 2)
#greenButton.grid(row=2, column=1)
greenButton.place(relx=0.5, rely=0.5, anchor = CENTER)
buttons["green"] = greenButton

yellowButton = Button(win, text = "Off", font = myFont, command = lambda: ledToggle(yellowLed, "yellow"), bg = 'yellow', height = 2, width = 12, borderwidth = 4, highlightthickness = 2)
#yellowButton.grid(row=4, column=1)
yellowButton.place(relx=0.8, rely=0.5, anchor = CENTER)
buttons["yellow"] = yellowButton

exitButton = Button(win, text = "Close", font = myFont, command = close, bg = 'light gray', height = 1, width = 6, borderwidth = 2, highlightthickness = 1)
exitButton.place(relx=0.5, rely=0.9, anchor = CENTER)

titleLabel = Label(win, text = "Light Box", font=myFont, bg = 'grey50')
titleLabel.place(relx=0.5, rely=0.1, anchor = CENTER)

textLabel = Label(win, text = "Enter Light Colour to Toggle Blow", font=myFont, bg = 'grey50', borderwidth = 2)
textLabel.place(relx=0.5, rely=0.65, anchor = CENTER)

textBox = Entry(win, font = myFont, borderwidth = 2)
textBox.place(relx=0.5, rely=0.7, anchor = CENTER)
textBox.bind("<Return>", onEnter)

win.protocol("WM_DELETE_WINDOW", close) ##clean exit

win.mainloop() ##loop forever