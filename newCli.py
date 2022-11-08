#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  newCli.py
#  
#  Copyright 2022 Arthur Maia <contato.94tech@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import PySimpleGUI as sg
import sqlite3
conn = sqlite3.connect("sys_cli.db")

class NewClient:
  def __init__(self):
    
    sg.theme('DarkAmber')
    layout = [
      [sg.Text('Nome: ', size=(8,0)), sg.Input(size=(30,0),key='nome', do_not_clear=False)],
      [sg.Text('Email: ', size=(8,0)), sg.Input(size=(30,0),key='email', do_not_clear=False)],
      [sg.Text('Empresa: ', size=(8,0)), sg.Input(size=(30,0), key='empresa', do_not_clear=False)],
      [sg.Button('Cadastrar'), sg.Button('Sair')],
      [sg.Output(size=(40,10))],
      [sg.Text('\nDesenvolvido por 94 Tech - Soloções em Informatica')]
    ]
    self.janela = sg.Window("Novo Cliente").layout(layout)

  def Iniciar(self):
    while True:
      self.button, self.values = self.janela.Read()

      nome = self.values['nome']
      email = self.values['email']
      empresa = self.values['empresa']
      
      cursor = conn.cursor()
      cursor.execute('''insert into clientes (Nome, Email, Empresa) values (?, ?, ?)''', (nome, email, empresa))
      conn.commit()

      print(f'- Nome: {nome}\n- E-mail: {email}\n- Empresa: {empresa}\n ---')
      
      if event == 'Sair':
        cursor.close()
        conn.close()
        break

tela = NewClient()
tela.Iniciar()

