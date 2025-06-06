import customtkinter
from PIL import Image
import cv2
import tkinter as tk
from tkinter import ttk
from PIL import ImageOps  
import tkinter.filedialog
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("custom.json")

# Colori che si adattano a tema chiaro/scuro
FG_LIGHT = "#F0F0F0"
FG_DARK = "#222222"
BTN_DARK = "#333333"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sidebar with TabView per Page")
        self.geometry("1100x580")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.zoom_factor = 1.0 # Inizializzo il fattore di zoom

        # ------ SIDEBAR ------
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color=(FG_LIGHT, FG_DARK))
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        for i in range(20):  # Tanti da coprire tutti i bottoni
            self.sidebar_frame.grid_rowconfigure(i, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="SIDEBAR", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="nsew")

        self.home_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Home", image=customtkinter.CTkImage(
                light_image=Image.open("img_home.png"),
                dark_image=Image.open("img_home.png"),
                size=(20, 20)
            ),
            compound="left", command=lambda: self.show_page("home"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.home_button.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        self.settings_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Settings", image=customtkinter.CTkImage(
                light_image=Image.open("setttings.png"),
                dark_image=Image.open("setttings.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("settings"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.settings_button.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")

        self.pipeline_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Pipeline", image=customtkinter.CTkImage(
                light_image=Image.open("pipeline.png"),
                dark_image=Image.open("pipeline.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("pipeline"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.pipeline_button.grid(row=3, column=0, padx=0, pady=0, sticky="nsew")

        self.production_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Production", image=customtkinter.CTkImage(
                light_image=Image.open("production.png"),
                dark_image=Image.open("production.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("production"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.production_button.grid(row=4, column=0, padx=0, pady=0, sticky="nsew")

        self.results_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Results", image=customtkinter.CTkImage(
                light_image=Image.open("results.png"),
                dark_image=Image.open("results.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("results"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.results_button.grid(row=5, column=0, padx=0, pady=0, sticky="nsew")

        self.kpi_button = customtkinter.CTkButton(
            self.sidebar_frame, text="KPI", image=customtkinter.CTkImage(
                light_image=Image.open("kpi.png"),
                dark_image=Image.open("kpi.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("kpi"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.kpi_button.grid(row=6, column=0, padx=0, pady=0, sticky="nsew")

        self.anomalies_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Anomalies", image=customtkinter.CTkImage(
                light_image=Image.open("anomalies.png"),
                dark_image=Image.open("anomalies.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("anomalies"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.anomalies_button.grid(row=7, column=0, padx=0, pady=0, sticky="nsew")

        self.guide_button = customtkinter.CTkButton(
            self.sidebar_frame, text="Guide", image=customtkinter.CTkImage(
                light_image=Image.open("guide.png"),
                dark_image=Image.open("guide.png"),
                size=(20, 20)
            ),
            command=lambda: self.show_page("guide"),
            fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
            hover_color=("gray70", "gray30"), anchor="w"
        )
        self.guide_button.grid(row=8, column=0, padx=0, pady=0, sticky="nsew")
        

        self.pages = {}

        self.update_button_text_colors()

        # Ascolta i cambi di tema per aggiornare i colori dei bottoni sidebar dinamicamente
        self.bind('<<CTkThemeChanged>>', lambda e: self.update_button_text_colors())

        # ---- HOME PAGE  ----

        home_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")

        def add_buttons(tab, labels, spacing=0.07):
            for i, label in enumerate(labels):
                b = customtkinter.CTkButton(tab, text=label, corner_radius=40, height=40, border_spacing=15,hover_color=("gray70", "gray30"), fg_color = BTN_DARK)
                tab.grid_columnconfigure(0, weight=1)
                tab.grid_columnconfigure(2, weight=1)
                b.grid(row=i, column=1, padx=20, pady=10, sticky="ew")

        home_tabs.add("pipeline")
        add_buttons(home_tabs.tab("pipeline"), ["start", "restart", "stop"])

        home_tabs.add("AI pipeline")
        add_buttons(home_tabs.tab("AI pipeline"), ["start", "restart", "stop"])

        home_tabs.add("pick and place cycle")
        add_buttons(home_tabs.tab("pick and place cycle"), ["start", "restart", "stop"])

        home_tabs.add("kpis")
        add_buttons(home_tabs.tab("kpis"), [
            "picking rate", "AI pipeline time", "pick and place cycle time"
        ])

        self.pages["home"] = home_tabs

        # ---- SETTINGS PAGE ----

        settings_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        settings_tabs.add("Zoom")
        settings_tabs.add("Theme")

        zoom_tab = settings_tabs.tab("Zoom")
        zoom_tab.grid_columnconfigure(0, weight=1)
        customtkinter.CTkButton(zoom_tab, text="Zoom In", command=self.zoom_in, corner_radius=40, height=40,hover_color=("gray70", "gray30"), fg_color = BTN_DARK).grid(row=0, column=0, padx=20, pady=10, sticky="")
        customtkinter.CTkButton(zoom_tab, text="Zoom Out", command=self.zoom_out, corner_radius=40, height=40,hover_color=("gray70", "gray30"), fg_color = BTN_DARK).grid(row=1, column=0, padx=20, pady=10, sticky="")
        customtkinter.CTkButton(zoom_tab, text="Reset Zoom", command=self.reset_zoom, corner_radius=40, height=40, hover_color=("gray70", "gray30"), fg_color = BTN_DARK).grid(row=2, column=0, padx=20, pady=10, sticky="")
        
        theme_tab = settings_tabs.tab("Theme")
        self.theme = customtkinter.CTkComboBox(theme_tab, values=["System", "Dark", "Light"], command = self.set_theme)
        self.theme.set("System")
        self.theme.pack(pady = 20)
        self.pages["settings"] = settings_tabs

        # ---- PIPELINE PAGE ----

        pipeline_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        pipeline_tabs.add("Load Config")

        load_config_tab = pipeline_tabs.tab("Load Config")
        load_config_tab.grid_columnconfigure(0, weight=1)
        load_config_tab.grid_columnconfigure(1, weight=0)
        self.config_textbox = customtkinter.CTkTextbox(load_config_tab, width=600, height=30, corner_radius=10, fg_color=BTN_DARK)        
        self.config_textbox.grid(row=0, column=0,  padx=20, pady=10, sticky="")

        load_button = customtkinter.CTkButton(
            load_config_tab, 
            text="Load", 
            command=self.open_file_dialog,
            corner_radius=40, height=40, border_spacing=15,
            hover_color=("gray70", "gray30"), fg_color = BTN_DARK
        )
        load_button.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="")

        self.pages["pipeline"] = pipeline_tabs

        # ---- PRODUCTION PAGE ----

        production_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        production_tabs.add("production")
        self.pages["production"] = production_tabs

        # ---- RESULTS PAGE ----

        results_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        results_tabs.add("Images")
        images_tab = results_tabs.tab("Images")
        results_tabs.add("Timings")
        timings_tab = results_tabs.tab("Timings")

        time_label = customtkinter.CTkLabel(timings_tab, text="the time is:")
        time_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")

        time_textbox = customtkinter.CTkTextbox(timings_tab, height=25, width=175, corner_radius=20, fg_color = BTN_DARK)
        time_textbox.insert("0.0", "")
        time_textbox.configure(state="disabled")
        time_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        results_tabs.add("Charts")
        charts_tab = results_tabs.tab("Charts")
        charts_frame = customtkinter.CTkFrame(charts_tab)
        charts_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Parametri per l'asse y fisso
        ymin = 0
        ymax = 20

        # Lista iniziale (puoi cambiare la lunghezza della finestra visibile)
        self.x_data = list(range(10))
        self.y_data = [random.randint(ymin, ymax) for _ in self.x_data]

        self.fig, self.ax = plt.subplots(figsize=(7, 4))
        self.line, = self.ax.plot(self.x_data, self.y_data, marker="o", color="#FFD700", label='Serie 1')
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Data")
        self.ax.legend()

        # Asse Y fisso, tick ogni 2
        self.ax.set_ylim(ymin, ymax)
        self.ax.set_yticks(range(ymin, ymax + 1, 2))

        self.canvas = FigureCanvasTkAgg(self.fig, master=charts_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        def update_chart():
            # Aggiungi nuovo punto, togli il primo per scorrere la finestra
            self.x_data.append(self.x_data[-1] + 1)
            self.x_data.pop(0)
            self.y_data.append(random.randint(ymin, ymax))
            self.y_data.pop(0)
            self.line.set_data(self.x_data, self.y_data)
            # NON modificare limiti Y o tick, così rimangono fissi
            self.ax.set_xlim(self.x_data[0], self.x_data[-1])
            self.canvas.draw()
            self.after(1000, update_chart)
        update_chart()
        self.pages["results"] = results_tabs

        # ------ IMAGES & UPTADING IMAGES --------

        self.image1_path = "img1.jpeg"
        pil_image = Image.open(self.image1_path)
        self.image1 = customtkinter.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500, 500))

        # Crea un frame per contenere l'immagine dentro la tab Images
        self.image1_frame = customtkinter.CTkFrame(images_tab)
        self.image1_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.image1_path = "img1.jpeg"
        pil_image = Image.open(self.image1_path)
        self.image1 = customtkinter.CTkImage(light_image=pil_image, dark_image=pil_image, size=(500, 500))

        self.image1_frame = customtkinter.CTkFrame(images_tab, fg_color="transparent")
        self.image1_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        images_tab.grid_rowconfigure(0, weight=1)
        images_tab.grid_columnconfigure(0, weight=1)

        self.image1_label = customtkinter.CTkLabel(self.image1_frame, image=self.image1, text="")
        self.image1_label.place(relx=0.5, rely=0.5, anchor="center")

        self.rotation_angle = 0
        
        def update_image():
            try:
                pil_img = Image.open("img1.jpeg").resize((500, 500))
                self.rotation_angle = (self.rotation_angle + 90) % 360
                pil_img = pil_img.rotate(self.rotation_angle)
                updated_image = customtkinter.CTkImage(light_image=pil_img, dark_image=pil_img, size=(500, 500))
                self.image1_label.configure(image=updated_image)
                self.image1_label.image = updated_image 
            except Exception as e:
                print("Errore durante aggiornamento immagine:", e)
            self.after(1000, update_image)
        update_image()  # avvia il loop

        # ---- KPI PAGE ----

        kpi_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        kpi_tabs.add("picking counter")
        kpi_tabs.add("collision counter")
        kpi_tabs.add("cycle counter")
        kpi_tabs.add("picking rate")
        kpi_tabs.add("collision rate")

        picking_counter_tab = kpi_tabs.tab("picking counter")
        picking_counter_label = customtkinter.CTkLabel(picking_counter_tab, text="the picking counter is:")
        picking_counter_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        picking_counter_textbox = customtkinter.CTkTextbox(picking_counter_tab, height=30, width=200,corner_radius=20, fg_color = BTN_DARK)
        picking_counter_textbox.insert("0.0", "")
        picking_counter_textbox.configure(state="disabled")
        picking_counter_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        collision_counter_tab = kpi_tabs.tab("collision counter")
        collision_counter_label = customtkinter.CTkLabel(collision_counter_tab, text="the collision counter is:")
        collision_counter_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        collision_counter_textbox = customtkinter.CTkTextbox(collision_counter_tab, height=30, width=200,corner_radius=20, fg_color = BTN_DARK)
        collision_counter_textbox.insert("0.0", "")
        collision_counter_textbox.configure(state="disabled")
        collision_counter_textbox.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        cycle_counter_tab = kpi_tabs.tab("cycle counter")
        cycle_counter_label = customtkinter.CTkLabel(cycle_counter_tab, text="the cycle counter is:")
        cycle_counter_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        cycle_counter_textbox = customtkinter.CTkTextbox(cycle_counter_tab, height=30, width=200,corner_radius=20, fg_color = BTN_DARK)
        cycle_counter_textbox.insert("0.0", "")
        cycle_counter_textbox.configure(state="disabled")
        cycle_counter_textbox.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        picking_rate_tab = kpi_tabs.tab("picking rate")
        picking_rate_label = customtkinter.CTkLabel(picking_rate_tab, text="the picking rate is:")
        picking_rate_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        picking_rate_textbox = customtkinter.CTkTextbox(picking_rate_tab, height=30, width=200,corner_radius=20, fg_color = BTN_DARK)
        picking_rate_textbox.insert("0.0", "")
        picking_rate_textbox.configure(state="disabled")
        picking_rate_textbox.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        collision_rate_tab = kpi_tabs.tab("collision rate")
        collision_rate_label = customtkinter.CTkLabel(collision_rate_tab, text="the collision rate is:")
        collision_rate_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        collision_rate_textbox = customtkinter.CTkTextbox(collision_rate_tab, height=30, width=200,corner_radius=20, fg_color = BTN_DARK)
        collision_rate_textbox.insert("0.0", "")
        collision_rate_textbox.configure(state="disabled")
        collision_rate_textbox.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        self.pages["kpi"] = kpi_tabs

        # ---- ANOMALIES PAGE ----
        anomalies_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        anomalies_tabs.add("collision")
        anomalies_tabs.add("failed picking")

        # Stile per la tabella
        # Miglioramento estetico mantenendo la palette nero/bianco

        style = ttk.Style()
        style.theme_use("clam") 
        style.configure(
            "Custom.Treeview", 
            background="#18181b",           # Celle: nero profondo ma non assoluto (meglio per contrasto)
            foreground="#F0F0F0",           # Testo celle
            rowheight=34,                   # Più spazio tra le righe
            fieldbackground="#18181b",      # Sfondo area vuota
            font=("Segoe UI", 13),
            borderwidth=0,                  # Nessun bordo visibile
            relief="flat"
        )
        style.configure(
            "Custom.Treeview.Heading", 
            background="#101014",           # Intestazione ancora più scura
            foreground="#FFFFFF",           # Testo intestazione bianco
            font=("Segoe UI", 14, "bold"),
            borderwidth=0,
            relief="flat"
        )
        style.map("Custom.Treeview", 
            background=[("selected", "#222e50")],    # Blu notte per la selezione
            foreground=[("selected", "#ffffff")]
        )
        style.layout("Custom.Treeview", [
            ('Treeview.treearea', {'sticky': 'nswe'})  # Rimuove i margini esterni
        ])

        # Tabella per "collision"
        collision_tab = anomalies_tabs.tab("collision")
        collision_table_frame = customtkinter.CTkFrame(
            collision_tab, fg_color="#22252a", corner_radius=16
        )
        collision_table_frame.pack(fill="x", padx=32, pady=24)

        collision_label = customtkinter.CTkLabel(
            collision_table_frame, 
            text="Storico Collisioni", 
            font=("Segoe UI", 17, "bold"), 
            text_color="#FFFFFF"
        )
        collision_label.pack(anchor="w", padx=18, pady=(14, 6))

        collision_columns = ("ID", "Timestamp", "Descrizione")
        collision_tree = ttk.Treeview(
            collision_table_frame, 
            columns=collision_columns, 
            show="headings", 
            height=6, 
            style="Custom.Treeview"
        )
        for col in collision_columns:
            collision_tree.heading(col, text=col)
            collision_tree.column(col, anchor="center", stretch=True, width=90 if col=="ID" else 230)
        # Alternanza colori riga (zebra)
        collision_tree.tag_configure("oddrow", background="#23242a")
        collision_tree.tag_configure("evenrow", background="#18181b")

        collision_tree.insert("", "end", values=("1", "2025-06-06 12:00", "Collisione"), tags=("oddrow",))
        collision_tree.insert("", "end", values=("2", "2025-06-06 12:04", "Collisione"), tags=("evenrow",))
        collision_tree.insert("", "end", values=("3", "2025-06-06 12:10", "Collisione"), tags=("oddrow",))

        collision_tree.pack(fill="x", expand=True, padx=12, pady=(0, 12))

        # Tabella per "failed picking"
        failed_picking_tab = anomalies_tabs.tab("failed picking")
        failed_picking_table_frame = customtkinter.CTkFrame(
            failed_picking_tab, fg_color="#22252a", corner_radius=16
        )
        failed_picking_table_frame.pack(fill="x", padx=32, pady=24)

        failed_label = customtkinter.CTkLabel(
            failed_picking_table_frame, 
            text="Storico Presa Fallita", 
            font=("Segoe UI", 17, "bold"), 
            text_color="#FFFFFF"
        )
        failed_label.pack(anchor="w", padx=18, pady=(14, 6))

        failed_picking_columns = ("ID", "Timestamp", "Descrizione")
        failed_picking_tree = ttk.Treeview(
            failed_picking_table_frame, 
            columns=failed_picking_columns, 
            show="headings", 
            height=6, 
            style="Custom.Treeview"
        )
        for col in failed_picking_columns:
            failed_picking_tree.heading(col, text=col)
            failed_picking_tree.column(col, anchor="center", stretch=True, width=90 if col=="ID" else 230)
        failed_picking_tree.tag_configure("oddrow", background="#23242a")
        failed_picking_tree.tag_configure("evenrow", background="#18181b")

        failed_picking_tree.insert("", "end", values=("1", "2025-06-06 12:01", "Presa fallita"), tags=("oddrow",))
        failed_picking_tree.insert("", "end", values=("2", "2025-06-06 12:10", "Presa fallita"), tags=("evenrow",))
        failed_picking_tree.insert("", "end", values=("3", "2025-06-06 12:15", "Presa fallita"), tags=("oddrow",))

        failed_picking_tree.pack(fill="x", expand=True, padx=12, pady=(0, 12))
        self.pages["anomalies"] = anomalies_tabs

        # ---- GUIDE PAGE ----
        guide_tabs = customtkinter.CTkTabview(self, fg_color = "transparent")
        guide_tabs.add("Guide")
        self.pages["guide"] = guide_tabs

        guide_tab = guide_tabs.tab("Guide")

        scrollable_guide_frame = customtkinter.CTkScrollableFrame(guide_tab, fg_color=(FG_LIGHT, FG_DARK))
        scrollable_guide_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.radio_var = customtkinter.StringVar(value="Option 1")

        radio_label = customtkinter.CTkLabel(scrollable_guide_frame, text="Select an option:")
        radio_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

        radio1 = customtkinter.CTkRadioButton(scrollable_guide_frame, text="Option 1", variable=self.radio_var, value="Option 1")
        radio1.grid(row=2, column=0,  padx=20, pady=10, sticky="ew")

        radio2 = customtkinter.CTkRadioButton(scrollable_guide_frame, text="Option 2", variable=self.radio_var, value="Option 2")
        radio2.grid(row=3, column=0,  padx=20, pady=10, sticky="ew")

        radio3 = customtkinter.CTkRadioButton(scrollable_guide_frame, text="Option 3", variable=self.radio_var, value="Option 3")
        radio3.grid(row=4, column=0,  padx=20, pady=10, sticky="ew")

        def print_selected_option():
            print("Selected:", self.radio_var.get())

        print_button = customtkinter.CTkButton(scrollable_guide_frame, text="Print Selection", command=print_selected_option, corner_radius=20, height=40, border_spacing=15,hover_color=("gray70", "gray30"), fg_color = BTN_DARK)
        print_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.current_page = None

        slider_bar_label = customtkinter.CTkLabel(scrollable_guide_frame, text="ZOOM")
        slider_bar_label.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        slider_bar = customtkinter.CTkSlider(scrollable_guide_frame)
        slider_bar.grid(row=7, column=0, padx=20, pady=10, sticky="ew")

        checkBox_label = customtkinter.CTkLabel(scrollable_guide_frame, text="CHECK BOX")
        checkBox_label.grid(row=8, column=0, padx=20, pady=10, sticky="ew")
        checkBox1 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 1")
        checkBox1.grid(row=9, column=0, padx=20, pady=10, sticky="ew")
        checkBox2 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 2")
        checkBox2.grid(row=10, column=0, padx=20, pady=10, sticky="ew")
        checkBox3 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 3")
        checkBox3.grid(row=11, column=0, padx=20, pady=10, sticky="ew")

        seg_button_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "SEGMENTED BUTTON")
        seg_button_label.grid(row=12, column=0, padx=20, pady=10, sticky="ew")
        seg_button = customtkinter.CTkSegmentedButton(scrollable_guide_frame, values = ["VALUE 1", "VALUE 2", "VALUE 3"])
        seg_button.grid(row=13, column=0, padx=20, pady=10, sticky="ew")
        
        progress_bar_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "PROGRESSBAR")
        progress_bar_label.grid(row=14, column=0, padx=20, pady=10, sticky="ew")
        progress_bar = customtkinter.CTkProgressBar(scrollable_guide_frame)
        progress_bar.grid(row=15, column=0, padx=20, pady=10, sticky="ew")

        textbox_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "TEXTBOX")
        textbox_label.grid(row=16, column=0, padx=20, pady=10, sticky="ew")
        guide_textbox = customtkinter.CTkTextbox(scrollable_guide_frame, width = 300, fg_color=BTN_DARK)
        guide_textbox.grid(row=17, column=0, padx=20, pady=10, sticky="nsew")

        switch_frame = customtkinter.CTkFrame(scrollable_guide_frame, fg_color = "#7f7f7f" )
        switch_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        
        switch = customtkinter.CTkSwitch(master=switch_frame, text="Switch 1",)
        switch.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        switch2 = customtkinter.CTkSwitch(master=switch_frame, text="Switch 2",)
        switch2.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        switch3 = customtkinter.CTkSwitch(master=switch_frame, text="Switch 3",)
        switch3.grid(row=0, column=2, padx=20, pady=10, sticky="ew")

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.grid_forget()
        page = self.pages.get(page_name)
        if page:
            page.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
            self.current_page = page

    def zoom_in(self):
        self.zoom_factor = min(self.zoom_factor + 0.1, 2.0)
        customtkinter.set_widget_scaling(self.zoom_factor)
        customtkinter.set_window_scaling(self.zoom_factor)
        print(f"Zoom In: fattore attuale = {self.zoom_factor:.2f}")

    def zoom_out(self):
        self.zoom_factor = max(self.zoom_factor - 0.1, 0.7)
        customtkinter.set_widget_scaling(self.zoom_factor)
        customtkinter.set_window_scaling(self.zoom_factor)
        print(f"Zoom Out: fattore attuale = {self.zoom_factor:.2f}")

    def reset_zoom(self):
        self.zoom_factor = 1.0
        customtkinter.set_widget_scaling(self.zoom_factor)
        customtkinter.set_window_scaling(self.zoom_factor)
        print("Reset Zoom (fattore = 1.0)")

    def load_config(self):
        content = self.config_textbox.get("0.0", "end").strip()
        print(f"Loading config:\n{content}")

    def open_file_dialog(self):
        file_path = tkinter.filedialog.askopenfilename(
            title="Seleziona file di configurazione",
            filetypes=[("Tutti i file", "*.*")]
        )
        if file_path:
            self.config_textbox.delete("0.0", "end")
            self.config_textbox.insert("0.0", file_path)

    def update_button_text_colors(self):
        mode = customtkinter.get_appearance_mode()
        if mode == "Dark":
            text_color = "white"
        else:
            text_color = "black"
        buttons = [
            self.home_button,
            self.settings_button,
            self.pipeline_button,
            self.production_button,
            self.results_button,
            self.kpi_button,
            self.anomalies_button,
            self.guide_button
        ]
        for btn in buttons:
            btn.configure(text_color=text_color)

    def set_theme(self, new_theme):
        customtkinter.set_appearance_mode(new_theme)
        self.update_button_text_colors()


if __name__ == "__main__":
    app = App()
    app.mainloop()