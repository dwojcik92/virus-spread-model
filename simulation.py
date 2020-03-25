from person import Person
import numpy as np


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
                    new_infections += self.virus.R0*(np.exp(-self.time/self.virus.HT))

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
                self.virus.R0 = self.virus.R0/4

            self.time +=1
            self.get_stats()
            print(self.time)
            if(self.log['infected'][-1]==0):
                break