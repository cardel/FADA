#!/usr/bin/python3
# -*- coding: utf-8 -*- 

#Author: Carlos Andres Delgado
#Creation date 14th March 2018
#Edition date 12th December 2018

#ESta función es un ejemplo de como se debe hacer la documentación de una función
def ejemplo(msg):
    """
    Esta función es un ejemplo de como se debe hacer la documentación de una función
    :param msg: Mensaje que se desea imprimir
    :type msg: String
    :return: mensaje formateado
    """

    return msg + " Mundo!"


if __name__ == "__main__":
    print(ejemplo("Hola"))
    print(ejemplo.__doc__)

