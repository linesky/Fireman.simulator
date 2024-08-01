
import socket
import threading
import sys

# Configurações do cliente IRC
SERVER = '192.168.1.2'  # Endereço do servidor IRC
PORT = 6667           # Porta do servidor IRC
NICK = 'TestUser'     # Nome de usuário do cliente IRC

# Função para enviar mensagens ao servidor
def send_msg(client_socket):
    while True:
        message = input()
        if message.startswith('/quit'):
            client_socket.send(b'QUIT\n')
            client_socket.close()
            sys.exit()
        else:
            client_socket.send(f"PRIVMSG #channel :{message}\n".encode('utf-8'))

# Função para receber mensagens do servidor
def receive_msg(client_socket):
    while True:
        try:
            message = client_socket.recv(2048).decode('utf-8')
            if message:
                print(message)
            else:
                client_socket.close()
                break
        except:
            print("Erro ao receber mensagem")
            client_socket.close()
            break

# Função principal para iniciar o cliente IRC
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER, PORT))

    client_socket.send(f"NICK {NICK}\n".encode('utf-8'))
    client_socket.send(f"USER {NICK} 0 * :{NICK}\n".encode('utf-8'))
    client_socket.send(b"JOIN #channel\n")

    threading.Thread(target=receive_msg, args=(client_socket,)).start()
    send_msg(client_socket)
print("\x1bc\x1b[47;34m")
if __name__ == "__main__":
    main()
