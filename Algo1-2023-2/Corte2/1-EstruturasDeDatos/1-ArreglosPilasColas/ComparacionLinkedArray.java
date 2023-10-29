/**
 * Esta clase va a comparar un LinkedList con un ArrayList
 */ 
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Random;
import java.util.Vector;

public class ComparacionLinkedArray {
  public static void main(String[] args) {
    ArrayList<Integer> a = new ArrayList();
    LinkedList<Integer> l = new LinkedList();
    //Tiempo de agregar elementos
    Random r = new Random();

    long inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      a.add(r.nextInt(1000));
    }

    long fin = System.currentTimeMillis();
    System.out.println("Tiempo de agregar elementos a ArrayList: "+(fin-inicio));
    inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      l.add(r.nextInt(1000));
    }
    fin = System.currentTimeMillis();
    System.out.println("Tiempo de agregar elementos a LinkedList: "+(fin-inicio));
    
    Vector v = new Vector();
    inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      v.add(r.nextInt(1000));
    }
    fin = System.currentTimeMillis();
    System.out.println("Tiempo de agregar elementos a Vector: "+(fin-inicio));
    //Tiempo de buscar elementos
    inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      a.get(i);
    }
    fin = System.currentTimeMillis();
    System.out.println("Tiempo de buscar elementos a ArrayList: "+(fin-inicio));
    inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      l.get(i);
    }
    fin = System.currentTimeMillis();
    System.out.println("Tiempo de buscar elementos a LinkedList: "+(fin-inicio));
    inicio = System.currentTimeMillis();
    for (int i=0; i<100000; i++) {
      v.get(i);
    }
    fin = System.currentTimeMillis();
    System.out.println("Tiempo de buscar elementos a Vector: "+(fin-inicio));
  }
}
