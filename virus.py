class Virus():
    IT = 7    # average incubation time
    HT = 21  # average heal time
    R0 = 2.3  # basic reproduction number
    DC = 0.03 # death chance


    def update(self,contacts):
        self.R0 = contacts