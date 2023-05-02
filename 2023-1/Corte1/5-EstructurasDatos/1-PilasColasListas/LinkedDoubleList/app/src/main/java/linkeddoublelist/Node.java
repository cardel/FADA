package linkeddoublelist;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import java.beans.ConstructorProperties;

@AllArgsConstructor //Esto hace un constructor con todos los elementos
public class Node {

    @Getter
    @Setter
    private Node prev;

    @Getter
    @Setter
    private Node next;

    @Getter
    @Setter
    private int value;


}
