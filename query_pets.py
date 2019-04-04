#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""File to query pets.db"""

import sqlite3 as sql


con = sql.connect('pets.db')

person_id = int(input('Please enter person ID or enter -1 to quit: '))
         
while person_id != -1:
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM person \
join person_pet on person.id = person_pet.person_id \
join pet on person_pet.pet_id = pet.id where person.id={}".format(person_id))
            row = cur.fetchall()
            print('{} {} is currently {} years old.'.format(
                row[0][1], row[0][2], row[0][3]))
            if (row[0][10]):
                print('{} {} owned {}, a {}, that was {} years old.'.format(
                    row[0][1], row[0][2], row[0][7], row[0][8], row[0][9]))
            else:
                print('{} {} owns {}, a {}, that is {} years old.'.format(
                    row[0][1], row[0][2], row[0][7], row[0][8], row[0][9]))
    except:
        print('Person with ID number {} does not exist'.format(person_id))
        
    person_id = int(input('Please enter person ID or enter -1 to quit: '))
