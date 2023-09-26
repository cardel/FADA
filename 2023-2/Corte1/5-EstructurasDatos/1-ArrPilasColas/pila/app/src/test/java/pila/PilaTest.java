package pila;

import excepciones.Overflow;
import excepciones.Underflow;
import org.junit.jupiter.api.Test;

import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.*;

class PilaTest {

    @Test
    void push() {
        Pila p = new Pila(5);
        try {
            assertEquals("[0, 0, 0, 0, 0] top = 0", p.toString());
            assertTrue(p.estaVacia());
            p.push(1);
            assertEquals("[1, 0, 0, 0, 0] top = 1", p.toString());
            p.push(2);
            assertEquals("[1, 2, 0, 0, 0] top = 2", p.toString());
            p.push(3);
            assertEquals("[1, 2, 3, 0, 0] top = 3", p.toString());
            p.push(4);
            assertEquals("[1, 2, 3, 4, 0] top = 4", p.toString());
            p.push(5);
            assertEquals("[1, 2, 3, 4, 5] top = 5", p.toString());
            p.push(6);
            fail("No se lanzo la excepcion");
        } catch (Overflow e) {
            assertEquals("La pila esta llena", e.getMessage());
        }

        assertEquals("[1, 2, 3, 4, 5] top = 5", p.toString());
    }


    @Test
    void pop() {
        Pila p = new Pila(5);
        assertTrue(p.estaVacia());
        try {
            p.pop();
            fail("No se lanzo la excepcion");
        } catch (Underflow e) {
            assertEquals("La pila esta vacia", e.getMessage());
        }
        try {
            p.push(1);
            p.push(2);
            p.push(3);
            p.push(4);
            p.push(5);
            assertEquals("[1, 2, 3, 4, 5] top = 5", p.toString());
            assertEquals(5, p.pop());
            assertEquals("[1, 2, 3, 4, 5] top = 4", p.toString());
            p.push(10);
            assertEquals("[1, 2, 3, 4, 10] top = 5", p.toString());
            assertEquals(10, p.pop());
            assertEquals("[1, 2, 3, 4, 10] top = 4", p.toString());
            assertEquals(4, p.pop());
            assertEquals("[1, 2, 3, 4, 10] top = 3", p.toString());
            assertEquals(3, p.pop());
            assertEquals("[1, 2, 3, 4, 10] top = 2", p.toString());
            assertEquals(2, p.pop());
            assertEquals("[1, 2, 3, 4, 10] top = 1", p.toString());
            assertEquals(1, p.pop());
            assertEquals("[1, 2, 3, 4, 10] top = 0", p.toString());
            assertTrue(p.estaVacia());
            p.pop(); //Aqui debe lanzar la excepción
            fail("No se lanzo la excepcion");
        } catch (Underflow e) {
            assertEquals("La pila esta vacia", e.getMessage());
        }
        catch (Overflow e) {
            fail("Se lanzo la excepcion equivocada");
        }
    }
}