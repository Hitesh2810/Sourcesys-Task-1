class Lead:
    def show(self, name):
        self.name= name
        print(f"Normal Lead: {self.name}")


class PremiumLead(Lead):
    def show(self, name): 
        self.name= name
        print(f"Premium Lead: {self.name}")


# Objects
l1 = Lead()
l2 = PremiumLead()

l1.show("Hitesh Kumar S")
l2.show("Prem Kumar S")