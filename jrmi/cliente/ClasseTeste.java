// package Client;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ClasseTeste extends Remote {

   public String getName() throws RemoteException;

   public Float getAltura() throws RemoteException;

   public int getIdade() throws RemoteException;
}