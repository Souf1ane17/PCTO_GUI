import customtkinter

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
        home_frame = customtkinter.CTkFrame(self)
        home_tabs = customtkinter.CTkTabview(home_frame)
        home_tabs.pack(fill="both", expand=True, padx=20, pady=20)

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

        self.pages["home"] = home_frame

        # ---- Settings Page ----
        settings_frame = customtkinter.CTkFrame(self)
        settings_tabs = customtkinter.CTkTabview(settings_frame)
        settings_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        settings_tabs.add("Zoom")
        settings_tabs.add("Theme")

        zoom_tab = settings_tabs.tab("Zoom")
        customtkinter.CTkButton(zoom_tab, text="Zoom In", command=self.zoom_in).pack(pady=10)
        customtkinter.CTkButton(zoom_tab, text="Zoom Out", command=self.zoom_out).pack(pady=10)
        customtkinter.CTkButton(zoom_tab, text="Reset Zoom", command=self.reset_zoom).pack(pady=10)

        theme_tab = settings_tabs.tab("Theme")
        customtkinter.CTkComboBox(theme_tab, values=["System", "Dark", "Light"]).pack(pady=20)

        self.pages["settings"] = settings_frame

        # ---- Pipeline Page ----
        pipeline_frame = customtkinter.CTkFrame(self)
        pipeline_tabs = customtkinter.CTkTabview(pipeline_frame)
        pipeline_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        pipeline_tabs.add("Load Config")

        load_config_tab = pipeline_tabs.tab("Load Config")
        self.config_textbox = customtkinter.CTkTextbox(load_config_tab, width=600, height=30)
        self.config_textbox.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")

        load_button = customtkinter.CTkButton(load_config_tab, text="Load", command=self.load_config)
        load_button.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        self.pages["pipeline"] = pipeline_frame

        # ---- Production Page ----
        production_frame = customtkinter.CTkFrame(self)
        production_tabs = customtkinter.CTkTabview(production_frame)
        production_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        production_tabs.add("production")
        self.pages["production"] = production_frame

        # ---- Results Page ----
        results_frame = customtkinter.CTkFrame(self)
        results_tabs = customtkinter.CTkTabview(results_frame)
        results_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        results_tabs.add("Images")
        results_tabs.add("Timings")
        timings_tab = results_tabs.tab("Timings")

        time_label = customtkinter.CTkLabel(timings_tab, text="the time is:")
        time_label.grid(row=0, column=0,  padx=20, pady=10, sticky="ew")

        time_textbox = customtkinter.CTkTextbox(timings_tab, height=30, width=200)
        time_textbox.insert("0.0", "")
        time_textbox.configure(state="disabled")
        time_textbox.grid(row=0, column=1,  padx=20, pady=10, sticky="ew")

        results_tabs.add("Charts")
        self.pages["results"] = results_frame

        # ---- KPI Page ----
        kpi_frame = customtkinter.CTkFrame(self)
        kpi_tabs = customtkinter.CTkTabview(kpi_frame)
        kpi_tabs.pack(fill="both", expand=True, padx=20, pady=20)

        kpi_tabs.add("picking counter")
        kpi_tabs.add("collision counter")
        kpi_tabs.add("cycle counter")
        kpi_tabs.add("picking rate")
        kpi_tabs.add("collision rate")

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

        self.pages["kpi"] = kpi_frame

        # ---- Anomalies Page ----
        anomalies_frame = customtkinter.CTkFrame(self)
        anomalies_tabs = customtkinter.CTkTabview(anomalies_frame)
        anomalies_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        anomalies_tabs.add("collision")
        anomalies_tabs.add("failed picking")
        self.pages["anomalies"] = anomalies_frame

        # ---- Guide Page ----
        guide_frame = customtkinter.CTkFrame(self)
        guide_tabs = customtkinter.CTkTabview(guide_frame)
        guide_tabs.pack(fill="both", expand=True, padx=20, pady=20)
        guide_tabs.add("Guide")
        self.pages["guide"] = guide_frame

        self.current_page = None

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


if __name__ == "__main__":
    app = App()
    app.mainloop()
