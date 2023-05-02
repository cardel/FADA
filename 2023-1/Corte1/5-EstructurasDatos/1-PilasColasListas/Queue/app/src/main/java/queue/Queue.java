package queue;

public class Queue {
    int[] queue;
    int head;
    int size;
    int tail;
    int n;

    public Queue(int n) {
        this.size = 0;
        this.queue = new int[n];
        this.tail = 1;
        this.head = 1;
        this.n = n;
    }

    public void enqueue(int val) throws UnsupportedOperationException {
        if (this.tail ==  this.head && this.size > 0) {
            throw new UnsupportedOperationException();
        }
        else {
            this.size++;
            this.queue[this.tail - 1] = val;
            if (this.tail == n)  {
                this.tail = 1;
            }
            else {
                this.tail++;
            }
        }
    }

    public int dequeue() throws  UnsupportedOperationException {
        if (this.tail == this.head && this.size == 0) {
            throw new UnsupportedOperationException();
        }
        else {
            this.size--;
            int val = this.queue[this.head - 1];
            if (this.head == n)  {
                this.head = 1;
            }
            else {
                this.head++;
            }
            return val;
        }
    }
}