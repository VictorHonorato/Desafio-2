#!/usr/bin/python
# -*- coding: utf-8 -*-
import time, os

class Lista:

   def __init__(self):
       self.contatos = []

   def AddContato(self, contato):
       self.contatos.append(contato)

   def DelContato(self, contato):
       self.contatos.pop(contato)

   def SelfPrint(self):
      i = 0
      for p, v in self.contatos:
        print(str(i) + " - " + str(p) + " -> " + str(v) )
        i += 1



   def WaitClear(self, sleep_time):
       time.sleep(sleep_time)
       os.system("cls")


class Contato:

   def __init__(self, name, numero):
       self.name = name
       self.numero = numero

   def ToString(self):
       return self.name + " -> " + str(self.numero)


class Menu:

   def __init__(self):

       self.main = {"1": self.ListContato,
                    "2": self.AddContato,
                    "3": self.RemoveContato,
                    "4":self.Sair }


       self.Lista = Lista()

       self.Control()

   def ListContato(self):
       self.Lista.SelfPrint()

   def AddContato(self):
       nome = input(" Nome do contato: ")
       telefone = input(" Número do contato: ")
       self.Lista.AddContato([nome,telefone])
       print("Contato adicionado !!")


   def RemoveContato(self):
       self.Lista.SelfPrint()
       r = int(input("Digite o número  :"))
       self.Lista.DelContato(r)
       print("Contato removido !!")

   def Exit(self):
       print("Tchau!")

   def Sair(self):
       self.Exit()

   def Show(self):
       self.WaitClear(1.5)

       option = input('''
        ----------------------------------
       |   Lista Telefonica               |
       |                                  |
       | 1 - Listar Números               |
       | 2 - Adicionar Número             |
       | 3 - Remover Número               |
       | 4 - Sair                         |
        ----------------------------------
       Digite a opção de numero desejado: ''')
       return option

   def Control(self):
       option = 0

       while option != "4":
           option = self.Show()
           try:
               function = self.main[option]
               function()
           except KeyError:
               print("Digite um número aceitável!")


   def WaitClear(self, sleep_time):
       time.sleep(sleep_time)
       os.system("cls")


Menu()
