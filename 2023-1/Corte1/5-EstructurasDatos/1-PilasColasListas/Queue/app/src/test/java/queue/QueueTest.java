package queue;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
public class QueueTest {

    @Test
    public void testQueue () {
        Queue objQueue = new Queue(5);

        objQueue.enqueue(10);
        assertEquals(objQueue.dequeue(),10);

        objQueue.enqueue(5);
        objQueue.enqueue(10);
        objQueue.enqueue(15);
        objQueue.enqueue(20);
        objQueue.enqueue(30);

        assertThrows(UnsupportedOperationException.class,
            () -> objQueue.enqueue(35)
        );

        objQueue.dequeue();
        objQueue.dequeue();
        objQueue.dequeue();
        objQueue.dequeue();
        objQueue.dequeue();

        assertThrows(UnsupportedOperationException.class,
                () -> objQueue.dequeue()
        );

    }
}
