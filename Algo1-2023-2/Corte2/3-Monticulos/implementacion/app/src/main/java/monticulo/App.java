/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package monticulo;
import java.util.Arrays;
public class App {
    public String getGreeting() {
        return "Hello World!";
    }

    public static void main(String[] args) {
    
      Monticulo obj = new Monticulo(20);
      int[] arr = {9,0,1,2,31,32,-1,10,12,13,15,16,18,0,-3,-4,-5};
      try{
        obj.insert(arr);
        System.out.println(Arrays.toString(obj.heapSort()));
      }
      catch(Exception e){

        System.out.println(e.getMessage());
      }
    }
}
