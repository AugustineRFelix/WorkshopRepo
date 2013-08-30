import sqlalchemy
import time

class DatabaseEngine:
	def __init__(self, connection_string='mssql://sa:sa@./WSS_Content'):
		self._engine = sqlalchemy.create_engine(connection_string)
	
	def query(self, sql):
		return self._engine.execute(sql).fetchall()
