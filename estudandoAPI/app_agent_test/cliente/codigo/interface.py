import os
from tkinter import *

import PIL
from PIL import Image, ImageTk
from codigo import executionrow
from pystray import MenuItem as item
import pystray
app = Tk()
class interface:
    def __init__(self):
        
        app.title("Agente Sesop")
        app.geometry("300x260")
        app.resizable(False, False)

        integer = 1
        decimal = 0

        app.tk.call('wm', 'iconphoto', app._w, PhotoImage(file="./cliente/image/TRE-MG.png"))

        datetime = executionrow.dateandhour()
        datetime = datetime.split(" ")

        # Container Label do Titulo
        title = Label(app)
        title["text"] = "AGENTE SESOP"
        title["font"] = "Rockwell", "20", "bold"

        # Container Linha no Canvas
        line = Canvas(app)
        line["height"] = 10
        line.create_line(0, 5, 300, 5)

        # Container Label da versão
        version = Label(app)
        version["text"] = "versão {}.{}".format(integer, decimal)

        # Container Label da consulta
        collect = Label(app)
        collect["text"] = "ÚLTIMA COLETA"
        collect["font"] = "Rockwell", "14"

        # Container Label da hora
        lb_time = Label(app)
        lb_time["text"] = "HORA:"
        lb_time["font"] = "Rockwell", "11"

        # Container Listbox da hora
        time = Listbox(app)
        time["font"] = "Rockwell", "10"
        time["width"] = 10
        time["height"] = 1
        time.insert(END, datetime[1])

        # Container Label do dia
        lb_date = Label(app)
        lb_date["text"] = "DATA:"
        lb_date["font"] = "Rockwell", "11"

        # Container Listbox do dia
        date = Listbox(app)
        date["font"] = "Rockwell", "10"
        date["width"] = 10
        date["height"] = 1
        date.insert(END, datetime[0])

        # Grid
        title.grid(column=0, row=0, columnspan=3)
        version.grid(column=1, row=1)
        line.grid(column=1, row=2, ipady=10)
        collect.grid(column=1, row=4)
        lb_time.grid(column=1, row=5, sticky="w")
        time.grid(column=1, row=5, sticky="e")
        lb_date.grid(column=1, row=6, sticky="w")
        date.grid(column=1, row=6, sticky="e")

        # Grid Pagina
        app.grid_columnconfigure(0, minsize=25, weight=50)
        app.grid_columnconfigure(1, minsize=200, weight=200)
        app.grid_columnconfigure(2, minsize=25, weight=50)

        app.grid_rowconfigure(0, minsize=40)
        app.grid_rowconfigure(1, minsize=20)
        app.grid_rowconfigure(2, minsize=10)
        app.grid_rowconfigure(3, minsize=10)
        app.grid_rowconfigure(4, minsize=50)
        app.grid_rowconfigure(5, minsize=50)
        app.grid_rowconfigure(6, minsize=50)

        app.protocol("WM_DELETE_WINDOW", interface.hide_window)

        app.mainloop()
        

    # Função para sair da janela
    def quit_window(icon, item):
        icon.stop()
        app.destroy()

    # Função para mostrar a janela novamente
    def show_window(icon, item):
        icon.stop()
        app.after(0, app.deiconify)

    # função para reiniciar
    def reload_window(icon, item):
        interface.quit_window

    def open_log():
        executionrow.commandspowershell("notepad.exe ./cliente/loguru.txt")


    # Esconder a janela e mostrar na barra de tarefas do sistema
    def hide_window():
        app.withdraw()
        image = PIL.Image.open("./cliente/image/AgenteSesop.ico")
        menu = (item("Fechar", interface.quit_window), 
        item("Abrir", interface.show_window),
        item("reload", interface.reload_window),
        item("log", interface.open_log))
        icon = pystray.Icon("name", image, "Agente Sesop", menu)
        icon.run()

        
interface()