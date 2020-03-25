import matplotlib.pyplot as plt

from virus import Virus
from simulation import Simulation
from country import Country


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
    
