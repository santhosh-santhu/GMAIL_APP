from tkinter import *
from tkinter.scrolledtext import ScrolledText
import smtplib
from PIL import ImageTk,Image


def btn_clicked():
    get_1 = sender_box.get()
    store_get_1 = get_1
    
    get_2 = password.get()
    store_get_2 = get_2

    get_3 = receiver_box.get()
    store_get_3 = get_3

    get_4 = mess_box.get()
    store_get_4 = get_4

    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(store_get_1,store_get_2)
        server.sendmail(store_get_1,store_get_3,store_get_4)
        statement_1 = "MAIL HAS BEEN SENT SUCCESSFULLY"
        return statement_1
    except:
        statement_2 = "SOMETHING WENT WRONG"
        return statement_2

def disp_mess(btn_clicked):
    display['text'] = btn_clicked()

window = Tk()
window.title("Email_App")
window.geometry('500x400')


filename = Image.open("C:\\Users\\Santh\\Desktop\\background1.jpg")
background = ImageTk.PhotoImage(filename)
background_img = Label(image =background)
background_img.pack()


sender = Label(text = "Sender Email", fg = "black", bg= "#DCDCDC")
sender.place(relx = 0.023, rely = 0.1)

sender_box = Entry(font = 20)
sender_box.place(relx = 0.3, rely = 0.1, relwidth = 0.6)

sender_password = Label(text = "Password", bg = "#DCDCDC", fg = "black")
sender_password.place(relx = 0.023, rely = 0.25)

password = Entry(font = 20)
password.place(relx = 0.3, rely = 0.25, relwidth = 0.6)

receiver = Label(text = "Recipient Email", bg = "#DCDCDC", fg = "black")
receiver.place(relx = 0.023, rely = 0.4)

receiver_box = Entry(font = 20)
receiver_box.place(relx = 0.3, rely = 0.4, relwidth = 0.6)

message_label = Label(text = "Message Box", bg = "#E6E6FA", fg = "black")
message_label.place(relx = 0.4, rely = 0.5)


mess_box = Entry(justify = 'left')
mess_box.place(relx = 0.023, rely = 0.58, relwidth = 0.95, relheight = 0.2)

button = Button(text = "SEND", bg = "white",fg = "blue", command = lambda:disp_mess(btn_clicked))
button.place(relx = 0.85, rely = 0.9)

display = Label( bg = "white", fg = "black", font = "italic")
display.place(relx = 0.023, rely = 0.9, relheight = 0.07, relwidth = 0.8)


window.mainloop()
