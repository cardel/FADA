package stack;
import java.util.ArrayList;
import java.util.Stack;
public class ExampleBrackets {
    public boolean solve(String str) {
        //Llenando dos arrays con los simbolos y de salida como listas paralelas
        ArrayList<Character> symInput = new ArrayList<>();
        symInput.add('(');
        symInput.add('{');
        symInput.add('<');
        symInput.add('[');

        ArrayList<Character> symOutput = new ArrayList<>();
        symOutput.add(')');
        symOutput.add('}');
        symOutput.add('>');
        symOutput.add(']');

        Stack<Character> objStack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            char elm = str.charAt(i); //Tomo el char
            //Si es un elemento de entrada lo inserto
            if (symInput.contains(elm)) {
                objStack.push(elm);
            }

            //Si es un elemento de salida
            if (symOutput.contains(elm)) {
                if (!objStack.empty()) {
                    //Obtengo a posición del elemento de salida
                    int pos = symOutput.indexOf(elm);
                    char elmStack = objStack.pop();
                    //Si el simbolo de apertura de lo que estoy cerrando es igual al tope de la pila
                    if (!(symInput.get(pos) == elmStack)) {
                        return false;
                    }
                }
                else {
                    return false;
                }
            }
        }

        return objStack.empty();
    }
}
