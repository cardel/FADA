/**
 * Definición de un nodo de un árbol
 * @author Carlos Delgado
 * @date 03/Oct/2023
 */

class Nodo {
	private int key;
	private Nodo left;
	private Nodo right;
	private Nodo father;

	public Nodo(int key) {
		this.key = key;
		this.left = null;
		this.right = null;
		this.father = null;
	}

	public int getKey() {
		return this.key;
	}

	public Nodo getLeft() {
		return this.left;
	}

	public Nodo getRight() {
		return this.right;
	}

	public Nodo getFather() {
		return this.father;
	}

	public void setKey(int key) {
		this.key = key;
	}

	public void setLeft(Nodo left) {
		this.left = left;
	}

	public void setRight(Nodo right) {
		this.right = right;
	}
	
	public void setFather(Nodo father) {
		this.father = father;
	}
	@Override
	public String toString() {
		if (this.left == null && this.right == null) {
			return this.key + "";
		}
		else {
			if (this.left == null) {
				return this.key + " " + this.right;
			}
			else {
				if (this.right == null) {
					return this.left + " " + this.key;
				}
			}
		}
		return  this.left + " " + this.key + " " + this.right;
	}

	

}
