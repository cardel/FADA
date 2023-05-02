/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package linkeddoublelist;

import java.util.ArrayList;
import java.util.LinkedList;

public class App {

    public static void main(String[] args) {
        int [] size = {800000,1000000,1200000};


        for (int i=0; i<size.length; i++) {
            double timeArray = 0;
            double timeList = 0;
            double timeArrayList = 0;
            double timeLinkedList = 0;

            double timeIList = 0;
            double timeIArrayList = 0;
            double timeILinkedList = 0;
            for(int exp = 0; exp < 100; exp++)
            {
                int array[] = new int[size[i]];
                LinkedDoubleList objList = new LinkedDoubleList();

                ArrayList<Integer> arrayList = new ArrayList<>();
                LinkedList<Integer> linkedListJava = new LinkedList<>();


                for (int j = 0; j<size[i];j++) {
                    long t1 = System.currentTimeMillis();
                    objList.insert(j*2);
                    timeIList += System.currentTimeMillis() - t1;

                    long t2 = System.currentTimeMillis();
                    arrayList.add(j*2);
                    timeIArrayList += System.currentTimeMillis() - t2;

                    long t3 = System.currentTimeMillis();
                    linkedListJava.add(j*2);
                    timeILinkedList += System.currentTimeMillis() - t3;
                }
                long time1 = System.currentTimeMillis();
                //Buscar en el array
                int a = array[0];
                int b = array[size[i]/2];
                int c = array[size[i]-1];
                timeArray += System.currentTimeMillis() - time1;


                //Buscar en la lista doblemente enlazada
                long time2 = System.currentTimeMillis();

                a = objList.search(0);
                b = objList.search(size[i]/2);
                c = objList.search(size[i]-1);
                timeList = System.currentTimeMillis() - time2;

                //Buscar en la arraylist
                long time3 = System.currentTimeMillis();

                a = arrayList.get(0);
                b = arrayList.get(size[i]/2);
                c = arrayList.get(size[i]-1);
                timeArrayList = System.currentTimeMillis() - time3;

                //Buscar en la arraylist
                long time4 = System.currentTimeMillis();

                a = linkedListJava.get(0);
                b = linkedListJava.get(size[i]/2);
                c = linkedListJava.get(size[i]-1);
                timeLinkedList = System.currentTimeMillis() - time4;

            }

            System.out.println("Tiempos de inserción");
            System.out.println("ListaDouble \t"+ size[i] + "\t" + timeIList/100.0);

            System.out.println("ArrayList \t"+ size[i] + "\t" + timeIArrayList/100.0);
            System.out.println("LinkedList \t"+ size[i] + "\t" + timeILinkedList/100.0);


            System.out.println("Tiempos de busqueda");
            System.out.println("Tipo \t n \t Valor (ms)");
            System.out.println("Arreglo \t"+ size[i] + "\t" + timeArray/100.0);
            System.out.println("ListaDouble \t"+ size[i] + "\t" + timeList/100.0);

            System.out.println("ArrayList \t"+ size[i] + "\t" + timeArrayList/100.0);
            System.out.println("LinkedList \t"+ size[i] + "\t" + timeLinkedList/100.0);

        }



    }
}