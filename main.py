import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.ttk import Combobox
import gtts
import tkinter.scrolledtext as Sc
import playsound
import pyttsx3
import os
import threading
import downlibrary
import PIL
from PIL import Image,ImageTk
import webbrowser

# downlibrary.install_laibrary()        # Run It at First Time You Run This Program......



class text_to_speach(tk.Tk):
    
    
    def read_text(self):
     try:
        gay_list=["zh-tw(Mandarin/Tiwan)","zh-cn(Mandarin/China)","en-au(English/Australia)","en-uk(English/United Kingom)","en-us(English/United State)",
                  "km(Khmer/Cambodian)","es-es(Spanish(Spain))","es-us(Spanish(United States))"]
        
        self.text=self.fill_text.get("0.1","end")
        
        if self.lang_combo.get()=="":
            messagebox.showinfo("Error","Enter Text To Read and Save It.....")
     
        elif self.lang_combo.get() in gay_list:
             Sound=gtts.gTTS(self.text,lang=f'{self.lang_combo.get()[0:5]}',lang_check=True)

             Sound.save(f"{self.home_directory}\\Desktop\\{self.lang_combo.get()[0:5]}.mp3")
             
             playsound.playsound(f"{self.home_directory}\\Desktop\\{self.lang_combo.get()[0:5]}.mp3")
             
             messagebox.showinfo("Succssfully","YOUR SOUND IS FINISHED\nCHECK YOUR DESKTOP\n\n..........")
             
        else:
             Sound=gtts.gTTS(self.text,lang=f'{self.lang_combo.get()[0:2]}',lang_check=True)
 
             Sound.save(f"{self.home_directory}\\Desktop\\{self.lang_combo.get()[0:2]}.mp3")
             playsound.playsound(f"{self.home_directory}\\Desktop\\{self.lang_combo.get()[0:2]}.mp3")
             messagebox.showinfo("Succssfully","YOUR SOUND IS FINISHED\nCHECK YOUR DESKTOP\n\n..........")
     except:
         messagebox.showerror("Error","1)Make Sure From Your Internet\n\n2)Select Correct Laguage With Correct Text\n\n3)Enter Text To Read And Convert It To Sound\n\n4)Try To Be More Smart :)\n\n...........")
        

        
        
    def speak(self):
        if self.fill_text.get("0.1","end")==" ":
            messagebox.showinfo("Empty Text","No Text Found To Read...")
        else:
         self.wel.say(self.fill_text.get("0.1","end"))
         self.wel.runAndWait()
         
    def thraed_sound(self):
        threading.Thread(target=self.speak).start()
        
    
    def thresd_download_sound(self):
        threading.Thread(target=self.read_text).start()    
        
    def open_git(self):
        webbrowser.open_new_tab("https://github.com/KILLER-RAMADAN")
        
    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/ahmed-ramadan-9b5a32221/")
        
        
        
    def __init__(self):
        super().__init__()
        
        # playsound.playsound("images//welcome.mp3")
        
        
        self.geometry("800x600+400+50")
        
        self.title("Text To Speach [BY Ahmed Ramadan]")
        
        self.iconbitmap("images//tts.ico")
        
        self.configure(bg="whitesmoke")
        
        
        self.resizable(0,0)
        
        self.attributes("-topmost",True)
        
        self.home_directory=os.path.expanduser( '~' )
        
        self.git_img=ImageTk.PhotoImage(Image.open("images//git.png").resize((30,30)))
        
        self.linkedin_img=ImageTk.PhotoImage(Image.open("images//link.png").resize((30,30)))
        
        self.logo_img=ImageTk.PhotoImage(Image.open("images//logo.png").resize((600,100)))
        
        #=============Lable==============#

        self.header_lable=tk.Label(text="Free Text-To-Speech and Text-to-MP3 for Arabic",font=("courier",20,"bold"),bg="whitesmoke",fg="black")
        
        self.header_lable.pack(fill="x")
        
        
        self.header_logo_lable=tk.Label(image=self.logo_img,bg="whitesmoke")
        
        self.header_logo_lable.place(x=100,y=33)
        
        
        self.down_lable=tk.Label(text="""Input limit: 3,000 characters / Don't forget to turn on your speakers :-)

Hint:\n   If you finish a sentence, leave a space after the dot before the next one starts for better \npronunciation.\n\nWith Best Regards 'Ahmed Ramadan'""",font=("courier",10,"bold"),bg="whitesmoke",fg="black")
        
        self.down_lable.place(x=0,y=475)
        
        #=============Lable==============#
        
        
        
        #=============Components==============#
        self.fill_text=Sc.ScrolledText()
        self.fill_text['font']=("courier",15,"bold")
        self.fill_text.place(x=87,y=141,width=630,height=300)
        self.fill_text.insert("0.1","Hello Man Click On Read To Read Me....")
        
        
        self.lang_combo=ttk.Combobox(width=20,height=10,cursor="hand2",state= "readonly",font=("courier",15,"bold"),background="white",foreground="black")
        self.lang_combo.place(x=87,y=445)
        self.lang_combo["values"]=("ar(Arabic)","en(English)","bn(Bengali)","ca(catalan)","zh(Chinses)","zh-cn(Mandarin/China)","zh-tw(Mandarin/Tiwan)","hr(Coratian)",
        "cs(Czech)","da(Danish)","nl(Dutch)","en-au(English/Australia)","en-uk(English/United Kingom)","en-us(English/United State)","fi(Finnish)",
        "fr(French)","de(German)","el(Greek)","hi(Hindi)","hu(Hungarian)","is(Icelandic)","id(Indonesian)","it(Italian)","ja(Japanese)",
        "km(Khmer/Cambodian)","ko(Korean)","sq(Albanian)",
        "la(Latin)","lv(Latvian)","no(Nowegian)",
        "pl(Polish)","pt(Portuguese)","ro(Romanian)","ru(Russian)","sr(Serbian)",
        "si(Sinhala)","sk(Slovak)","es(Spanish)","es-es(Spanish(Spain))",
        "es-us(Spanish(United States))","sw(Swahili)",
        "sv(Swedish)","ta(Tamil)","th(Thai)",
        "tr(Turkish)","uk(Ukrainian)","vi(Vietnamese)")
        
        self.lang_combo.set("ar(Arabic)")
        
        
        
        self.read_button=tk.Button(text="Read",command=self.thraed_sound,width=20,font=("courier",10,"bold"),relief="solid",bg="white",fg="black",activeforeground="black")
        
        self.read_button.place(x=360,y=445)
        
        
        self.Download_button=tk.Button(text="Download aS MP3",command=self.thresd_download_sound,width=20,font=("courier",10,"bold"),relief="solid",bg="white",fg="black",activeforeground="black")
        
        self.Download_button.place(x=548,y=445)
        
        
        self.wel=pyttsx3.Engine()
        self.voices=self.wel.getProperty("voices")
        self.rate=self.wel.setProperty("rate",150)
        self.set_voice=self.wel.setProperty("voice",self.voices[0].id)
        
        
        self.git_button=tk.Button(image=self.git_img,command=self.open_git,bg="whitesmoke",activebackground="whitesmoke",relief="flat",bd=0)
        self.git_button.place(x=750,y=553)
        
        
        self.link_button=tk.Button(image=self.linkedin_img,command=self.open_linkedin,bg="whitesmoke",activebackground="whitesmoke",relief="flat",bd=0)
        self.link_button.place(x=700,y=553)
        
        #=============Components==============#
        
        
        




#=============Run_App==========#
app=text_to_speach()
app.mainloop()    
#=============Run_App==========#