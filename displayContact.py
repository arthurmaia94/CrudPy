#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  displayContact.py
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
cursor = conn.cursor()
cursor.execute("select * from clientes")
contact_information_array = cursor.fetchall()

sg.theme('DarkAmber')
headings = ['ID','Full Name', 'Email', 'Empresa']

layout = [
  [sg.Table(values=contact_information_array, headings=headings,
  max_col_width=35,
  auto_size_columns=True,
  #display_row_number=True,
  justification='left',
  num_rows=12,
  key='Table',
  row_height=35)],
  [sg.Button('Fechar')],
  [sg.Text('\nDesenvolvido por 94 Tech - Soloções em Informatica')]
]
window = sg.Window("Informações de Contato", layout)

while True:
  event, values = window.read()
  if event == "Fechar" or event == sg.WIN_CLOSED:
    cursor.close()
    conn.close()
    break

window.close()
