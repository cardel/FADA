public class Raiz {
  
  public void get_raiz(double x, double d) {
    double a = 1.0;
    while (Math.abs(a*a-x)>=d) {
      System.out.println(a);
      a = (a + x/a)/2.0;
    }

  }
  public static void main(String[] args) {
    Raiz obRaiz = new Raiz();
    obRaiz.get_raiz(49, 0.0000001);
    obRaiz.get_raiz(100,0.0000001);
  }
}
