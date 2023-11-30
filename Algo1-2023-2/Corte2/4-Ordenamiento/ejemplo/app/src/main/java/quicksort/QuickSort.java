/**
 * Clase que implementa el algoritmo Quicksort
 * @author Carlos Delgado
 * @note 30 Nov 2023
 */
package quicksort;

public class QuickSort {
  /**
   * Metodo que ordena un arreglo de enteros
   * @param A Arreglo de enteros
   * @param p Indice de inicio
   * @param r Indice de fin
   * @return es el indice donde los elementos de la izquierda son menores o igual al pivote y a la derecha son mayores
   */
  public int particion(int[] A, int p, int r) {
    int pivote = A[p];
    int i = p - 1;
    int j = r + 1;
    while(i<j) {
      do {
        j--;
      }while (!(A[j] <= pivote));
      do {
        i++;
      } while (!(A[i] >= pivote));
      if (i<j){
        int aux = A[i];
        A[i] = A[j];
        A[j] = aux;
      }
    }
    return j;
  }

  public void sort(int[] A, int p, int r) {
    if (p<r) {
      int q = particion(A, p, r);
      sort(A, p, q);
      sort(A, q+1, r);
    }

  }

}
