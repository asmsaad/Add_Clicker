import tkinter as tk
import re

def highlight_info(event):
    text.tag_configure("info", foreground="#405db1" ,  font=("Helvetica", 8, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")
    # text.tag_remove("info", "1.0", "end")  # Remove previous highlights

    while True:
        pos = text.search(r"[ INFO]", "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+6c")  # Move to end of matched pattern
        text.tag_add("info", "matchStart", "matchEnd")

    text.tag_configure("debug", foreground="orange" , font=("Helvetica", 8, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")

    while True:
        pos = text.search(r"[DEBUG]"+' ', "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+6c")  # Move to end of matched pattern
        text.tag_add("debug", "matchStart", "matchEnd")

    
    text.tag_configure("error", foreground="red" , font=("Helvetica", 8, "bold"))  # Configure tag for highlighting
    text.mark_set("matchStart", "1.0")
    text.mark_set("matchEnd", "1.0")

    while True:
        pos = text.search(r"[ERROR]"+' ', "matchEnd", stopindex="end")
        if not pos:
            break
        text.mark_set("matchStart", pos)
        text.mark_set("matchEnd", f"{pos}+6c")  # Move to end of matched pattern
        text.tag_add("error", "matchStart", "matchEnd")


    text.tag_configure("datetime", foreground="#c5ebe8" , font=("Helvetica", 8, "bold"))  # Configure tag for highlighting
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

root = tk.Tk()
root.title("Highlighting '[INFO]' in Text Widget")

text = tk.Text(root, wrap="word", bg="#1f1f1f", foreground="#4c4c4c" , font=("Helvetica", 8, "bold"))
text.pack(expand=True, fill="both")

text.insert("end", "This is a sample text. [INFO] This part will be highlighted.\n")

# Bind the highlight_info function to the KeyRelease event
text.bind("<KeyRelease>", highlight_info)

root.mainloop()
