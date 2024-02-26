from tkinter import *
from tkinter import ttk


tab_details = {
    "fingerprints": {"Device types": ["Mobile + Desktop", "Desktop", "Mobile"]}
}

fonts_ = {
    "body": {"tabs": ("Arial", 14, "normal")},
    "cb": ("Arial", 12, "normal"),
}


dimension = {
    "app": {"height": 550, "width": 900},
    # "header": {"height": 20, "width": 0},
    "footer": {"height": 50, "width": 0},
    "body": {
        "height": 550 - 50,
        "width": 150,
        "tabs": {"height": 550 - 50, "width": 150},
        "work": {"height": 550 - 50, "width": 900 - 150},
    },
}

color = {
    "app": {"height": 550, "width": 800},
    # "header": {"height": 20, "width": 0},
    "footer": {"bg": "#313131", "fg": 0},
    "body": {
        "bg": "red",
        "fg": "red",
        "tabs": {
            "bg": "#2c3136",
            "fg": "red",
            "b": {"bg": "#303334", "fg": "#9AACB7", "abg": "#202020", "afg": "#A1C2D6"},
        },
        "work": {"bg": "#202020", "fg": "red"},
    },
}

GUI_SETTINGS = {
    "d": dimension,
    "c": color,
    "f": fonts_,
}




