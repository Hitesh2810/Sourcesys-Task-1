class Lead:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print(f"Name: ", self.name)
        print(f"Email: ", self.email)
        print(f"Phone: ", self.phone)

class Customer(Lead):
    def show(self):
        print("I am a customer.")
        print("====================")


lead1 = Customer("Hitesh", "hiteshkumar@gmail.com", "9241516587")
lead2 = Customer("Prem", "premkumar@gmail.com", "9245655187")
lead1.display()
lead1.show()
lead2.display()
lead2.show()