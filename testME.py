from mongoengine import *

connect('employeeDB')

class Employee(Document):
    name = StringField(max_length=50)
    age = IntField(required=False)

john = Employee(name="John Doe", age=25)
john.save()

jane = Employee(name="Jane Doe", age=27)
jane.save()

for e in Employee.objects.all():
    print( e["id"], e["name"], e["age"])
