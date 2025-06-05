# 💻 PCTO GUI – Monitoraggio Pipeline Industriale

> 🔄 *Progetto sviluppato durante il Percorso per le Competenze Trasversali e l’Orientamento (PCTO)*

## 🇮🇹 Versione Italiana

Questo progetto consiste nello sviluppo di una GUI (interfaccia grafica) in **Python** per il **monitoraggio e la gestione** di una pipeline industriale simulata.  
L'interfaccia è stata realizzata con le librerie **CustomTkinter** e **Pillow (PIL)**, con l'aggiunta di **OpenCV** per future estensioni.

---

### 🛠 Tecnologie Utilizzate

- **Python**
- **CustomTkinter** – Framework moderno basato su Tkinter per GUI eleganti
- **Pillow (PIL)** – Per la gestione e manipolazione di immagini
- **OpenCV** – Importato per possibili sviluppi futuri

---

### 🎯 Obiettivi del Progetto

- Progettare un’interfaccia **multi-pagina** per il controllo di processi industriali simulati  
- Implementare una **navigazione semplice** tramite sidebar  
- Gestire **immagini**, **zoom**, **temi** e **aggiornamenti in tempo reale**  
- Visualizzare **KPI**, **anomalie** e **dati testuali** simulati o in tempo reale

---

### 📑 Funzionalità Principali

- ✅ **Sidebar Navigabile**  
  Accesso rapido a 8 sezioni: `Home`, `Settings`, `Pipeline`, `Production`, `Results`, `KPI`, `Anomalies`, `Guide`

- 🗂️ **Pagine Tabulate**  
  Ogni sezione utilizza `CTkTabview` per organizzare i contenuti in tab

- 🔍 **Zoom & Tema**  
  La sezione *Settings* permette di regolare lo zoom e scegliere il tema: `System`, `Light`, `Dark`

- 🖼️ **Gestione Immagini**  
  Caricamento e rotazione di immagini in tempo reale

- 📊 **KPI & Anomalie**  
  Visualizzazione di dati di produzione simulati

- 📘 **Guida Interattiva**  
  Pannello scrollabile con opzioni selezionabili, pulsanti e slider

---

## 🇬🇧 English Version

This project was developed as part of the **PCTO** (Work-related Learning Program) and involves creating a **Python-based GUI** for monitoring and managing a **simulated industrial pipeline**.  
The interface was built using **CustomTkinter** and **Pillow (PIL)**, with **OpenCV** imported for future extensions.

---

### 🛠 Technologies Used

- **Python**
- **CustomTkinter** – Modern GUI framework based on Tkinter
- **Pillow (PIL)** – For image processing and manipulation
- **OpenCV** – Imported for potential future upgrades

---

### 🎯 Project Objectives

- Design a **multi-page GUI** for controlling simulated industrial processes  
- Implement an intuitive **sidebar-based navigation system**  
- Handle **images**, **zoom**, **themes**, and **real-time updates**  
- Display **KPIs**, **anomalies**, and **textual data**, either simulated or real-time

---

### 📑 Key Features

- ✅ **Navigable Sidebar**  
  Quick access to 8 sections: `Home`, `Settings`, `Pipeline`, `Production`, `Results`, `KPI`, `Anomalies`, `Guide`

- 🗂️ **Tabbed Pages**  
  Each section uses `CTkTabview` to organize content in tabs

- 🔍 **Zoom & Theme Management**  
  The *Settings* page allows zoom level adjustments and theme selection (`System`, `Light`, `Dark`)

- 🖼️ **Image Handling**  
  Real-time image upload and rotation

- 📊 **KPI & Anomalies**  
  Displays simulated production data

- 📘 **Interactive Guide**  
  Scrollable panel with buttons, options, and sliders

---

## 📸 Screenshot & Demo

*WORK IN PROGRESS...*

---

## 📦 Requirments

- Python 3.10+
- `customtkinter`
- `pillow`

---

## 🚀 Project Launch

```bash
pip install customtkinter pillow opencv-python
python main.py
