import json
import sqlite3
import os

conn = sqlite3.connect('userLibrary.sqlite3')
cur = conn.cursor()

cur.executescript(''' 

		DROP TABLE IF EXISTS User;
		DROP TABLE IF EXISTS Course;
		DROP TABLE IF EXISTS Member;

''')
		
cur.execute('''
		CREATE TABLE User (
				id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
				name 	TEXT
		);
''')

cur.executescript ('''
		CREATE TABLE Course (
				id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
				title	TEXT
		);
''')

cur.executescript('''
		
		CREATE TABLE Member (
				user_id						INTEGER,
				course_id					INTEGER,
				role							INTEGER,
				PRIMARY KEY (user_id, course_id) 	
		)
		
''')


fname = raw_input('Input file name:')
if ( len(fname) < 1 ) : fname = 'c:/users/rcollier/downloads/roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

#print (json_data)
#print json.dumps(str_data, indent=4, separators=(',', ': '))

for element in json_data :
		#print element
		name = element[0]
		course = element[1]
		role = element[2]
		
		#print name, course, role

		cur.execute(''' INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (name, ))
		cur.execute(''' SELECT id FROM User WHERE (name) = ?''', (name, ))
		name_id = cur.fetchone()[0]
		
		cur.execute(''' INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (course, ))
		cur.execute(''' SELECT id FROM Course WHERE title = ?''', (course, ))
		course_id = cur.fetchone()[0]
		
		cur.execute(''' INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''',(name_id, course_id, role))		
		
conn.commit()














