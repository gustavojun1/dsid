import java.rmi.RemoteException;

public class TestesImpl implements Testes {
    
    public TestesImpl() throws RemoteException {
        super();
    }

    public void voidTeste() throws RemoteException{
        System.out.println("Requisição Void");
        System.out.println("#################");
    }
    
    public long longSimplesTeste(long a) throws RemoteException{

        System.out.println("Requisição Long 1 Arg");
        System.out.println("#################");
        return a;
    }
    
    public long longComplexTeste(long arg1, long arg2,long arg3,long arg4,long arg5,long arg6,long arg7,long arg8) throws RemoteException{
        
        System.out.println("Requisição Long 8 Args");
        System.out.println("#################");

        return arg1 +arg2 + arg3 + arg4 + arg5 + arg6 + arg7 + arg8;

    }
    
    public String stringTeste(String string) throws RemoteException{

        System.out.println("Requisição De String");
        System.out.println("#################");

        return string;
    
    };

}
