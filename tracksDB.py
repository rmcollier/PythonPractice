import sqlite3
import xml.etree.ElementTree as ET

conn = sqlite3.connect('trackDB.sqlite3')
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Artist''')
cur.execute('''DROP TABLE IF EXISTS Genre''')
cur.execute('''DROP TABLE IF EXISTS Album''')
cur.execute('''DROP TABLE IF EXISTS Track''')
cur.executescript('''
	
	CREATE TABLE Artist (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name    TEXT UNIQUE
	);

	CREATE TABLE Genre (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name    TEXT UNIQUE
	);

	CREATE TABLE Album (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id  INTEGER,
		title   TEXT UNIQUE
	);

	CREATE TABLE Track (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		title TEXT  UNIQUE,
		album_id  INTEGER,
		genre_id  INTEGER,
		len INTEGER, rating INTEGER, count INTEGER
	);
	''')
conn.commit()
