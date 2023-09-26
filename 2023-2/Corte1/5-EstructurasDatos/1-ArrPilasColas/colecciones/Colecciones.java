/**
 * Ejemplo de colecciones en java
 * @author Carlos A Delgado
 * @date 26/Sep/2023
 */
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
public class Colecciones {
	public static void main(String[] args) {
		Stack<Integer> pila = new Stack<Integer>();
		System.out.println("Pila: " + pila);
		pila.push(1);
		pila.push(2);
		pila.push(3);
		pila.push(4);
		System.out.println("Pila: " + pila);
		System.out.println("Pila.pop(): " + pila.pop()); //4
		System.out.println("Pila.pop(): " + pila.pop()); //3
		pila.push(10);
		System.out.println("Pila.pop(): " + pila.pop()); //10
		pila.stream().forEach((n) -> {
			System.out.println("Pila: " + n);
		});
		System.out.println("******************************");
		pila.stream().map((n) -> n * 2).forEach((n) -> {
			System.out.println("Pila: " + n);
		});
		System.out.println("******************************");
		pila.stream().filter((n) -> (n % 2 == 0)).forEach((n) -> {
			System.out.println("Pila: " + n);
		});
		System.out.println("******************************");
		pila.stream().reduce((n, m) -> n + m).ifPresent((n) -> {
			System.out.println("Pila: " + n);
		});

		Queue<Integer> cola = new LinkedList<Integer>();
		cola.add(1);
		cola.add(2);
		System.out.println("Cola: " + cola);
		System.out.println("Cola.poll(): " + cola.poll()); //1
		System.out.println("Cola: " + cola);
	}

}
