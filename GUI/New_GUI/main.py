from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


from tabs.fingerprints import fingerprints_tab
from tabs.proxy import proxy_tab
from tabs.main_tab import main_tab
from tabs.visits_tab import visits_tab
from tabs.emulation_tab import emulation_tab
from tabs.utility_tab import utility_tab
from tabs.res import *





making_command_log_formate()



# Change 'Helvetica' to your desired font family, 12 is the font size, 'bold' is the font weight

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

fonts_ = {
    "body": {"tabs": ("Arial", 14, "normal")},
    "footer": ("Arial", 12, "normal"),
}

GUI_SETTINGS = {
    "d": dimension,
    "c": color,
    "f": fonts_,
}


root = Tk()


# # Header
# header_frame = Frame(
#     root, background="black", height=10
# )
# header_frame.pack(fill=X)

# Body
body_frame = Frame(
    root,
    background=GUI_SETTINGS["c"]["body"]["tabs"]["bg"],
    height=GUI_SETTINGS["d"]["footer"]["height"],
    border=0, borderwidth=0,highlightthickness=0
)
body_frame.pack(fill=X)

# Left
tab_frame = Frame(
    body_frame,
    background=GUI_SETTINGS["c"]["body"]["tabs"]["bg"],
    width=GUI_SETTINGS["d"]["body"]["tabs"]["width"],
    height=GUI_SETTINGS["d"]["body"]["tabs"]["height"],
    border=0, borderwidth=0,highlightthickness=0
)
tab_frame.pack(side=LEFT, expand=False)

# Right
working_body_frame = Frame(
    body_frame,
    background=GUI_SETTINGS["c"]["body"]["work"]["bg"],
    width=GUI_SETTINGS["d"]["body"]["work"]["width"],
    height=GUI_SETTINGS["d"]["body"]["work"]["height"],
    border=0, borderwidth=0,highlightthickness=0
)
working_body_frame.pack(side=RIGHT, expand=False)


# footer
footer_frame = Frame(
    root,
    background=GUI_SETTINGS["c"]["footer"]["bg"],
    height=GUI_SETTINGS["d"]["footer"]["height"],
    border=0, borderwidth=0,highlightthickness=0
)
footer_frame.pack(fill=X)


app_tab_list = [
    "Main",
    # "Visits",
    "Emulation",
    "Proxy",
    # "Profiles",
    "Fingerprints",
    # "Captcha",
    # "Timeouts",
    # "Timeouts",
    'Others',
]

selected_tab = app_tab_list[0].lower()
app_tab_widges = {}


def get_current_selected_tab(tab_name):
    for each_tab_name in app_tab_list:
        each_tab_name = each_tab_name.lower()
        if each_tab_name == tab_name:
            app_tab_widges[each_tab_name].configure(
                background=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["abg"],
                foreground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["afg"],
                state="disabled"
            )
            #Display Tab
            tab_working_frame[each_tab_name].pack(side=RIGHT, expand=False)
            
        else:
            # print("x ", each_tab_name)
            app_tab_widges[each_tab_name].configure(
                background=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["bg"],
                foreground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["fg"],
                activebackground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["abg"],
                activeforeground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["afg"],
                state="normal"
            )
            
            #Disappear Tab
            tab_working_frame[each_tab_name].pack_forget()


for index, each_tab_name in enumerate(app_tab_list):
    app_tab_widges[each_tab_name.lower() + "_frame"] = Frame(
        tab_frame,
        background=GUI_SETTINGS["c"]["body"]["tabs"]["bg"],
        width=GUI_SETTINGS["d"]["body"]["tabs"]["width"],
        height=80,
        padx=10,
        pady=3,
        border=0, borderwidth=0,highlightthickness=0
    )
    app_tab_widges[each_tab_name.lower() + "_frame"].grid(row=index, column=1)

    app_tab_widges[each_tab_name.lower()] = Button(
        app_tab_widges[each_tab_name.lower() + "_frame"],
        text=each_tab_name,
        font=GUI_SETTINGS["f"]["body"]["tabs"],
        relief=GROOVE,
        background=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["bg"],
        foreground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["fg"],
        activebackground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["abg"],
        activeforeground=GUI_SETTINGS["c"]["body"]["tabs"]["b"]["afg"],
        width=15,
        padx=10,
        # border=0, borderwidth=0,highlightthickness=0
    )
    app_tab_widges[each_tab_name.lower()].grid(row=index, column=1)
    app_tab_widges[each_tab_name.lower()][
        "command"
    ] = lambda tab_name=each_tab_name.lower(): get_current_selected_tab(tab_name)

Label(
    tab_frame, background=GUI_SETTINGS["c"]["body"]["tabs"]["bg"], padx=80, pady=85 +40
).grid(row=index + 1, column=1)




tab_working_frame = {}
for tab_name in app_tab_list:
    tab_name = tab_name.lower()
    tab_working_frame[tab_name] = Frame( working_body_frame, background=GUI_SETTINGS["c"]["body"]["work"]["bg"], width=GUI_SETTINGS["d"]["body"]["work"]["width"], height=GUI_SETTINGS["d"]["body"]["work"]["height"], border=0, borderwidth=0,highlightthickness=0)
    
    if tab_name == "main": main_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    elif tab_name == "visits": visits_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    elif tab_name == "emulation": emulation_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    elif tab_name == "proxy": proxy_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    #
    elif tab_name == "profiles": main_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    
    elif tab_name == "fingerprints": fingerprints_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    
    #
    elif tab_name == "captcha": main_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    elif tab_name == "timeouts": main_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])

    elif tab_name == "Others": utility_tab(tab_working_frame[tab_name],GUI_SETTINGS["d"]["body"]["work"])
    
    # main_tab_frame.pack(side=RIGHT, expand=False)

