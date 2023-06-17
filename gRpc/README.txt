!!!!!!!!!!!!!!! dependencias do gRpc !!!!!!!!!!!!!!!!!!

Versão do python:
Python 3.11.3

Versão pip:
pip 23.1.2

----------------------------
Rodar estes comando no terminal

Atualizar pip:
    pip install --upgrade pip

instalar Pacotes:
    pip install grpcio==1.54.2 grpcio-tools==1.54.2

----------------------------
Versão dos pacotes:
grpcio             1.54.2
grpcio-tools       1.54.2

##################################################################################################

Pasta gRpc

Contém 3 pastas:

servidor - Importante para rodar o servidor
cliente - Importante para rodar o cliente

protos - gerar o arquivo de configuração do grpcio -- os arquivos já estão gerados,
         mas caso queira gerar os arquivos na pasta protos 
         tem o comando para gera-los, lembre-se de estar um diretório "atrás",
         
-- Exemplo

[edgarlira@127 gRpc]$ pwd
/*PATH*/gRpc
[edgarlira@127 gRpc]$ ls
cliente  protos  servidor
[edgarlira@127 gRpc]$ python -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/greet.proto
[edgarlira@127 gRpc]$ ls
cliente  greet_pb2_grpc.py  greet_pb2.py  protos  servidor
[edgarlira@127 gRpc]$ 

-- Fim Exemplo

!!!!!!!!!!!!!!!!!!!1 Como Rodar gRpc !!!!!!!!!!!!!!!!!!!!!!!

Abra 2 terminais (O ip configurado no cliente é o localhost. Há um comentario indicando onde fazer a mudança de IP, se desejar)

No terminal 1 vá para pasta servidor e rode o comando:
$ python greet_server.py

No terminal 2 vá para pasta cliente e rode o comando:

$ python greet_client.py

ou para gerar os tempos (em segundos) de execução (10x) em arquivos (lembre-se de possuir uma pasta chamada "tempos" no diretório do cliente)

$ python greet_client_geraTxt.py
