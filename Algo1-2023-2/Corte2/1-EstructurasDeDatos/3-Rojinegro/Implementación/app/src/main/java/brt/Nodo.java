/**
 * Clase nodo
 * @author Carlos Delgado
 * @date 02-Nov-2023
 */
package brt;

import lombok.Getter;
import lombok.Setter;
@Getter @Setter //Anotacion de lombok para generar los getters y setters
class Nodo {
    // Atributos
    private int dato;
    private Nodo hIzq;
    private Nodo hDer;
    private boolean negro;
    private Nodo padre;
    // Constructor
    Nodo(int dato) {
      this.dato = dato;
      this.hDer = null;
      this.hIzq = null;
      this.padre = null;
      this.negro = false;
    }

    @Override
    public String toString() {
      String l = ""+this.hIzq;
      String r = ""+this.hDer;
      return "( " +this.dato + " " + l + r + ")";
    }

}
