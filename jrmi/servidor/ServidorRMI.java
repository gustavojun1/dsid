import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner; 

public class ServidorRMI {
    public static void main(String[] args) {
        //Mudar o IP que esta presente no setProperty
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o ip a ser utilizado: ");
        String ip = sc.nextLine();
        System.setProperty("java.rmi.server.hostname", ip);
        try {
            Testes testes = new TestesImpl();
            ClasseTesteImpl teste5 = new ClasseTesteImpl("Jun", (float) 1.7, 13);
            
            ClasseTeste stub1 = (ClasseTeste) UnicastRemoteObject.exportObject(teste5, 50050);
            Testes stub2 = (Testes) UnicastRemoteObject.exportObject(testes, 50050);

            System.out.println("Digite a porta a ser utilizada: ");
            int porta = sc.nextInt();

            Registry registry = LocateRegistry.createRegistry(porta);
            
            registry.rebind("Classe", stub1);
            registry.rebind("Testes", stub2);
            
            System.out.println("Servidor RMI pronto.");
        
        } catch (Exception e) {

            System.err.println("Erro no servidor: " + e.toString());
            e.printStackTrace();

        }
        sc.close();
    }
}
