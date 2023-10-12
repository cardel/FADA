/**
 * Descripción: Solución de un problema de pilas
 * Ejemplo brackets: {[(())]}
 * @author Carlos A Delgado
 * @date 12/10/2023
 */
import java.util.Stack;
import java.util.HashMap;
public class PilasEjemplo {
	public boolean verificar(String cadena) {
		HashMap<String, String> entradas = new HashMap<String, String>();
		entradas.put("{", "}");
		entradas.put("[", "]");
		entradas.put("(", ")");
		entradas.put("<", ">");
	 	String abiertos = "{[(<";
		String cerrados = "}])>";

		Stack<String> pila = new Stack<String>();
		for (String e : cadena.split("")) {
			if (abiertos.contains(e)) {
				pila.push(e);
			}
			else {
				if (cerrados.contains(e)) {
					if (pila.empty()) {
						return false;
					}
					String elem = pila.pop();
					String cerrado = entradas.get(elem);
					if (!cerrado.equals(e)) {
						return false;
					}
				}
			}
		}


		return pila.empty();

	}
	public static void main(String[] args) {
		
		PilasEjemplo pe = new PilasEjemplo();
		System.out.println(pe.verificar("([<{abc123abc}>])"));
		System.out.println(pe.verificar("([<{abc123abc}>])}"));
		System.out.println(pe.verificar("([<{abc123abc)>]}"));
		System.out.println(pe.verificar("(){}[]<>{{}}()"));
	}
	
}
