from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import json

#estrutura de dados centralizados
dados = {
    "eleitores": {},
    "votos": {"candidato_A": 0, "candidato_B": 0}
}

def processar_requisicao(requisicao):
    dados_requisicao = json.loads(requisicao)
    
    if dados_requisicao["tipo"] == "salvar_dados":
        global dados
        dados = dados_requisicao["dados"]
        return ""

    elif dados_requisicao["tipo"] == "obter_dados":
        return json.dumps(dados)

#servidor
servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind(("127.0.0.1", 1024))
servidor.listen()

while True:
    conexao, endereco = servidor.accept()

    #poderia, mas nao vou usar thread pq na minha concepcao inicial, o servidor de votacao
    #vai ter thread pra atender as requisicoes dos eleitores; e este servidor de dados nao
    #vai ser tao intensamente usado nesse sistema de votacao simples
    requisicao = conexao.recv(4096).decode()
    resposta = processar_requisicao(requisicao)

    conexao.send(resposta.encode())

    conexao.close()