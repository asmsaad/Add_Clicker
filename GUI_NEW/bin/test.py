from tkinter import *
from tkinter import scrolledtext
import re, time
from threading import Thread

global LAST_LINE 
LAST_LINE = 0

global text


def highlight_info():
    #INFO
    text.tag_configure("info", foreground="#3e7cba", font=("Consolas", 10, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")

    while True:
        pos = text.search(r"[ INFO]"+' ', "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+6c")  # Move to end of matched pattern
        text.tag_add("info", "matchStart", "matchEnd")

    text.tag_configure("debug", foreground="#ae673e", font=("Consolas", 10, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")


    #DEBUG
    while True:
        pos = text.search(r"[DEBUG]"+' ', "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+7c")  # Move to end of matched pattern
        text.tag_add("debug", "matchStart", "matchEnd")

    text.tag_configure("error", foreground="red", font=("Consolas", 10, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")

    while True:
        pos = text.search(r"[ERROR]"+' ', "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+7c")  # Move to end of matched pattern
        text.tag_add("error", "matchStart", "matchEnd")


    #DATE TIME
    text.tag_configure("datetime", foreground="#5e9148", font=("Consolas", 10, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")
    text.tag_remove("datetime", "1.0", "end")  # Remove previous highlights

    while True:
        pos = text.search(r"\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}:\d{2}", "matchEnd", stopindex="end", regexp=True)
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+19c")  # Move to end of matched pattern
        text.tag_add("datetime", "matchStart", "matchEnd")






def terminal_log_view(base_frame):
    global text
    # Create a scrolled text widget with a vertical scrollbar
    text = scrolledtext.ScrolledText(base_frame, wrap="word", bg="#1f1f1f", foreground="#aeabae", font=("Consolas", 10, "normal"))
    text.pack(expand=True, fill="both")


    thread = Thread(target=update_log_terminal, args=())
    thread.start()





def update_log_terminal():
    global text
    global LAST_LINE 

    while True:
        with open("adclicker.log", 'br') as RF:
            data = RF.read().decode('utf-8')  # Change 'utf-8' to the appropriate encoding if needed
        RF.close()

        data_ = data.split('\n')
        LAST_LINE_ = len(data_)

        

        # print(LAST_LINE , LAST_LINE_)
   

        if LAST_LINE_ != LAST_LINE:
            text.delete("1.0", "end")
            text.insert("end", '\n'.join(data_))
            highlight_info()
            text.yview_moveto(1.0)

            LAST_LINE = LAST_LINE_

        time.sleep(2.5)







if __name__ == '__main__':
    root = Tk()

    terminal_log_view(root)
    root.mainloop()
