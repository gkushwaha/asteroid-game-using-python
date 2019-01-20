import pygame
import sqlite3
from datetime import date


class Database:
	def __init__(self, score):
		self.score = score
		self.played_date = str(date.today())
		self.create_database()

	def create_database(self):
		self.conn =sqlite3.connect('game.db')
		self.c=self.conn.cursor()

		self.conn.execute('''
			CREATE TABLE IF NOT EXISTS GAME
				(score INTEGER NOT NULL,
				played_date STRING NOT NULL)
		''')

		self.conn.execute('''INSERT INTO GAME (score, played_date) VALUES (?, ?)''', (self.score, self.played_date))

		self.conn.commit()
		self.conn.close()
