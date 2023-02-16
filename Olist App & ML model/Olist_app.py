from customtkinter import CTk, CTkFrame, CTkLabel, CTkOptionMenu, CTkButton
from customtkinter import set_appearance_mode, set_default_color_theme
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import pyplot as plt, figure, colormaps as cm, ticker
from tkcalendar import DateEntry
from tkinter import ttk, TOP, BOTH
import sqlite3 as sq
import pandas as pd
import numpy as np
import joblib


# Inicia classe App, dentro se definen todas las funciones y especificaciones de la app customtkinter
class App():

    def __init__(self, root):

        self.root = root
        self.root.title("Olist Report Viewer")
        self.root.geometry("1100x560")
        self.gral_query = """
            SELECT oi.product_id, oi.seller_id, oi.shipping_limit_date, oi.price, oi.freight_value, oi.review_score,
            o.customer_id, o.order_purchase_timestamp, o.order_approved_at, o.order_delivered_carrier_date,
            o.order_delivered_customer_date, o.order_estimated_delivery_date, p.product_name_lenght,
            p.product_description_lenght, p.product_photos_qty, p.product_weight_g, p.product_length_cm,
            p.product_height_cm, p.product_width_cm, pc.product_category_id, pc.product_category_name_spanish,
            c.CEP AS CEP_customer, g_cus.cod_estado AS cod_estado_customer, g_cus.estado AS estado_customer,
            s.CEP AS CEP_seller, g_sell.cod_estado AS cod_estado_seller, op.payment_sequential, op.payment_type,
            op.payment_installments, op.payment_value
            FROM order_items oi
            JOIN orders o ON (oi.order_id = o.order_id)
            JOIN products p ON (oi.product_id = p.product_id)
            JOIN product_category pc ON (p.product_category_id = pc.product_category_id)
            JOIN customers c ON (o.customer_id = c.customer_id)
            JOIN geolocation g_cus ON (c.CEP = g_cus.CEP)
            JOIN sellers s ON (oi.seller_id = s.seller_id)
            JOIN order_payments op ON (op.order_id = o.order_id)
            JOIN geolocation g_sell ON (s.CEP = g_sell.CEP)
            WHERE o.order_status != 'canceled'
            AND o.order_delivered_customer_date != '2016-01-01 00:00:00.000000'"""

    def main_window(self):

        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.main_frame = CTkFrame(self.root, height=400, width=1030)
        self.main_frame.grid(pady=30, padx=30)  # grid(row=0, column=0)#, padx=30, pady=40, sticky=E)

        filters_frame = CTkFrame(self.main_frame, height=50, width=1000)
        filters_frame.grid(row=0, column=0, padx=10, pady=10)

        # configuración Frame Calendarios
        date_frame = CTkFrame(filters_frame, width=400)
        date_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        style = ttk.Style()
        style.theme_use('clam')  # -> uncomment this line if the styling does not work
        style.configure('my.DateEntry',
                        fieldbackground='#1F538D',
                        background='#14375E',
                        foreground='white',
                        arrowcolor='white')

        since_date_label = CTkLabel(date_frame, text="Desde", width=70)
        since_date_label.grid(row=0, column=0)

        self.since_date = DateEntry(date_frame, date_pattern='yyyy-MM-dd', width=13, style='my.DateEntry')
        self.since_date.set_date('2016-01-01')
        self.since_date.grid(row=0, column=1)

        until_date_label = CTkLabel(date_frame, text="Hasta", width=70)
        until_date_label.grid(row=0, column=2)

        self.until_date = DateEntry(date_frame, date_pattern='yyyy-MM-dd', width=13, style='my.DateEntry')
        self.until_date.grid(row=0, column=3)

        # Configuración frame estado
        state_frame = CTkFrame(filters_frame, width=200)
        state_frame.grid(row=0, column=2, padx=10, pady=10)
        state_label = CTkLabel(state_frame, text="Estado", width=70)
        state_label.grid(row=0, column=0)

        # Configuración menu desplegable
        estados = [
            'Todos', 'Acre', 'Alagoas', 'Amapa', 'Amazonas', 'Bahia', 'Ceara', 'Brasilia', 'Espírito Santo', 'Goias',
            'Maranhao', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Para', 'Paraíba', 'Parana', 'Pernambuco',
            'Piaui', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondonia', 'Roraima',
            'Santa Catarina', 'Sao Paulo', 'Sergipe', 'Tocantins']
        self.state_list = CTkOptionMenu(state_frame, values=estados, width=160)
        self.state_list.grid(row=0, column=1)

        # Configuración frame categories
        category_frame = CTkFrame(filters_frame, width=200)
        category_frame.grid(row=0, column=3, padx=10, pady=10)
        category_label = CTkLabel(category_frame, text="Categoría", width=70)
        category_label.grid(row=0, column=0)

        # Configuración menu desplegable
        categories = [
            'Todos', 'Salud y belleza', 'Accesorios de computadores', 'Automovil', 'Cama, mesa y baño',
            'Decoracion y muebles', 'Ocio y deportes', 'Perfumeria', 'Articulos del hogar', 'Telefonia',
            'Relojes y regalos', 'Alimentos y bebidas', 'Bebes', 'Papeleria', 'Impresion de imagen y tablets',
            'Juguetes', 'Telefonia fija', 'Herramientas de jardin', 'Bolsos, moda y accesorios', 'Pequeños accesorios',
            'Consolas y juegos', 'Audio', 'Moda y zapatos', 'Cosas interesantes', 'Accesorios de equipaje',
            'Aire acondicionado', 'Herramientas de construccion', 'Cocina, comedor, lavanderia, jardin y muebles',
            'Herramientas de construccion de jardin', 'Ropa moda hombre', 'Tienda de mascotas', 'Muebles de oficina',
            'Mercado', 'Electronica', 'Electrodomesticos', 'Suministros fiesta', 'Comodidad del hogar',
            'Herramientas de construccion y herramientas', 'Agroindustria y comercio', 'Muebles, colchones y tapiceria',
            'Libros tecnicos', 'Construccion del hogar', 'Instrumentos musicales', 'Muebles de sala',
            'Herramientas de construccion y luces', 'Industria, comercio y negocios', 'Comida', 'Arte',
            'Muebles de dormitorio', 'Libros de interes general', 'Herramientas de construccion y seguridad',
            'Moda, ropa interior, playa', 'Moda y deportes', 'Señalizacion y seguridad', 'Computadores',
            'Suministros de navidad', 'Ropa moda mujer', 'Electrodomesticos 2', 'Libros importados', 'Bebidas',
            'Cine y fotografia', 'Cocina', 'Musica', 'Comodidad del hogar 2',
            'Pequeños accesorios del hogar, horno y cafe', 'CDs, DVDs y musicales', 'DVDs y blu-ray', 'Flores',
            'Arte y artesania', 'Pañales e higiene', 'Moda ropa de niños', 'Seguridad y servicios',
            'Computadores gamer', 'Sin dato', 'Portatiles de cocina y preparadores de comida',  'Decoracion muebles']
        self.category_list = CTkOptionMenu(category_frame, values=categories, width=300)
        self.category_list.grid(row=0, column=1)

        # Configuración frame gráfica
        self.graph_frame = CTkFrame(self.main_frame, width=1000, height=278)
        self.graph_frame.grid(row=1, column=0, padx=10, pady=10)

        # Configuración frame toolbar
        self.toolbar_frame = CTkFrame(self.main_frame, width=240, height=42)
        self.toolbar_frame.grid(row=2, column=0, padx=10, pady=5)

        # Configuración frame botones
        button_frame = CTkFrame(self.main_frame, width=1000)
        button_frame.grid(row=3, column=0, padx=10, pady=15)

        # Configuración de boton Categorías más vendidas
        button_top_sales_category = CTkButton(
            button_frame, fg_color="transparent", width=200, border_width=2, command=self.get_sales_category,
            text="Top ventas por categoría")
        button_top_sales_category.grid(row=0, column=0, padx=10, pady=10)

        # Configuración de boton Estados con mayores ventas
        button_top_sales_estado = CTkButton(
            button_frame, fg_color="transparent", width=200, border_width=2, command=self.get_sales_state,
            text="Top ventas por estado")
        button_top_sales_estado.grid(row=0, column=1, padx=10, pady=10)

        # Configuración de boton Categorías mejor ranqueadas
        buttonRank = CTkButton(
            button_frame, fg_color="transparent", width=200, border_width=2, command=self.get_profitability_ratio,
            text="Categorías por rentabilidad")
        buttonRank.grid(row=0, column=2, padx=10, pady=10)

        # Configuración Botón Predicción
        predictionButton = CTkButton(
            button_frame, fg_color="transparent", width=200, border_width=2, command=self.get_profitability_ratio,
            text="Generar predicción")
        predictionButton.grid(row=0, column=3, padx=10, pady=10)

    def run_query(self, query):
        """Esta función toma como parametros una query, parametros de filtro en caso de necesitarse, ejecuta dicha
        query y retorna una lista de tuplas donde cada tupla es un registro de la base de datos. Si el paremetro
        'to_df' es 'True', retorna un Dataframe de Pandas con el nombre de las columnas y los registros de la query."""

        db_name = 'Olist.db'

        with sq.connect(db_name) as conexion:
            cursor = conexion.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns_names = [desc[0] for desc in cursor.description]
            result = pd.DataFrame(result, columns=columns_names)

            return result

    def graph_gen(self, query, args={}):

        def format_tooltip(x, y):
            idx = int(np.round(y))
            if idx < 0 or idx >= len(df_query):
                info_label.configure(text="")
                return ""
            y_col = df_query[args['y_col']].iloc[idx]
            x_col = df_query[args['x_col']].iloc[idx]
            agg_col = df_query[args['agg_col']].iloc[idx]
            if args['x_col'] == 'Coeficiente':
                id_prod = df_query['product_id'].iloc[idx]
                count = df_query['Cantidad'].iloc[idx]
                amount = df_query['Monto'].iloc[idx]
                info_label.configure(
                    text=args['string'] % (y_col, id_prod, count, amount, x_col, agg_col))
            else:
                info_label.configure(
                    text=args['string'] % (args['y_col'], y_col, args['xlabel'], x_col, args['agglabel'], agg_col))
            return ""

        def format_tick(value, pos):
            if value >= 1e7 and value < 1e8:
                return f'{value/1e7:.1f} B'
            elif value >= 1e6 and value < 1e7:
                return f'{value/1e6:.1f} M'
            elif value >= 1e3 and value < 1e6:
                return f'{value/1e3:.0f} K'
            else:
                return f'{value:.1f}'

        for widget in self.graph_frame.winfo_children():
            widget.pack_forget()

        for widget in self.toolbar_frame.winfo_children():
            widget.pack_forget()

        # Consulting data
        df_query = self.run_query(query)
        if args['x_col'] == 'Coeficiente':
            df_col = df_query['Coeficiente']
            df_query['Coeficiente'] = round((df_col - min(df_col)) / (max(df_col) - min(df_col)) * 10, 2)
            df_query.sort_values(by='Coeficiente', ascending=False, inplace=True)
            df_query = df_query.head(10)
            lista = [f'{b} {a}' for a, b in enumerate(df_query['Categoría'], start=1)]
            df_query['Categoría'] = lista

        df_query.sort_values(args['x_col'], inplace=True)

        # Crear una lista de colors para el gradiente
        norm = plt.Normalize(vmin=df_query[args['agg_col']].min(), vmax=df_query[args['agg_col']].max())
        colors = cm.get_cmap('Blues')(norm(df_query[args['agg_col']]))

        # Generando gráfico de ventas
        x_values = df_query[args['x_col']]
        y_values = df_query[args['y_col']]
        fig = figure.Figure(figsize=(10, 2.5))
        fig.set_facecolor('#292929')
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title(args['title'], color='white').set_position([args['titlepos'], 1.05])
        ax.barh(y=y_values, width=x_values, height=0.5, color=colors)
        ax.set_xlabel(args['xlabel'], color='white').set_position([args['xlabelpos'], 1.05])
        ax.set_ylabel(args['ylabel'], color='white')
        ax.tick_params(axis='both', colors='white')
        ax.set_facecolor('#292929')
        ax.format_coord = format_tooltip

        # Agregar una barra de colors al lado derecho del gráfico para mostrar el gradiente
        sm = plt.cm.ScalarMappable(cmap='Blues', norm=norm)
        sm._A = []
        cbar = fig.colorbar(sm, ax=ax, fraction=0.05, pad=0.05)
        cbar.ax.set_ylabel(args['agglabel'], color='white')
        cbar.ax.tick_params(axis='y', colors='white')
        cbar.ax.format_cursor_data(data='')
        cbar.ax.yaxis.set_major_formatter(ticker.FuncFormatter(format_tick))

        for spine in ax.spines.values():
            spine.set_visible(False)
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        info_label = CTkLabel(self.graph_frame, text='')
        info_label.pack()

        class MyNavigationToolbar(NavigationToolbar2Tk):
            def set_message(self, s):
                pass

        toolbar = MyNavigationToolbar(canvas, self.toolbar_frame, pack_toolbar=False)
        toolbar.update()
        toolbar.pack()

    def get_sales_category(self):

        query = f'''SELECT product_category_name_spanish AS Categoría, COUNT(*) AS Cantidad, SUM(payment_value) as Monto
            FROM ({self.gral_query})'''
        state_list = self.state_list.get()
        since_date = self.since_date.get()
        until_date = self.until_date.get()

        if state_list == "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}"
                GROUP BY Categoría ORDER BY Cantidad DESC LIMIT 10'''
        else:
            filter = f'''WHERE estado_customer = "{state_list}" AND order_purchase_timestamp BETWEEN
            "{since_date}" AND "{until_date}" GROUP BY Categoría ORDER BY Cantidad DESC LIMIT 10'''
            print(state_list)

        args = {
            'x_col': 'Cantidad', 'y_col': 'Categoría', 'agg_col': 'Monto', 'title': 'Categorías más vendidas',
            'titlepos': .4, 'xlabel': 'Cantidad de ventas', 'ylabel': 'Categorías', 'agglabel': 'Monto de ventas',
            'xlabelpos': .4, 'string': '%s: %s | %s: %d | %s: R$ %.1f'}

        self.graph_gen(query + filter, args)

    def get_sales_state(self):

        query = f'''SELECT estado_customer AS Estado, COUNT(*) AS Cantidad, SUM(payment_value) as Monto
            FROM ({self.gral_query})'''
        category_list = self.category_list.get()
        since_date = self.since_date.get()
        until_date = self.until_date.get()

        if category_list == "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}"
                GROUP BY Estado ORDER BY Cantidad DESC LIMIT 10'''
        else:
            filter = f'''WHERE product_category_name_spanish = "{category_list}" AND order_purchase_timestamp BETWEEN
            "{since_date}" AND "{until_date}" GROUP BY Estado ORDER BY Cantidad DESC LIMIT 10'''

        args = {
            'x_col': 'Cantidad', 'y_col': 'Estado', 'agg_col': 'Monto', 'title': 'Mayores ventas por estado',
            'titlepos': .47, 'xlabel': 'Cantidad de ventas', 'ylabel': 'Estados', 'agglabel': 'Monto de ventas',
            'xlabelpos': .47, 'string': '%s: %s | %s: %d | %s: R$ %.1f'}

        self.graph_gen(query + filter, args)

    def get_profitability_ratio(self):

        query = f'''SELECT product_category_name_spanish AS Categoría, product_id, COUNT(*) AS Cantidad,
            ROUND(SUM(price + freight_value), 2) AS Monto, ROUND(AVG(review_score), 2) AS Promedio,
            CAST(ROUND((AVG(review_score)*COUNT(*)*SUM(price + freight_value)), 0) AS INT) AS Coeficiente
            FROM ({self.gral_query}) '''

        state_list = self.state_list.get()
        category_list = self.category_list.get()
        since_date = self.since_date.get()
        until_date = self.until_date.get()

        if state_list == "Todos" and category_list == "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}" GROUP BY product_id
                HAVING COUNT(product_id) > 2 AND Promedio > 3.5'''

        elif state_list != "Todos" and category_list != "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}" AND
            product_category_name_spanish = "{category_list}" AND estado_customer = "{state_list}" GROUP BY product_id
            HAVING COUNT(product_id) > 1 AND Promedio > 3.5'''

        elif state_list == "Todos" and category_list != "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}" AND
            product_category_name_spanish = "{category_list}" GROUP BY product_id HAVING COUNT(product_id) > 1
            AND Promedio > 3.5'''

        elif state_list != "Todos" and category_list == "Todos":
            filter = f'''WHERE order_purchase_timestamp BETWEEN "{since_date}" AND "{until_date}" AND
            estado_customer = "{state_list}" GROUP BY product_id HAVING COUNT(product_id) > 1 AND Promedio > 3.5'''

        args = {
            'x_col': 'Coeficiente', 'y_col': 'Categoría', 'agg_col': 'Promedio',
            'title': 'Mayor rentabilidad por producto', 'titlepos': .38, 'xlabel': 'Coeficiente de rentabilidad',
            'ylabel': 'Categorías', 'agglabel': 'Promedio review score', 'xlabelpos': .38,
            'string': 'Categoría: %s | Producto: %s | Cantidad: %d | Ventas: R$ %.1f | Coeficiente: %.2f | Score: %.2f'}

        self.graph_gen(query + filter, args)

    def get_prediction(self):

        query = f"""SELECT
            product_id, seller_id, strftime('%s', shipping_limit_date) shipping_limit_date, price, freight_value,
            customer_id, strftime('%s', order_purchase_timestamp) order_purchase_timestamp,
            strftime('%s', order_approved_at) order_approved_at, strftime('%s', order_delivered_carrier_date)
            order_delivered_carrier_date, strftime('%s', order_delivered_customer_date) order_delivered_customer_date,
            strftime('%s', order_estimated_delivery_date) order_estimated_delivery_date, product_name_lenght,
            product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm,
            product_width_cm, product_category_id, CEP_customer, cod_estado_customer, CEP_seller, cod_estado_seller,
            payment_sequential, payment_type, payment_installments, payment_value  FROM ({self.gral_query})"""

        state_list = self.state_list.get()
        since_date = self.since_date.get()
        until_date = self.until_date.get()

        # Consulting data
        if state_list == "Todos" and since_date == "":
            # No se cambia ninguno
            query_spec = " AND o.order_purchase_timestamp BETWEEN DATETIME('now', '-7 days') AND DATETIME('now')"
            df_to_predict = self.run_query(self.gral_query + query_spec, to_df=True)
        elif state_list != "Todos" and since_date == "":
            # Cambia el estado pero no el tiempo
            query = f''''''
            df_to_predict = self.run_query(query, to_df=True)
        elif since_date != "" and state_list == "Todos":
            # se cambia el tiempo pero no el estado
            query = f''''''
            df_to_predict = self.run_query(query, to_df=True)
        elif since_date != "" and state_list != "Todos":
            # se cambia el tiempo y el estado
            query = f''''''
            df_to_predict = self.run_query(query, to_df=True)

        pipe = joblib.load('Olist App & ML model/GaussPipeline.pkl')
        score = pipe.predict(df_to_predict)

        df_to_predict = pd.concat([df_to_predict, score], axis=1)

        df_to_predict[['score', 'payment_value', '']]


# Creamos un objeto de la clase App y la ejecutamos
if __name__ == '__main__':
    root = CTk()
    app = App(root).main_window()
    root.mainloop()
