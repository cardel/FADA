/**
 * Clase main para probar los ABB
 * @author Carlos Delgado
 * @date 03/Oct/2023
 */
public class Main {
	public static void main(String args[]) {
		ABB arbol = new ABB();
		arbol.insert(5);
		arbol.insert(3);
		arbol.insert(7);
		arbol.insert(2);
		arbol.insert(4);
		arbol.insert(6);
		arbol.insert(8);
		arbol.insert(1);
		arbol.insert(9);
		arbol.insert(0);
		arbol.insert(60);
		System.out.println("Arbol: "+arbol);

	}
}
