import customtkinter
from PIL import Image
import os
import sqlite3 as sq

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    db_name = 'olist.db'
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{700}x{380}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((3, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


                # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/graph.png"), size = [450,220])
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)



        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Producto")
        self.entry.grid(row=3, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, command = self.open_input_dialog_event)
        self.main_button_1.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")


        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Ventas")
        self.tabview.add("Score")
        self.tabview.add("Tab 3")
        self.tabview.tab("Ventas").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Score").grid_columnconfigure(0, weight=1)


        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("Ventas"))
        self.textbox.grid(row=0, column=0, padx=20, pady=(20, 10))




      

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def run_query(self, query, parameters=()):
        with sq.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            result = cursor.execute(query, parameters)
            conexion.commit()
            #  conexion.close()

        return result

    def get_product(self):

        # Consulting data
        query = 'SELECT * FROM city ORDER BY name DESC'
        db_rows = self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text=row[1], values=row[2])

if __name__ == "__main__":
    app = App()
    app.mainloop()