import tkinter

root = tkinter.Tk()

options = {
    "title": "Generic Title",
    "favicon": "favicon.ico",
    "bgcolor": "red",
    "ratio": "600x400",
}

root.title(options["title"])
root.geometry(options["ratio"])
root.wm_iconbitmap(options["favicon"])
root.configure(options["bgcolor"])

# Main
root.mainloop()