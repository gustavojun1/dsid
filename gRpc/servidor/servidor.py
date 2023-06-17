from concurrent import futures
import time
import grpc
import greet_pb2
import greet_pb2_grpc
from classeComplexa import *

class GreeterServicer(greet_pb2_grpc.GreeterServicer):
    
    def VoidTeste(self, request, context):
        
        print("###"*8)
        print("Requisição Void Iniciada")
        
        void_reply = greet_pb2.VoidReply()
        
        print("Requisição Void Terminada")
        
        return void_reply
    
    def LongSimplesTeste(self, request, context):
        
        print("###"*8)
        print("Requisição Long Simples Iniciada")

        long_reply = greet_pb2.LongReply()
        long_reply.result = 9223372036854775807

        print("Requisição Long Simples Terminada")
        
        return long_reply
        
    def LongComplexoTeste(self, request, context):
        
        print("###"*8)
        print("Requisição Long Complexo Iniciada")
        
        longComplex_reply = greet_pb2.LongReply()
        longComplex_reply.result = request.arg1+request.arg2+request.arg3+request.arg4+request.arg5+request.arg6+request.arg7+request.arg8
        
        print("Requisição Long Complexo Terminada")
        
        return longComplex_reply        

    def StringTeste(self, request, context):
        
        print("###"*8)
        print("Requisição String Teste Iniciada")
        
        string_reply = greet_pb2.StringReply()
        string_reply.message = request.name
        
        print("Requisição String Teste Terminada")
        
        return string_reply
    
    def ClassTeste(self, request, context):

        print("###"*8)
        print("Requisição Classe Teste Iniciada")
        
        pessoa = classeComplexa("Jun", 1.7, 16)
        
        class_reply = greet_pb2.ClasseReply()
        class_reply.person.nome = pessoa.nome
        class_reply.person.altura = pessoa.altura
        class_reply.person.idade = pessoa.idade
        
        print("Requisição Classe Teste Terminada")
        
        return class_reply

def servidor():
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port("[::]:50000")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    servidor()
