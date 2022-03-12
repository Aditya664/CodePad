import tkinter as tk
from tkinter import ttk,Menu
from tkinter import font,colorchooser,filedialog,messagebox
import os


main_app = tk.Tk()
main_app.geometry('1200x600')
main_app.title('Codepad 1.0')
######################################################################################################
#                                         Main menu Start                                            #            
######################################################################################################

main_menu = tk.Menu()
# File
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
saveas_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")
file = tk.Menu(main_menu,tearoff=False)
# Edit
copy_icon = tk.PhotoImage(file = "icons2/copy.png")
paste_icon = tk.PhotoImage(file = "icons2/paste.png")
cut_icon = tk.PhotoImage(file = "icons2/cut.png")
clr_icon = tk.PhotoImage(file = "icons2/clear_all.png")
find_icon = tk.PhotoImage(file = "icons2/find.png")
edit = tk.Menu(main_menu,tearoff=False)
# View
toolbar_icon = tk.PhotoImage(file = "icons2/tool_bar.png")
statusbar_icon = tk.PhotoImage(file = "icons2/status_bar.png")
view = tk.Menu(main_menu,tearoff=False)
# Color Theme
light_default_icon = tk.PhotoImage(file = "icons2/light_default.png")
light_plus_icon = tk.PhotoImage(file = "icons2/light_plus.png")
dark_icon = tk.PhotoImage(file="icons2/dark.png")
color = tk.Menu(main_menu,tearoff=False)
theme_choosed = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,dark_icon)
color_dict = {
    'Light Default' : ('#000000','#ffffff'),
    'Light Plus' : ('#474747','#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d')
}
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
######################################################################################################
#                                         Main Menu End                                              #            
######################################################################################################

######################################################################################################
#                                         Main menu Funct                                            #            
######################################################################################################
url = ''
## new
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)

## Open file

def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(),title = 'Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())

    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

## Save File 
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content = text_editor.get(1.0,tk.END)
            url.write(content)
            url.close()
    except:
        return

## Save as 

def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        url.write(content)
        url.close()
    except:
        return

## Exit 

def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning','Do You want to save the file ???')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open(url, 'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    url = filedialog.asksaveasfile(mode = 'w',defaultextension = '.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy();
    except:
        return

## Find
def find_func(event=None):

    def find():
        word = find_ip.get();
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0' 
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
        

    def replace():
        word = find_ip.get();
        replace_text = replace_ip.get();
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)


    find_dia= tk.Toplevel();
    find_dia.geometry('450x250+500+200')
    find_dia.title("Find")
    find_dia.resizable(0,0)

    ## Frame 
    find_frame = ttk.LabelFrame(find_dia,text="Find/Replace")
    find_frame.pack(pady = 20)

    ## labels 
    text_find_label = ttk.Label(find_frame,text="Find: ")
    text_replace_label = ttk.Label(find_frame,text="Replace: ")

    ## entry
    find_ip = ttk.Entry(find_frame,width = 30)
    replace_ip = ttk.Entry(find_frame,width =30)

    ## Buttons
    find_btn = ttk.Button(find_frame,text="Find",command=find)
    replace_btn = ttk.Button(find_frame,text="Replace",command=replace)

    ## label grid
    text_find_label.grid(row = 0,column=0,padx = 4,pady = 4)
    text_replace_label.grid(row = 1,column=0,padx = 4,pady = 4)

    ## Entry grind
    find_ip.grid(row = 0,column = 1,padx = 4,pady = 4)
    replace_ip.grid(row = 1,column = 1,padx = 4,pady = 4)

    ## buttons grid
    find_btn.grid(row = 2,column = 0,padx = 8,pady = 4)
    replace_btn.grid(row = 2,column = 1,padx = 8,pady = 4)

    find_dia.mainloop()



