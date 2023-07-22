import os
import psycopg2
import uuid
import random

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sc = os.environ["CONNECTION_STRING_DB"]    
connection = psycopg2.connect(sc, sslmode='require',)


cursor = connection.cursor()
area_id =str(uuid.uuid4())
area_numb = 1
cursor.execute(f"INSERT INTO areas (id, name, description) VALUES ('{area_id}', 'Area {area_numb}', 'Description Area {area_numb}' );")
cursor.close()

num_ability = 4
for ability_numb in range(0, num_ability):
    print("1")
    cursor = connection.cursor()
    ability_id = str(uuid.uuid4())
    cursor.execute(f"INSERT INTO abilities (id, name, description, area_id) VALUES ('{ability_id}', 'Area {area_numb}, Ability {ability_numb}', 'Description Ability {ability_numb}', '{area_id}');")
    cursor.close()
    
    num_questions = 15
    for question_numb in range(0, num_questions):
        print("2")
        cursor = connection.cursor()
        question_id = str(uuid.uuid4())
        answer_id = str(uuid.uuid4())
        cursor.execute(f"INSERT INTO questions (id, statement, answer, rating, rating_deviation, volatility, last_rating_update, is_essay, ability_id) VALUES ('{question_id}', '<p>Area {area_numb}, Ability {ability_numb}, Question {question_numb}, Answer 0</p>','{answer_id}' , {random.randint(0,3000)}, {random.randint(0,300)}, 0.6, %s, false, '{ability_id}');", (datetime.utcnow().date(), ))
        cursor.close()
        
        num_alt = 5
        for alt_num in range(0, num_alt):
            print("3")
            cursor = connection.cursor()
            alt_id = str(uuid.uuid4())
            if(alt_num == 0):
                alt_id = answer_id
            cursor.execute(f"INSERT INTO alternatives (id, text, question_id) VALUES ('{alt_id}', '<p>Alt {alt_num}, Area {area_numb}, Ability {ability_numb}, Question {question_numb} </p>', '{question_id}');")
            cursor.close()
            
        
connection.commit()

connection.close()