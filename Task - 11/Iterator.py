class LeadIterator:
    def __init__(self, leads):
        self.leads = leads
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.leads):
            lead = self.leads[self.index]
            self.index += 1
            return lead
        else:
            raise StopIteration


leads = ["Hitesh", "Rahul", "Prem"]

for l in LeadIterator(leads):
    print("Lead:", l)