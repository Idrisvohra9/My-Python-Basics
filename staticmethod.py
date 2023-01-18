<<<<<<< HEAD
# to use a function inside a class without a self parameter staticmethod is used.
# Only when the class functions do not need the self parameter staticmethod is used.
class human_Body:
     parts="Mental, physical, internal organs"
     @staticmethod 
     def mental():
          print("Frontal lobe, Parietal lobe, Temporal lobe, occipital lobe")
     @staticmethod
     def physical():
          print("Skin, Muscular structure, Skeleton structure")
     # Without using @staticmethod 
     def internal_organs(self):
          self.abdominal="Large intestine, small intestine, stomach, Oesophagus"
          print(self.abdominal)
body=human_Body()
print(body.parts) # This is class attribute
# Output: Mental, physical, internal organs
print()
body.mental() # We also do not need to add any arguments while calling the particular function.
# Output: Frontal lobe, Parietal lobe, Temporal lobe, occipital lobe
print()
body.physical()
# Output: Skin, Muscular structure, Skeleton structure
print()
body.internal_organs()
=======
# to use a function inside a class without a self parameter staticmethod is used.
# Only when the class functions do not need the self parameter staticmethod is used.
class human_Body:
     parts="Mental, physical, internal organs"
     @staticmethod 
     def mental():
          print("Frontal lobe, Parietal lobe, Temporal lobe, occipital lobe")
     @staticmethod
     def physical():
          print("Skin, Muscular structure, Skeleton structure")
     # Without using @staticmethod 
     def internal_organs(self):
          self.abdominal="Large intestine, small intestine, stomach, Oesophagus"
          print(self.abdominal)
body=human_Body()
print(body.parts) # This is class attribute
# Output: Mental, physical, internal organs
print()
body.mental() # We also do not need to add any arguments while calling the particular function.
# Output: Frontal lobe, Parietal lobe, Temporal lobe, occipital lobe
print()
body.physical()
# Output: Skin, Muscular structure, Skeleton structure
print()
body.internal_organs()
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
# Output: Large intestine, small intestine, stomach, Oesophagus