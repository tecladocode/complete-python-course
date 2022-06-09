import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)

root.rowconfigure(1, weight=1)
rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white").grid(column=0, row=0, columnspan=2,  ipadx=20, ipady=20, sticky='NSEW')
rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white").grid(column=0,row=1,ipadx=10, ipady=10, sticky='NSEW')
rectangle_3 = tk.Label(root, text="Rectangle 3", bg="blue", fg="white").grid(column=1,row=1,ipadx=10, ipady=10, sticky='NSEW')
root.mainloop()