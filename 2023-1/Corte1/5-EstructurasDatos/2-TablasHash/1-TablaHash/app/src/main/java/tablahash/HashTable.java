package tablahash;

import java.util.LinkedList;

public class HashTable {

    private LinkedList<LinkedList<Integer> >[] array;
    private int m;
    public HashTable(int n){
        this.array = new LinkedList[n];
        for (int i = 0; i<n; i++) {
            this.array[i] = new LinkedList<LinkedList<Integer>>();
        }
        this.m = n;
    }

    public void insert(int key, int value) {
        int pos = hashFunction(key);
        LinkedList<Integer> elm = new LinkedList<Integer>();
        elm.add(key);
        elm.add(value);
        array[pos].add(elm);
    }

    public int search(int key) throws NullPointerException{
        int pos = hashFunction(key);
        LinkedList<LinkedList<Integer> > elm = this.array[pos];

        for (LinkedList<Integer> e : elm){
            if (e.get(0) == key) {
                return e.get(1);
            }
        }
        throw new NullPointerException();
    }

    public void delete(int key) {
        int pos = hashFunction(key);
        LinkedList<LinkedList<Integer> > elm = this.array[pos];

        for (LinkedList<Integer> e : elm){
            if (e.get(0) == key) {
                elm.remove(e);
                return;
            }
        }
        throw new NullPointerException();
    }

    public int hashFunction(int key) {
        return key % this.m;
    }
}
