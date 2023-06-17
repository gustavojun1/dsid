from concurrent import futures
import time
import random
import grpc
import greet_pb2
import greet_pb2_grpc

def cliente():
    
    ### IP DO SERVIDOR ###
    #Exemplo
    #with grpc.insecure_channel('123.123.123.43:50051') as channel:
    with grpc.insecure_channel('179.99.71.34:50000') as channel:
        
        stub = greet_pb2_grpc.GreeterStub(channel)
        rpc_call = 1
        voidArq = open("tempos/voidArq.txt", "w")
        long1Arq = open("tempos/long1Arq.txt", "w")
        long8Arq = open("tempos/long8Arq.txt", "w")
        stringArq = open("tempos/stringArq.txt", "w")
        classeArq = open("tempos/classeArq.txt", "w")
        
        while rpc_call < 6:

            for _ in range (10):
                if rpc_call == 1:
                    
                    inicio = time.time()
                    void_request = greet_pb2.VoidRequest()

                    void_reply = stub.VoidTeste(void_request)
                    voidArq.write(str(round(time.time()-inicio,4))+"\n")
        

                elif rpc_call == 2:
                    inicio = time.time()
                    x = 9223372036854775807
                    long_request = greet_pb2.LongRequest(value = x)

                    long_reply = stub.LongSimplesTeste(long_request)
                    
                    long1Arq.write(str(round(time.time()-inicio,4))+"\n")
        
                elif rpc_call == 3:

                    inicio = time.time()

                    val = 305843009213693951
                    longComplex_request = greet_pb2.LongComplexRequest(arg1=val, arg2=val, arg3=val, arg4 =val, arg5=val, arg6 =val, arg7 =val, arg8 =val)

                    longComplex_reply = stub.LongComplexoTeste(longComplex_request)
        
                    long8Arq.write(str(round(time.time()-inicio,4))+"\n")
        
                elif rpc_call == 4:

                    inicio = time.time()

                    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*"

                    for x in range(12):
                        string = ""
                        for y in range (2**x):
                            string += caracteres[random.randint(0, len(caracteres)-1)]

        
                        string_request = greet_pb2.StringRequest(name = string)
                        string_reply = stub.StringTeste(string_request)
                        
                        stringArq.write(str(round(time.time()-inicio,4))+","+str(len(string))+"\n")

                elif rpc_call == 5:

                    inicio = time.time()
                    class_request = greet_pb2.ClasseRequest(id = 1)
                    class_reply = stub.ClassTeste(class_request)
                    classeArq.write(str(round(time.time()-inicio,4))+"\n")
        
                else:
                    break

            rpc_call += 1

if __name__ == "__main__":
    cliente()
