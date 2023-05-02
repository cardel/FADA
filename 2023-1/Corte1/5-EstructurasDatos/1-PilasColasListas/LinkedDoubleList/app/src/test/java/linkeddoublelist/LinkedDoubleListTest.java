package linkeddoublelist;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class LinkedDoubleListTest {

    @Test
    void insert() {
        LinkedDoubleList objList = new LinkedDoubleList();

        objList.insert(10);
        objList.insert(20);
        objList.insert(30);

        assertEquals(objList.search(0), 30);
        assertEquals(objList.search(1), 20);
        assertEquals(objList.search(2), 10);
    }

    @Test
    public void delete() {
        LinkedDoubleList objList = new LinkedDoubleList();

        objList.insert(10); //2
        objList.insert(20); //1
        objList.insert(30); //0

        objList.delete(1);
        assertEquals(objList.search(1),10);
        objList.delete(0);
        assertThrows(
                ArrayIndexOutOfBoundsException.class,
                () -> objList.delete(1)
        );

        objList.delete(0);

        assertThrows(
                ArrayIndexOutOfBoundsException.class,
                () -> objList.delete(0)
        );
    }
}