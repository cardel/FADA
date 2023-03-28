

public class Factorial {

  public long getFactorial(long n) {
    if (n==0) {
      return 1;
    }
    else {
      if (n==1) {
        return 1;
      }
      else {
        return n*getFactorial(n-1);
      }
    }

  }
  public long algoritmoFactorial(long n){
    long indice = 0;
    long resultado = 1;

    while(indice !=n) {
      System.out.println("("+indice+","+resultado+")"+"("+indice+","+getFactorial(indice)+")");
      indice++;
      resultado*=indice;
    }
    return resultado;
  }
  public static void main(String[] args) {
    Factorial objFactorial = new Factorial();
    objFactorial.algoritmoFactorial(10);
  }
  
}