# Default Selected Tab
get_current_selected_tab("main")
tab_working_frame["main"].pack(side=RIGHT, expand=False)



# main_tab(working_body_frame,GUI_SETTINGS["d"]["body"]["work"])

# # fingerprints_tab(working_body_frame,GUI_SETTINGS["d"]["body"]["work"])
# # proxy_tab(working_body_frame,GUI_SETTINGS["d"]["body"]["work"])
# # main_tab(working_body_frame,GUI_SETTINGS["d"]["body"]["work"])
# # visits_tab(working_body_frame,GUI_SETTINGS["d"]["body"]["work"])
# emulation_tab(fingerprints_tab_frame,GUI_SETTINGS["d"]["body"]["work"])
# # print(GUI_SETTINGS["d"]["body"]["work"])


# def on_file_option1():
#     print("File > Option 1 clicked")


# def on_file_option2():
#     print("File > Option 2 clicked")


# def on_file_option3():
#     print("File > Option 3 clicked")


# def on_settings_option43_task1():
#     print("Settings > Option 43 > Task 1 clicked")


# def on_settings_option43_task2():
#     print("Settings > Option 43 > Task 2 clicked")


# def on_settings_option55():
#     print("Settings > Option 55 clicked")


# menubar = Menu(root)

# # File Menu
# file_menu = Menu(menubar, tearoff=0, bg="blue")
# file_menu.add_command(label="Option 1", command=on_file_option1)
# file_menu.add_command(label="Option 2", command=on_file_option2)
# file_menu.add_command(label="Option 3", command=on_file_option3)
# menubar.add_cascade(label="File", menu=file_menu)

# # Settings Menu
# settings_menu = Menu(menubar, tearoff=0)
# option43_menu = Menu(settings_menu, tearoff=0)
# option43_menu.add_command(label="Task 1", command=on_settings_option43_task1)
# option43_menu.add_command(label="Task 2", command=on_settings_option43_task2)
# settings_menu.add_cascade(label="Option 43", menu=option43_menu)
# settings_menu.add_command(label="Option 55", command=on_settings_option55)
# menubar.add_cascade(label="Settings", menu=settings_menu)


# root.config(menu=menubar)


# Footer
footer_left_frame = Frame(footer_frame, background=GUI_SETTINGS["c"]["footer"]["bg"],border=0, borderwidth=0,highlightthickness=0)
footer_left_frame.pack(side=LEFT, pady=7)
footer_right_frame = Frame(footer_frame, background=GUI_SETTINGS["c"]["footer"]["bg"],border=0, borderwidth=0,highlightthickness=0)
footer_right_frame.pack(side=RIGHT, pady=7)


# restart_BTN = Button(
#     footer_left_frame,
#     text="Restart",
#     width=15,
#     height=10,
#     font=GUI_SETTINGS["f"]["footer"],
#     # relief=SUNKEN,
#     background="#ffc926",
#     foreground="#997917",
#     activebackground="#e6b522",
#     activeforeground="#66500f",
#     border=0, borderwidth=0,highlightthickness=0
# )
# restart_BTN.pack(side=LEFT, padx=5, pady=0)
# scheduler_BTN = Button(
#     footer_left_frame,
#     text="Scheduler",
#     width=15,
#     height=10,
#     font=GUI_SETTINGS["f"]["footer"],
#     # relief=SUNKEN,
#     background="#14489b",
#     foreground="#0a244e",
#     activebackground='#103a7c',
#     activeforeground='#040e1f',
#     border=0, borderwidth=0,highlightthickness=0
# )
# scheduler_BTN.pack(side=RIGHT, padx=5, pady=0)

# cancel_BTN = Button(
#     footer_right_frame,
#     text="Cancel",
#     width=15,
#     height=10,
#     font=GUI_SETTINGS["f"]["footer"],
#     # relief=SUNKEN,
#     background="#fe6464",
#     foreground="#7f3838",
#     activebackground='#e55a5a',
#     activeforeground='#7f3232',
#     border=0, borderwidth=0,highlightthickness=0
# )
# cancel_BTN.pack(side=LEFT, padx=5, pady=0)


ok_BTN = Button(
    footer_right_frame,
    text="Ok",
    width=15,
    height=10,
    font=GUI_SETTINGS["f"]["footer"],
    # relief=SUNKEN,
    background="#24b982",
    foreground="#125d41",
    activebackground='#20a775',
    activeforeground='#166f4e',
    border=0, borderwidth=0,highlightthickness=0,
    command= making_run_command
)
ok_BTN.pack(side=RIGHT, padx=5, pady=0)


icon_img = Image.open("res/tap.png")
icon_img = icon_img.resize((32, 32), Image.LANCZOS)
icon = ImageTk.PhotoImage(icon_img)
root.iconphoto(True, icon)

root.title("Add Clicker")
root.resizable(0, 0)
root.geometry(
    f"{str(GUI_SETTINGS['d']['app']['width'])}x{str(GUI_SETTINGS['d']['app']['height'])}"
)



# if ma
root.mainloop()
