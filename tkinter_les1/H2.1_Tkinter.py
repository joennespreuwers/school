# Imports
import tkinter, json

# Vars
root = tkinter.Tk()
options = json.load(open("config.json"))


root.title(options["title"])
root.geometry(options["ratio"])
root.wm_iconbitmap(options["favicon"])
root.configure(bg=options["bgcolor"])

# Main
root.mainloop()
