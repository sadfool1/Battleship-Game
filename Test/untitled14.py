from tkinter import *
root = Tk()
frame = Frame(root)
pyList = ["Eric", "Terry", "Graham", "Terry", "John", "Carol?", "Michael"]
arbList = ['ham', 'spam', 'eggs', 'potatos', 'tots', 'home fries']
pythons = Listbox(root, width=10, height=5, selectmode=EXTENDED, exportselection=0)
food = Listbox(root, width=10, height=5, selectmode=EXTENDED, exportselection=0)
def hider():
    if pythons.selection_includes(4):
        food.lower(frame)
    elif pythons.selection_includes(0):
        food.lift(frame)
b2 = Button(frame, text="Hide!", command=hider)
b2.grid(row=2, column=1)

food.grid(row=0, column=1, in_=frame)
pythons.grid(row=1, column=1, pady=10, in_=frame)
frame.grid()

for python in pyList:
        pythons.insert('end', python)

for thing in arbList:
        food.insert('end', thing)


root.mainloop()