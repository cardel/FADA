/**
 * Ejemplo de arreglos en Java
 * @author Carlos A Delgado
 * @date 12 de Oct de 2023
 */
import java.util.Arrays;
public class Arreglos {

	public void modificarArreglo(int arr[]){
		arr[0] = 100;
	}
	
	public static void main(String[] args) {
		int arreglo[] = {1,2,3,4,5};
		int[] arreglo2 = arreglo.clone();
		//Ver el arreglo
		System.out.println(arreglo);
		//Ver el primer elemento
		System.out.println(arreglo[0]);
		//Ver el segundo elemento
		System.out.println(arreglo[1]);
		//Ver el arreglo
		System.out.println(Arrays.toString(arreglo));
		Arreglos a = new Arreglos();
		a.modificarArreglo(arreglo);
		//Ver el arreglo
		System.out.println(Arrays.toString(arreglo));
		//Pasar el arreglo por valor
		a.modificarArreglo(arreglo2.clone());
		//Ver el arreglo
		System.out.println(Arrays.toString(arreglo2));

		
	}
}
