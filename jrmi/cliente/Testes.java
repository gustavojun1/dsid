import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Testes extends Remote {

    void voidTeste() throws RemoteException;
    
    long longSimplesTeste(long a) throws RemoteException;
    
    long longComplexTeste(long arg1, long arg2,long arg3,long arg4,long arg5,long arg6,long arg7,long arg8) throws RemoteException;
    
    String stringTeste(String string) throws RemoteException;

}

