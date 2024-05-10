import tkinter
import customtkinter
from tkinter import PhotoImage
import qrcode

def startDownload():
    try:
        urlLink = link.get()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(urlLink)
        qr.make(fit = True)  
        img = qr.make_image(fill_color="black", back_color="white")
        img.save('MyQRCode.png')
    except:
        print("There was an error generating the qr code for this link")
    print("Download Complete!")
#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Qodo")
photo = PhotoImage(file = "./QODO LOGO.png")
app.iconphoto(True,photo)
app.iconbitmap()

##Add ui elements
title = customtkinter.CTkLabel(app,text = "Enter the url you want as a QR code: ")
title.pack(padx = 10,pady = 10)

##add link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width = 350,height=40,textvariable=url_var)
link.pack()

##download button
download = customtkinter.CTkButton(app,text="Convert to QRcode",command=startDownload)
download.pack()

##run app
app.mainloop()




