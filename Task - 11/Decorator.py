def log_action(func):
    def wrapper():
        print("Action started")
        func()
        print("Action completed")
    return wrapper


@log_action
def add_lead():
    print("Lead added")


add_lead()