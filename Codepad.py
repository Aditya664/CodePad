import tkinter as tk
from tkinter import ttk,Menu
from tkinter import font,colorchooser,filedialog,messagebox
import os


main_app = tk.Tk()
main_app.geometry('1200x800')
main_app.title('Codepad text editor created by Aditya.')

################################# main menu ####################################
main_menu = tk.Menu()
# File
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
saveas_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")

file = tk.Menu(main_menu,tearoff=False)
file.add_command(label='New', image = new_icon,compound = tk.LEFT,accelerator = 'Ctrl+n')
file.add_command(label='Open', image = open_icon,compound = tk.LEFT,accelerator = 'Ctrl+o')
file.add_command(label='Save', image = save_icon,compound = tk.LEFT,accelerator = 'Ctrl+s')
file.add_command(label='Save as', image = saveas_icon,compound = tk.LEFT,accelerator = 'Ctrl+Alt+s')
file.add_command(label='Exit', image = exit_icon,compound = tk.LEFT,accelerator = 'Ctrl+e')
# Edit

copy_icon = tk.PhotoImage(file = "icons2/copy.png")
paste_icon = tk.PhotoImage(file = "icons2/paste.png")
cut_icon = tk.PhotoImage(file = "icons2/cut.png")
clr_icon = tk.PhotoImage(file = "icons2/clear_all.png")
find_icon = tk.PhotoImage(file = "icons2/find.png")

edit = tk.Menu(main_menu,tearoff=False)
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+c')
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+p')
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label="Clear All",image=clr_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+x')
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator='Ctrl+f')


view = tk.Menu(main_menu,tearoff=False)
color = tk.Menu(main_menu,tearoff=False)

# cascade
main_menu.add_cascade(
    label="File",
    menu=file,
    underline=0
)
main_menu.add_cascade(
    label="Edit",
    menu=edit,
    underline=0
)
main_menu.add_cascade(
    label="View",
    menu=view,
    underline=0
)
main_menu.add_cascade(
    label="Color Theme",
    menu=color,
    underline=0
)






############################### main menu ending##############################





main_app.config(menu = main_menu)
main_app.mainloop()
