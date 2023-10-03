/**
 * Ejemplo de las coleccion en Java
 * @author Carlos A Delgado
 * @date 03/Oct/2023
 */
import java.util.ArrayList; //Internamente es un arreglo (requiere reconstruir)
import java.util.LinkedList; //Internamente es una lista enlazada
import java.util.Date;
import java.util.stream.Collectors;

class ListaColecciones {

	public static void main(String args[]){
		ArrayList<Integer> array1 = new ArrayList<Integer>();
		LinkedList<Integer> list1 = new LinkedList<Integer>();
		//Comparar insertar
		long start = new Date().getTime();

		for(int i=0; i<100000; i++){
			array1.add(i);
		}
		long end = new Date().getTime();
		System.out.println("Tiempo de insercion en ArrayList: " + (end-start));

		start = new Date().getTime();
		for(int i=0; i<100000; i++){
			list1.add(i);
		}
		end = new Date().getTime();
		System.out.println("Tiempo de insercion en LinkedList: " + (end-start));
	
		//Comparar busqueda
		start = new Date().getTime();
		for(int i=0; i<100000; i++){
			array1.get(i);
		}
		end = new Date().getTime();

		System.out.println("Tiempo de busqueda en ArrayList: " + (end-start));
		
		start = new Date().getTime();
		for(int i=0; i<100000; i++){
			list1.get(i);
		}
		end = new Date().getTime();
		System.out.println("Tiempo de busqueda en LinkedList: " + (end-start));
		

		//Aplicar funciones sobre las colecciones
		LinkedList<Integer> lista2 = new LinkedList<Integer>();
		for (int i=0; i<10; i++) {
			lista2.add(i);
		}

		LinkedList<Integer> lista6 = new LinkedList<Integer>();
		for (int i=0; i<100000; i++) {
			lista6.add(i);
		}
		System.out.println("lista2: " + lista2);
		//Elevar al cuadrado con iterador (stream)
		start = new Date().getTime();
		LinkedList<Integer> lista3 = lista6.stream().map((x) -> x*x).collect(Collectors.toCollection(LinkedList::new));
		end = new Date().getTime();
		System.out.println("Tiempo de elevar al cuadrado con stream: " + (end-start));
		//Elevar al cuadrado con iterador (for)
		start = new Date().getTime();
		LinkedList<Integer> lista5 = new LinkedList<Integer>();
		for (int i=0; i<lista6.size(); i++) {
			lista5.add(lista6.get(i)*lista6.get(i));
		}
		end = new Date().getTime();

		System.out.println("Tiempo de elevar al cuadrado con for: " + (end-start));
		//Filtrar numeros pares
		LinkedList<Integer> lista4 = lista2.stream().filter((x) -> x%2==0).collect(Collectors.toCollection(LinkedList::new));
		System.out.println("Lista4: " + lista4);

		//Reduce (sumar los elementos de la lista)
		start = new Date().getTime();
		int suma = lista6.stream().reduce(0, (x,y) -> x+y);
		end = new Date().getTime();
		System.out.println("Suma: " + suma);
		System.out.println("Tiempo de sumar con reduce: " + (end-start));
		//SUmar los elementos con un for
		start = new Date().getTime();
		int suma2 = 0;
		for (int i=0; i<lista6.size(); i++) {
			suma2 += lista6.get(i);
		}
		end = new Date().getTime();
		System.out.println("Suma2: " + suma2);
		System.out.println("Tiempo de sumar con for: " + (end-start));
	}
} 
