/**
 * Lista enlazada
 * @author Carlos Delgado
 * @date 03/Oct/2023
 */

class Lista {
	private Nodo head;
	private int  size;

	public Lista() {
		head = null;
		size = 0;
	}

	public void insertar(int x) {
		Nodo nuevo = new Nodo(x);
		if (head==null) {
			head = nuevo;
		}
		else {
			Nodo aux = head;
			nuevo.setSiguiente(aux);
			head = nuevo;
			size++;	
			aux.setAnterior(nuevo);		
		}
	}
	//Complejidad O(n)
	public Nodo buscar(int x) {
		Nodo aux = head;
		while (aux != null) {

			if(aux.getDato()==x) {
				return aux;
			}
			else {
				aux = aux.getSiguiente();
			}
		}
		return null;
	}
	//Complejidad O(i) --> O(n)
	public Nodo elementoAt(int i) {
		Nodo aux = head;
		while (aux != null){
			if (i==0){
				return aux;
			}
			else {
				aux = aux.getSiguiente();
				i--;
			}
		}
		throw new IndexOutOfBoundsException("Indice por fuera del rango");

	}
	
	public void eliminar(int n) {
		Nodo x = buscar(n); //Nodo o null O(n)
		if (x!=null) {
			Nodo anterior = x.getAnterior();
			Nodo siguiente = x.getSiguiente();
			if (anterior == null) { //Elimino el primero
				head = siguiente;
			}
			else {
				anterior.setSiguiente(siguiente);
			}

			if (siguiente != null) { //No aplica para el ultimo elemento
				siguiente.setAnterior(anterior);
			}
		}
	
	}

	@Override
	public String toString() {
		String salida = "";
		Nodo aux = head;
		while (aux!=null) {
			salida += String.valueOf(aux.getDato()) + " ";
			aux = aux.getSiguiente();
		}
		return salida;
	}

}
