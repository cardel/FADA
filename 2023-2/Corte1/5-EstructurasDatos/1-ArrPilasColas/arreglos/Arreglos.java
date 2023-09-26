/**
 * Clase para probar arreglos
 * @author Carlos Delgado
 * @date 26 de Sept de 2023
 */
import java.util.Arrays;
public class Arreglos {

	public void modificar(int[] arr) {
		arr[1] = 20; //Paso es por referencia (arr = pos del arrelo) se modifica el arreglo original
	}
	public static void main(String args[]) {
		int arreglo[] = new int[6]; //Estoy reservando 6*32 bits memoria
		System.out.println(arreglo);
		System.out.println(Arrays.toString(arreglo));
		Arreglos objArreglos = new Arreglos();
		objArreglos.modificar(arreglo);
		System.out.println(Arrays.toString(arreglo));
	}
}
