package brt;
import lombok.Data;
/**
 * Arbol rojinegro
 * @author Carlos Delgado
 * @date 02-Nov-2023
 */
@Data
class BRT {
  private Nodo raiz;

  BRT () {
    this.raiz = null;
  }

  public void rotacion_derecha(Nodo y) { 
    Nodo x = y.getHIzq(); //x
    Nodo c = y.getHDer(); 
    Nodo b = x.getHDer();
    //Cambio
    if (y.getPadre() == null) {
      raiz = x;
    }
    else {
      if (y == y.getPadre().getHIzq())      {
        y.getPadre().setHIzq(x);
      }
      else{
        y.getPadre().setHDer(x);
      }
    }
    x.setPadre(y.getPadre());
    y.setPadre(x);
    x.setHDer(y);
    if (b!= null) b.setPadre(y);
    y.setHIzq(b);



  }

  public void rotacion_izquierda(Nodo x) {
    Nodo y = x.getHDer();
    Nodo b = y.getHIzq();

    if (x.getPadre() == null) {
      raiz = y;
    }
    else {
      if (x == x.getPadre().getHIzq())      {
        x.getPadre().setHIzq(y);
      }
      else{
        x.getPadre().setHDer(y);
      }
    }
    //Cambiar padres
    y.setPadre(x.getPadre());
    x.setPadre(y);
    
    if (b!= null) b.setPadre(x);
    //Cambiamos hijos
    y.setHIzq(x);
    x.setHDer(b);
  }

}
