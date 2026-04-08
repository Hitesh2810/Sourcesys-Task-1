from abc import ABC, abstractmethod

class System(ABC):
    @abstractmethod
    def process(self):
        pass


class LeadSystem(System):
    def process(self):
        print("Processing leads...")


obj = LeadSystem()
obj.process()