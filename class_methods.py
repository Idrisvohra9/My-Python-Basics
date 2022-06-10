import os
os.system("cls")
# A class method is a method that is bound to the class and not the object of the class. @classmethod decorator is used to create a class method.
class human:
    blood_type ="O+"
    skin_color="White"
    hair_color="Blonde"
    sex="Female"
    def Change_blood_type(self,bld_typ):    # This changes Instance attribute of blood_type. 
        self.blood_type = bld_typ

    def Change_skin_color(self, skn_clr):   # This changes Class attribute of skin_color.
        self.__class__.skin_color = skn_clr
    
    @classmethod # The decorators comes before the function definition. 
    def Change_hair_color(cls, hr_clr):      # This changes Class attribute of hair_color.
        cls.hair_color = hr_clr


Cindrella=human()

print("Changing the instance attribute: (The class attribute will remain unchanged)\n")

print("Instance attribute before change:",Cindrella.blood_type) # O+

Cindrella.Change_blood_type("B+")

print("Instance attribute After change:",Cindrella.blood_type) # B+

print("Class attribute After change:",human.blood_type) # The class attribute remains the same: O+

# blood_type is a class attribute and by this way we can change the blood type of instance attribute. But what if we need to change the class attribute blood_type ?
# to do that there are 2 ways

"""class dundar or __class__ method to change the class attribute: """

print("\n\nChanging the Class attribute by __class__: \n")

print("Instance attribute before change:",Cindrella.skin_color) # White

Cindrella.Change_skin_color("Brown")

print("Instance attribute After change:",Cindrella.skin_color) # This changes the skin color (class attribute) to : Brown
print("Class attribute After change:",human.skin_color) # The class attribute : Brown



"""@classmethods way of changing the class attribute: """

print("\n\nChanging the Class attribute by @classmethod: \n")

print("Instance attribute before change:",Cindrella.hair_color) # Blonde

Cindrella.Change_hair_color("Brunette")

print("Instance attribute After change:",Cindrella.hair_color) # Brunette

print("Class attribute After change:",human.hair_color)
