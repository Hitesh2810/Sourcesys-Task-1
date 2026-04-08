class LeadHub:
    c = 1
    print("============")
    def __init__(self):
        self.__leads = 100   # private

    def add_leads(self, count):
        self.__leads += count

    def show(self):
        
        print(f"Leads: {LeadHub.c}", self.__leads)
        LeadHub.c+=1


lh = LeadHub()
lh.add_leads(50)
lh.show()

lh1 = LeadHub()
lh1.add_leads(100)
lh1.show()