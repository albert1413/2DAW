class Person:
    def __init__(self, firstName, lastName):
        self.abilities = []
        self.firstName = firstName
        self.lastName = lastName
    
    def add_ability(self, abilitat):
        self.abilities.append(abilitat)
    
    def info(self):
        return self.abilities
    
class Candidate(Person):
    def __init__(self, firstName, lastName, gender):
        super().__init__(firstName, lastName)
        self.gender = gender
        

    def info(self):
        if  self.gender == "male":
            print(f"He is {self.firstName} {self.lastName}")
        else:
            print(f"She is {self.firstName} {self.lastName}")
        print(super().info())

c1 = Candidate('Manel', 'Cantells','male')
c1.add_ability('JavaScript')
c1.add_ability('Python')
c2 = Candidate('Maria', 'Gironés','female')
c2.add_ability('PHP')

c1.info()
c2.info()