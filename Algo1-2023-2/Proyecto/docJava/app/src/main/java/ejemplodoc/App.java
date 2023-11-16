package ejemplodoc;

/**
 * Esta clase es principal
 * @author Carlos Delgado
 * @version 1.0
 */
public class App {
    /**
     * Esta función genera un saludo personalizador
    * @param msg Mensaje personalizado
    * @return Saludo personalizado
    */
    public String getGreeting(String msg) {
        return "Hello World! "+msg;
    }

    public static void main(String[] args) {
        System.out.println(new App().getGreeting("Hola"));
    }
}