# ,width=dimension['width'],height=dimension['height']
def fingerprints_tab(base_frame, dimension):
    fingerprints_tab_frame = Canvas(base_frame, background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , border=0, borderwidth=0 , highlightthickness=0, )
    fingerprints_tab_frame.place(x=0, y=0)
    fingerprints_tab_frame.pack_propagate()

    Label(fingerprints_tab_frame, background=GUI_SETTINGS["c"]["body"]["work"]["bg"], padx=346 , border=0, borderwidth=0 , highlightthickness=0).grid(row=0, column=1)
    # Label(fingerprints_tab_frame, background="red", padx=342).grid(row=1, column=0, rowsp)

    fingerprints_widgets = {}
    
    
    
    def show_hide_percentage_entry(e):
        print(fingerprints_widgets["device_type_cb"].get())
        
        selected_fingerprints = fingerprints_widgets["device_type_cb"].get()
        if selected_fingerprints == 'Mobile':
            fingerprints_widgets["desktop_percentage_label_placeholder"].grid_forget()
            fingerprints_widgets["desktop_percentage_label"].grid_forget()
            fingerprints_widgets["desktop_percentage_cb"].grid_forget()
            
            fingerprints_widgets["mobile_percentage_label_placeholder"].grid(row=1, column=1,ipady=10)
            fingerprints_widgets["mobile_percentage_label"].grid(row=1, column=1, sticky="e",ipadx=10)
            fingerprints_widgets["mobile_percentage_cb"].grid(row=1, column=2, ipadx=3)
            fingerprints_widgets["mobile_percentage_cb"]['state']=NORMAL
            fingerprints_widgets["mobile_percentage_cb"].delete(0, "end")
            fingerprints_widgets["mobile_percentage_cb"].insert(0, 100)
            fingerprints_widgets["mobile_percentage_cb"]['state']=DISABLED
            
        elif selected_fingerprints == 'Desktop':         
            fingerprints_widgets["mobile_percentage_label_placeholder"].grid_forget()
            fingerprints_widgets["mobile_percentage_label"].grid_forget()
            fingerprints_widgets["mobile_percentage_cb"].grid_forget()
            
            fingerprints_widgets["desktop_percentage_label_placeholder"].grid(row=2, column=1,ipady=10)
            fingerprints_widgets["desktop_percentage_label"].grid(row=2, column=1, sticky="e",ipadx=10)
            fingerprints_widgets["desktop_percentage_cb"].grid(row=2, column=2, ipadx=3)
            fingerprints_widgets["desktop_percentage_cb"]['state']=NORMAL
            fingerprints_widgets["desktop_percentage_cb"].delete(0, "end")
            fingerprints_widgets["desktop_percentage_cb"].insert(0, 100)
            fingerprints_widgets["desktop_percentage_cb"]['state']=DISABLED
        else:
            
            fingerprints_widgets["mobile_percentage_label_placeholder"].grid(row=1, column=1,ipady=10)
            fingerprints_widgets["mobile_percentage_label"].grid(row=1, column=1, sticky="e",ipadx=10)
            fingerprints_widgets["mobile_percentage_cb"].grid(row=1, column=2, ipadx=3)
            fingerprints_widgets["mobile_percentage_cb"]['state']=NORMAL
            fingerprints_widgets["mobile_percentage_cb"].delete(0, "end")
            fingerprints_widgets["mobile_percentage_cb"].insert(0, 50)
            fingerprints_widgets["mobile_percentage_cb"]['state']='readonly'
            
            fingerprints_widgets["desktop_percentage_label_placeholder"].grid(row=2, column=1,ipady=0)
            fingerprints_widgets["desktop_percentage_label"].grid(row=2, column=1, sticky="e",ipadx=10)
            fingerprints_widgets["desktop_percentage_cb"].grid(row=2, column=2, ipadx=3)
            fingerprints_widgets["desktop_percentage_cb"]['state']=NORMAL
            fingerprints_widgets["desktop_percentage_cb"].delete(0, "end")
            fingerprints_widgets["desktop_percentage_cb"].insert(0, 50)
            fingerprints_widgets["desktop_percentage_cb"]['state']='readonly'
        

    fingerprints_widgets["cb_frame"] = Frame(
        fingerprints_tab_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , border=0, borderwidth=0 , highlightthickness=0,
    )
    fingerprints_widgets["cb_frame"].grid(row=1, column=1)

    fingerprints_widgets["device_type_label_placeholder"] = Label(
        fingerprints_widgets["cb_frame"],
        width=35,
        # background="green",
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , border=0, borderwidth=0 , highlightthickness=0,
        font=fonts_["cb"],
    )
    fingerprints_widgets["device_type_label_placeholder"].grid(row=1, column=1)
    fingerprints_widgets["device_type_label"] = Label(
        fingerprints_widgets["cb_frame"], font=fonts_["cb"], text="Device Type",
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , border=0, borderwidth=0 , highlightthickness=0,
        foreground='white'
        
    )
    fingerprints_widgets["device_type_label"].grid(row=1, column=1, sticky="e",ipadx=10)

    fingerprints_widgets["device_type_cb"] = ttk.Combobox(
        fingerprints_widgets["cb_frame"],
        width=20,
        values=tab_details["fingerprints"]["Device types"],
        font=fonts_["cb"],
        state="readonly",
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] 
    )
    fingerprints_widgets["device_type_cb"].grid(row=1, column=2, ipadx=0)
    fingerprints_widgets["device_type_cb"].set(
        tab_details["fingerprints"]["Device types"][0]
    )
    
    fingerprints_widgets["device_type_cb"].bind("<<ComboboxSelected>>", show_hide_percentage_entry)

    # ----------
    
    def manage_spinbox_value():
        # print('>>',100-int(fingerprints_widgets["mobile_percentage_cb"].get()))
        
        fingerprints_widgets["desktop_percentage_cb"]["state"] = NORMAL 
        fingerprints_widgets["desktop_percentage_cb"].delete(0, "end")  # Clear any existing value
        fingerprints_widgets["desktop_percentage_cb"].insert(0, 100-int(fingerprints_widgets["mobile_percentage_cb"].get()))  # Insert the default value
        fingerprints_widgets["desktop_percentage_cb"]["state"] = 'readonly' 

    fingerprints_widgets["percentage_frame"] = Frame(
        fingerprints_tab_frame,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , border=0, borderwidth=0 , highlightthickness=0,
        pady=15
    )
    fingerprints_widgets["percentage_frame"].grid(row=2, column=1)

    fingerprints_widgets["mobile_percentage_label_placeholder"] = Label(
        fingerprints_widgets["percentage_frame"],
        width=35,
        background="green",
        font=fonts_["cb"],
        # background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , 
        border=0, borderwidth=0 , highlightthickness=0,
        foreground='white'
    )
    fingerprints_widgets["mobile_percentage_label_placeholder"].grid(row=1, column=1,ipady=10)
    
    #Label
    fingerprints_widgets["mobile_percentage_label"] = Label(
        fingerprints_widgets["percentage_frame"], font=fonts_["cb"], text="Chance of using mobile fingerprints %",
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , 
        foreground='white',
        border=0, borderwidth=0 , highlightthickness=0,
    )
    fingerprints_widgets["mobile_percentage_label"].grid(row=1, column=1, sticky="e",ipadx=10)
    
    # SpinBox
    fingerprints_widgets["mobile_percentage_cb"] = Spinbox(
        fingerprints_widgets["percentage_frame"],
        width=20,
        font=fonts_["cb"],
        from_=1,
        to=99,
        command=manage_spinbox_value
    )
    fingerprints_widgets["mobile_percentage_cb"].grid(row=1, column=2, ipadx=3, )

    fingerprints_widgets["mobile_percentage_cb"].delete(0, "end")  # Clear any existing value
    fingerprints_widgets["mobile_percentage_cb"].insert(0, 50)  # Insert the default value
    fingerprints_widgets["mobile_percentage_cb"]["state"] = 'readonly'

        


   
   #---------------------------------------
    #Place Holder Label
    fingerprints_widgets["desktop_percentage_label_placeholder"] = Label(
        fingerprints_widgets["percentage_frame"],
        width=35,
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , 
        font=fonts_["cb"],
        border=0, borderwidth=0 , highlightthickness=0,
    )
    fingerprints_widgets["desktop_percentage_label_placeholder"].grid(row=2, column=1)
    
    #Label
    fingerprints_widgets["desktop_percentage_label"] = Label(
        fingerprints_widgets["percentage_frame"], font=fonts_["cb"], text="Chance of using PC fingerprints %",
        background=GUI_SETTINGS["c"]["body"]["work"]["bg"] , 
        foreground='white',
        border=0, borderwidth=0 , highlightthickness=0,        
    )
    fingerprints_widgets["desktop_percentage_label"].grid(row=2, column=1, sticky="e",ipadx=10)

    #SpinBox
    fingerprints_widgets["desktop_percentage_cb"] = Spinbox(
        fingerprints_widgets["percentage_frame"],
        width=20,
        font=fonts_["cb"],
        from_=1,
        to=99,
        command=manage_spinbox_value
    )
    fingerprints_widgets["desktop_percentage_cb"].grid(row=2, column=2, ipadx=3)


    fingerprints_widgets["desktop_percentage_cb"].delete(0, "end")  # Clear any existing value
    fingerprints_widgets["desktop_percentage_cb"].insert(0, 50)  # Insert the default value
    fingerprints_widgets["desktop_percentage_cb"]["state"] = 'readonly'
   
   
    
   



   

if __name__ == "__main__":
    root = Tk()
    fingerprints(root)

    root.mainloop()


