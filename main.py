import family_tree
import cli_handler as cli





def initFamily():
    family = family_tree.family
    family.add_available_relations("son")
    family.add_available_relations("father")
    family.add_available_relations("daughter")
    family.add_available_relations("mother")
    family.add_available_relations("spouse")
    
    family.add_person("john sh", "male")
    family.add_person("mary a", "female")
    
    
    # CONNECT -> PERSON1 TO PERSON2 RELATION
    family.connect("john sh", "mary a", "spouse")
    family.add_person("joan", "male")
    family.add_person("margarat", "female")
    # family.connect("joan", "margarat", "spouse")
    
    # joan is son of john sh
    family.connect("joan", "john sh", "son")
    family.connect("joan", "mary a", "son")
    
    # mary a is mother of margarat.
    family.connect("mary a", "margarat", "mother")
    family.connect("john sh", "margarat", "father")
    
    family.add_person("gilbert", "male")
    family.connect("gilbert", "john sh", "son")
    family.connect("gilbert", "mary a", "son")
    
    family.add_person("joan-f", "female")
    family.connect("mary a", "joan-f", "mother")
    family.connect("john sh", "joan-f", "father")
    
    family.add_person("anne", "female")
    family.connect("anne", "john sh", "daughter")
    family.connect("anne", "mary a", "daughter")
    
    family.add_person("richard", "male")
    family.connect("richard", "john sh", "son")
    family.connect("richard", "mary a", "son")
    
    family.add_person("edmond", "male")
    family.connect("edmond", "john sh", "son")
    family.connect("edmond", "mary a", "son")
    
    family.add_person("william", "male")
    family.connect("william", "john sh", "son")
    family.connect("william", "mary a", "son")
    
    family.add_person("anne hathaway", "female")
    family.connect("william", "anne hathaway", "spouse")
    
    family.add_person("susanna", "female")
    family.connect("william", "susanna", "father")
    family.connect("anne hathaway", "susanna", "mother")
    
    family.add_person("hamnet", "male")
    family.connect("william", "hamnet", "father")
    family.connect("anne hathaway", "hamnet", "mother")
    
    family.add_person("judith", "female")
    family.connect("william", "judith", "father")
    family.connect("anne hathaway", "judith", "mother")
    
    family.add_person("john h")
    family.connect("john h", "susanna", "spouse")
    
    family.add_person("elizabeth", "female")
    family.connect("john h", "elizabeth", "father")
    family.connect("susanna", "elizabeth", "mother")
    
    family.add_person("thomas quiney", "male")
    family.connect("thomas quiney", "judith", "spouse")
    
    family.add_person("shakespeare", "male")
    family.connect("thomas quiney", "shakespeare", "father")
    family.connect("judith", "shakespeare", "mother")
    
    family.add_person("richard-t", "male")
    family.connect("thomas quiney", "richard-t", "father")
    family.connect("judith", "richard-t", "mother")
    
    family.add_person("thomas", "male")
    family.connect("thomas quiney", "thomas", "father")
    family.connect("judith", "thomas", "mother")
    
    family.get_ancestors("elizabeth")
    family.get_next_generation_family_members("john sh")
    
    
    family.get_son_counts("john sh")
    family.get_children("william")
    family.get_father_name("hamnet")
    
    family.get_children_counts("mary a")
    family.get_son_counts("mary a")
    family.get_daughter_counts("mary a")
    family.get_daughters("mary a")
    family.get_sons("mary a")
    family.get_son_counts("judith")
    

if __name__ == '__main__':

    initFamily()
    cliHandler = cli.CliHandler()
    while True:
        user_input =input("\n \n >>> ")
        print("user input is ", user_input)
        if user_input == 'family-tree \q':
            print('exiting program')
            break
        try:
            cliHandler.run_cli(user_input)
        except ValueError:
            print('Invalid input.')
            continue
        except:
            print("something went wrong.")
            continue
    print("exited")