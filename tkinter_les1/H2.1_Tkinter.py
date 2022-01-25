from pickletools import optimize
from ssl import Options
import tkinter, json

root = tkinter.Tk()

options = json.load(open("config.json"))

root.title(options["title"])
root.geometry(options["ratio"])
root.wm_iconbitmap(options["favicon"])
root.configure(bg=options["bgcolor"])

# Main
root.mainloop()
