from neo4j_db.special_db import SpecialDB

db = SpecialDB("bolt://localhost:7687", "neo4j", "password", "my company")

print("Create employees:")
print(db.createEmployee("Aleksandra", "Mikhaylova", "bonni_1998@mail.ru"))
print(db.createEmployee("Ilya", "Bobkin", ""))
print(db.createEmployee("Semen", "Eroshenko", ""))
print(db.createEmployee("Svetlana", "Pershutkina", ""))

print()

print("Select employee:")
for employee in db.selectNodes(db.ALL, "employee"):
    print(employee)

print()

print("Delete employee:")
print(db.deleteEmployees({"name": "Ilya"}))

print()

print("Get connection with company:")
for connection in db.getConnection(db.NAME_CONNECTION_WITH_COMPANY):
    print(connection)
