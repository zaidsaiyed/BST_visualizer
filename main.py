import tkinter as tk

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = BSTNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr = self.root
            while True:
                if value < curr.value:
                    if curr.left is None:
                        curr.left = new_node
                        break
                    else:
                        curr = curr.left
                elif value > curr.value:
                    if curr.right is None:
                        curr.right = new_node
                        break
                    else:
                        curr = curr.right
    
    def build_tree(self, values):
        for value in values:
            self.insert(value)
            
    def print_tree(self, node, canvas, x, y, diff):
        if node is not None:
            self.print_tree(node.left, canvas, x-diff, y+50, diff/2)
            canvas.create_oval(x-10, y-10, x+10, y+10, fill="white")
            canvas.create_text(x, y, text=str(node.value))
            if node.left is not None:
                canvas.create_line(x, y, x-diff/2, y+50)
                
            if node.right is not None:
                canvas.create_line(x, y, x+diff/2, y+50)
            self.print_tree(node.right, canvas, x+diff, y+50, diff/2)
            

def draw_tree(values):
    tree = BST()
    tree.build_tree(values)

    window = tk.Tk()
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    tree.print_tree(tree.root, canvas, 400, 50, 300)

    window.mainloop()

#Main
values = [5,3,7,1,4,6,8]
draw_tree(values)

# def add_bst():
#     element = text_box.get()
#     list = element.split(",")
#     print_ele = list[-1]
#     obj.create_oval(40,40,80,80)
#     obj.create_text(60,60,text=print_ele)

# window = tk.Tk()
# window.title("BST")
# window.geometry("500x500")

# label = tk.Label(window, text="Generate a BST: Enter comma-delimited values below and press 'Submit':", font=("arial",10))
# label.pack()

# frame = tk.Frame(window)

# text_box = tk.Entry(frame, font=("arial",10))
# text_box.pack(pady=20, side="left")

# submit_bt = tk.Button(frame, text="Submit", command=add_bst)
# submit_bt.pack(padx=10, side="left")

# reset_bt = tk.Button(frame, text="Reset")
# reset_bt.pack(side="left")

# frame.pack()

# obj = tk.Canvas(window, width=200, height=200, bg="grey")
# obj.pack()
# window.mainloop()