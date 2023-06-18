import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Random;
import java.util.Scanner;

public class ClienteRMI {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        try {

            ////// MUDAR IP
            ////// Exemplo 
            // Registry registry = LocateRegistry.getRegistry("198.168.15.11", 50051);
            System.out.println("Digite o ip a ser utilizado: ");
            String ip = sc.nextLine();
            System.out.println("Digite a porta a ser utilizada: ");
            int porta = sc.nextInt();
            Registry registry = LocateRegistry.getRegistry(ip, porta);

            Testes testes = (Testes) registry.lookup("Testes");
            
            ClasseTeste classe = (ClasseTeste) registry.lookup("Classe");
            
            while (true) {
                
                System.out.println("###".repeat(8));
                System.out.println("Escolha o método para testar");
                System.out.println("1. Void");
                System.out.println("2. Long");
                System.out.println("3. Long Complex");
                System.out.println("4. String");
                System.out.println("5. Classe");

                int opcao = sc.nextInt();
                System.out.println("###".repeat(8));
                
                long startTime = System.currentTimeMillis();
                switch (opcao) {
                    case 1:
                        testarVoid(testes);
                        break;
                    case 2:
                        testarLong(testes);
                        break;
                    case 3:
                        testarLongComplex(testes);
                        break;
                    case 4:
                        testarString(testes);
                        break;
                    case 5:
                        testarClasse(classe);
                        break;
                    default:
                        System.out.println("Opção inválida");
                    }
                    long endTime = System.currentTimeMillis();
                    long executionTime = endTime - startTime;
                    System.out.println("Tempo de execução: " + executionTime + "ms");
                    Thread.sleep(500);
            }

        } catch (Exception e) {
            System.err.println("Erro no cliente: " + e.toString());
            e.printStackTrace();
        }
        sc.close();
    }

    public static void testarVoid(Testes testes) throws RemoteException {
        System.out.println("Método Void selecionado");
        testes.voidTeste();
    }

    public static void testarLong(Testes testes) throws RemoteException {
        System.out.println("Método Long selecionado");
        long x = 2147483647;
        long longSimples_reply = testes.longSimplesTeste(x);
        System.out.println("Resultado: " + longSimples_reply);
    }

    public static void testarLongComplex(Testes testes) throws RemoteException {
        System.out.println("Método Long Complex selecionado");
        long val = 26843545;
        long longComplex_reply = testes.longComplexTeste(val, val, val, val, val, val, val, val);
        System.out.println("Resultado: " + longComplex_reply);
    }

    public static void testarString(Testes testes) throws RemoteException {
        String caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*";
        Random random = new Random();

        for (int x = 0; x < 12; x++) {
            long startTime = System.currentTimeMillis();
                
        
            String string = "";
            for (int y = 0; y < Math.pow(2, x); y++) {
                int randomIndex = random.nextInt(caracteres.length());
                char randomChar = caracteres.charAt(randomIndex);
                string += randomChar;
            }       
            testes.stringTeste(string);   
    
            long endTime = System.currentTimeMillis();
            long executionTime = endTime - startTime;
            System.out.println("Tempo de execução: " + executionTime + "ms" +" Tamanho da String= "+(int)Math.pow(2, x));
             
        }
    }

    public static void testarClasse(ClasseTeste testeClasse) throws RemoteException, NotBoundException {
    
        System.out.println("Método Classe selecionado");
        String nome = testeClasse.getName();
        Float altura = testeClasse.getAltura();
        double idade = testeClasse.getIdade();
        System.out.println("Nome: " + nome);
        System.out.println("Altura: " + altura);
        System.out.println("Idade: " + idade);
        
    }
}
