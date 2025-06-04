import customtkinter
#from PIL import Image
import cv2

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sidebar with TabView per Page")
        self.geometry("1100x580")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(10, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Sidebar", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_buttons = [
            ("home", lambda: self.show_page("home")),
            ("settings", lambda: self.show_page("settings")),
            ("pipeline", lambda: self.show_page("pipeline")),
            ("production", lambda: self.show_page("production")),
            ("results", lambda: self.show_page("results")),
            ("kpi", lambda: self.show_page("kpi")),
            ("anomalies", lambda: self.show_page("anomalies")),
            ("guide", lambda: self.show_page("guide")),
        ]

        for index, (text, command) in enumerate(self.sidebar_buttons, start=1):
            button = customtkinter.CTkButton(self.sidebar_frame, text=text, command=command)
            button.grid(row=index, column=0, padx=20, pady=10, sticky="ew")

        self.pages = {}

        # ---- Home Page ----
        home_tabs = customtkinter.CTkTabview(self)
        #home_tabs = customtkinter.CTkTabview(home_tabs)
        #home_tabs.pack(fill="both", expand=True, padx=20, pady=20)

        def add_buttons(tab, labels, spacing=0.07):
            for i, label in enumerate(labels):
                b = customtkinter.CTkButton(tab, text=label)
                b.place(relx=0.5, rely=0.3 + i * spacing, anchor="center")

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
        settings_tabs = customtkinter.CTkTabview(self)
        #settings_tabs = customtkinter.CTkTabview(settings_frame)
        #settings_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        settings_tabs.add("Zoom")
        settings_tabs.add("Theme")

        zoom_tab = settings_tabs.tab("Zoom")
        customtkinter.CTkButton(zoom_tab, text="Zoom In", command=self.zoom_in).pack(pady=10)
        customtkinter.CTkButton(zoom_tab, text="Zoom Out", command=self.zoom_out).pack(pady=10)
        customtkinter.CTkButton(zoom_tab, text="Reset Zoom", command=self.reset_zoom).pack(pady=10)

        theme_tab = settings_tabs.tab("Theme")
        self.theme = customtkinter.CTkComboBox(theme_tab, values=["System", "Dark", "Light"], command = self.set_theme)
        self.theme.set("System")
        self.theme.pack(pady = 20)
        self.pages["settings"] = settings_tabs


        # ---- PIPELINE PAGE ----
        pipeline_tabs = customtkinter.CTkTabview(self)
        #pipeline_tabs = customtkinter.CTkTabview(pipeline_frame)
        #pipeline_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        pipeline_tabs.add("Load Config")
        # ------ TEXTBOX PIPELINE PAGE -----
        load_config_tab = pipeline_tabs.tab("Load Config")
        self.config_textbox = customtkinter.CTkTextbox(load_config_tab, width=600, height=30)
        self.config_textbox.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")

        load_button = customtkinter.CTkButton(load_config_tab, text="Load", command=self.load_config)
        load_button.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        self.pages["pipeline"] = pipeline_tabs

        # ---- PRODUCTION PAGE ----
        production_tabs = customtkinter.CTkTabview(self)
        #production_tabs = customtkinter.CTkTabview(production_frame)
        #production_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        production_tabs.add("production")
        self.pages["production"] = production_tabs

        # ---- RESULTS PAGE ----
        results_tabs = customtkinter.CTkTabview(self)
        #results_tabs = customtkinter.CTkTabview(results_frame)
        #results_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        results_tabs.add("Images")
        images_tab = results_tabs.tab("Images")
        results_tabs.add("Timings")
        timings_tab = results_tabs.tab("Timings")

        # ------ TEXTBOX RESULTS PAGE -------
        time_label = customtkinter.CTkLabel(timings_tab, text="the time is:")
        time_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")

        time_textbox = customtkinter.CTkTextbox(timings_tab, height=30, width=200)
        time_textbox.insert("0.0", "")
        time_textbox.configure(state="disabled")
        time_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        results_tabs.add("Charts")
        self.pages["results"] = results_tabs

        # ------ IMAGES --------

        img_path = "C:/Users/soufi/OneDrive/Desktop/PCTO/PCTO_GUI/img1.jpg"

        #pil_image = Image.open(img_path)
        open_image = cv2.imread(img_path)

        image1 = customtkinter.CTkImage(light_image=open_image, dark_image=open_image, size=(300, 300))
        image1_label = customtkinter.CTkLabel(images_tab, image = image1)
        image1_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        # ---- KPI PAGE ----
        kpi_tabs = customtkinter.CTkTabview(self)
        #kpi_tabs = customtkinter.CTkTabview(kpi_frame)
        #kpi_tabs.pack(fill="both", expand=True, padx=20, pady=20)

        kpi_tabs.add("picking counter")
        kpi_tabs.add("collision counter")
        kpi_tabs.add("cycle counter")
        kpi_tabs.add("picking rate")
        kpi_tabs.add("collision rate")

        #  ----- TEXTBOX KPI PAGE ------
        picking_counter_tab = kpi_tabs.tab("picking counter")
        picking_counter_label = customtkinter.CTkLabel(picking_counter_tab, text="the picking counter is:")
        picking_counter_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        picking_counter_textbox = customtkinter.CTkTextbox(picking_counter_tab, height=30, width=200)
        picking_counter_textbox.insert("0.0", "")
        picking_counter_textbox.configure(state="disabled")
        picking_counter_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        collision_counter_tab = kpi_tabs.tab("collision counter")
        collision_counter_label = customtkinter.CTkLabel(collision_counter_tab, text="the collision counter is:")
        collision_counter_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        collision_counter_textbox = customtkinter.CTkTextbox(collision_counter_tab, height=30, width=200)
        collision_counter_textbox.insert("0.0", "")
        collision_counter_textbox.configure(state="disabled")
        collision_counter_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        cycle_counter_tab = kpi_tabs.tab("cycle counter")
        cycle_counter_label = customtkinter.CTkLabel(cycle_counter_tab, text="the cycle counter is:")
        cycle_counter_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        cycle_counter_textbox = customtkinter.CTkTextbox(cycle_counter_tab, height=30, width=200)
        cycle_counter_textbox.insert("0.0", "")
        cycle_counter_textbox.configure(state="disabled")
        cycle_counter_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        picking_rate_tab = kpi_tabs.tab("picking rate")
        picking_rate_label = customtkinter.CTkLabel(picking_rate_tab, text="the picking rate is:")
        picking_rate_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        picking_rate_textbox = customtkinter.CTkTextbox(picking_rate_tab, height=30, width=200)
        picking_rate_textbox.insert("0.0", "")
        picking_rate_textbox.configure(state="disabled")
        picking_rate_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        collision_rate_tab = kpi_tabs.tab("collision rate")
        collision_rate_label = customtkinter.CTkLabel(collision_rate_tab, text="the collision rate is:")
        collision_rate_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")
        collision_rate_textbox = customtkinter.CTkTextbox(collision_rate_tab, height=30, width=200)
        collision_rate_textbox.insert("0.0", "")
        collision_rate_textbox.configure(state="disabled")
        collision_rate_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        self.pages["kpi"] = kpi_tabs

        # ---- Anomalies Page ----
        anomalies_tabs = customtkinter.CTkTabview(self)
        #anomalies_tabs = customtkinter.CTkTabview(anomalies_frame)
        #anomalies_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        anomalies_tabs.add("collision")
        anomalies_tabs.add("failed picking")
        self.pages["anomalies"] = anomalies_tabs

        # ---- Guide Page ----
        guide_tabs = customtkinter.CTkTabview(self)
        #guide_tabs = customtkinter.CTkTabview(guide_frame)
        #guide_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        guide_tabs.add("Guide")
        self.pages["guide"] = guide_tabs

        guide_tab = guide_tabs.tab("Guide")

        # ----- SCROLLBAR ------ 
        scrollable_guide_frame = customtkinter.CTkScrollableFrame(guide_tab)
        scrollable_guide_frame.pack(fill="both", expand=True, padx=10, pady=10)

        #   ----- RADIO BUTTON ------
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

        print_button = customtkinter.CTkButton(scrollable_guide_frame, text="Print Selection", command=print_selected_option)
        print_button.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.current_page = None

        #  ------ SLIDER BAR ------
        slider_bar_label = customtkinter.CTkLabel(scrollable_guide_frame, text="ZOOM")
        slider_bar_label.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        slider_bar = customtkinter.CTkSlider(scrollable_guide_frame)
        slider_bar.grid(row=7, column=0, padx=20, pady=10, sticky="ew")

        #  ------ CHECK BOX ------
        checkBox_label = customtkinter.CTkLabel(scrollable_guide_frame, text="CHECK BOX")
        checkBox_label.grid(row=8, column=0, padx=20, pady=10, sticky="ew")
        checkBox1 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 1")
        checkBox1.grid(row=9, column=0, padx=20, pady=10, sticky="ew")
        checkBox2 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 2")
        checkBox2.grid(row=10, column=0, padx=20, pady=10, sticky="ew")
        checkBox3 = customtkinter.CTkCheckBox(scrollable_guide_frame, text = "OPTION 3")
        checkBox3.grid(row=11, column=0, padx=20, pady=10, sticky="ew")

        # ------- SEGMENTED BUTTON --------
        seg_button_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "SEGMENTED BUTTON")
        seg_button_label.grid(row=12, column=0, padx=20, pady=10, sticky="ew")
        seg_button = customtkinter.CTkSegmentedButton(scrollable_guide_frame, values = ["VALUE 1", "VALUE 2", "VALUE 3"])
        seg_button.grid(row=13, column=0, padx=20, pady=10, sticky="ew")
        
        # ----- PROGRESSBAR -----
        progress_bar_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "PROGRESSBAR")
        progress_bar_label.grid(row=14, column=0, padx=20, pady=10, sticky="ew")
        progress_bar = customtkinter.CTkProgressBar(scrollable_guide_frame)
        progress_bar.grid(row=15, column=0, padx=20, pady=10, sticky="ew")

        # ------ TEXTBOX -------
        textbox_label = customtkinter.CTkLabel(scrollable_guide_frame, text = "TEXTBOX")
        textbox_label.grid(row=16, column=0, padx=20, pady=10, sticky="ew")
        guide_textbox = customtkinter.CTkTextbox(scrollable_guide_frame, width = 300)
        guide_textbox.grid(row=17, column=0, padx=20, pady=10, sticky="nsew")

        # ------ SWITCH ------
        switch_frame = customtkinter.CTkFrame(scrollable_guide_frame, fg_color = "#7f7f7f" )
        switch_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        
        switch = customtkinter.CTkSwitch(master=switch_frame, text="Switch 1",)
        switch.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        switch2 = customtkinter.CTkSwitch(master=switch_frame, text="Switch 2",)
        switch2.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        switch3 = customtkinter.CTkSwitch(master=switch_frame, text="Switch 3",)
        switch3.grid(row=0, column=2, padx=20, pady=10, sticky="ew")




    def switch_event():
        print("Switch toggled:", switch_var.get())

    def show_page(self, page_name):
        if self.current_page:
            self.current_page.grid_forget()
        page = self.pages.get(page_name)
        if page:
            page.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
            self.current_page = page

    def zoom_in(self):
        print("Zoom In")

    def zoom_out(self):
        print("Zoom Out")

    def reset_zoom(self):
        print("Reset Zoom")

    def load_config(self):
        content = self.config_textbox.get("0.0", "end").strip()
        print(f"Loading config:\n{content}")
    
    def set_theme(self, new_theme):
            customtkinter.set_appearance_mode(new_theme)


if __name__ == "__main__":
    app = App()
    app.mainloop()
