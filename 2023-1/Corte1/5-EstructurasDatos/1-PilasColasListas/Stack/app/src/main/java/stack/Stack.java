package stack;

import java.nio.BufferOverflowException;
import java.nio.BufferUnderflowException;

public class Stack {
    private int[] array;
    private int top;
    private int size;
    public Stack(int n)
    {
        array = new int[n];
        top = 0;
        size = n;
    }

    public boolean emptyStack()
    {
        return this.top == 0;
    }

    public void push(int value) throws StackOverflowError
    {
        if (this.top < this.size)
        {
            this.top++;
            this.array[this.top - 1] = value;
        }
        else
        {
            throw new BufferOverflowException();
        }
    }

    public int pop()
    {
        if (this.top > 0)
        {
            int value = this.array[this.top - 1];
            this.top--;
            return value;
        }
        throw new BufferUnderflowException();
    }
}
