/**
 * Esta clase va a implementar los elementos de la lista enlazada
 * @author Carlos A Delgado
 * @date 03 de Oct de 2023
 */

class Nodo {
	private int dato;
	private Nodo siguiente;
	private Nodo anterior;

	Nodo(int dato) {
		this.dato = dato;
		this.siguiente = null;
		this.anterior = null;
	}

	public int getDato() {
		return dato;
	}

	public Nodo getSiguiente() {
		return siguiente;
	}

	public Nodo getAnterior() {
		return anterior;
	}

	public void setDato(int dato) {
		this.dato = dato;
	}

	public void setSiguiente(Nodo siguiente) {
		this.siguiente = siguiente;
	}

	public void setAnterior(Nodo anterior) {
		this.anterior = anterior;
	}

	@Override
	public String toString() {
		return "Nodo [dato=" + dato + "]";
	}



}
