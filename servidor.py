import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind(("0.0.0.0", 5000))

servidor.listen(2)

print("================================")
print("   PEDRA, PAPEL E TESOURA")
print("================================")
print("Esperando jogadores...")

jogador1, endereco1 = servidor.accept()
print("Jogador 1 conectado:", endereco1)

jogador2, endereco2 = servidor.accept()
print("Jogador 2 conectado:", endereco2)

print("\nOs dois jogadores estão conectados!")
print("Escolhas sendo aguardadas...")

escolha1 = jogador1.recv(1024).decode().lower()

escolha2 = jogador2.recv(1024).decode().lower()

print("\nJogador 1:", escolha1)
print("Jogador 2:", escolha2)

if escolha1 == escolha2:

    resultado = "Empate!"

elif (
    (escolha1 == "pedra" and escolha2 == "tesoura") or
    (escolha1 == "papel" and escolha2 == "pedra") or
    (escolha1 == "tesoura" and escolha2 == "papel")
):

    resultado = "Jogador 1 venceu!"

else:

    resultado = "Jogador 2 venceu!"

print("\nResultado:", resultado)

jogador1.send(resultado.encode())
jogador2.send(resultado.encode())

jogador1.close()
jogador2.close()
servidor.close()

print("\nServidor encerrado.")
