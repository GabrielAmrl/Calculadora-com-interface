from tkinter import *
from tkinter import ttk

# Cores
background_color = "#303030"
button_color = "#2c2c2c"
button_text_color = "#ffffff"
text_color = "#ffffff"
text_entry_color = "#424242"
display_color = "#212121"
button_hover_color = "#505050"
button_active_color = "#d32f2f"

janela = Tk()
janela.title('')
janela.geometry('235x318')
janela.configure(bg=background_color)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

# Frames
frame_tela = Frame(janela, width=235, height=56, bg=background_color)
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=235, height=340, bg=background_color)
frame_quadros.grid(row=2, column=0, sticky=NW)

# Variáveis
expression = StringVar()
expression.set("")

def enter_value(event):
    current_expression = expression.get()
    current_expression += str(event)
    expression.set(current_expression)

def clear_display():
    expression.set("")

def square():
    try:
        result = str(eval(expression.get() + "**2"))
        expression.set(result)
    except:
        expression.set("Error")

def calculate():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

def power():
    current_expression = expression.get()
    current_expression += "**"
    expression.set(current_expression)

# Display
display = Entry(frame_tela, textvariable=expression, width=16, font=('Helvetica', 18), bg=display_color, fg=text_color, bd=0, justify="right")
display.pack()

# Lista de botões e suas posições
buttons = [
    ('C', 0, 0, clear_display),
    ('x²', 59, 0, square),
    ('%', 118, 0, lambda: enter_value('%')),
    ('/', 177, 0, lambda: enter_value('/')),
    ('7', 0, 52, lambda: enter_value('7')),
    ('8', 59, 52, lambda: enter_value('8')),
    ('9', 118, 52, lambda: enter_value('9')),
    ('*', 177, 52, lambda: enter_value('*')),
    ('4', 0, 104, lambda: enter_value('4')),
    ('5', 59, 104, lambda: enter_value('5')),
    ('6', 118, 104, lambda: enter_value('6')),
    ('-', 177, 104, lambda: enter_value('-')),
    ('1', 0, 156, lambda: enter_value('1')),
    ('2', 59, 156, lambda: enter_value('2')),
    ('3', 118, 156, lambda: enter_value('3')),
    ('+', 177, 156, lambda: enter_value('+')),
    ('0', 0, 208, lambda: enter_value('0')),
    ('.', 59, 208, lambda: enter_value('.')),
    ('^', 118, 208, power),  # Botão para elevação à potência
    ('=', 177, 208, calculate)
]

# Criação dos botões usando loop
for text, x, y, command in buttons:
    Button(frame_quadros, text=text, width=5, height=2, bg=button_color, fg=button_text_color,
           font=('Helvetica', 14), relief=FLAT, activebackground=button_active_color,
           activeforeground=button_text_color, bd=0, highlightthickness=0, padx=2, pady=2,
           command=command).place(x=x, y=y)

janela.mainloop()
