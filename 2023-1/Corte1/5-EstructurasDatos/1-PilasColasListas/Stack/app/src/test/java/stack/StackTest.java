package stack;

import org.junit.jupiter.api.Test;

import java.nio.BufferOverflowException;
import java.nio.BufferUnderflowException;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertThrows;

class StackTest {


    @Test
    void emptyStack() {
        Stack objStack = new Stack(10);
        assertTrue(objStack.emptyStack());

        objStack.push(1);
        objStack.push(2);
        objStack.pop();
        assertFalse(objStack.emptyStack());
        objStack.pop();
        assertTrue(objStack.emptyStack());
    }

    @Test
    void push() {
        Stack objStack = new Stack(5);
        objStack.push(5);
        objStack.push(10);
        objStack.push(15);
        objStack.push(200);
        objStack.push(100);
        assertThrows(BufferOverflowException.class, () -> objStack.push(300));
    }

    @Test
    void pop() {
        Stack objStack = new Stack(5);
        objStack.push(5);
        objStack.push(10);
        objStack.push(15);
        objStack.push(200);
        objStack.push(100);
        assertEquals(objStack.pop(), 100);
        assertEquals(objStack.pop(), 200);
        assertEquals(objStack.pop(), 15);
        assertEquals(objStack.pop(), 10);
        assertEquals(objStack.pop(), 5);
        assertTrue(objStack.emptyStack());
        assertThrows(BufferUnderflowException.class, () -> objStack.pop());

    }
}