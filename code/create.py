from app import db, task ,project,jointable

db.drop_all()
db.create_all()

testtask = task(name = "clean" ,complete = False) # Extra: this section populates the table with an example entry
testtask = project(name = "cook", staatus = False)

db.session.add(testtask)
db.session.commit()