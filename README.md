# KeyLogger ![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.6%2B-brightgreen) ![Status](https://img.shields.io/badge/status-active-success)

> **DISCLAIMER:** This tool is for educational use only. Misuse of this software can lead to legal consequences. Do not use this on devices you do not own or without proper authorization.

---

## 📚 Table of Contents

- [📌 Overview](#-overview)
- [✨ Features](#-features)
- [🧠 How It Works](#-how-it-works)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [📦 Installation](#-installation)
  - [▶️ Usage](#️-usage)
  - [🛑 Stopping](#-stopping)
- [🗂️ File Structure](#️-file-structure)
- [🧩 Project Roadmap](#-project-roadmap)
- [🛠️ Customization Ideas](#️-customization-ideas)
- [🧪 Sample Output](#-sample-output)
- [⚖️ Disclaimer](#️-disclaimer)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

## 📌 Overview

This project is a simple keylogger implemented in Python using the `pynput` library. It captures all keystrokes pressed on the keyboard and stores them in a log file for later analysis. 

This project is useful for:
- Monitoring your own typing activity
- Developing security and monitoring tools
- Understanding how key event capturing works in Python

It **does not** provide advanced hiding techniques, so it's best used in controlled or experimental environments.

---

## ✨ Features

- ✔️ Real-time keystroke capture
- ✔️ Lightweight and minimal
- ✔️ Logs stored in plain text format
- ✔️ Symbolic representation of special keys
- ✔️ Easy to understand and extend
- ✔️ Platform-independent (Windows/Linux/macOS)

---

## 🧠 How It Works

The tool uses `pynput.keyboard.Listener` to hook into global keyboard events. Whenever a key is pressed:
- It's captured in the `on_press()` callback
- Keys are formatted appropriately
- Appends each keystroke with timestamp into `log.txt`

This continues until the script is manually stopped.

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.6 or higher
- OS: Windows / Linux / macOS

### 📦 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/TheGodAnnihilator/KeyLogger.git
cd KeyLogger
pip install pynput
```

### ▶️ Usage

To start logging:

```bash
python keylogger.py
```

This will create a `log.txt` file where all keystrokes will be stored.

### 🛑 Stopping

Use `Ctrl+C` in the terminal to stop logging, or terminate the process using Task Manager / Activity Monitor.

---

## 🗂️ File Structure

```
KeyLogger/
├── keylogger.py       # Core logic for keylogging
├── log.txt            # File where keystrokes are stored
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (pynput)
```

---

## 🧩 Project Roadmap

| Version | Feature/Task                            | Status       |
|---------|------------------------------------------|--------------|
| 1.0     | Basic keylogger with local logging       | ✅ Completed |
| 1.1     | Timestamped entries                      | ✅ Completed |
| 1.2     | Session-wise log files                   | 🔜 Planned   |
| 1.3     | Encrypt logs                             | 🔜 Planned   |
| 1.4     | Auto-start on system boot (Windows)      | 🔜 Planned   |
| 2.0     | Send logs via email                      | 🔜 Planned   |

---

## 🛠️ Customization Ideas

You can extend the project by adding:
- 🔒 Encrypted log files using AES
- 📩 Email/SMS log delivery
- 🖥️ Logging current window title
- 🧑‍💻 GUI toggle for starting/stopping keylogger
- 📊 Dashboard to view analytics of typed keys
- 🧹 Auto-delete logs older than N days

---

## 🧪 Sample Output

```
2025-07-11 09:23:14 - Key pressed: a
2025-07-11 09:23:14 - Key pressed: b
2025-07-11 09:23:15 - Key pressed: Key.space
2025-07-11 09:23:15 - Key pressed: c
2025-07-11 09:23:16 - Key pressed: Key.enter
```

The log is plain and human-readable, with timestamps.

---

## ⚖️ Disclaimer

> This software is intended **only for educational and ethical testing purposes**.  
> You must **not** use this tool on machines you do not own or without the user's consent.  
> The creator of this software is **not responsible for any misuse or damages** caused by this code.

---

## 👨‍💻 Author

- **TheGodAnnihilator**  
GitHub: [@TheGodAnnihilator](https://github.com/TheGodAnnihilator)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it—while giving proper attribution.

---
