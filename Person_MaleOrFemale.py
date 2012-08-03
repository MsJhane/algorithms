class Person:
    def __init__(self,name,isMale):
            self.name=name
            if(isMale==True):
                self.sex="Male"
            else:
                self.sex="Female"
    def show(self):
            print(" %s is %s " % (self.name,self.sex))

Errol=Person("John",True)
Maricar=Person("Maricar",False)
Joy=Person("Joy",False)
Johnny=Person("Johnny",True)
Elvira=Person("Elvira",False)

ListOfPerson=[ Errol,Maricar,Joy,Johnny,Elvira]
ListOfMale=[]
ListOfFemale=[]


for person in ListOfPerson:
    if(person.sex=="Male"):
        ListOfMale.append(person)
    else:
        ListOfFemale.append(person)
        
    
print("")    
print("Male:")
for male in ListOfMale:
    male.show()

print("")
print("Female:")
for female in ListOfFemale:
    female.show()


     
