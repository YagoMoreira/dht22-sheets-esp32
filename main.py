import dht
from machine import Pin
import time
import network
import urequests  # biblioteca para requisições HTTP

# --- CONFIG WiFi ---
SSID = "Wokwi-GUEST"
PASSWORD = ""
print("Conectando-se ao Wi-Fi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(SSID, PASSWORD)

while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.1)
print(" Conectado!")

# --- CONFIG Google Sheets ---
# coloque aqui a URL gerada no Apps Script
URL = "https://script.google.com/macros/s/AKfycbwTs53kn8JmXAzQRr3H-9w6heRC7I6YdZh4AzQ0n3kntache3qs_M_lybO9kR01_rSI/exec"

# --- CONFIG Sensor ---
d = dht.DHT22(Pin(15))
print("Sensor DHT22 iniciado. Enviando temperatura para a planilha...")

# --- LOOP Principal ---
while True:
    try:
        d.measure()
        temperatura = d.temperature()
        umidade = d.humidity()

        print(f"Temperatura: {temperatura}°C | Umidade: {umidade}%")

        # Monta a URL com os parâmetros GET
        url_final = f"{URL}?id=7&temp={temperatura}"

        # Faz a requisição HTTP
        response = urequests.get(url_final)
        print("Resposta do servidor:", response.text)
        response.close()

    except OSError as e:
        print("Erro ao ler o sensor:", e)

    # Espera pelo menos 2s (recomendado pelo datasheet do DHT22)
    time.sleep(5)
