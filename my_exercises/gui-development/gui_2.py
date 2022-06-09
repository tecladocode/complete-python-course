import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame()
main.pack(side='left', fill='both', expand=True)

tk.Label(main, text='Label top', bg='red').pack(side='top', fill='both', expand=True)
tk.Label(main, text='Label top', bg='red').pack(side='top', fill='both', expand=True)

tk.Label(root, text='Label left', bg='green').pack(side='left', fill='both', expand=True)

root.mainloop()
