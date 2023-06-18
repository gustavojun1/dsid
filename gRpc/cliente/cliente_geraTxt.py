from concurrent import futures
import time
import random
import grpc
import greet_pb2
import greet_pb2_grpc

def cliente():
    decimals = 8
    
    ### IP DO SERVIDOR ###
    #Exemplo
    #with grpc.insecure_channel('123.123.123.43:50051') as channel:
    ip = input("Digite o ip a ser utilizado: ")
    porta = input("Digite a porta a ser utilizada: ")
    
    with grpc.insecure_channel(ip + ':' + porta) as channel:
        
        stub = greet_pb2_grpc.GreeterStub(channel)

        mediaVoid = 0;
        mediaLong1 = 0;
        mediaLong8 = 0;
        mediaString = 0;
        mediaClasse = 0;
       


        voidArq = open("tempos/voidArq.txt", "w")
        long1Arq = open("tempos/long1Arq.txt", "w")
        long8Arq = open("tempos/long8Arq.txt", "w")
        stringArq = open("tempos/stringArq.txt", "w")
        classeArq = open("tempos/classeArq.txt", "w")

        numTests = 10
        firstConnectionControl = True
        for _ in range(numTests):
            rpc_call = 1
            while rpc_call < 6:
                if rpc_call == 1:
                    inicio = time.time()
                    void_request = greet_pb2.VoidRequest()

                    void_reply = stub.VoidTeste(void_request)
                    tempo = round(time.time()-inicio, decimals)
                    voidArq.write(str(tempo) + "\n")
                    if not firstConnectionControl:
                        mediaVoid = mediaVoid + tempo

                elif rpc_call == 2:
                    inicio = time.time()
                    x = 9223372036854775807
                    long_request = greet_pb2.LongRequest(value = x)

                    long_reply = stub.LongSimplesTeste(long_request)
                    tempo = round(time.time()-inicio, decimals)
                    long1Arq.write(str(tempo)+"\n")
                    if not firstConnectionControl:
                        mediaLong1 = mediaLong1 + tempo

                elif rpc_call == 3:

                    inicio = time.time()

                    val = 305843009213693951
                    longComplex_request = greet_pb2.LongComplexRequest(arg1=val, arg2=val, arg3=val, arg4 =val, arg5=val, arg6 =val, arg7 =val, arg8 =val)

                    longComplex_reply = stub.LongComplexoTeste(longComplex_request)
                    tempo = round(time.time()-inicio,decimals)
                    long8Arq.write(str(tempo)+"\n")
                    if not firstConnectionControl:
                        mediaLong8 = mediaLong8 + tempo

                elif rpc_call == 4:

                    inicio = time.time()

                    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*"

                    for x in range(12):
                        string = ""
                        for y in range (2**x):
                            string += caracteres[random.randint(0, len(caracteres)-1)]


                        string_request = greet_pb2.StringRequest(name = string)
                        string_reply = stub.StringTeste(string_request)
                        tempo = round(time.time()-inicio,decimals)
                        stringArq.write(str(tempo)+", "+str(len(string))+"\n")
                        if not firstConnectionControl:
                            mediaString = mediaString + tempo

                elif rpc_call == 5:

                    inicio = time.time()
                    class_request = greet_pb2.ClasseRequest(id = 1)
                    class_reply = stub.ClassTeste(class_request)
                    tempo = round(time.time()-inicio, decimals)
                    classeArq.write(str(tempo)+"\n")
                    if not firstConnectionControl:
                        mediaClasse = mediaClasse + tempo

                else:
                    break
                rpc_call += 1
            firstConnectionControl = False

        # descarta a primeira operação
        mediaVoid = mediaVoid / (numTests - 1)
        mediaLong1 = mediaLong1 / (numTests - 1)
        mediaLong8 = mediaLong8 / (numTests - 1)
        mediaString = mediaString / (12 * (numTests - 1)) # 12 tamanhos de strings diferentes a cada iteração
        mediaClasse = mediaClasse / (numTests - 1)

        mediasArq = open("tempos/mediasArq.txt", "w")
        mediasArq.write("Void: " + str(round(mediaVoid, decimals)) + "\n") # discarta a primeira conexão
        mediasArq.write("Long de 1 arg: " + str(round(mediaLong1, decimals)) + "\n")
        mediasArq.write("Long de 8 arg: " + str(round(mediaLong8, decimals)) + "\n")
        mediasArq.write("String: " + str(round(mediaString, decimals)) + "\n")
        mediasArq.write("Classe: " + str(round(mediaClasse, decimals)) + "\n")

if __name__ == "__main__":
    cliente()
