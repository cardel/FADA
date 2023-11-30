/**
 *
* Implementación de Bucket Sort
* @note 30/11/2023
*/

package ordenamiento;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.HashMap;

public class BucketSort {
  public void sort(double[] A){
    int buckets = 10;
    HashMap<Integer, LinkedList<Double>> map = new HashMap<Integer, LinkedList<Double>>();
    for (int i=0; i<buckets; i++) {
      map.put(i, new LinkedList<Double>());
    }
    for (int i=0; i<A.length; i++) {
      int pos = (int) A[i]*buckets;
      map.get(pos).add(A[i]);
    }
    //Ordenar los buckets
    for (int i=0; i<buckets; i++) {
      map.get(i).sort(Comparator.naturalOrder());
    }
    //Unir los buckets
    int index = 0;
    for (int i=0; i<buckets; i++) {
      for (int j=0; j<map.get(i).size(); j++) {
      A[index] = map.get(i).get(j);
      index++;
      }
    }
  }
}
