# -*- coding: utf-8 -*-

from Tkinter import *

class Application:
    def __init__(self, master=None):
      self.widget1 = Frame(master)
      self.widget1.pack()
      self.msg = Label(self.widget1, text="Primeiro widget")
      self.msg["font"] = ("Calibri", "9", "italic")
      self.msg.pack ()
      self.sair = Button(self.widget1)
      self.sair["text"] = "Clique aqui"
      self.sair["font"] = ("Calibri", "9")
      self.sair["width"] = 10
      self.sair.bind("<Button-1>", self.mudarTexto)
      self.sair.pack ()

    def mudarTexto(self, event):
        import ipdb; ipdb.set_trace()
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Application(root)
root.mainloop()
