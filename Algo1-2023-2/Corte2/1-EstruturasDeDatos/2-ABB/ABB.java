/**
 * Implementación de un arbol binario de búsqueda
 * @author Carlos Delgado
* @date 26/10/2023
*/ 

public class ABB {
  private Nodo raiz;

  public ABB(){
    this.raiz = null;
  }

  public Nodo getRaiz(){
    return raiz;
  }

  /**
   * Insertar un elemento
   */
  public void insertar(int dato) {
    Nodo nuevo = new Nodo(dato); //Creo un nuevo Nodo
    Nodo actual = raiz;
    //Si el arbol está vacio
    if (raiz == null) {
      raiz = nuevo;
    }
    else {
      while (true) {
        if (nuevo.getDato() <= actual.getDato()){
          if (actual.getHizq()==null) {
            nuevo.setPadre(actual);
            actual.setHizq(nuevo);
            break;
          }
          else {
            actual = actual.getHizq();
          }
        }
        else {
          if (actual.getHder()==null) {
            nuevo.setPadre(actual);
            actual.setHder(nuevo);
            break;
          }
          else {
            actual = actual.getHder();
                      
          }
        }
      }
    }
  }
  public Nodo buscar(int dato) {
    Nodo actual = raiz;
    while (actual != null) {
      if (dato == actual.getDato()) {
        return actual;
      }
      else if (dato <= actual.getDato()) {
        actual = actual.getHizq();
      }
      else {
        actual = actual.getHder();
      }
    }
    return null;
  }
  public Nodo minimo(Nodo nodo) {
    Nodo actual = nodo;
    while (actual.getHizq() != null) {
      actual = actual.getHizq();
    }
    return actual;
  }
  public Nodo sucesor(int dato) {
    Nodo nodo = buscar(dato);
    if (nodo != null && nodo.getHder()!= null) {
      return minimo(nodo.getHder());
    }
    else {
      Nodo padre = nodo.getPadre();
      while (padre != null && nodo == padre.getHder()) {
        nodo = padre;
        padre = padre.getPadre();
      }
      return padre;
    }
  }
  public void eliminar(int dato) {
    Nodo nodo = buscar(dato);
    if (nodo != null) {
      //Primer caso
      if (nodo.getHizq() == null && nodo.getHder() == null) {
        Nodo padre = nodo.getPadre();
        if (padre == null) {
          raiz = null;
        }
        else {
          if (nodo == padre.getHizq()) {
            padre.setHizq(null);
          }
          else {
            padre.setHder(null);
          }
        }
      }
      //Segundo caso nodo tiene un sólo hijo
      else {
        if (nodo.getHizq() != null && nodo.getHder() == null) {
          Nodo padre = nodo.getPadre();
          if (padre == null) {
            Nodo hizq = nodo.getHizq();
            hizq.setPadre(null);
            raiz = hizq;
          }
          else {
            Nodo aux = nodo.getHizq();
            aux.setPadre(padre);
            padre.setHizq(nodo.getHizq());
          }
        }
        else {
          if (nodo.getHizq() == null && nodo.getHder() != null) {
            Nodo padre = nodo.getPadre();
            if (padre == null) {
              Nodo hder = nodo.getHder();
              hder.setPadre(null);
              raiz = hder;
            }
            else {
              Nodo aux = nodo.getHder();
              aux.setPadre(padre);
              padre.setHder(nodo.getHder());
            } 
          }
          else {
            //Tercer caso tiene dos HIJOS
            //Busco el sucesor
            Nodo succ = (Nodo)((Object)sucesor(nodo.getDato())).clone();
            Nodo padre = nodo.getPadre();
            if (padre == null) {
              raiz = succ;
              succ.setPadre(null);
            }
            else {
              if (nodo == padre.getHizq()) {
                padre.setHizq(succ);
              }
              else {
                padre.setHder(succ);
              }
              succ.setPadre(padre);
            }
            succ.setHizq(nodo.getHizq());
            succ.setHder(nodo.getHder());
          }
        }
        
      }
    }
  }
  @Override
  public String toString(){
    return "ABB{" + "raiz=" + raiz + '}';
  }
}
