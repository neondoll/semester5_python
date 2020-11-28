from neo4j_db.db import DB

db = DB("bolt://localhost:7687", "neo4j", "password", "company")
db.select(DB.ALL)
