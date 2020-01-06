class Family:
    """This is a program representation of a nuclear family.

       parent_name: name of the mother or father of the family.

       children_name: a list of the children in the family.

       child_gender: a list of the corresponding genders of each child."""

    def __init__(self,parent_name,children_name=[],child_gender=[]):
        if children_name == [] and child_gender == []:
            print("You don't have a child or your children have not been given a gender.")
            self.children_name = children_name
            self.child_gender = child_gender
        else:
            self.parent_name = parent_name
            self.children_name = children_name
            self.child_gender = child_gender

    def is_male(self,name):
        if not self.children_name:                    #checks if list is empty
            print("You don't have a child.")            #returns this when list is empty
        else:
            if name in self.children_name:             #checks if name is in list
                return self.child_gender[self.children_name.index(name)] == "male"     #returns this when name in list

    def is_female(self,name):                          #does the same as the is_male method
        if not self.children_name:
            print("You don't have a child")
        else:
            if name in self.children_name:
                return self.child_gender[self.children_name.index(name)] == "male"

    def set_parents(self,child_name,parent_name):
        self.parent_name = parent_name
        self.children_name.append(child_name)

    def get_parents(self,name):
        """This returns the parent name if the list of children is not empty and the parameter 'name' is in the
           list of children."""
        if not self.children_name:
            print("This child is not part of the family")
        else:
            if name in self.children_name:
                return self.parent_name

    def get_children(self,name):
        """This first check if the parameter 'name' is in the list of children return the corresponding
           output. if the list is empty is tells the user. if the child is not in the list, it also informs
           the user and if it is there, ut returns the name."""
        if not self.children_name:
            print("This child is not part of the family")
        else:
            if name in self.children_name:
                return name
            else:
                print("This child is not your child")


    def __repr__(self):
        return "Family:{}\t{}".format(self.parent_name,self.children_name)