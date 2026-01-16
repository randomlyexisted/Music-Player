---

# 🎵 Music Player (Python + Tkinter)

A modern **dark-themed desktop music player** built using **Python, Tkinter, and Pygame**.
It supports loading multiple audio files, playlist management, playback controls, and a vertical volume slider with a neon UI.

---

## ✨ Features

* 🎶 Play MP3 audio files
* 📂 Load multiple songs at once
* 📜 Playlist with song names
* ▶ Play / ⏸ Pause / ⏯ Resume / ⏹ Stop controls
* 🔊 Vertical volume control
* 🌙 Modern dark UI with neon accent colors
* 🖥 Desktop GUI application (no terminal required)

---

## 🛠 Technologies Used

* **Python**
* **Tkinter** – GUI
* **Pygame** – Audio playback
* **OS module** – File handling

---

## 📦 Required Libraries (for source code)

If you want to run the `.py` file directly, install:

```bash
pip install pygame
```

> Tkinter comes preinstalled with Python on Windows.

---

## ▶ How to Run (Source Code)

1. Clone or download the project
2. Open terminal in project folder
3. Run:

```bash
python basicGui_audio.py
```

---

## 🚀 Portable Version (EXE)

A **portable Windows executable** can be created using **PyInstaller**.

### Build command:

```bash
python -m PyInstaller --onefile --windowed --collect-all pygame basicGui_audio.py
```

After building, the portable app will be available at:

```
dist/basicGui_audio.exe
```

✔ Runs without Python
✔ No library installation required

---

## 🖼 User Interface

* Dark background
* Neon green highlight
* Playlist with selected track highlight
* Volume slider placed beside playback buttons

(You can add screenshots here later)

---

## ⚠ Notes

* Works on **Windows**
* Built EXE size may be large (Python bundled)
* Antivirus may flag EXE (false positive – common with PyInstaller)

---

## 📌 Future Improvements

* ⏭ Next / Previous buttons
* 🎵 Song progress bar
* 🖼 Album art display
* 🔘 Rounded buttons (CustomTkinter)
* 📁 Folder-based song loading

---

## 👤 Author

**Lakshya**
Python Desktop Application Project

---

## 📄 License

This project is for **educational and personal use**.
You may modify and extend it freely.

---
