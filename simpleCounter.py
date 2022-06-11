import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.title("simple counter app")
root.geometry('360x360+800+300')

# incrementer function
#num = 0
def incrementer(num = 1):
    num = num + 1

    
########### fix this shit #####################################
########### incrementer is not working ########################


 # label number showing count
 
label = tk.Label(root, text= ' count is: ${num}')
label.pack()



# add increment button
button = tk.Button(root, text="increment", command=incrementer)
button.pack()

# run main program
root.mainloop()