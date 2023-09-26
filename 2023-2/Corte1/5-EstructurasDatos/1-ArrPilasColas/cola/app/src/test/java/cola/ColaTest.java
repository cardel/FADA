package cola;

import exceptions.OverFlow;
import exceptions.UnderFlow;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class ColaTest {

    @Test
    void enqueue() {
        Cola objCola = new Cola(9);
        assertEquals("[0, 0, 0, 0, 0, 0, 0, 0, 0] head: 1 tail: 1 num_elementos: 0", objCola.toString());
        try {
            objCola.enqueue(1);
            assertEquals("[1, 0, 0, 0, 0, 0, 0, 0, 0] head: 1 tail: 2 num_elementos: 1", objCola.toString());
            objCola.enqueue(2);
            assertEquals("[1, 2, 0, 0, 0, 0, 0, 0, 0] head: 1 tail: 3 num_elementos: 2", objCola.toString());
            objCola.enqueue(3);
            assertEquals("[1, 2, 3, 0, 0, 0, 0, 0, 0] head: 1 tail: 4 num_elementos: 3", objCola.toString());
            objCola.enqueue(4);
            assertEquals("[1, 2, 3, 4, 0, 0, 0, 0, 0] head: 1 tail: 5 num_elementos: 4", objCola.toString());
            objCola.enqueue(5);
            assertEquals("[1, 2, 3, 4, 5, 0, 0, 0, 0] head: 1 tail: 6 num_elementos: 5", objCola.toString());
            objCola.enqueue(6);
            assertEquals("[1, 2, 3, 4, 5, 6, 0, 0, 0] head: 1 tail: 7 num_elementos: 6", objCola.toString());
            objCola.enqueue(7);
            assertEquals("[1, 2, 3, 4, 5, 6, 7, 0, 0] head: 1 tail: 8 num_elementos: 7", objCola.toString());
            objCola.enqueue(8);
            assertEquals("[1, 2, 3, 4, 5, 6, 7, 8, 0] head: 1 tail: 9 num_elementos: 8", objCola.toString());
            objCola.enqueue(9);
            assertEquals("[1, 2, 3, 4, 5, 6, 7, 8, 9] head: 1 tail: 1 num_elementos: 9", objCola.toString());
            objCola.enqueue(10);
            fail("No se ha lanzado la excepción");
        } catch (OverFlow overFlow) {
            assertEquals("La cola está llena", overFlow.getMessage());
        }
    }

    @Test
    void dequeue() {
        Cola objCola = new Cola(10);
        try {
            objCola.dequeue();
            fail("No se ha lanzado la excepción");
        } catch (UnderFlow e) {
            assertEquals("La cola está vacía", e.getMessage());
        }
        try {
            objCola.enqueue(10);
            objCola.enqueue(20);
            objCola.enqueue(30);
            objCola.enqueue(40);
            objCola.enqueue(50);
            assertEquals("[10, 20, 30, 40, 50, 0, 0, 0, 0, 0] head: 1 tail: 6 num_elementos: 5", objCola.toString());
            objCola.enqueue(60);
            objCola.enqueue(70);
            objCola.enqueue(80);
            objCola.enqueue(90);
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 0] head: 1 tail: 10 num_elementos: 9", objCola.toString());
            objCola.enqueue(100);
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 1 tail: 1 num_elementos: 10", objCola.toString());
            assertEquals(10, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 2 tail: 1 num_elementos: 9", objCola.toString());
            assertEquals(20, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 3 tail: 1 num_elementos: 8", objCola.toString());
            assertEquals(30, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 4 tail: 1 num_elementos: 7", objCola.toString());
            assertEquals(40, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 5 tail: 1 num_elementos: 6", objCola.toString());
            assertEquals(50, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 6 tail: 1 num_elementos: 5", objCola.toString());
            assertEquals(60, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 7 tail: 1 num_elementos: 4", objCola.toString());
            assertEquals(70, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 8 tail: 1 num_elementos: 3", objCola.toString());
            assertEquals(80, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 9 tail: 1 num_elementos: 2", objCola.toString());
            assertEquals(90, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 10 tail: 1 num_elementos: 1", objCola.toString());
            assertEquals(100, objCola.dequeue());
            assertEquals("[10, 20, 30, 40, 50, 60, 70, 80, 90, 100] head: 1 tail: 1 num_elementos: 0", objCola.toString());
            objCola.dequeue();
            fail("No se ha lanzado la excepción");
        }
        catch (UnderFlow e) {
            assertEquals("La cola está vacía", e.getMessage());
        }
        catch (OverFlow e) {
            fail("No se esperaba la excepción");
        }
    }
}