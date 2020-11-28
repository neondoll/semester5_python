from mongo_db.db import DB

db = DB('StudentsDB')

print(db.insert('students', {'std_id': 1, 'std_fullname': 'Александра Михайлова', 'std_login': 'mikhaylova_a', 'std_pswd': 'user001'}))
print(db.insert('students', {'std_id': 2, 'std_fullname': 'Илья Бобкин', 'std_login': 'bobkin_i', 'std_pswd': 'user002'}))
print(db.insert('students', {'std_id': 3, 'std_fullname': 'Сергей Громов', 'std_login': 'gromov_s', 'std_pswd': 'user003'}))
print(db.insert('students', {'std_id': 4, 'std_fullname': 'Сагорь Амелин', 'std_login': 'amelin_s', 'std_pswd': 'user004'}))
print(db.insert('students', {'std_id': 5, 'std_fullname': 'Дмитрий Куликов', 'std_login': 'kulikov_d', 'std_pswd': 'user005'}))

print()

print('select documents:')
for r in db.select('students', {}, True):
    print(r)

print()

db.update('students', {'std_login': 'mikhaylova_a'}, {'std_pswd': 'F1k2z3'})
print('updating document: ')
print(db.select('students', {'std_login': 'mikhaylova_a'}))

print()

db.delete('students', {'std_login': 'gromov_s'})
print('select documents:')
for r in db.select('students', {}, True):
    print(r)
