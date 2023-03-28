public class Computa3 {
  
  public int sumatoria3(int i){
    int suma = 0;
    for(int j=0; j<=i-1; j++) {
      suma += Math.pow(j,3.0);
    }
    return suma;
  }

  public void calculo(int N) {
    int A = 0;
    int i = 1;
    System.out.println("Inicio ciclo externo");

    while(i<=N) {
      System.out.println(A+" "+sumatoria3(i));
      int B = 1;
      int j = 1;
      System.out.println("Inicio ciclo interno");

      while (j<=3) {
        System.out.println(B+" "+Math.pow(i,j-1));
        B = B*i;
        j++;
      }
      System.out.println("Fin ciclo interno");

      A = A+B;
      i++;
    }
    System.out.println("Fin ciclo externo");

  }
  
  public static void main(String[] args) {
    Computa3 obComputa3 = new Computa3();
    obComputa3.calculo(20); 
  }
}
