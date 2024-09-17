class Dad:
    def __init__(self, firstName, lastName, name):
        self.firstName = firstName
        self.lastName = lastName
        self.name =  name

    def getDadFirstName(self):
        return self.firstName
    def getDadFullName(self):
        return self.name + " " +self.firstName + " " + self.lastName
    
class Mom:
    def __init__(self, firstName, lastName, name):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name

    def getMomFirstName(self):
        return self.firstName
    def getMomFullName(self):
        return self.name + " " +self.firstName + " " + self.lastName

class Child():

    def __init__(self, name, dad, mom):
        self.name = name
        self.dad = dad
        self.mom = mom

    def getFullName(self):
        return self.name + " " + self.dad.getDadFirstName() + " " + self.mom.getMomFirstName()
    
dad = Dad("Fibla", "Armengol", "Josep")
mom = Mom("Agustin", "Franch", "Maria")
child = Child("Xavi", dad, mom)
print(child.getFullName())
print(dad.getDadFullName())
print(mom.getMomFullName())

