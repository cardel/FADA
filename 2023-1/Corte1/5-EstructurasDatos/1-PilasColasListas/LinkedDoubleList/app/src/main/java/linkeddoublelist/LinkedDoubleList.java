package linkeddoublelist;

public class LinkedDoubleList {
    private Node head;
    private int size;

    public LinkedDoubleList() {
        this.head = null;
        this.size = 0;
    }

    public void insert(int value){
        Node newNode = new Node(null,this.head, value);

        if (head != null) {
            this.head.setPrev(newNode);
        }
        this.head = newNode;
    }

    public void delete(int index) throws ArrayIndexOutOfBoundsException {
        Node current = this.head;
        int cnt = 0;
        while (current!=null && cnt < index) {
            cnt++;
            current = current.getNext();
        }

        if (current == null || index < 0) {
            throw new ArrayIndexOutOfBoundsException();
        }

        Node prev = current.getPrev();
        Node next = current.getNext();

        if (prev != null) {
            prev.setNext(next);
        }
        else {
            this.head = next;
        }

        if (next != null) {
            next.setPrev(prev);
        }

    }
    public int search(int index) {
        Node current = this.head;
        int cnt = 0;
        while (cnt < index) {
            current = current.getNext();
            cnt++;
        }
        return current.getValue();
    }

}
