/**
 * Implementación de un árbol binario de búsqueda
 * @author Carlos Delgado
 * @date 03/Oct/2023
 */

class ABB {
	private Nodo raiz;

	public ABB() {
		raiz = null;
	}
	

	public Nodo buscar(int x) {
		Nodo aux = raiz;
		while (aux != null) {
				if (x == aux.getKey()) {
					return aux;
				}
				else {
					if (x <= aux.getKey()) {
						aux = aux.getLeft();
					}
					else {
						aux = aux.getRight();
					}
				}
		}
		return null;
	}

	public Nodo minimum(int x) {
		Nodo aux = buscar(x);
		while (aux.getLeft() != null) {
			aux = aux.getLeft();
		}
		return aux;
	}

	public Nodo maximum(int x) {
		Nodo aux = buscar(x);
		while (aux.getRight() != null) {
			aux = aux.getRight();
		}
		return aux;
	}

	public Nodo successor(int x) {
		Nodo aux = buscar(x);
		if (aux== null) {
			return null;
		}
		else {
			if (aux.getRight() != null) {
				return minimum(aux.getRight().getKey());
			}
			else {
				Nodo aux2 = aux.getFather();
				while (aux2 != null && aux == aux2.getRight()) {
					aux = aux2;
					aux2 = aux2.getFather();
				}
				return aux2;
			}
		}

	}

	public void insert(int x) {
		Nodo newNodo = new Nodo(x);
		if (raiz == null) {
			raiz = newNodo;
		}
		else {
			Nodo aux = raiz;
			while (true) {
				if (x <= aux.getKey()) {
					if (aux.getLeft() == null) {
						aux.setLeft(newNodo);
						newNodo.setFather(aux);
						break;
					}
					else {
						aux = aux.getLeft();
					}
				}
				else {
					if (aux.getRight() == null) {
						aux.setRight(newNodo);
						newNodo.setFather(aux);
						break;
					}
					else {
						aux = aux.getRight();
					}
				}
			
			}
		}

	}

	@Override
	public String toString() {
		return "ABB: " + raiz;
	}

}
