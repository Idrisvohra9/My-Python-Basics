<<<<<<< HEAD
# Heirarchical inheritance: When more than one child class inherits from one single parent class This inheritance is called Heirarchical inheritance.

class Network:               # Single (Base) parent class
    Name = "Jio"
    Speed= "5 mb/s"

class User1(Network):        # Derived Child class
    def Connectivity(self):
        self.Connectivity = self.Connectivity
    Data="2 Gb"
    plan="2 months"

class User2(Network):        # Derived Child class
    Data="3 Gb"
    plan="6 months"
    def Connectivity(self):
        self.Connectivity = self.Connectivity

class User3(Network):        # Derived Child class
    Data="1.5 Gb"
    plan="3 months"
    def Connectivity(self):
        self.Connectivity = self.Connectivity

# Making instances and calling the functions:
u1=User1
u2=User2
u3=User3
u1.Connectivity="Slow"
u2.Connectivity="Medium"
u3.Connectivity="Fast"
print(f"The configurations of user1: \nNetwork: {u1.Name}\n Speed: {u1.Speed}\n Data: {u1.Data}\n Plan: {u1.plan}\n Connectivity: {u1.Connectivity}\n")
print(f"The configurations of user2: \nNetwork: {u2.Name}\n Speed: {u2.Speed}\n Data: {u2.Data}\n Plan: {u2.plan}\n Connectivity: {u2.Connectivity}\n")
=======
# Heirarchical inheritance: When more than one child class inherits from one single parent class This inheritance is called Heirarchical inheritance.

class Network:               # Single (Base) parent class
    Name = "Jio"
    Speed= "5 mb/s"

class User1(Network):        # Derived Child class
    def Connectivity(self):
        self.Connectivity = self.Connectivity
    Data="2 Gb"
    plan="2 months"

class User2(Network):        # Derived Child class
    Data="3 Gb"
    plan="6 months"
    def Connectivity(self):
        self.Connectivity = self.Connectivity

class User3(Network):        # Derived Child class
    Data="1.5 Gb"
    plan="3 months"
    def Connectivity(self):
        self.Connectivity = self.Connectivity

# Making instances and calling the functions:
u1=User1
u2=User2
u3=User3
u1.Connectivity="Slow"
u2.Connectivity="Medium"
u3.Connectivity="Fast"
print(f"The configurations of user1: \nNetwork: {u1.Name}\n Speed: {u1.Speed}\n Data: {u1.Data}\n Plan: {u1.plan}\n Connectivity: {u1.Connectivity}\n")
print(f"The configurations of user2: \nNetwork: {u2.Name}\n Speed: {u2.Speed}\n Data: {u2.Data}\n Plan: {u2.plan}\n Connectivity: {u2.Connectivity}\n")
>>>>>>> 66ba5faed76c21bba0a6cb181bc8a77bae565f4f
print(f"The configurations of user3: \nNetwork: {u3.Name}\n Speed: {u3.Speed}\n Data: {u3.Data}\n Plan: {u3.plan}\n Connectivity: {u3.Connectivity}\n")