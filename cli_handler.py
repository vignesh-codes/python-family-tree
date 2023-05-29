import shlex
import main
from family_tree import family
import person

class CliHandler:
    def __init__(self):
        self.valid_actions = [
        "add", 
        "connect", 
        "count", 
        "children", 
        "father",
        "mother", 
        "daughters", 
        "sons",
        "ancestors",
        "generations",
        "update"
        ]
        self.available_prefix = ["family-tree"]
    
    def print_help_statement(self):
        print("** This is a simple python program data structure to manage and print the family tree heirarchy** \n\n \
              Available Valid Actions: ", self.valid_actions, " \n\n valid prefix: ", self.available_prefix)
        print("example: ", "add person_name_can_handle_with_space gender")
        print("available genders: ", person.available_genders)
        return

    def run_cli(self, user_input):
        
        try:
            args = shlex.split(user_input)
            if args[0] not in self.available_prefix:
                raise ValueError("invalid input. ")
            if args[1] == "help":
                self.print_help_statement()
                return
            if args[1] not in self.valid_actions:
                raise ValueError("invalid action.")
            self.handle_actions(args[1], args[2:])
        except ValueError as e:
            print(e)
        except:
            print("something went wrong.")

    def handle_actions(self, action, args):
            try:
                # handle the strings differently for different type of actions.
                # for example -> the conditions must handle names with spaces and seprated by "of" or "as"
                if action == "add":
                    # handleAddAction(args)
                    # check the args
                    # check if relationship
                    if args[0] == "relationship":
                        family.add_available_relations(args[1])
                    else:
                        print("args are ", args)
                        if len(args) < 3:
                            raise ValueError("invalid person. need name and gender")
                        family.add_person(" ".join(args[:-1]), args[-1])
                
                elif action == "connect":
                    if len(args) < 5:
                        raise ValueError("invalid args")
                    name1 = ""
                    i = 0
                    while i < len(args):
                        if args[i] == "as":
                            name1 = name1[:-1]
                            break
                        name1 += args[i] + " "
                        i += 1
                    relationship = args[i+1]
                    if args[i+2] != "of":
                        raise ValueError("invalid args")
                    name2 = " ".join(args[i+3:])
                    family.connect(name1, name2, relationship)
                    return
                
                elif action == "count":
                    if len(args) < 3:
                        print("invalid args ", args)
                        return
                    relationship = args[0]
                    if args[1] != "of":
                        raise ValueError("invalid args")
                    name = " ".join(args[2:])
                    if relationship == "sons":
                        family.get_son_counts(name)
                    if relationship == "children":
                        family.get_children_counts(name)
                    elif relationship == "daughters":
                        family.get_daughter_counts(name)
                    elif relationship == "spouse":
                        family.get_spouse_counts(name)

                elif action == "father":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_father_name(name)
                elif action == "mother":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_mother_name(name)
                elif action == "ancestors":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_ancestors(name)
                elif action == "generations":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_next_generation_family_members(name)
                elif action == "sons":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_sons(name)
                elif action == "daughters":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_daughters(name)
                elif action == "children":
                    if len(args) < 2:
                        raise ValueError("invalid args")

                    name = " ".join(args[1:])
                    family.get_children(name)
                elif action == "update":
                    print("update args ", args)
                    if len(args) < 2:
                        raise ValueError("invalid args")
                    if args[0] != "name":
                        raise ValueError("invalid input")
                    prev_name = ""
                    i = 1
                    while i < len(args):
                        if args[i] == "to":
                            break
                        prev_name += args[i]
                        i += 1
                    new_name = " ".join(args[i+1:])
                    family.update_person_name(prev_name, new_name)
            except ValueError as e:
                print(e)
            except:
                print("something went wrong.")
    