from customtkinter import *

#cg = Calculadora Geométrica.
cg = CTk()
cg.title('Calculadora Geométrica')

cg.geometry('600x400')
cg.register(False, False)
cg._set_appearance_mode("light")
cg._disable_macos_dark_title_bar()

cg.mainloop()
