/**
 * Implementación del algoritmo Counting Sort
 * @author Carlos A Delgado
* @note 30/11/2023i
 */
package ordenamiento;

public class CountingSort {
  public int[] sort (int[] A) {
    //Buscar el maximo
    int k = A[0];
    for (int i=1; i<A.length; i++) {
      if (A[i] > k) {
        k = A[i];
      }
    }
    int B[] = new int[A.length];
    int C[] = new int[k+1];
    //Conteos
    for (int i=0; i<A.length; i++) {
      C[A[i] - 1]++;
    }
    //Acumulamos
    for (int i=1; i<k; i++) {
      C[i] += C[i-1];
    }

    //Llena el arreglo B
    for (int i=A.length-1; i>=0; i--) {
      B[C[A[i]-1]-1] = A[i];
      C[A[i]-1]--;
    }
    return B;

  }
}
