/**
 * Clase que implementa una pila
 * @author Carlos Delgado
 * @date 26 de Sep de 2023
 */

package pila;

import excepciones.Overflow;
import excepciones.Underflow;

import java.util.Arrays;

public class Pila {

    private int[] arr;
    private int top;
    private int tam;
    public Pila(int tam) {
        this.arr = new int[tam];
        this.tam = tam;
        this.top = 0;
    }

    /**
     * Este metodo inserta un elemento en la pila
     * @param x
     */
    public void push(int x) throws Overflow {
        if (top == tam) {
            throw new Overflow("La pila esta llena");
        }
        top++;
        arr[top-1] = x;

    }
    /**
     * Este pregunta si una pila está vacia
     */
    public boolean estaVacia() {
        return top == 0;
    }

    /**
     * Este metodo saca un elemento de la pila
     * @return el elemento que se saco de la pila
     */
    public int pop() throws Underflow {
        if (estaVacia()) {
            throw new Underflow("La pila esta vacia");
        }
        top--;
        return arr[top];
    }
    /**
     * Representa la pila como un String
     * @return String que representa la pila
     */
    @Override
    public String toString() {
        return Arrays.toString(arr) + " top = " + top;
    }
}
