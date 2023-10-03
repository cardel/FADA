/**
 * Clase principal para mostrar ejemplos
 * @author Carlos Delgado
 * @date 03-Oct-2023
 */

class Main {
	public static void main(String args[]){
		Lista objLista = new Lista();
		System.out.println("Lista vacia: " + objLista);
		objLista.insertar(5);
		objLista.insertar(10);
		System.out.println("Lista con 2 elementos: " + objLista);
		objLista.insertar(15);
		objLista.insertar(20);
		System.out.println("Lista con 4 elementos: " + objLista);
		System.out.println("Buscando el elemento 10: " + objLista.buscar(10));
		System.out.println("Buscando el elemento 100: " + objLista.buscar(100));
		System.out.println("Devolver la posición 3: " + objLista.elementoAt(3));
		try {
			objLista.elementoAt(4);
		}
		catch (IndexOutOfBoundsException e) {
			System.out.println("Error: " + e.getMessage());
		}

		objLista.eliminar(5);
		System.out.println("Lista con 3 elementos: " + objLista);

		objLista.eliminar(20);
		System.out.println("Lista con 2 elementos: " + objLista);

		objLista.eliminar(15);
		System.out.println("Lista con 1 elemento: " + objLista);

		objLista.eliminar(10);
		System.out.println("Lista vacia: " + objLista);
		
	}

	

}
