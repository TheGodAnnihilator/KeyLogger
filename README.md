n
# KeyLogger

> A Python-based keylogger that captures keystrokes, system information, and screenshots, and sends them via email.

[![License: Not specified](https://img.shields.io/badge/License-Not%20specified-yellow.svg)](https://github.com/TheGodAnnihilator/KeyLogger)
[![GitHub stars](https://img.shields.io/github/stars/TheGodAnnihilator/KeyLogger?style=social)](https://github.com/TheGodAnnihilator/KeyLogger)

## Description

This keylogger is designed to monitor keyboard input, gather system information, and capture screenshots. It saves keystrokes to a log file, collects details about the host machine (including hostname, IP address, operating system, and processor), and takes screenshots of the active screen. All this information is then sent to a specified email address. The collected data can be optionally encrypted before being emailed. Finally, the keylogger attempts to remove the original log files to conceal its activity.

## ✨ Key Features

- **Keystroke Logging:** Records all keystrokes and saves them to a text file (`key_log.txt`).
- **System Information Gathering:** Collects and saves system information such as hostname, IP address, operating system, and processor details to a text file (`syseminfo.txt`).
- **Screenshot Capture:** Takes screenshots of the active screen and saves them as a PNG image (`screenshot.png`).
- **Email Reporting:** Sends collected keystrokes, system information, and screenshots to a predefined email address.
- **File Encryption:** Encrypts the keylog, system information, and clipboard data using Fernet encryption before emailing.
- **Data Removal:** Attempts to delete the log files and screenshots after sending them via email to remove traces of activity.

## 🛠️ Technology Stack

- **Frontend:** N/A
- **Backend:** Python
- **Database:** N/A

## 🚀 Getting Started

### Prerequisites

- Python 3.6+ (Required for libraries such as `pynput`, `cryptography`, `scipy`, and `sounddevice`)
- `pip` (Python package installer)

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/TheGodAnnihilator/KeyLogger
    ```
2.  Navigate to the project directory:
    ```sh
    cd KeyLogger
    ```
3.  Install dependencies:
    ```sh
    pip install pynput cryptography Pillow requests scipy sounddevice
    ```
                
### Running the Project
```sh
python main.py
```

## 🤝 Contributing

Contributions are welcome! Please check the [issues page](https://github.com/TheGodAnnihilator/KeyLogger/issues) for ways to contribute.

## 📝 License

This project is licensed under the **Not specified**.
