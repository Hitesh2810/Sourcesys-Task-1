def lead_generator():
    leads = ["Hitesh", "Rahul", "Prem"]
    for l in leads:
        yield l


for lead in lead_generator():
    print("Generated Lead:", lead)