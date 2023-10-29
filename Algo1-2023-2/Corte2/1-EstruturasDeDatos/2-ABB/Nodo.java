/**
 * Implementación del nodo
 * @author Carlos Delgado
 * @date 26/10/2023
 */ 

public class Nodo {
  private int dato;
  private Nodo padre;
  private Nodo hizq;
  private Nodo hder;
  Nodo(int dato){
    this.dato = dato;
    this.padre = null;
    this.hizq = null;
    this.hder = null;
  }
  public int getDato(){
    return dato;
  }
  public void setDato(int dato){
    this.dato = dato;
  }
  public Nodo getPadre(){
    return padre;
  }
  public void setPadre(Nodo padre){
    this.padre = padre;
  }
  public Nodo getHizq(){
    return hizq;
  }
  public void setHizq(Nodo hizq){
    this.hizq = hizq;
  }
  public Nodo getHder(){
    return hder;
  }
  public void setHder(Nodo hder){
    this.hder = hder;
  }
  @Override
  public String toString(){
    return "Nodo{" + "dato=" + dato + ", hizq=" + hizq + ", hder=" + hder + '}';
  }
}
