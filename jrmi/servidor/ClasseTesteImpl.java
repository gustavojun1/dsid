import java.rmi.RemoteException;

public class ClasseTesteImpl implements ClasseTeste{

    public String name;
    public Float altura;
    public int idade;

    public ClasseTesteImpl(String newName, Float altura, int idade) throws RemoteException {
        
        this.name  = newName;
        this.altura = altura;
        this.idade = idade;

    }

    public String getName() throws RemoteException {
        System.out.println("Requisição Classe Complexa Atributo Nome");

        return this.name;
    }

    public Float getAltura() throws RemoteException {
        System.out.println("Requisição Classe Complexa Atributo Altura");
        return this.altura;

    }

    public int getIdade() throws RemoteException {
        System.out.println("Requisição Classe Complexa Atributo Idade");
        
        System.out.println("####################");
        return this.idade;
    }
}
