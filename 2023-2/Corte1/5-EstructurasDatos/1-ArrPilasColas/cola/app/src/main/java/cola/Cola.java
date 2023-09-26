/**
 * Implementación de una cola
 * @author Carlos Delgado
 * @date 26/09/2023
 */
package cola;

import exceptions.OverFlow;
import exceptions.UnderFlow;

import java.util.Arrays;

public class Cola {
    private int[] arr;
    private int head;
    private int tail;
    private int num_elements;
    private int size;

    public Cola(int size) {
        this.arr = new int[size];
        this.head = 1;
        this.tail = 1;
        this.num_elements = 0;
        this.size = size;
    }

    public void enqueue(int n) throws OverFlow {
        if (num_elements == size) {
            throw new OverFlow("La cola está llena");
        } else {
            arr[tail - 1] = n;
            if (tail == arr.length) {
                tail = 1;
            } else {
                tail++;
            }
            num_elements++;
        }
    }

    /**
     * Metodo de dequeue
     *
     * @return int elemento eliminado
     * @throws UnderFlow si la cola está vacía
     */
    public int dequeue() throws UnderFlow {
        if (num_elements == 0) {
            throw new UnderFlow("La cola está vacía");
        }
        int elemento = arr[head - 1];
        if (head == arr.length) {
            head = 1;
        } else {
            head++;
        }
        num_elements--;
        return elemento;
    }

    /**
     * Representación de la cola en una cadena de caracteres
     */
    @Override
    public String toString() {
        return Arrays.toString(arr) + " head: " + head + " tail: " + tail + " num_elementos: " + num_elements;
    }


}
