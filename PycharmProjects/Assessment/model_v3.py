import sys


class Lengaburu:
    family_members = {}

    def __init__(self, name, gender, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.mother = mother
        self.father = father
        self.spouse = None
        self.children = None
        self.siblings = None
        self.family_members[name] = self

    def __repr__(self):
        return self.name

    # defining getters and setters
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return self

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
        return self

    def get_spouse(self):
        return self.spouse

    def set_spouse(self, spouse):
        self.spouse = spouse
        return self

    def get_mother(self):
        return self.mother

    def set_mother(self, mother):
        self.mother = mother
        return self

    def get_father(self):
        return self.father

    def set_father(self, father):
        self.father = father
        return self

    def get_children(self):
        return self.children

    def set_children(self, children):
        if type(children) is list:
            self.children = children
        else:
            self.children.append(children)
        return self

    def get_siblings(self):
        return self.siblings

    def set_siblings(self, siblings):
        if type(siblings) is list:
            self.siblings = siblings
        else:
            self.siblings.append(siblings)
        return self

    # computing defined relation ships
    def get_paternal_aunt(self):
        ctr = 0
        if self.father:
            if self.father.siblings:
                for aunt in self.father.siblings:
                    if aunt.gender == "Female":
                        print(aunt.name, end=" ")
                        ctr += 1
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("NONE")

    def get_paternal_uncle(self):
        ctr = 0
        if self.father:
            if self.father.siblings:
                for uncle in self.father.siblings:
                    if uncle.gender == "Male":
                        print(uncle.name, end=" ")
                        ctr += 1
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("NONE")

    def get_maternal_aunt(self):
        ctr = 0
        if self.mother:
            if self.mother.siblings:
                for aunt in self.mother.siblings:
                    if aunt.gender == "Female":
                        print(aunt.name, end=" ")
                        ctr += 1
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("NONE")

    def get_maternal_uncle(self):
        ctr = 0
        if self.mother:
            if self.mother.siblings:
                for uncle in self.mother.siblings:
                    if uncle.gender == "Male":
                        print(uncle.name, end=" ")
                        ctr += 1
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("NONE")

    def get_brother_in_law(self):
        ctr = 0
        if self.spouse or self.siblings:
            if self.spouse:
                if self.spouse.siblings:
                    for brother in self.spouse.siblings:
                        if brother.gender == "Male":
                            print(brother.name, end=" ")
                            ctr += 1
            if self.siblings:
                for brother in self.siblings:
                    if brother.gender == "Female":
                        if brother.spouse:
                            print(brother.spouse.name, end=" ")
                            ctr += 1
            if not ctr:
                print("NONE")

        else:
            print("NONE")

    def get_sister_in_law(self):
        ctr = 0
        if self.spouse or self.siblings:
            if self.spouse:
                if self.spouse.siblings:
                    for sister in self.spouse.siblings:
                        if sister.gender == "Female":
                            print(sister.name, end=" ")
                            ctr += 1
            if self.siblings:
                for sister in self.siblings:
                    if sister.gender == "Male":
                        if sister.spouse:
                            print(sister.spouse.name, end=" ")
                            ctr += 1
            if not ctr:
                print("NONE")

        else:
            print("NONE")

    def get_son(self):
        ctr = 0
        if self in Lengaburu.family_members.values():
            if self.children:
                for son in self.children:
                    if son.gender == "Male":
                        ctr += 1
                        print(son, end=" ")
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def get_daughter(self):
        ctr = 0
        if self in Lengaburu.family_members.values():
            if self.children:
                for daughter in self.children:
                    if daughter.gender == "Female":
                        ctr += 1
                        print(daughter, end=" ")
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")


# Object creation along with family tree modelling
king_shan = Lengaburu("Shan", "Male")
queen_anga = Lengaburu("Anga", "Female")
chit = Lengaburu("Chit", "Male", king_shan, queen_anga)
ish = Lengaburu("Ish", "Male", king_shan, queen_anga)
vich = Lengaburu("Vich", "Male", king_shan, queen_anga)
aras = Lengaburu("Aras", "Male", king_shan, queen_anga)
satya = Lengaburu("Satya", "Female", king_shan, queen_anga)
amba = Lengaburu("Amba", "Female")
lika = Lengaburu("Lika", "Female")
chitra = Lengaburu("Chitra", "Female")
vyan = Lengaburu("Vyan", "Male")

king_shan.set_spouse(queen_anga).set_children([chit, ish, vich, aras, satya])
queen_anga.set_spouse(king_shan).set_children([chit, ish, vich, aras, satya])

dritha = Lengaburu("Dritha", "Female", chit, amba)
jaya = Lengaburu("Jaya", "Male")
tritha = Lengaburu("Tritha", "Female", chit, amba)
vritha = Lengaburu("Vritha", "Male", chit, amba)
vila = Lengaburu("Vila", "Female", vich, lika)
chika = Lengaburu("Chika", "Female", vich, lika)
jnki = Lengaburu("Jnki", "Female", aras, chitra)
arit = Lengaburu("Arit", "Male")
ahit = Lengaburu("Ahit", "Male", aras, chitra)
asva = Lengaburu("Asva", "Male", vyan, satya)
satvy = Lengaburu("Satvy", "Female")
vyas = Lengaburu("Vyas", "Male", vyan, satya)
krpi = Lengaburu("Krpi", "Female")
atya = Lengaburu("Atya", "Female", vyan, satya)

chit.set_spouse(amba).set_siblings([ish, vich, aras, satya]).set_children([dritha, tritha, vritha])
amba.set_spouse(chit).set_children([dritha, tritha, vritha])
ish.set_siblings([chit, vich, aras, satya])
vich.set_spouse(lika).set_siblings([chit, ish, aras, satya]).set_children([vila, chika])
lika.set_spouse(vich).set_children([vila, chika])
aras.set_spouse(chitra).set_siblings([chit, ish, vich, satya]).set_children([jnki, ahit])
chitra.set_spouse(aras).set_children([jnki, ahit])
satya.set_spouse(vyan).set_siblings([chit, ish, vich, aras]).set_children([asva, vyas, atya])
vyan.set_spouse(satya).set_children([asva, vyas, atya])

yodhan = Lengaburu("Yodhan", "Male", jaya, dritha)
laki = Lengaburu("Laki", "Male", arit, jnki)
lavnya = Lengaburu("Lavnya", "Female", arit, jnki)
vasa = Lengaburu("Vasa", "Male", asva, satvy)
kriya = Lengaburu("Kriya", "Male", vyas, krpi)
krithi = Lengaburu("Krithi", "Female", vyas, krpi)

dritha.set_spouse(jaya).set_siblings([tritha, vritha]).set_children([yodhan])
jaya.set_spouse(dritha).set_children([yodhan])
tritha.set_siblings([dritha, vritha])
vritha.set_siblings([dritha, tritha])
vila.set_siblings([chika])
chika.set_siblings([vila])
jnki.set_spouse(arit).set_siblings([ahit]).set_children([laki, lavnya])
arit.set_spouse(jnki).set_children([laki, lavnya])
ahit.set_siblings([jnki])
asva.set_spouse(satvy).set_siblings([vyas, atya]).set_children([vasa])
satvy.set_spouse(asva).set_children([vasa])
vyas.set_spouse(krpi).set_siblings([asva, atya]).set_children([kriya, krithi])
krpi.set_spouse(vyas).set_children([kriya, krithi])
atya.set_siblings([asva, vyas])

laki.set_siblings([lavnya])
lavnya.set_siblings([laki])
kriya.set_siblings([krithi])
krithi.set_siblings([kriya])


# method to add __children
def add_child(mother, name, gender):
    if mother in Lengaburu.family_members.keys():
        if Lengaburu.family_members[mother].name == mother and Lengaburu.family_members[mother].gender == "Female" and Lengaburu.family_members[mother].spouse:
            temp_mother = Lengaburu.family_members[mother]
            name = Lengaburu(name, gender, temp_mother.spouse, temp_mother)
            if temp_mother.children:
                name.siblings = temp_mother.children[:]
                for children in temp_mother.children:
                    if children.siblings:
                        children.siblings.append(name)
                    else:
                        children.siblings = [name]
                temp_mother.children.append(name)
                temp_mother.spouse.children = temp_mother.children

            print("CHILD_ADDITION_SUCCEEDED")
        else:
            print("CHILD_ADDITION_FAILED")
    else:
        print("PERSON_NOT_FOUND")


# method to compute relation-ships
def get_relationship(name, relationship):
    if name in Lengaburu.family_members.keys():
        temp_member = Lengaburu.family_members[name]
        if "Son" == relationship:
            temp_member.get_son()
        elif "Daughter" == relationship:
            temp_member.get_daughter()
        elif "Siblings" == relationship:
            if temp_member.siblings:
                for siblings in temp_member.get_siblings():
                    print(siblings)
            else:
                print("NONE")
        elif "Brother-In-Law" == relationship:
            temp_member.get_brother_in_law()
        elif "Sister-In-Law" == relationship:
            temp_member.get_sister_in_law()
        elif "Paternal-Aunt" == relationship:
            temp_member.get_paternal_aunt()
        elif "Paternal-Uncle" == relationship:
            temp_member.get_paternal_uncle()
        elif "Maternal-Aunt" == relationship:
            temp_member.get_maternal_aunt()
        elif "Maternal-Uncle" == relationship:
            temp_member.get_maternal_uncle()
        else:
            print("RELATION_SHIP_CANNOT_BE_COMPUTED")
    else:
        print("PERSON_NOT_FOUND")

    print("")


# Accepting inputs via a command line
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    print(vars(king_shan))
    for i in range(0, len(lines)):
        params = lines[i].rstrip().split(" ")
        if "ADD_CHILD" == params[0]:
            add_child(params[1], params[2], params[3])
        if "GET_RELATIONSHIP" == params[0]:
            get_relationship(params[1], params[2])

quit()