###### View
show_toolbar = tk.BooleanVar();
show_toolbar.set(True)
show_statusbar = tk.BooleanVar();
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget();
        show_toolbar = False
    else:
        text_editor.pack_forget();
        status_bar.pack_forget();
        toolbar.pack(side = tk.TOP,fill = tk.X)
        text_editor.pack(fill = tk.BOTH,expand = True)
        status_bar.pack(side = tk.BOTTOM)
        show_toolbar = True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget();
        show_statusbar = False
    else:
        show_statusbar.pack(side=tk.BOTTOM)
        show_statusbar = True

## bind 
main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",save_as)
main_app.bind("<Control-e>",exit_func)


## File Commands
file.add_command(label='New', image = new_icon,compound = tk.LEFT,accelerator = 'Ctrl+n',command=new_file)
file.add_command(label='Open', image = open_icon,compound = tk.LEFT,accelerator = 'Ctrl+o',command=open_file)
file.add_command(label='Save', image = save_icon,compound = tk.LEFT,accelerator = 'Ctrl+s',command=save_file)
file.add_command(label='Save as', image = saveas_icon,compound = tk.LEFT,accelerator = 'Ctrl+Alt+s',command=save_as)
file.add_command(label='Exit', image = exit_icon,compound = tk.LEFT,accelerator = 'Ctrl+e',command=exit_func)
## Edit Commands
edit.add_command(label="Copy",image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+c',command = lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+p',command = lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+C',command = lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear All",image=clr_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+x',command = lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label="Find",image=find_icon,compound=tk.LEFT,accelerator='Ctrl+f',command=find_func)
## View Commands
view.add_checkbutton(label = "Toolbar",onvalue=True,offvalue=False,image=toolbar_icon,compound=tk.LEFT,variable=show_toolbar,command=hide_toolbar)
view.add_checkbutton(label = "Statusbar",onvalue=True,offvalue=False,image=statusbar_icon,compound=tk.LEFT,variable=show_statusbar,command=hide_statusbar)
## Color Theme 
def change_theme():
    choosen_theme = theme_choosed.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color,bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background= bg_color,fg = fg_color)

count = 0
for i in color_dict:
    color.add_radiobutton(label = i,image = color_icons[count],variable = theme_choosed,compound = tk.LEFT,command = change_theme)
    count += 1;    
######################################################################################################
#                                                                                                    #            
######################################################################################################


######################################################################################################
#                                         Toolbar Start                                              #           
######################################################################################################

toolbar = ttk.Label(main_app)
toolbar.pack(side = tk.TOP,fill = tk.X)

## Font box
fonts = tk.font.families();
font_family = tk.StringVar();
font_box = ttk.Combobox(toolbar,width = 30,textvariable = font_family,state="readonly");
font_box['values'] = fonts
font_box.current(fonts.index("Arial"))
font_box.grid(row = 0,column = 0 ,padx = 5)

## Size box
size = tk.IntVar();
size_box = ttk.Combobox(toolbar,width = 14,textvariable = size,state="readonly")
size_box['values'] = tuple(range(8,81))
size_box.current(4)
size_box.grid(row = 0,column = 1,padx = 5)
## Bold Button
bold_icon = tk.PhotoImage(file = "icons2/bold.png")
bold_btn = ttk.Button(toolbar,image = bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)
## Italic Button
italic_icon = tk.PhotoImage(file = "icons2/italic.png")
italic_btn = ttk.Button(toolbar,image = italic_icon)
italic_btn.grid(row = 0,column = 3,padx = 5)
## Underline icon
underline_icon = tk.PhotoImage(file = "icons2/underline.png")
underline_btn = ttk.Button(toolbar,image = underline_icon)
underline_btn.grid(row = 0,column = 4,padx = 5)
## Font Color Button
font_color_icon = tk.PhotoImage(file = "icons2/font_color.png")
font_color_btn = ttk.Button(toolbar,image = font_color_icon)
font_color_btn.grid(row = 0,column = 5,padx = 5)
## Aligne Left Button
align_left_icon = tk.PhotoImage(file = "icons2/align_left.png")
align_left_btn = ttk.Button(toolbar,image = align_left_icon)
align_left_btn.grid(row = 0,column = 6 , padx = 5)
## Aligne Center Button
align_center_icon = tk.PhotoImage(file = "icons2/align_center.png")
align_center_btn = ttk.Button(toolbar,image = align_center_icon)
align_center_btn.grid(row = 0,column = 7 , padx = 5)
## Aligne Right Button
align_right_icon = tk.PhotoImage(file = "icons2/align_right.png")
align_right_btn = ttk.Button(toolbar,image = align_right_icon)
align_right_btn.grid(row = 0,column = 8 , padx = 5)

