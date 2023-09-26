/*
 * Ejercicio de los brackets, parentesis y llaves
 * @author: Carlos Delgado
 * @date: 26/Sep/2023
 */
import java.util.Stack;

public class EjercicioEmpresa {
	public boolean validar(String cadena) {  
		Stack<Character> pila = new Stack<Character>();
		char[] cadenaChar = cadena.toCharArray();
		for (Character e : cadenaChar) {
			//Si es un simbolo de apertura lo metemos en la pila
		    if (e == '(' || e == '[' || e == '{' || e == '<') {
		    		pila.push(e);
			}
			/*
 			Si es un simbolo de cerradura comprobamos que el simbolo de apertura de acuerdo a su posicion dado que son listas paralelas
 			*/
		    if (e == ')' || e == ']' || e == '}' || e == '>') {
			char c = '(';
			switch(e) {
				case ']':
					c = '[';
					break;
				case '}':
					c = '{';
					break;
				case '>':
					c = '<';
					break;	
			}
			if (pila.pop() != c) {
				return false;
			}
		    }
		}
		return pila.isEmpty();

	}
	public static void main(String[] args) {
		EjercicioEmpresa ejercicio = new EjercicioEmpresa();
		String cadena = "({})";
		System.out.println(ejercicio.validar(cadena));
		String cadenamala = "({)}";
		System.out.println(ejercicio.validar(cadenamala));
		String cadenamala2 = "";
		System.out.println(ejercicio.validar(cadenamala2));
    	}
}
