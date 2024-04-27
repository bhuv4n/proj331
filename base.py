# Importing required API libraries
from tkinter import *
from tkinter import ttk
from google.oauth2 import service_account
from googleapiclient.discovery import build


# Center the application window on screen
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


# API Call function
def retrieve():
    global res_lbl
    res_lbl.destroy()
    input_url = url.get("1.0", 'end-1c').strip()
    set = data["values"]
    present = 0
    
    # Filters API response and creates labels in application
    for i in range(0, len(set)):
        if set[i][0] == input_url:
            present += 1
            if set[i][1] == "good":
                res_lbl = Label(root, text="GREENLISTED", font="Consolas 22", bg="#191919", fg="green")
                res_lbl.place(x=160, y=130)
            else:
                res_lbl = Label(root, text="BLACKLISTED", font="Consolas 22", bg="#191919", fg="red")
                res_lbl.place(x=160, y=130)
    if present == 0:
        res_lbl = Label(root, text="UNKNOWN", font="Consolas 22", bg="#191919", fg="#828282")
        res_lbl.place(x=190, y=130)


# Initialize a root window for application
root = Tk()
# Style the window with properties
style = ttk.Style()
style.theme_use("alt")
ebg = "#363636"
fg = "#cdcdcd"
# Import Database KeyID for MaliciousURLs.csv
spid = "1w3SIDdnR9IkyYulGPLOcyWa7uANSWFQMyvz1ZCnG1XM"
# API private key credentials from local file
credentials = service_account.Credentials.from_service_account_file("key.json", scopes=[
    "https://www.googleapis.com/auth/spreadsheets"])
# Start a API listener on application host with credentials
service = build("sheets", "v4", credentials=credentials)
data = (
    # API called to read all data set upto line 333388
    service.spreadsheets()
    .values()
    .get(spreadsheetId=spid, range="A1:B333388")
    .execute()
)
# Edit some window properties like geometry and styling
root.geometry("500x220")
root.resizable(width=False, height=False)
root.title("Bhuvan & Chirag  |  IT 331 Project")
root.configure(bg="#191919")
# Set a icon for our application
photo = PhotoImage(file="ico.png")
root.wm_iconphoto(False, photo)
center(root) # Centralize the app window
# Create a button to exit the application
exit_btn = Button(root, text="EXIT", bg="#363636", fg="#fdf8e1", height=1, width=7, command=exit)
exit_btn.place(x=415, y=19)
# Create a label that specifies the project developers for professor
dev = Label(
    root,
    text="© 2024. Developed by Bhuvan & Chirag for professor Md Morshedul Islam.",
    font=("Arial", 10),
    bg="#191919",
    fg="#828282",
)
dev.place(x=36, y=180)
# Additional labels for good UI
api_lbl = Label(root, text="API_CONN", bg="#191919", fg="#828282")
api_lbl.place(x=20, y=21)
conn = Label(root, text="GoogleAPI/8393: MaliciousURLs.csv", bg="#191919", fg="#fdf8e1")
conn.place(x=105, y=21)
# Button that calls the API function
retrieve_btn = Button(root, text="RETRIEVE", bg="#363636", fg="#fdf8e1", height=1, width=10, command=retrieve)
retrieve_btn.place(x=315, y=19)
# Initialize user input for URL check 
url_lbl = Label(root, text="URL", bg="#191919", fg="#828282")
url_lbl.place(x=20, y=67)
url = Text(root, height=1, width=40, font="Consolas 12", bg="#131313", fg="#fdf8e1")
url.place(x=110, y=65)
# Styling
isolator = Label(
    root,
    text="-----------------------------------------  STATUS  -----------------------------------------",
    bg="#191919",
    fg="#828282",
)
isolator.place(x=15, y=100)
res_lbl = Label(root, text="UNKNOWN", font="Consolas 22", bg="#191919", fg="#828282")
res_lbl.place(x=190, y=130)
# Run and deploy the application on host
root.mainloop()
