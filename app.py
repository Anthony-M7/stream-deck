import webbrowser
import pyautogui
import pygetwindow as gw
from multiprocessing.util import debug
from flask import Flask, render_template, jsonify, request
import pyautogui
import os, json, webbrowser, ctypes
import datetime 
from io import BytesIO
import win32clipboard
from io import BytesIO
from PIL import Image

app = Flask(__name__)
pyautogui.FAILSAFE = True

DATA_FILE = 'atajos.json'

def cargar_atajos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def guardar_atajos(lista_atajos):
    with open(DATA_FILE, 'w') as f:
        json.dump(lista_atajos, f, indent=4)

def enviar_al_portapapeles(imagen):
    output = BytesIO()
    imagen.convert("RGB").save(output, "BMP")
    
    data = output.getvalue()[14:]
    output.close()

    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    except Exception as e:
        print(f"Error al acceder al portapapeles: {e}")
    finally:
        win32clipboard.CloseClipboard()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estado_pc')
def estado_pc():
    try:
        ventana = gw.getActiveWindow()
        titulo = ventana.title if ventana else "Desconocido"

        if len(titulo) > 50:
            titulo = titulo[:50] + "..."

        return jsonify({'titulo_ventana': titulo})

    except:
        return jsonify({'titulo_ventana': "Esperando..."})

@app.route('/ejecutar/<comando>')
def ejecutar_comando(comando):
    print(f"Comando: {comando}")
    
    try:
        if comando == 'play_pause':
            pyautogui.press('playpause')
        elif comando == 'next':
            pyautogui.press('nexttrack')
        elif comando == 'prev':
            pyautogui.press('prevtrack')
        elif comando == 'mute':
            pyautogui.press('volumemute')
            
        elif comando == 'youtube':
            webbrowser.open("https://www.youtube.com")
        elif comando == 'brave_new':
            pyautogui.hotkey('ctrl', 't')
        elif comando == 'netflix':
            webbrowser.open("https://www.netflix.com")
        elif comando == 'gemini':
            webbrowser.open("https://gemini.google.com/u/1/app?hl=es_419")
        elif comando == 'whatsapp':
            webbrowser.open("https://web.whatsapp.com")
            
        elif comando == 'antigravity':
            os.system("start antigravity")

        elif comando == 'minimizar_todo':
            os.system('powershell -command "(new-object -com shell.application).minimizeall()"')
            
        elif comando == 'cerrar_ventana':
            pyautogui.hotkey('alt', 'f4')
            
        elif comando == 'bloquear_pc':
            ctypes.windll.user32.LockWorkStation()
            
        elif comando == 'alt_tab':
            pyautogui.hotkey('alt', 'tab')

        elif comando == 'screenshot':
            foto = pyautogui.screenshot()
            
            nombre_archivo = datetime.datetime.now().strftime("Captura_%Y-%m-%d_%H-%M-%S.png")
            foto.save(nombre_archivo)
            
            enviar_al_portapapeles(foto)
            
            print(f"Foto guardada: {nombre_archivo} y copiada al portapapeles")
            
    except Exception as e:
        print(f"Error grave: {e}")
        return "Error", 500

    return "OK", 200

@app.route('/ejecutar_custom', methods=['POST'])
def ejecutar_custom():
    data = request.json
    tipo = data.get('tipo')
    valor = data.get('valor')
    
    print(f"Custom: {tipo} -> {valor}")
    
    try:
        if tipo == 'hotkey':
            teclas = valor.split('+')
            pyautogui.hotkey(*teclas)
            
        elif tipo == 'web':
            webbrowser.open(valor)
            
        elif tipo == 'texto':
            pyautogui.write(valor)
            
    except Exception as e:
        print(f"Error Custom: {e}")
        
    return "OK", 200

@app.route('/api/atajos', methods=['GET'])
def api_get_atajos():
    return jsonify(cargar_atajos())

@app.route('/api/crear', methods=['POST'])
def api_crear_atajo():
    data = request.json
    atajos = cargar_atajos()
    atajos.append(data)
    guardar_atajos(atajos)
    return jsonify({"status": "OK"})

@app.route('/api/borrar/<int:index>', methods=['DELETE'])
def api_borrar_atajo(index):
    atajos = cargar_atajos()
    if 0 <= index < len(atajos):
        atajos.pop(index)
        guardar_atajos(atajos)
        return jsonify({"status": "OK"})
    return jsonify({"error": "Indice no valido"}), 400

@app.route('/volumen/<direction>/<int:steps>')
def volumen_slider(direction, steps):
    key = 'volumeup' if direction == 'up' else 'volumedown'
    
    steps = max(1, int(steps / 2)) 
    
    pyautogui.press(key, presses=steps)
        
    print(f"Volumen {direction} x {steps}")
    return "OK", 200

if __name__ == '__main__':
    from waitress import serve

    print("-------------------------------------------------------")
    print("SERVIDOR ACTIVADO")
    print("1. En tu PC entra a:  http://localhost:8000")
    print("2. En tu Celular busca tu IP (ej: 192.168.1.X) y entra a:")
    print("   http://TU_IP:8000")
    print("-------------------------------------------------------")
    
    serve(app, host='0.0.0.0', port=8000) # Produccion
    # app.run(debug=True, host='0.0.0.0', port=8000) # Programando