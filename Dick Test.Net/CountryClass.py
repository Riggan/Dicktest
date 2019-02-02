class Country:

    counter = 0

    def __init__(self, cname):

        self.id = Country.counter
        Country.counter += 1

        self.dicks = []

        self.name = cname

    def add_dick(self, d):
        self.dicks.append(d)
        d.cid = self.id
