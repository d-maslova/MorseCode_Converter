from tkinter import *
from tkinter import messagebox
import pyperclip

morse_dict = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
    "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
    "q": "--.-", "r": "-.-", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "  ",
}


def convert_to_morse():
    to_morse = message_entry.get().lower()
    result = ""
    for char in to_morse:
        result += str(morse_dict[char]+" ")
    converted_msg = Label(text=f"Your message in Morse is: {result}", font=("Arial", 16))
    converted_msg.grid(row=2, column=2, columnspan=2)
    pyperclip.copy(result)
    copied_msg = Label(text="It has been copied to your clipboard")
    copied_msg.grid(row=3, column=2)

# UI Setup:
window = Tk()
window.title("Morse Code Converter")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=150)

# Entries
message_entry = Entry(width=60)
message_entry.focus()
message_entry.grid(row=0, column=2)

# Button
convert_button = Button(text="Convert to Morse", width=51, command=convert_to_morse)
convert_button.grid(row=1, column=2)

# Labels
message_label = Label(text="Enter your message:", font=("Arial", 10))
message_label.grid(row=0, column=1)


window.mainloop()
