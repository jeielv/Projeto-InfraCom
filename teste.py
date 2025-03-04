import socket
import json

def enviar_dados(dados):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 1024))
    cliente.sendall(json.dumps({"tipo": "salvar_dados", "dados": dados}).encode())
    cliente.close()

def requisitar_dados():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 1024))
    cliente.sendall(json.dumps({"tipo": "obter_dados"}).encode())

    resposta = cliente.recv(4096).decode() 
    cliente.close()
    
    return json.loads(resposta)

#simulação do servidor de votação
dados_votacao = {
    "eleitores": {"eleitor_1": True, "eleitor_2": False},  #por enquanto, so com dois eleitores
    "votos": {"candidato_A": 0, "candidato_B": 1}
}

print("Enviando dados...")
enviar_dados(dados_votacao)

print("Requisitando dados armazenados...")
dados_recebidos = requisitar_dados()
print(dados_recebidos)