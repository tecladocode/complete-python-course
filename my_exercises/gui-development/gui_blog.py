import tkinter as tk
from tkinter import ttk

root = tk.Tk()
container = ttk.Frame(root)
canvas = tk.Canvas(container)
scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    '<Configure>',
    lambda e: canvas.configure(
        scrollregion=canvas.bbox('all')
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

for i in range(50):
    ttk.Label(scrollable_frame, text='Sample scrolling label').pack()

container.pack()
canvas.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

root.mainloop()
