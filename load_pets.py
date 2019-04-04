#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""File to load pets.db with data"""

import sqlite3 as sql

owners =(
    ('John', 'Doe', 25),
    ('Jane', 'Smith', 23),
    ('Duke', 'Phung', 37),
    ('Hurricane', 'Katrina', 32),
    ('Kevin', 'Hart', 39),
    ('Tom', 'Brady', 28)
    )

pets = (
    ('Jesse', 'Lhasa Apso', 13, 0),
    ('Lucky', 'Cocker Spaniel', 7, 0),
    ('Rover', 'Labradoodle', 2, 0),
    ('Fatty', 'Bulldog', 9, 1),
    ('Salem', 'Yorkie', 11, 0),
    ('Handsome', 'Yellow Lab', 1, 0))

pet_owner = ((1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1))

con = sql.connect('pets.db')

with con:
    cur = con.cursor()
    
    cur.executemany('INSERT INTO person (first_name, last_name, age) values(?,?,?)', owners)
    cur.executemany('INSERT INTO pet (name, breed, age, dead) values(?,?,?,?)', pets)
    cur.executemany('INSERT INTO person_pet (person_id, pet_id) values(?,?)', pet_owner)
    con.commit()
