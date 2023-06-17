from concurrent import futures
import time
import random
import grpc
import greet_pb2
import greet_pb2_grpc

def cliente():
    ### MUDAR IP ###
    #Exemplo 179.99.71.34
    #with grpc.insecure_channel('201.26.6.236:50051') as channel:
    
    with grpc.insecure_channel('179.99.71.34:50000') as channel:
        
        stub = greet_pb2_grpc.GreeterStub(channel)
        
        while True:

            print("###"*8)
            print("Escolha o método para testar")
            print("1. Void")
            print("2. Long")
            print("3. Long Complex")
            print("4. String")
            print("5. Classe")
            print("6. Encerra Cliente")
            rpc_call = int(input(""))

            #Caso queira aumentar o número de vezes que ocorre a requisição escolhida, aumente o valor da variavel abaixo
            repeticao = 1
            for _ in range (repeticao):

                print("###"*8)
                if rpc_call == 1:
                    
                    inicio = time.time()
                    void_request = greet_pb2.VoidRequest()

                    void_reply = stub.VoidTeste(void_request)
                    
                    print("Duração Total da requisição Void: ",round(time.time()-inicio,2))

                elif rpc_call == 2:

                    inicio = time.time()
                    x = 9223372036854775807
            
                    long_request = greet_pb2.LongRequest(value = x)

                    long_reply = stub.LongSimplesTeste(long_request)
            
                    print("Valor retornado pelo servidor:",long_reply.result)
                    print("Duração Total da Requisição:",round(time.time()-inicio,3))

                elif rpc_call == 3:

                    inicio = time.time()

                    val = 305843009213693951
                    print("8 Valores iguais foram enviado. Valor =", 305843009213693951)
                    longComplex_request = greet_pb2.LongComplexRequest(arg1=val, arg2=val, arg3=val, arg4 =val, arg5=val, arg6 =val, arg7 =val, arg8 =val)

                    longComplex_reply = stub.LongComplexoTeste(longComplex_request)
        
                    
                    print("Valor retornado pelo servidor:",longComplex_reply.result)
                    
                    print("Duração Total:",round(time.time()-inicio,3))

                elif rpc_call == 4:

                    inicio = time.time()

                    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*"

                    for x in range(12):
                        string = ""
                        for y in range (2**x):
                            string += caracteres[random.randint(0, len(caracteres)-1)]

        
                        string_request = greet_pb2.StringRequest(name = string)
                        string_reply = stub.StringTeste(string_request)
                        
                        #print(string_reply)

                        print("Tempo ",round(time.time()-inicio,3)," "*1," | Tamanho",2**x)
                
                elif rpc_call == 5:

                    inicio = time.time()
                    class_request = greet_pb2.ClasseRequest(id = 1)
                    class_reply = stub.ClassTeste(class_request)

                    print("Resposta:\n",class_reply)

                    print("Duração Total:",round(time.time()-inicio,4))
            
            if rpc_call >= 6:
                break

            time.sleep(0.5)

if __name__ == "__main__":
    cliente()
