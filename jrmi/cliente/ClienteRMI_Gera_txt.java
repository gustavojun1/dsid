import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Random;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class ClienteRMI_Gera_txt {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            
            FileWriter arquivoVoid = new FileWriter("tempos/tempo_execucao_void.txt");
            FileWriter arquivoLong = new FileWriter("tempos/tempo_execucao_long.txt");
            FileWriter arquivoLongComplex = new FileWriter("tempos/tempo_execucao_long_complex.txt");
            FileWriter arquivoString = new FileWriter("tempos/tempo_execucao_string.txt");
            FileWriter arquivoClasse = new FileWriter("tempos/tempo_execucao_classe.txt");
            
            ////// MUDAR IP
            ////// Exemplo 
            // Registry registry = LocateRegistry.getRegistry("184.343.345.32", 50051);
            System.out.println("Digite o ip a ser utilizado: ");
            String ip = sc.nextLine();
            System.out.println("Digite a porta a ser utilizada: ");
            int porta = sc.nextInt();
            Registry registry = LocateRegistry.getRegistry(ip, porta);
            Testes testes = (Testes) registry.lookup("Testes");
            ClasseTeste classeTeste = (ClasseTeste) registry.lookup("Classe");
            
            int opcao = 1;
            while (opcao < 6) {
                
                for (int x = 0; x < 10; x++){
                    switch (opcao) {
                        case 1:
                            testarVoid(testes, arquivoVoid);
                            break;
                        case 2:
                            testarLong(testes, arquivoLong);
                            break;
                        case 3:
                            testarLongComplex(testes, arquivoLongComplex);
                            break;
                        case 4:
                            testarString(testes, arquivoString);
                            break;
                        case 5:
                            testarClasse(classeTeste, arquivoClasse);
                            break;
                        default:
                            System.out.println("Opção inválida");
                        }
                }
                opcao++;        
            }

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
            e.printStackTrace();
        } finally {
            sc.close();
        }
    }
    
    public static void testarVoid(Testes testes, FileWriter arquivo) throws RemoteException, IOException {
        
        long inicio = System.currentTimeMillis();
        testes.voidTeste();
        long fim = System.currentTimeMillis();
        
        arquivo.write("" + ((fim-inicio)*0.01)+"\n");
        
        arquivo.flush();
    
    }
    
    public static void testarLong(Testes testes, FileWriter arquivo) throws RemoteException, IOException {
        long inicio = System.currentTimeMillis();
        
        long x = 2147483647;
        testes.longSimplesTeste(x);
        long fim = System.currentTimeMillis();
        
        arquivo.write("" + ((fim-inicio)*0.01)+"\n");
        
        arquivo.flush();
    
    }

    public static void testarLongComplex(Testes testes, FileWriter arquivo) throws RemoteException, IOException {
        long inicio = System.currentTimeMillis();
        
        long val = 26843545;
        testes.longComplexTeste(val, val, val, val, val, val, val, val);
        long fim = System.currentTimeMillis();
        
        arquivo.write("" + ((fim-inicio)*0.01)+"\n");
        
        arquivo.flush();
    
    }

    public static void testarString(Testes testes, FileWriter arquivo) throws RemoteException, IOException {

        String caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*";
        Random random = new Random();

        for (int x = 0; x < 12; x++) {
            long inicio = System.currentTimeMillis();
                
            String string = "";

            for (int y = 0; y < Math.pow(2, x); y++) {
                int randomIndex = random.nextInt(caracteres.length());
                char randomChar = caracteres.charAt(randomIndex);
                string += randomChar;
            }       
            testes.stringTeste(string);   
    
            long fim = System.currentTimeMillis();
            
            arquivo.write("" + ((fim-inicio)*0.01)+", "+(int)Math.pow(2, x)+ "\n" );
        
            arquivo.flush();
    
             
        }
    }

    public static void testarClasse(ClasseTeste testeClasse, FileWriter arquivo) throws RemoteException, NotBoundException, IOException{
    
        long inicio = System.currentTimeMillis();
        
        
        testeClasse.getName();
        testeClasse.getAltura();
        testeClasse.getIdade();
    
        long fim = System.currentTimeMillis();
        
        arquivo.write("" + ((fim-inicio)*0.01)+"\n");
        
        arquivo.flush();
           
  
    }
    
}
