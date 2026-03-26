import serial
import time

s = serial.Serial(port='COM4', baudrate=115200, timeout=2)
time.sleep(2)

while True:
    cmd = input("Comando (on/off/salir): ").strip().lower()

    if cmd == "salir":
        break

    s.write((cmd + '\n').encode())

    respuesta = s.readline().decode().strip()

    if respuesta:
        print("Respuesta:", respuesta)
    else:
        print("No llegó respuesta desde la Pico")

s.close()