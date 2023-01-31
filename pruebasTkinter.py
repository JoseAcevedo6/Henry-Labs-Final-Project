from PIL import Image, ImageTk
import os
import sqlite3 as sq
from sys import platform
import customtkinter as ctk
from tkinter import ttk, LabelFrame
from tkcalendar import DateEntry
from customtkinter import CTk, E, CENTER
import matplotlib.pyplot as plt
from tkinter import StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np 

# Inicia classe App, dentro se definen todas las funciones y especificaciones de la app customtkinter 
class App():

    def __init__(self, root):
        self.root = root
        self.root.title("Olist Report Viewer")
        self.root.geometry("1130x500")
        # se setean la apariencia y el color por default de la app de customtkinter
        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("dark-blue") 
        self.db_name = 'olistDataBase.db'
        self.mainframe = ctk.CTkFrame(self.root,height=800, width=400)
        self.mainframe.grid(row=0, column=0, padx=30, pady=40,sticky=E)

        #configuración Frame Calendarios
        self.timeframe = ctk.CTkFrame(self.mainframe,height=2, width=25)
        self.timeframe.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.timestart = ctk.CTkLabel(self.timeframe, text = "Desde")
        self.timestart.grid(row = 0,column=0, padx=10, pady=10, sticky=E)
        self.timemenu = DateEntry(self.timeframe, date_pattern='yyyy-MM-dd')
        self.timemenu.delete(0, "end")
        self.timemenu.grid(row = 0,column=1, padx=10, pady=10, sticky=E)

        self.timeend = ctk.CTkLabel(self.timeframe, text = "Hasta")
        self.timeend.grid(row = 0,column=2, padx=10, pady=10, sticky=E)
        self.timemenu2 = DateEntry(self.timeframe, date_pattern='yyyy-MM-dd')
        self.timemenu2.delete(0, "end")
        self.timemenu2.grid(row = 0,column=3, padx=10, pady=10, sticky=E)

        #configuración Frame ESTADO
        self.stateframe = ctk.CTkFrame(self.mainframe,height=200, width=500)
        self.stateframe.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.state = ctk.CTkLabel(self.stateframe, text = "Estado")
        self.state.grid(row = 0,column=0, padx=10, pady=10, sticky=E)

        # configuración Menu desplegable
        estados = ['Todos','Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Brasilia', 'Espírito Santo', 'Goias', 'Maranhao', 'Mato Grosso',
            'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraíba', 'Parana', 'Pernambuco', 'Piaui', 'Rio de Janeiro', 'Rio Grande do Norte',
            'Rio Grande do Sul', 'Rondonia', 'Roraima', 'Santa Catarina', 'Sao Paulo', 'Sergipe', 'Tocantins']
        self.optionmenu_1 = ctk.CTkOptionMenu(self.stateframe,values = estados)
        self.optionmenu_1.grid(row=0, column=1, padx=10, pady=10, sticky=E)
        
        #configuración Frame CATEGORIAS
        self.categoryframe = ctk.CTkFrame(self.mainframe,height=2, width=25)
        self.categoryframe.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        self.category = ctk.CTkLabel(self.categoryframe, text = "Categoría")
        self.category.grid(row = 0,column=0, padx=10, pady=10, sticky=E)

        categorias = ['Todos','Salud y belleza', 'Accesorios de computadores', 'Automovil', 'Cama, mesa y baño', 'Decoracion y muebles', 'Ocio y deportes', 'Perfumeria',
                'Articulos del hogar', 'Telefonia', 'Relojes y regalos', 'Alimentos y bebidas', 'Bebes', 'Papeleria', 'Impresion de imagen y tablets', 'Juguetes',
                'Telefonia fija', 'Herramientas de jardin', 'Bolsos, moda y accesorios', 'Pequeños accesorios', 'Consolas y juegos', 'Audio', 'Moda y zapatos',
                'Cosas interesantes', 'Accesorios de equipaje', 'Aire acondicionado', 'Herramientas de construccion', 'Cocina, comedor, lavanderia, jardin y muebles',
                'Herramientas de construccion de jardin', 'Ropa moda hombre', 'Tienda de mascotas', 'Muebles de oficina', 'Mercado', 'Electronica', 'Electrodomesticos',
                'Suministros fiesta', 'Comodidad del hogar', 'Herramientas de construccion y herramientas', 'Agroindustria y comercio', 'Muebles, colchones y tapiceria',
                'Libros tecnicos', 'Construccion del hogar', 'Instrumentos musicales', 'Muebles de sala', 'Herramientas de construccion y luces',
                'Industria, comercio y negocios', 'Comida', 'Arte', 'Muebles de dormitorio', 'Libros de interes general', 'Herramientas de construccion y seguridad',
                'Moda, ropa interior, playa', 'Moda y deportes', 'Señalizacion y seguridad', 'Computadores', 'Suministros de navidad', 'Ropa moda mujer',
                'Electrodomesticos 2', 'Libros importados', 'Bebidas', 'Cine y fotografia', 'Cocina', 'Musica', 'Comodidad del hogar 2', 
                'Pequeños accesorios del hogar, horno y cafe', 'CDs, DVDs y musicales', 'DVDs y blu-ray', 'Flores', 'Arte y artesania', 'Pañales e higiene',
                'Moda ropa de niños', 'Seguridad y servicios', 'Computadores gamer', 'Sin dato', 'Portatiles de cocina y preparadores de comida',  'Decoracion muebles']
        self.categorymenu = ctk.CTkOptionMenu(self.categoryframe, values=categorias)
        self.categorymenu.grid(row=0, column=1, padx=10, pady=10, sticky=E)

        #Configuración Botón Predicción 
        self.predictionButton = ctk.CTkButton(self.mainframe, fg_color="transparent", 
                            border_width=2, command = self.get_ranking, text = "Predicción", height= 2, width= 25)
        self.predictionButton.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

        #configuración Frame Gráfica
        self.graphframe = ctk.CTkFrame(self.mainframe,height=3, width=25)
        self.graphframe.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan = 2)

        # configuración estilo de Treeview 
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview.Heading', background="Dark-blue")

        # Se genera Treeview
        self.tableview = ttk.Treeview(self.mainframe, height=10, columns=("#1"))
        self.tableview.grid(row=1, column=2, padx=20, pady=20, columnspan = 2)
        self.tableview.heading('#0', text='Posición')
        self.tableview.heading('#1', text='Variable')
        self.tableview.column('#0', anchor=CENTER)
        self.tableview.column('#1', anchor=CENTER)

        # configuración frame Botones   
        self.Buttonframe = ctk.CTkFrame(self.mainframe,height=2, width=25)
        self.Buttonframe.grid(row=2, column=0, padx=10, pady=10, sticky="nsew", columnspan = 4)

        #configuración de boton Categorías más vendidas
        self.buttontop10 = ctk.CTkButton(master=self.Buttonframe, fg_color="transparent", 
                            border_width=2, command = self.get_ventas, text = "Categorías más vendidas")
        self.buttontop10.grid(row=1, column=0, padx=90, pady=20, sticky="nsew")

        #configuración de boton Categorías mejor ranqueadas
        self.buttonRank = ctk.CTkButton(master=self.Buttonframe, fg_color="transparent", 
                            border_width=2, command = self.get_ranking, text = "Categorías mejor ranqueados")
        self.buttonRank.grid(row=1, column=1, padx=90, pady=20, sticky="nsew")

        #configuración de boton Estados con mayores ventas 
        self.buttonStateTop = ctk.CTkButton(master=self.Buttonframe, fg_color="transparent", 
                            border_width=2, command = self.get_region, text = "Estados con mayores ventas")
        self.buttonStateTop.grid(row=1, column=2, padx=90, pady=20, sticky="nsew")

    
    def run_query(self, query, parameters=()):
        """Esta función toma como parametros el self, una query y los parametros,
        y ejecuta una query de MySQL en python"""
        with sq.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
        return result.fetchall()

    def get_ventas(self):
        """Esta función ejecuta la query para imprimir la información del Top de ventas"""
        for widget in self.graphframe.winfo_children():
            widget.pack_forget()
        
        # Cleaning table
        records = self.tableview.get_children()
        for record in records:
            self.tableview.delete(record)


        # Consulting data
        state = self.optionmenu_1.get()
        if state == "Todos" and self.timemenu.get() == "":
            # no se cambia ninguno
            query = ('SELECT count(distinct o.order_id) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP) group by pr.product_category_name_english order by Cantidad desc limit 10') 
            db_rows = self.run_query(query)
        elif state != "Todos" and self.timemenu.get() == "":
            #cambia el estado pero no el tiempo 
            query = f'SELECT count(distinct o.order_id) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP) where g.estado = "{state}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif self.timemenu.get() != "" and state == "Todos":
            # se cambia el tiempo pero no el estado 
            query = f'SELECT count(distinct o.order_id) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP) where ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif self.timemenu.get() != "" and state != "Todos":
            # se cambia el tiempo y el estado 
            query = f'SELECT count(distinct o.order_id) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP) where g.estado = "{state}" and ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        
        # generando gráfico de ventas
        x = len(db_rows)
        valuesx = []
        valuesy = []
        for row in reversed(db_rows):
            self.tableview.insert('', 0, text=x, values = (row[1]))
            valuesx.append(row[1])
            valuesy.append(row[0])
            x -=1
        # generate the figure and plot object which will be linked to the root element
        fig, ax = plt.subplots(figsize = (6,2.5))
        #self.graphframe.quit()
        ax.barh(valuesx,valuesy)
        ax.set_title("Top 10 categorias más vendidas")
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,master=self.graphframe)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def get_ranking(self):
        """Esta función ejecuta la query para imprimir la información del Top Ranking"""
        for widget in self.graphframe.winfo_children():
            widget.pack_forget()

        # Cleaning table
        records = self.tableview.get_children()
        for record in records:
            self.tableview.delete(record)

        # Consulting data
        state = self.optionmenu_1.get()
        if state == "Todos" and self.timemenu.get() == "":
        # no cambia ninguno 
            query = 'SELECT sum(o.review_score) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on o.product_id = p.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on s.seller_id = o.seller_id inner join geolocation g on s.CEP = g.CEP group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif state != "Todos" and self.timemenu.get() == "":
        # cambia el estado pero no el tiempo 
            query = f'SELECT sum(o.review_score) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on o.product_id = p.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on s.seller_id = o.seller_id inner join geolocation g on s.CEP = g.CEP  where g.estado = "{state}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
            pass
        elif self.timemenu.get() != "" and state == "Todos":
        # cambia el tiempo pero no el estado 
            query = f'SELECT sum(o.review_score) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join  orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP)  where ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif self.timemenu.get() != "" and state != "Todos":
        # cambia el estado y el tiempo 
            query = f'SELECT sum(o.review_score) as Cantidad, pr.product_category_name_english FROM order_items o inner join products p on (o.product_id = p.product_id) inner join  orders ord on (ord.order_id = o.order_id) inner join product_category pr on (p.product_category_id = pr.product_category_id) inner join customers c on (c.customer_id = ord.customer_id) inner join geolocation g on (c.CEP = g.CEP)  where g.estado = "{state}" and ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by pr.product_category_name_english order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        # generando gráfico de ranking
        x = len(db_rows)
        valuesx = []
        valuesy = []
        for row in reversed(db_rows):
            self.tableview.insert('', 0, text=x, values = row[1])
            valuesx.append(row[1])
            valuesy.append(row[0])
            x -=1
        # generate the figure and plot object which will be linked to the root element
        fig, ax = plt.subplots(figsize = (6,2.5))
        #self.graphframe.quit()
        ax.barh(valuesx,valuesy)
        ax.set_title("Top 10 categorias mejor ranqueadas")
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,master=self.graphframe)
        canvas.draw()
        canvas.get_tk_widget().pack()
        
    def get_region(self):
        """Esta función ejecuta la query para imprimir la información del Top de ventas por Región"""
        for widget in self.graphframe.winfo_children():
            widget.pack_forget()

        # Cleaning table
        records = self.tableview.get_children()
        for record in records:
            self.tableview.delete(record)

        # Consulting data
        category = self.categorymenu.get()
        if category == "Todos" and self.timemenu.get() == "":
        # no cambia ninguno 
            query = 'SELECT count(distinct o.order_id) * o.price as Cantidad, g.cidade FROM order_items o inner join products p on p.product_id = o.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on o.seller_id = s.seller_id  inner join geolocation g on s.CEP = g.CEP group by g.cod_estado  order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif category != "Todos" and self.timemenu.get() == "":
        # cambia la categoría pero no el tiempo 
            query = f'SELECT count(distinct o.order_id) * o.price as Cantidad, g.cidade FROM order_items o inner join products p on p.product_id = o.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on o.seller_id = s.seller_id  inner join geolocation g on s.CEP = g.CEP  where pr.product_category_name_spanish = "{category}"group by g.cod_estado  order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
            pass
        elif self.timemenu.get() != "" and category == "Todos":
        # cambia el tiempo pero no la categoría
            query = f'SELECT count(distinct o.order_id) * o.price as Cantidad, g.cidade FROM order_items o inner join orders ord on ord.order_id = o.order_id inner join products p on p.product_id = o.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on o.seller_id = s.seller_id  inner join geolocation g on s.CEP = g.CEP where ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by g.cod_estado  order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        elif self.timemenu.get() != "" and category != "Todos":
        # cambia el estado y la categoría 
            query = f'SELECT count(distinct o.order_id) * o.price as Cantidad, g.cidade FROM order_items o inner join orders ord on ord.order_id = o.order_id inner join products p on p.product_id = o.product_id inner join product_category pr on p.product_category_id = pr.product_category_id inner join sellers s on o.seller_id = s.seller_id  inner join geolocation g on s.CEP = g.CEP where pr.product_category_name_spanish = "{category}" and ord.order_purchase_timestamp between "{self.timemenu.get()}" and "{self.timemenu2.get()}" group by g.cod_estado  order by Cantidad desc limit 10'
            db_rows = self.run_query(query)
        # generando gráfico de ranking
        x = len(db_rows)
        valuesx = []
        valuesy = []
        for row in reversed(db_rows):
            self.tableview.insert('', 0, text=x, values = row[1])
            valuesx.append(row[1])
            valuesy.append(row[0])
            x -=1
        # generate the figure and plot object which will be linked to the root element
        fig, ax = plt.subplots(figsize = (6,2.5))
        #self.graphframe.quit()
        ax.barh(valuesx,valuesy)
        ax.set_title("Top 10 Estados con mayores ventas")
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig,master=self.graphframe)
        canvas.draw()
        canvas.get_tk_widget().pack()


# creamos un objeto de la clase App y la ejecutamos 
if __name__ == "__main__":
    root = CTk()
    app = App(root)
    root.mainloop()