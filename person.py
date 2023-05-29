import family_tree
class Person:
    def __init__(self, name, gender):
        self.name:str = name
        self.gender:str = gender
        self.spouse = set()
        self.father:str = None
        self.mother:str = None
        self.children = set()
        self.sonCount:int = 0
        self.daughterCount:int = 0
        self.dob:int = None
        self.dod:int = None
        self.isAlive:bool = True if not self.dod else False
        
        

    def add_son(self, child_name: str):
        try:
            if child_name in self.children:
                raise ValueError("child already exist")
            self.children.add(child_name)
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")

    def add_daughter(self, child_name: str):
        try:
            if child_name in self.children:
                raise ValueError("child already exist")
            self.children.add(child_name)
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")

    def add_father(self, father_name: str):
        self.father = father_name
        if self.gender == "male":
            family_tree.family.family_members[father_name].sonCount += 1
        else:
            family_tree.family.family_members[father_name].daughterCount += 1
        return

    def add_mother(self, mother_name: str):
        self.mother = mother_name
        if self.gender == "male":
            family_tree.family.family_members[mother_name].sonCount += 1
        else:
            family_tree.family.family_members[mother_name].daughterCount += 1
        return

    def add_spouse(self, spouse_name: str):
        self.spouse.add(spouse_name)
        return

    def update_dates(self, dob:int, dod: int):
        if len(dob) > 0:
            self.dob = dob
        if len(dod) > 0:
            self.dod = dod
        return
available_genders = ["male", "female"]