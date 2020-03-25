class Country():
    population = 10000#37.98e6
    infected   = 0 
    recovered  = 0
    died       = 0
    young_age_per  = 0.155
    middle_age_per = 0.67
    old_age_per    = 0.175
    young  = 0
    middle = 0
    old    = 0 


    def __init__(self):
        self.get_age_distribution()

    def get_age_distribution(self):
        self.young  = self.population*self.young_age_per
        self.middle = self.population*self.middle_age_per
        self.old    = self.population*self.old_age_per