import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from random import random,randint,uniform,gauss

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


class Virus():
    IT = 5    # average incubation time
    HT = 21  # average heal time
    R0 = 2.3  # basic reproduction number
    DC = 0.03 # death chance


    def update(self,contacts):
        self.R0 = contacts

class Person():
    time = 0        # time since the infection
    virus     = None
    tested    = False  # 
    healthy   = True
    alive     = True
    recovered = False 

    def advance(self):
        if(not self.healthy):
            self.time +=1
            if(self.time>=self.virus.HT):
                if(randint(0,1000)/10<self.virus.DC*100):
                    self.alive = False

        if(self.alive):    
            if(self.time>=self.virus.IT):
                self.tested  = True
            if(self.time>=self.virus.HT):
                self.healthy = True
                self.recovered = True

    def can_infect(self):
        t1 = self.alive
        t2 = not self.healthy
        t3 = not self.tested
        t4 = not self.recovered
        return t1 and t2 and t3 and t4

    def can_be_infected(self):
        t1 = self.alive
        t2 = self.healthy
        t3 = not self.tested
        t4 = not self.recovered
        return t1 and t2 and t3 and t4


class Simulation():
    log       = {'time':[],'healthy':[],'infected':[],'recovered':[],'dead':[]}
    time      = 0
    virus     = None
    country   = None
    people    = []

    def __init__(self,country,virus):
        self.country = country
        self.virus   = virus

    def get_stats(self):
        healthy   = 0
        infected  = 0
        recovered = 0
        dead      = 0
        for p in self.people:
            if(p.healthy) and (p.alive):
                healthy  +=1
            if(not p.healthy) and (p.alive):
                infected +=1
            if(not p.alive):
                dead +=1
            if(p.recovered):
                recovered +=1

        self.log["infected"].append(infected)
        self.log["healthy"].append(healthy)
        self.log["dead"].append(dead)
        self.log["recovered"].append(recovered)
        self.log["time"].append(self.time)



    def simulate(self):
        # create population
        for i in range(self.country.population):
            person = Person()
            person.virus = self.virus
            self.people.append(person)

        # infect one person
        self.people[0].healthy = False
        while True:

            #  ==========================
            # infecting people
            new_infections = 0
            for p in self.people:
                if p.can_infect():
                    new_infections += self.virus.R0*(np.exp(-self.time/20))

            new_infections = np.floor(new_infections)
            for p in self.people:
                if p.can_be_infected():
                    p.healthy = False
                    new_infections -= 1
                if(new_infections==0):
                    break
            #  ==========================

            for p in self.people:
                p.advance()

            # after a 1 week engage social isolation:
            if(self.time>=7):
                self.virus.update(0.1)

            self.time +=1
            self.get_stats()
            print(self.time)
            if(self.log['infected'][-1]==0):
                break

if __name__=="__main__":
    poland = Country()
    virus  = Virus()
    sim    = Simulation(poland,virus)
    sim.simulate()


    plt.figure()
    plt.plot(sim.log["time"],sim.log["healthy"])
    plt.plot(sim.log["time"],sim.log["infected"])
    plt.plot(sim.log["time"],sim.log["dead"])
    plt.plot(sim.log["time"],sim.log["recovered"])
    plt.legend(("healthy","infected","dead","recovered"))
    plt.show()
    
