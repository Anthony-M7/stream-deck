<div align="center">

# 🚀 Stream Deck Ultimate | Bit & Vatio

**Ingeniería real para el mundo digital.**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Convierte tu teléfono móvil en un **Controlador Maestro (Stream Deck)** para tu PC de escritorio con cero inversión. Desarrollado con Python, este sistema se comunica a través de tu red WiFi local y te permite ejecutar aplicaciones, atajos de teclado y comandos directos al sistema operativo.

[Ver el tutorial en YouTube](https://youtu.be/X1tGgnF36EI)

</div>

---

## ✨ Características Principales

- 🎛️ **Control de Volumen Dinámico:** Slider táctil para controlar el audio maestro de Windows.
- 📸 **Capturas de Pantalla Pro:** Toma un screenshot, guárdalo en tu disco duro e inyéctalo directamente en el portapapeles de tu PC al instante.
- 🔒 **Control de Sistema a Bajo Nivel:** Utiliza la API de Windows (`ctypes`) y PowerShell para bloquear la PC o minimizar ventanas de forma infalible, sin depender de atajos de teclado inestables.
- 🎵 **Monitor "Now Playing":** La interfaz web lee el título de la ventana activa en tu PC en tiempo real.
- 🛠️ **Botones 100% Personalizables:** Crea nuevos atajos directamente desde tu celular. Se guardan dinámicamente en una base de datos local (`atajos.json`).

---

## 🏗️ Arquitectura del Proyecto

El sistema utiliza una arquitectura **Cliente-Servidor** local:

- **Servidor (Backend):** Tu PC ejecuta un script de Python con `Flask` y `Waitress` para alta estabilidad, utilizando librerías como `PyAutoGUI` y `win32clipboard` para manipular el entorno de Windows.
- **Cliente (Frontend):** Tu celular accede a una interfaz web (HTML/CSS/JS) diseñada con estilo "Modo Oscuro/Cyberpunk" que envía peticiones HTTP asíncronas (`fetch`) al servidor.

---

## ⚙️ Requisitos Previos

Asegúrate de tener instalado [Python 3.10 o superior](https://www.python.org/downloads/) y que esté agregado al `PATH` de Windows.

Este proyecto está optimizado para **Windows**.

---

## 🚀 Instalación y Uso

**1. Clonar el repositorio**

```bash
git clone [https://github.com/Anthony-M7/stream-deck.git] (https://github.com/Anthony-M7/stream-deck.git)
cd stream-deck
```
