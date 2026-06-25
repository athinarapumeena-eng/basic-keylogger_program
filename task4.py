import tkinter as tk

def log_key(event):
    with open("key_log.txt", "a") as file:
        file.write(event.keysym + "\n")

window = tk.Tk()
window.title("Keyboard Activity Logger")
window.geometry("400x200")

label = tk.Label(
    window,
    text="Click here and type.\nKeys will be saved to key_log.txt",
    font=("Arial", 12)
)
label.pack(pady=50)

window.bind("<Key>", log_key)

window.mainloop()
