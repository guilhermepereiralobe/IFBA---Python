from customtkinter import *

#cg = Calculadora Geométrica.
cg = CTk()
cg.title('Calculadora Geométrica')
cg.geometry('600x400')
cg.resizable(False, False)
cg._set_appearance_mode("light")

cg_frame = CTkFrame(
    cg,
    width=600,
    height=400,
    fg_color='#ffffff',
)
cg_frame.place(x=0, y=0)

bloco_azul = CTkFrame(
    cg_frame,
    width=376,
    height=400,
    fg_color='#297ead'
)
bloco_azul.place(x=0, y=0)

geo = CTkFrame(
    cg_frame,
    width=249,
    height=166,
    border_width=2,
    corner_radius=0,
    fg_color='#ffffff',
    bg_color='#297ead',
    border_color='#000000'
)
geo.place(x=40, y=79)

conf_geo = {
    'width':30,
    'height':30,
    'border_width':2,
    'corner_radius':0,
    'fg_color':'#ffffff',
    'bg_color':'#297ead',
    'border_color':'#000000'
}

conf_linha_h = {
    'width':15,
    'height':5,
    'corner_radius':0,
    'fg_color':'#000000',
    'bg_color':'#000000'
}

conf_linha_v = {
    'width':5,
    'height':15,
    'corner_radius':0,
    'fg_color':'#000000',
    'bg_color':'#000000'
}

geo_1 = CTkFrame(
    cg_frame, **conf_geo
)
geo_1.place(x=40, y=79.5)

geo_2 = CTkFrame(
    cg_frame, **conf_geo
)
geo_2.place(x=259, y=79.5)

geo_3 = CTkFrame(
    cg_frame, **conf_geo
)
geo_3.place(x=40, y=215)

geo_4 = CTkFrame(
    cg_frame, **conf_geo
)
geo_4.place(x=259, y=215)



linha_1 = CTkFrame(
    cg_frame, **conf_linha_v
)
linha_1.place(x=166, y=72)

linha_2 = CTkFrame(
    cg_frame, **conf_linha_v
)
linha_2.place(x=157, y=72)


linha_3 = CTkFrame(
    cg_frame, **conf_linha_v
)
linha_3.place(x=157, y=235.9)

linha_4 = CTkFrame(
    cg_frame, **conf_linha_v
)
linha_4.place(x=166, y=235.9)


linha_5 = CTkFrame(
    cg_frame, **conf_linha_h
)
linha_5.place(x=32.6, y=158.7)

linha_6 = CTkFrame(
    cg_frame, **conf_linha_h
)
linha_6.place(x=281.7, y=159.5)

# Valor de h cm.
h = 2


# Valor de b cm.
b = 2


# A = b * h
a = b * h


calculo_texto = CTkLabel(
    cg_frame,
    width=0,
    height=0,
    fg_color='#297ead',
    text=f'{a} cm³ = {b} cm * {h} cm',
    font=('Impact', 22, "bold")
)
calculo_texto.place(x=60, y=325)

texto_h = CTkLabel(
    cg_frame,
    width=0,
    height=0,
    fg_color='#297ead',
    text=f'{h} cm',
    font=('Garet', 12, "bold")
)
texto_h.place(x=300, y=154)

texto_b = CTkLabel(
    cg_frame,
    width=0,
    height=0,
    fg_color='#297ead',
    text=f'{b} cm',
    font=('Garet', 12, "bold")
)
texto_b.place(x=150, y=251)

botao = CTkButton(
    cg_frame,
    width=110,
    height=37,
    corner_radius=10,
    fg_color='#dcb77d',
    bg_color='#ffffff',
    hover_color="#a1875d",
    text='Calcular',
    text_color='#000000',
    font=('Garet', 12, "bold")
)
botao.place(x=435, y=149)


entrada = {
    'width':196,
    "height":45,
    'border_width':4,
    'corner_radius':10,
    'border_color':'#000000'
}

entrada_b = CTkEntry(
    cg_frame, **entrada,
    placeholder_text='Qual o valor da base?',
    font=('Garet', 12),
)
entrada_b.place(x=392, y=40)

entrada_h = CTkEntry(
    cg_frame, **entrada,
    placeholder_text='Qual o valor da altura?',
    font=('Garet', 12)
)
entrada_h.place(x=392, y=92)

area = CTkLabel(
    cg_frame,
    width=196,
    height=46,
    corner_radius=10,
    fg_color='#ffffff',
    text=f"{a} cm³",
    font=('Garet', 18)
)
area.place(x=392, y=314)

cg.mainloop()
