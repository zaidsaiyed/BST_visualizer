import tkinter as tk


def add_bst():
    element = text_box.get()
    list = element.split(",")
    print_ele = list[-1]
    obj.create_oval(40,40,80,80)
    obj.create_text(60,60,text=print_ele)

window = tk.Tk()
window.title("BST")
window.geometry("500x500")

label = tk.Label(window, text="Generate a BST: Enter comma-delimited values below and press 'Submit':", font=("arial",10))
label.pack()

frame = tk.Frame(window)

text_box = tk.Entry(frame, font=("arial",10))
text_box.pack(pady=20, side="left")

submit_bt = tk.Button(frame, text="Submit", command=add_bst)
submit_bt.pack(padx=10, side="left")

reset_bt = tk.Button(frame, text="Reset")
reset_bt.pack(side="left")

frame.pack()

obj = tk.Canvas(window, width=200, height=200, bg="grey")
obj.pack()
window.mainloop()