import person
import collections

class FamilyTree:

    def __init__(self):
        self.family_members = {}
        self.active_relations = set()
        self.available_relations = ['father', 'mother', 'spouse', 'son', 'daughter']

    # add a person to data structure
    def add_person(self, name: str, gender: str="male"):
        try:
            if name in self.family_members:
                raise ValueError("person already exists in family tree")
                # return
            node = person.Person(name, gender)
            self.family_members[name] = node
        except ValueError as e:
            print("\n ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("successfully added person to family-tree ", name, gender)

    # add possible relationship matches
    def add_available_relations(self, relation_name: str):
        try:
            if relation_name not in self.available_relations:
                raise ValueError("not a valid relation to add")
                # return
            self.active_relations.add(relation_name)
        except ValueError as e:
            print("\n ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("successfull activated relationship type ", relation_name)

    # connect from person -> to person with relationship
    def connect(self, from_name: str, to_name: str, relation_name: str):
        try:
            if relation_name not in self.active_relations:
                raise ValueError('invalid relations')
            if from_name not in self.family_members or to_name not in self.family_members:
                raise ValueError("invalid from and to")
            
            if relation_name == "father":
                father_node = self.family_members[from_name]
                son_node = self.family_members[to_name]
                if son_node.father != None:
                    raise ValueError("father already assigned")
                father_node.add_son(to_name)
                son_node.add_father(from_name)
                
            if relation_name == "mother":
                mother_node = self.family_members[from_name]
                son_node = self.family_members[to_name]
                if son_node.mother != None:
                    raise ValueError("mother already assigned")
                mother_node.add_son(to_name)
                son_node.add_mother(from_name)

            if relation_name == "son":
                # check if father or mother
                parent_node = self.family_members[to_name]
                son_node = self.family_members[from_name]

                if from_name in parent_node.children:
                    raise ValueError("child already exists")
                parent_node.add_son(from_name)
                if parent_node.gender == person.available_genders[0]:
                    son_node.add_father(to_name)
                else:
                    son_node.add_mother(to_name)
                    
            elif relation_name == "daughter":
                father_node = self.family_members[to_name]
                daughter_node = self.family_members[from_name]

                if from_name in father_node.children:
                    raise ValueError("child already exists")
                father_node.add_daughter(from_name)
                daughter_node.add_father(to_name)
                
            elif relation_name == "spouse":
                person_node = self.family_members[from_name]
                spouse_node = self.family_members[to_name]
                person_node.add_spouse(to_name)
                spouse_node.add_spouse(from_name)
                
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("successfully connected ", relation_name, "- ", from_name, " -> ", to_name)
        return

    # gets that person object
    def get_info(self, name: str) -> str:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        else:
            print(str(self.family_members[name].__dict__))
            return str(self.family_members[name].__dict__)

    # get children counts
    def get_children_counts(self, name) -> int:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print(
                "children count of " , name, " is: ", self.family_members[name].sonCount +
                self.family_members[name].daughterCount)
            return (self.family_members[name].sonCount +
                self.family_members[name].daughterCount)
        return None

    # get male children counts
    def get_son_counts(self, name: str) -> int:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("son count of " , name, " is: ", self.family_members[name].sonCount)
            return self.family_members[name].sonCount
        return None

    # get female children counts
    def get_daughter_counts(self, name: str) -> int:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
            
        else:
            print("daughter count of " , name, " is: ", self.family_members[name].daughterCount)
            return self.family_members[name].daughterCount
        
        return None

    # get spouse counts
    def get_spouse_counts(self, name: str)-> int:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            print("wife count: ", len(self.family_members[name].spouse))
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("spouse count of ", name, "is: ", len(self.family_members[name].spouse))
            return len(self.family_members[name].spouse)
        return None

    # get father name of a person
    def get_father_name(self, name: str) -> str:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("father name of ", name, "is: ", self.family_members[name].father)
            return self.family_members[name].father
        return None
    
    # get mother name of a person
    def get_mother_name(self, name: str) -> str:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("mother name of ", name, "is: ", self.family_members[name].mother)
            return self.family_members[name].mother
        return None

    # get ancestors of a person
    def get_ancestors(self, name: str, from_relation: str="all")-> str:
        res: str = ""
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            node = self.family_members[name]
            if from_relation == "father":
                while node.father is not None:
                    res += node.father + " - "
                    node = self.family_members[node.father]
            elif from_relation == "mother":
                while node.mother is not None:
                    res += node.mother + " - "
                    node = self.family_members[node.mother]
            else:
                q = collections.deque()
                q.append(node)
                while q:
                    for i in range(len(q)):
                        n = q.popleft()
                        if n.father:
                            res += self.family_members[n.father].name + " - "
                            q.append(self.family_members[n.father])
                        if n.mother:
                            res += self.family_members[n.mother].name + " - "
                            q.append(self.family_members[n.mother])
            if len(res)>0:
                res = res[:-2]
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("acestors of ", name, "from ", from_relation, "are: ", res)
            return res
        return None

    # get heirarchy of a person. son, grandkids etc
    def get_next_generation_family_members(self, name: str) -> str:
        res: str = ""
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            node = self.family_members[name]
            q = collections.deque()
            q.append(node)
            while q:
                for i in range(len(q)):
                    n = q.popleft()
                    for child in n.children:
                        res += self.family_members[child].name + " - "
                        q.append(self.family_members[child])
            if len(res)>0:
                res = res[:-2]
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("next generation family members are: ", res)
            return res
        return None

    # get son names
    def get_sons(self, name: str) -> list:
        res = []
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            node = self.family_members[name]
            for child in node.children:
                if self.family_members[child].gender == "male":
                    res.append(child)
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("sons of ", name, " are: ", res)
            return res
        return None

    # get daughters name
    def get_daughters(self, name: str) -> list:
        res = []
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            node = self.family_members[name]
            
            for child in node.children:
                if self.family_members[child].gender == "female":
                    res.append(child)
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("daughters of ", name, " are: ", res)
            return res
        return None
    
    # get children names
    def get_children(self, name: str) -> list:
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
        except ValueError as e:
            print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("children of ", name, " are: ", list(self.family_members[name].children))
            return list(self.family_members[name].children)
        return None

    # update person name in his object and his relations' object too
    def update_person_name(self, name: str, new_name: str):
        try:
            if name not in self.family_members:
                raise ValueError("family member name not found")
            node = self.family_members[name]
            # update spouse name
            print("nod eis ", str(node.__dict__))
            if node.spouse:
                for w in node.spouse:
                    w_node = self.family_members[w]
                    w_node.spouse.remove(name)
                    w_node.spouse.add(new_name)
            # update children's father or mothers name based on gender
            if node.children:
                for c in node.children:
                    c_node = self.family_members[c]
                    if node.gender == "male":
                        c_node.father = new_name
                    elif node.gender == "female":
                        c_node.mother = new_name
            # update parents children field
            if node.father:
                f_node = self.family_members[node.father]
                f_node.children.remove(name)
                f_node.children.add(new_name)
            if node.mother:
                m_node = self.family_members[node.mother]
                m_node.children.remove(name)
                m_node.children.add(new_name)

            # update family member set
            node.name = new_name
            del self.family_members[name]
            self.family_members[new_name] = node
        except ValueError as e:
                print("ERROR - ", e)
        except:
            print("something went wrong.")
        else:
            print("successfully updated person's name to: ", new_name)

family = FamilyTree()