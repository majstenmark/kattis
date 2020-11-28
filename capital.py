import tkinter as tk
    


root = tk.Tk()
root.geometry("800x480")
frame = tk.Frame(root, width=800, height=480, background="bisque")
frame.pack()

country = tk.Label(frame, text= 'Hej')

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
country.pack(side=tk.LEFT)
button.pack(side=tk.LEFT)


root.mainloop()