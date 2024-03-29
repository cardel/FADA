/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package ordenamiento;

import org.junit.jupiter.api.Test;
import java.util.Arrays;
import static org.junit.jupiter.api.Assertions.*;

class CountingSortTest {
  @Test void casoBase() {
    CountingSort classUnderTest = new CountingSort();
    int[] A = {3, 5, 2, 1, 4};
    int[] B = {1, 2, 3, 4, 5};
    assertArrayEquals(B, classUnderTest.sort(A), "El arreglo no esta ordenado");
      
  }

  @Test 
  void casoFuerteProMega() {
  CountingSort classUnderTest = new CountingSort();
  for (int i=0; i<1000; i++) {
      int[] A = new int[10000];
      for (int j=0; j<10000; j++) {
        A[j] = 1 + (int) (Math.random() * 10000);
      }
      int[] B = classUnderTest.sort(A);
      int[] expected = A.clone();
      Arrays.sort(expected);
      assertArrayEquals(expected, B, "El arreglo no esta ordenado");
          
          
    }

  }
}
