/**
 * Clase main para pruebas del ABB
 * @author Carlos Delgado
* @date 26/10/2023
*/ 

public class Main {
  public static void main(String[] args) {
    ABB arbol = new ABB();
    System.out.println(arbol);
    arbol.insertar(10);
    System.out.println(arbol);
    arbol.insertar(5);
    System.out.println(arbol);
    arbol.insertar(15);
    System.out.println(arbol);
    arbol.insertar(3);
    System.out.println(arbol);
  }
}
