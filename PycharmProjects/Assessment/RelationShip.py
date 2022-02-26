import Family


class RelationShip:
    # computing defined relation ships
    def get_paternal_aunt(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_father():
                if self.get_father().get_siblings():
                    for aunt in self.get_father().get_siblings():
                        if aunt.get_gender() == "Female":
                            print(aunt.get_name(), end=" ")
                            ctr += 1
                    if not ctr:
                        print("NONE")
                else:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def get_paternal_uncle(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_father():
                if self.get_father().get_siblings():
                    for uncle in self.get_father().get_siblings():
                        if uncle.get_gender() == "Male":
                            print(uncle.get_name(), end=" ")
                            ctr += 1
                    if not ctr:
                        print("NONE")
                else:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")
        
    def get_maternal_aunt(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_mother():
                if self.get_mother().get_siblings():
                    for aunt in self.get_mother().get_siblings():
                        if aunt.get_gender() == "Female":
                            print(aunt.get_name(), end=" ")
                            ctr += 1
                    if not ctr:
                        print("NONE")
                else:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def get_maternal_uncle(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_mother():
                if self.get_mother().get_siblings():
                    for uncle in self.get_mother().get_siblings():
                        if uncle.get_gender() == "Male":
                            print(uncle.get_name(), end=" ")
                            ctr += 1
                    if not ctr:
                        print("NONE")
                else:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def get_brother_in_law(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_spouse() or self.get_siblings():
                if self.get_spouse():
                    if self.get_spouse().get_siblings():
                        for brother in self.get_spouse().get_siblings():
                            if brother.get_gender() == "Male":
                                print(brother.get_name(), end=" ")
                                ctr += 1
                if self.get_siblings():
                    for brother in self.get_siblings():
                        if brother.get_gender() == "Female":
                            if brother.get_spouse():
                                print(brother.get_spouse().get_name(), end=" ")
                                ctr += 1
                if not ctr:
                    print("NONE")

            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def get_sister_in_law(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_spouse() or self.get_siblings():
                if self.get_spouse():
                    if self.get_spouse().get_siblings():
                        for sister in self.get_spouse().get_siblings():
                            if sister.get_gender() == "Female":
                                print(sister.get_name(), end=" ")
                                ctr += 1
                if self.get_siblings():
                    for sister in self.get_siblings():
                        if sister.get_gender() == "Male":
                            if sister.get_spouse():
                                print(sister.get_spouse().get_name(), end=" ")
                                ctr += 1
                if not ctr:
                    print("NONE")

            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")
        
    def get_son(self):
        ctr = 0
        if self in Family.Family.family_members.values():
            if self.get_children():
                for son in self.get_children():
                    if son.get_gender() == "Male":
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
        if self in Family.Family.family_members.values():
            if self.get_children():
                for daughter in self.get_children():
                    if daughter.get_gender() == "Female":
                        ctr += 1
                        print(daughter, end=" ")
                if not ctr:
                    print("NONE")
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")

    def fetch_siblings(self):
        if self in Family.Family.family_members.values():
            if self.get_siblings():
                for siblings in self.get_siblings():
                    print(siblings)
            else:
                print("NONE")
        else:
            print("PERSON_NOT_FOUND")