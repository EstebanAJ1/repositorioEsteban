import os
from os import system

def create():
    system("python -m pip install --upgrade pip")
    system("python -m pip --version")
    system("python -m pip install --user virtualenv")
    system("python -m pip install numpy")
    system("python -m pip install matplotlib")
    system("python -m pip install pandas")
    system("python -m pip install scipy")
    system("python -m pip install mne")
    system("python -m pip install Seaborn")
    system("python -m pip install pingouin")
    system("python -m pip install opencv-python")
    print("Su entorno esta listo para ser utilizado")

create()
   