from pony.orm import Database

db = Database()
db.bind(provider='postgres', user='postgres', password='postgres', host='localhost', database='mydb')
