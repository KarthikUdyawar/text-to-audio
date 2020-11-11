#import
import io
import pygame
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox

#variable
root=tk.Tk()
root.title("Text to Audio")
text_var=tk.StringVar()

#main function
def speak():

    text = text_entry.get()

    try:
        with io.BytesIO() as file:
            gTTS(text=text, lang="en").write_to_fp(file)
            file.seek(0)
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                continue

    except:
        messagebox.showerror("Error", "Please enter valid text")

    text_var.set("")

#GUI
text_label = tk.Label(root, text = 'What should i say? : ', font=('calibre', 10, 'bold'))
text_entry = tk.Entry(root,textvariable = text_var, font=('calibre',10,'normal'), width=45)

sub_btn=tk.Button(root,text = 'Speak',command = speak)

text_label.grid(row=0,column=0)
text_entry.grid(row=0,column=2)
sub_btn.grid(row=1,column=2)

root.mainloop()
