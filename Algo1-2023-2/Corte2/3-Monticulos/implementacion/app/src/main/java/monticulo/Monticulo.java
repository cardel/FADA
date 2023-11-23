/**
 * Implementación de monticulos en Java
 * @author Carlos Delgado
 * @note 23-Nov-2023
 */
package monticulo; 
public class Monticulo {
  private int[] monticulo;
  private int size; //Num de elementos
  private int length; //Max capacidad del monticulo

  public Monticulo(int length) {
    this.monticulo = new int[length+1];
    this.length = length+1;
    this.size = 0;
  }

  private int father(int i) {
    return i/2;
  }

  private int left(int i) {
    return 2*i;
  }

  private int right(int i) {
    return 2*i+1;
  }
  
  public void insert(int [] arr) throws Exception {
    int n = arr.length;
    if (n > this.length) {
      throw new Exception("El arreglo que es mas grande que la capacidad");
    }
    for(int i=0; i<arr.length; i++){
      this.monticulo[i] = arr[i];
    }
    this.size = n;
  }
  
  private void heapify(int i) {
    if (i < this.size) {
      int l = left(i);
      int r = right(i);
      if (l > this.size) {
        return;
      }
      if (r < this.size ) { // el hizq y der existen en el monticulo
          if (this.monticulo[l] > this.monticulo[r] && this.monticulo[l] > this.monticulo[i]) {
          int aux = this.monticulo[i];
          this.monticulo[i] = this.monticulo[l];
          this.monticulo[l] = aux;
          heapify(l);
        }
        else {
          if (this.monticulo[r] > this.monticulo[i]){
            int aux = this.monticulo[i];
            this.monticulo[i] = this.monticulo[r];
            this.monticulo[r] = aux;
            heapify(r);
          }
        }
      }
      else { //En caso de que el hijo derecho no existe
          if (this.monticulo[l] > this.monticulo[i]){
            
            int aux = this.monticulo[i];
            this.monticulo[i] = this.monticulo[l];
            this.monticulo[l] = aux;
            heapify(l);
          }
        }
      }
    }
    private void buildHeap() {
      for (int i=this.size/2; i>=1; i--) {
        heapify(i);
      }
    }

    public int[] heapSort() {
      int size = this.size;
      int[] arrSal = new int[size];
      buildHeap();
      for (int i=this.size; i>=2; i--) {
        int aux = this.monticulo[i];
        this.monticulo[i] = this.monticulo[1];
        this.monticulo[1] = aux;
        this.size--;
        heapify(1);
      }

      for (int i=1; i<=size; i++) {
        arrSal[i-1] = this.monticulo[i];
      }
      return arrSal;
    }

  }

