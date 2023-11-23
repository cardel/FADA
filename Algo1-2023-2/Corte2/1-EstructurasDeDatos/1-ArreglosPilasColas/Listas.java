/**
* Implementación una lista enlazada.
* @author Carlos Delgado
* @date 26/10/2023
* @version 1.0
*/ 
import java.util.Random;
public class Listas {
 
  public void ejemplo() {
    ListaEnlazada objLista = new ListaEnlazada(); //Creando una lista vacia
    System.out.println(objLista);
    objLista.insertar(1);
    System.out.println(objLista);
    objLista.insertar(2);
    System.out.println(objLista);
    Random r = new Random();
    for (int i=0; i<100; i++) {
      int valor = r.nextInt(100);
      objLista.insertar(valor);
    }
    System.out.println(objLista);
    System.out.println("Buscando el 5: "+objLista.search(5));
    System.out.println("Buscando el octavo elemento: "+objLista.indexOf(7));
    //Prueba de eliminar
    ListaEnlazada objLista2 = new ListaEnlazada();
    objLista2.insertar(1);
    objLista2.insertar(2);
    objLista2.insertar(3);
    objLista2.insertar(4);
    objLista2.insertar(5);
    System.out.println(objLista2);
    objLista2.delete(3);
    System.out.println(objLista2);
    objLista2.delete(1);
    System.out.println(objLista2);
    objLista2.delete(5);
    System.out.println(objLista2);
    objLista2.delete(2);
    System.out.println(objLista2);
    objLista2.delete(4);
    System.out.println(objLista2);
  }

  public static void main(String[] args) {
    Listas objListas = new Listas();
    objListas.ejemplo();
      
  }
  /**
  * Esta clase implementa un elemento de la lista enlazada.
  */
  class Nodo {
    public int dato;
    public Nodo sig; //Elemento siguiente
    public Nodo ant; //Elemento anterior
    
    Nodo(int dato) {
      this.dato = dato;
      sig = null;
      ant = null;
    }
    @Override
    public String toString() {
      return dato+"";
    }
      
  }

  /**
   * Clase lista enlazada
   */
  class ListaEnlazada {
    private Nodo head; //Primer elemento de lprivate Nodo head; //Primer elemento de la Lista e
    ListaEnlazada() {
      head = null;
    }
    void insertar(int dato) {
      Nodo nuevo = new Nodo(dato);
      if (head == null) {
        head = nuevo;
      }
      else {
        //El nodo a insertar es la nueva cabeza, es necesario actualizar
        //los punteriores de siguiente (al nuevo segundo) y el anterior del que insertamos
        Nodo copia = head;
        copia.ant = nuevo;
        nuevo.sig = copia;
        head = nuevo;


      }
    }
    /**
    * Metodo search para buscar un elemento en la lista
    */
    public Nodo search(int dato) {
      Nodo copia = head;
      while (copia != null) {
        if (copia.dato == dato) {
          return copia;
        }
        copia = copia.sig;
      }
      return null;
    }
    /**
    * Busqueda por indice
    */ 
    public Nodo indexOf(int index) {
      Nodo copia = head;
      int i = 0;
      while (copia != null) {
        if (i == index) {
          return copia;
        }
        copia = copia.sig;
        i++;
      }
      return null;
          
    }
    /**
     * Metodo para eliminar un elemento de la lista enlazada
     */
    public void delete(int dato) {
      Nodo elemento = search(dato);
      if (elemento != null) {
        Nodo ant = elemento.ant;
        Nodo sig = elemento.sig;
        //Si el elemento eliminar es el primero
        if (ant == null) {
          if (sig != null) sig.ant = null; //Al anterior del siguiente es nulo
          head = sig; 
        }
        else {
          if (sig == null) {
            ant.sig = null; 
          }
          else {
            ant.sig = sig;
            sig.ant = ant;
                      
          }
        }
      }
    }

    @Override
    public String toString() {
      String str = "[";
      Nodo copia = head;
      while (copia != null) {
        str += copia.dato + ",";
        copia = copia.sig;
      }
      return str+"]";
    }


      
  }
}
