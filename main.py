#!/usr/bin/env python3
# coding: utf-8
from os import system
from random import randrange


class Main:
    def __init__(self):
        self.alfabeto_minusculo = [
            "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z"
        ]
        self.alfabeto_maiusculo = [
            "A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R",
            "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
        self.caracteres_especiais = ["*", "/", "(", ")", "@", "#", ".", "&"]
        self.numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.lista_caracteres_validos = []
        self.Password = ""

    def main(self):
        print("Bem vindo ao Password Generator!!")
        tamanho = int(input("Infomrme o tamanho da senha a ser gerada: "))
        adiciona_caracteres_especiais = input("Adiciona caracteres especiais ? [sim, não] : ")
        adiciona_maiusculas = input("Adiciona letras maiúsculas ? [sim, não] : ")
        adiciona_numeros = input("Adiciona números ? [sim, não] : ")

        self.lista_caracteres_validos += self.alfabeto_minusculo
       
        if adiciona_caracteres_especiais.lower() == "sim":
            self.lista_caracteres_validos += self.caracteres_especiais
        if adiciona_maiusculas.lower() == "sim":
            self.lista_caracteres_validos += self.alfabeto_maiusculo

        if adiciona_numeros.lower() == "sim":
            self.lista_caracteres_validos += self.numeros

        for numero in range(tamanho):
            letra = str(self.lista_caracteres_validos[randrange(len(self.lista_caracteres_validos) - 1)])
            self.Password += letra

        system("clear")
       
        print(
            """
       
       

                %s


         
            """ % self.Password
            )
