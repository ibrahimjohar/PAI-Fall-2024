class car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


c = car('audi', 'a4', 2016)
name = c.get_name()
print("long name: ",name)