######################################################################################################
#                                         Toolbar End                                                #           
######################################################################################################

######################################################################################################
#                                          Text Editor start                                         #           
######################################################################################################

text_editor = tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_app)
scroll_bar.pack(side = tk.RIGHT,fill=tk.Y)
text_editor.focus_set()
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command = text_editor.yview)
text_editor.config(yscrollcommand = scroll_bar.set)

######################################################################################################
#                                          Text Editor End                                           #           
######################################################################################################

######################################################################################################
#                                          Text Editor funct                                         #           
######################################################################################################

## Font and size funct
current_font_family = "Arial"
current_font_size = 12

## Change Font
def change_font(main_app):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font = (current_font_family,current_font_size))
## Change size
def change_size(main_app):
    global current_font_size
    current_font_size = size.get()
    text_editor.configure(font = (current_font_family,current_font_size))
## Buttons functionality

#### Bold Butons functionality

def change_bold():
   text_property = tk.font.Font(font = text_editor['font'])
   if text_property.actual()['weight'] == 'normal':
       text_editor.configure(font = (current_font_family,current_font_size,'bold'))

   if text_property.actual()['weight'] == 'bold':
       text_editor.configure(font = (current_font_family,current_font_size,'normal'))
    
bold_btn.configure(command=change_bold)
#### Italic Butons functionality

def change_italic():
   text_property = tk.font.Font(font = text_editor['font'])
   if text_property.actual()['slant'] == 'roman':
       text_editor.configure(font = (current_font_family,current_font_size,'italic'))

   if text_property.actual()['slant'] == 'italic':
       text_editor.configure(font = (current_font_family,current_font_size,'roman'))

italic_btn.configure(command = change_italic)

#### Underline Butons functionality

def change_under():
   text_property = tk.font.Font(font = text_editor['font'])
   if text_property.actual()['underline'] == 0:
       text_editor.configure(font = (current_font_family,current_font_size,"underline"))

   if text_property.actual()['underline'] == 1:
       text_editor.configure(font = (current_font_family,current_font_size,"normal"))
underline_btn.configure(command =  change_under)

## Font color functionality

def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg = color_var[1])

font_color_btn.configure(command = change_font_color)

## Align Functionality

def aline_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command = aline_left)

def aline_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command = aline_center)

def aline_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command = aline_right)

size_box.bind("<<ComboboxSelected>>",change_size)
font_box.bind("<<ComboboxSelected>>",change_font)
text_editor.configure(font=(current_font_family, current_font_size))



######################################################################################################
#                                                                                                    #           
######################################################################################################

######################################################################################################
#                                          Statusbar start                                           #           
######################################################################################################

status_bar = tk.Label(main_app,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)





######################################################################################################
#                                                                                                    #           
######################################################################################################

######################################################################################################
#                                          Statusbar funct                                           #           
######################################################################################################
text_changed = False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words =  len(text_editor.get(1.0,'end-1c').split())
        character = len(text_editor.get(1.0,'end-1c').replace(' ',''))
        status_bar.config(text = f'Characters : {character} Words : {words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)
      




######################################################################################################
#                                                                                                    #           
######################################################################################################
main_app.config(menu = main_menu)
main_app.mainloop()