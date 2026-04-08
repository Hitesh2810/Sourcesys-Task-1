class Leadhub:
    def __init__(self, name, company, email, status, assigned_to):
        self.name = name
        self.company = company
        self.email = email
        self.status = status
        self.assigned_to = assigned_to

    def show(self):
        print("================================")
        print("Lead:", self.name)
        print("Company:", self.company)
        print("Email:", self.email)
        print("Status:", self.status)
        print("Assigned To:", self.assigned_to)


l1 = Leadhub("Hitesh", "Infosys", "hitesh@infosys.com", "Completed", "Likitha")
l2 = Leadhub("Rahul", "TCS", "rahul@tcs.com", "Pending", "Nithya")
l3 = Leadhub("Suresh", "Wipro", "suresh@wipro.com", "In Progress", "Keerthi")

l1.show()
l2.show()
l3.show()