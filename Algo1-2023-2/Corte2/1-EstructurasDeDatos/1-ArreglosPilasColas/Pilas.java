/**
 * Esta implementación es de las pilas en java
 * @author Carlos Delgado
 * @date 12/10/2023
 */

public class Pilas {
	
	public void ejecutar() {

		Pila p = new Pila(5);
		
		try {
			System.out.println(p);
			p.Push(1);
			System.out.println(p);
			p.Push(2);
			System.out.println(p);
			p.Push(3);
			System.out.println(p);
			p.Push(4);
			System.out.println(p);
			p.Push(5);
			System.out.println(p);
			p.Push(6); //Excepción
		} catch (OverFlow e) {
			System.out.println("Excepción capturada " + e.getMessage());
		}

		//Prueba de pop
		try {
			Pila p2 = new Pila(5);
			p2.Push(1);
			p2.Push(2);
			p2.Push(3);
			p2.Push(4);
			p2.Push(5);
			System.out.println(p2);
			System.out.println(p2.Pop());
			System.out.println(p2);
			System.out.println(p2.Pop());
			System.out.println(p2);
			System.out.println(p2.Pop());
			System.out.println(p2);
			System.out.println(p2.Pop());
			System.out.println(p2);
			System.out.println(p2.Pop());
			System.out.println(p2);
			System.out.println(p2.Pop()); //Excepción
		}
		catch(UnderFlow e) {
			System.out.println("Excepción capturada " + e.getMessage());
		}
	}


	public static void main(String[] args) {
		Pilas p = new Pilas();
		p.ejecutar();

	}

	class Pila {
		private int[] arr;
		private int top;

		public Pila(int size) {
			arr = new int[size];
			top = 0;
		}
		
		public void Push(int data) throws OverFlow {
			if(top == arr.length) {
				throw new OverFlow();
			}
			arr[top] = data;
			top++;
		}
		
		public int Pop() throws UnderFlow{
			if (top == 0) {
				throw new UnderFlow();
			}
			top--;
			return arr[top];
		}

		@Override
		public String toString() {
			String str = "[";
			for (int i = 0; i < top; i++) {
				str += arr[i] + " ";
			}
			return str + "]" + "top = "+top;
		}

	
	}

	class OverFlow extends RuntimeException {
		public OverFlow() {
			super("Pila llena");
		}

	}
	class UnderFlow extends RuntimeException {
		public UnderFlow() {
			super("Pila vacía");
		}
	}

}
