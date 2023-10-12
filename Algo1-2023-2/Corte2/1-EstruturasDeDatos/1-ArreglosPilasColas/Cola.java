/**
 * Implementación de cola
 * @author Carlos Delgado
 * @date 12/10/2023
 */
import java.util.Random;
public class Cola {
	public void ejecutar() {
		
		Queue cola = new Queue(5);
		try {
			System.out.println(cola);
			cola.enqueue(1);
			System.out.println(cola);
			cola.enqueue(2);
			System.out.println(cola);
			cola.enqueue(3);
			System.out.println(cola);
			cola.enqueue(4);
			System.out.println(cola);
			cola.enqueue(5);
			System.out.println(cola);
			cola.enqueue(6);
		} catch (OverFlow e) {
			System.out.println(e.getMessage());
		}

		Queue cola2 = new Queue(5);
		try {
			System.out.println(cola2);
			cola2.enqueue(1);
			System.out.println(cola2);
			cola2.enqueue(2);
			System.out.println(cola2);
			cola2.enqueue(3);
			System.out.println(cola2);
			cola2.enqueue(4);
			System.out.println(cola2);
			cola2.enqueue(5);
			System.out.println(cola2);
			//Desencolar
			System.out.println("Desencolando: " + cola2.dequeue());
			System.out.println(cola2);
			System.out.println("Desencolando: " + cola2.dequeue());
			System.out.println(cola2);
			System.out.println("Desencolando: " + cola2.dequeue());
			System.out.println(cola2);
			System.out.println("Desencolando: " + cola2.dequeue());
			System.out.println(cola2);
			System.out.println("Desencolando: " + cola2.dequeue());
			System.out.println(cola2);
			System.out.println("Desencolando: " + cola2.dequeue());
		}
		catch (UnderFlow e) {
			System.out.println(e.getMessage());
		}
		catch (OverFlow e) {
			System.out.println(e.getMessage());
		}
		
		try {
			Queue cola3 = new Queue(100);
			Random objRandom = new Random();
			for (int i = 0; i < 90; i++) {
				cola3.enqueue(objRandom.nextInt(1000));
				System.out.println(cola3);
				if (objRandom.nextInt(1000) % 2 == 0) {
					System.out.println("Desencolando: " + cola3.dequeue());
					System.out.println(cola3);
				}
				if (objRandom.nextInt(1000) % 3 == 0) {
					cola3.enqueue(objRandom.nextInt(1000));
					System.out.println(cola3);
				}
			}
			cola3.dequeue();


		}
		catch (UnderFlow e) {
			System.out.println(e.getMessage());
		}
		catch (OverFlow e) {
			System.out.println(e.getMessage());
		}

			
	}
	public static void main(String args[]){
		Cola cola = new Cola();
		cola.ejecutar();

	}
	class Queue {
		private int head;
		private int tail;
		private int size;
		private int[] queue;
		private int num_elements;

		public Queue(int size) {
			this.head = 0; //Posición inicial de la cabeza
			this.tail = 0; //Posición inicial de la cola
			this.size = size;
			this.queue = new int[size];
			this.num_elements = 0;
		}

		public void enqueue(int x) throws OverFlow {
		
			//Si la cola está llena: head = tail y num_elements = size
			if (this.head == this.tail && this.num_elements == this.size) {
				throw new OverFlow();
			} else {
				//Colocando el elemento en la posición de tail
				this.queue[this.tail] = x;
				this.tail++; //Incrementamos tail
				//Si tail = size, tail = 1, sino tail = tail +
				if (this.tail == this.size) {
					this.tail = 0;
				} 
				this.num_elements++;
			}
		}

		/**
		 * Metodo para desencolar dequeue
		 * @return int elemento desencolado
		 */
		 public int dequeue() throws UnderFlow {
			if (num_elements == 0) {
				throw new UnderFlow();
			}
			int x = this.queue[this.head];
			this.head++;
			if (this.head == this.size) {
				this.head = 0;
			}
			this.num_elements--;
			return x;
		 }
		@Override
		public String toString() {
			String result = "";
			for (int i = 0; i < this.size; i++) {
				if (i == this.head) {
					result += " H ";
				}
				if (i == this.tail) {
					result += " T ";
				}
				result += this.queue[i] + " ";
			}
			return result + " head = " + head + " tail = " + tail;
		}

	}

	class OverFlow extends Exception {
		public OverFlow() {
			super("Overflow");
		}
	}

	class UnderFlow extends Exception {
		public UnderFlow() {
			super("Underflow");
		}
	}
}
