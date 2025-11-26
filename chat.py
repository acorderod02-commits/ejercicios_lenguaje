import socket
import threading
import sys
import random

# Lista de colores ANSI
colores = [
    "\033[31m",  # Rojo
    "\033[32m",  # Verde
    "\033[33m",  # Amarillo
    "\033[34m",  # Azul
    "\033[35m",  # Magenta
    "\033[36m",  # Cian
]

# Función para recibir mensajes del servidor
def recibir_mensajes(cliente):
    """Función que recibe y muestra los mensajes del servidor"""
    while True:
        try:
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                # Limpiar la línea de escritura (si es necesario)
                sys.stdout.write('\r' + ' ' * 100 + '\r')  # Limpiar la línea actual
                # Mostrar el mensaje recibido con color
                print(f"\r{mensaje}", end="")  # Mostrar el mensaje recibido
                sys.stdout.write('Tú: ')  # Volver al inicio para permitir escribir sin interferencia
                sys.stdout.flush()
            else:
                print("\nEl servidor ha cerrado la conexión.")
                break
        except ConnectionResetError:
            print("\nConexión perdida con el servidor.")
            break
        except Exception as e:
            print(f"\nError al recibir mensaje: {e}")
            break

# Función para enviar mensajes al servidor
def enviar_mensajes(cliente, nombre_usuario, color):
    """Función que permite enviar mensajes al servidor con nombre colorido"""
    while True:
        try:
            mensaje = input("\nTú: ")  # Tomar el mensaje desde la consola
            if mensaje.lower() == "salir":
                cliente.send(mensaje.encode('utf-8'))
                break
            # Enviar mensaje con el nombre de usuario coloreado
            mensaje_con_nombre = f"{color}{nombre_usuario}\033[0m: {mensaje}"
            cliente.send(mensaje_con_nombre.encode('utf-8'))
        except Exception as e:
            print(f"\nError al enviar mensaje: {e}")
            break

    cliente.close()

def iniciar_cliente():
    """Función principal para iniciar el cliente"""
    host = '192.168.50.12'  # IP del servidor (ajustar según la red)
    puerto = 5555          # El mismo puerto que el servidor está usando

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((host, puerto))
        print(f"\nConectado al servidor {host}:{puerto}")
    except Exception as e:
        print(f"\nError al conectar con el servidor: {e}")
        return

    # Pedir el nombre de usuario al cliente
    nombre = input("\nIngresa tu nombre de usuario: ")
    # Asignar un color aleatorio al usuario
    color = random.choice(colores)
    
    # Enviar el nombre de usuario y su color al servidor
    cliente.send(f"{color}{nombre}\033[0m".encode('utf-8'))

    # Iniciar un hilo para recibir mensajes en segundo plano
    threading.Thread(target=recibir_mensajes, args=(cliente,), daemon=True).start()

    # Iniciar la función para enviar mensajes al servidor
    enviar_mensajes(cliente, nombre, color)

if __name__ == "__main__":
    print("Bienvenido al cliente de chat!")
    iniciar_cliente()