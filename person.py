from random import random,randint,uniform,gauss


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
