import tkinter as tk
from tests.test_search import test_login_shopify_partner
from tests.test_search import browser
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

button1 = tk.Button(text='Click Me',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)




root.mainloop()