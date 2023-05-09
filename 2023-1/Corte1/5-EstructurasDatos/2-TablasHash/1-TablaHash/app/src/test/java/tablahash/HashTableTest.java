package tablahash;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

class HashTableTest {

    @Test
    void insert() {
        HashTable objHashTable = new HashTable(5);
        objHashTable.insert(300,500);
        objHashTable.insert(400,200);
        objHashTable.insert(1000,400);
        objHashTable.insert(20,500);
        objHashTable.insert(30,500);
        objHashTable.insert(40,60);
        objHashTable.insert(150,40);
        objHashTable.insert(1200,400);
        objHashTable.insert(27,110);
        objHashTable.insert(33,5332);

        assertEquals(objHashTable.search(300),500);
        assertEquals(objHashTable.search(33),5332);
        assertEquals(objHashTable.search(150),40);
        assertEquals(objHashTable.search(27),110);
        assertThrows(NullPointerException.class, () -> objHashTable.search(999));

    }

    @Test
    void delete() {
        HashTable objHashTable = new HashTable(5);
        objHashTable.insert(300,500);
        objHashTable.insert(400,200);
        objHashTable.insert(1000,400);
        objHashTable.insert(20,500);
        objHashTable.insert(30,500);
        objHashTable.insert(40,60);
        objHashTable.insert(150,40);
        objHashTable.insert(1200,400);
        objHashTable.insert(27,110);
        objHashTable.insert(33,5332);

        objHashTable.delete(33);
        objHashTable.delete(1200);
        assertThrows(NullPointerException.class, () -> objHashTable.delete(33));
        assertThrows(NullPointerException.class, () -> objHashTable.search(1200));
    }
}