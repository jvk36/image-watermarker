import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack()


def button_got_clicked():
    # label["text"] = "Button Got Clicked"
    label.config(text=entry.get())


button = tkinter.Button(text="Click Me", command=button_got_clicked)
button.pack()

entry = tkinter.Entry(width=10)
entry.pack()

window.mainloop()
