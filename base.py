from tkinter import *
from tkinter import ttk
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# pip install google-cloud
# pip install google-auth
# pip install google-auth-oauthlib
# pip install google-api-python-client
# 1w3SIDdnR9IkyYulGPLOcyWa7uANSWFQMyvz1ZCnG1XM
# https://developers.google.com/sheets/api/guides/values

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    win.deiconify()


root = Tk()
style = ttk.Style()
style.theme_use("alt")
ebg = "#363636"
fg = "#cdcdcd"
menu = [" Select a dataset", " MaliciousURLs.csv", " Add new DB server"]
root.geometry("500x220")
root.resizable(width=False, height=False)
root.title("Bhuvan & Chirag  |  IT 331 Project")
root.configure(bg="#191919")
# root.iconbitmap("cue.ico")
photo = PhotoImage(file="ico.png")
root.wm_iconphoto(False, photo)
center(root)
exit_btn = Button(root, text="EXIT", bg="#363636", fg="#fdf8e1", height=1, width=11)
exit_btn.place(x=390, y=19)
dev = Label(
    root,
    text="© 2024. Developed by Bhuvan & Chirag for professor Md Morsheful Islam.",
    font=("Arial", 10),
    bg="#191919",
    fg="#828282",
)
dev.place(x=36, y=180)
dataset_lbl = Label(root, text="DATASET", bg="#191919", fg="#828282")
dataset_lbl.place(x=20, y=21)
root.option_add("*TCombobox*Listbox*Background", ebg)
root.option_add("*TCombobox*Listbox*Foreground", fg)
root.option_add("*TCombobox*Listbox*selectBackground", fg)
root.option_add("*TCombobox*Listbox*selectForeground", ebg)
style.map("TCombobox", fieldbackground=[("readonly", ebg)])
style.map("TCombobox", selectbackground=[("readonly", ebg)])
style.map("TCombobox", selectforeground=[("readonly", fg)])
style.map("TCombobox", background=[("readonly", ebg)])
style.map("TCombobox", foreground=[("readonly", fg)])
myCombo = ttk.Combobox(root, state="readonly", values=menu)
myCombo.current(0)
# myCombo2.bind("<FocusIn>", menuFocus2)
myCombo.place(x=110, y=21)
retrieve = Button(root, text="RETRIEVE", bg="#363636", fg="#fdf8e1", height=1, width=11)
retrieve.place(x=280, y=19)
url_lbl = Label(root, text="URL", bg="#191919", fg="#828282")
url_lbl.place(x=20, y=70)
url = Text(root, height=2, width=45, bg="#131313", fg="#fdf8e1")
url.place(x=110, y=60)
isolator = Label(
    root,
    text="-----------------------------------------  RESULT  -----------------------------------------",
    bg="#191919",
    fg="#828282",
)
isolator.place(x=15, y=105)
result = Text(root, height=2, width=56, bg="#131313", fg="#fdf8e1")
result.place(x=23, y=135)
result.configure(state="disabled")
root.mainloop()
