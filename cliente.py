import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("127.0.0.1", 5000))

print("================================")
print("   PEDRA, PAPEL E TESOURA")
print("================================")

escolha = input("Escolha pedra, papel ou tesoura: ").lower()

cliente.send(escolha.encode())

resultado = cliente.recv(1024).decode()

print("\nResultado:", resultado)

cliente.close()
