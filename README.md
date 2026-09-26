# Monitoramento de Temperatura com DHT22 + Google Sheets (ESP32)

Simulação em MicroPython que lê temperatura e umidade de um sensor DHT22 e envia os dados via Wi-Fi para uma planilha do Google Sheets, usando um Google Apps Script como endpoint HTTP.

## 🔌 Componentes
- ESP32 DevKit C V4
- Sensor DHT22

## 🧷 Conexões

| ESP32 | DHT22 |
|---|---|
| GPIO 15 | SDA / DATA |
| 3V3 | VCC |
| GND | GND |

## ⚙️ Funcionamento
1. Conecta ao Wi-Fi (na simulação, à rede `Wokwi-GUEST`).
2. A cada 5 segundos, lê temperatura e umidade do DHT22.
3. Envia a temperatura via requisição HTTP GET para a URL do Google Apps Script, que grava o valor na planilha.

## ⚠️ Antes de usar
- Troque `SSID` e `PASSWORD` pela rede Wi-Fi real, caso rode em hardware físico.
- A variável `URL` no `main.py` contém o endpoint do Google Apps Script usado na simulação. Como esse link fica público no repositório, considere trocá-lo por um novo endpoint (ou movê-lo para uma variável de ambiente/arquivo `.env` ignorado pelo Git) antes de tornar o repositório público, para evitar que outras pessoas enviem dados falsos para sua planilha.

## ▶️ Como simular
https://wokwi.com/projects/441732869318786049

## 📁 Arquivos
- `main.py` — código MicroPython
- `diagram.json` — esquema de ligação (Wokwi)
- `wokwi-project.txt` — referência do projeto original
