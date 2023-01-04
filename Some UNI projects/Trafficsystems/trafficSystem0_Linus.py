
from time import sleep
import destinations as dst
import trafficComponents as tc


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        self.time = 0
        self.laneOut = tc.Lane(5)
        self.laneIN = tc.Lane(5)
        self.light1 = tc.Light(10,8)
        self.dest = dst.Destinations()
        self.Queue = []


        self.carstats = 0
        self.car_amount = 0
        self.insystem = 0

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        print(f'{self.laneOut} {self.light1} {self.laneIN} {self.Queue}')

    def step(self):
        """Take one time step for all components."""
                                                    #   35 - 39
                                                    #   Om första obj. existerar (inte = none), ta bort första obj.
                                                    #   Ta bort bil
                                                    #   Stegar
        if self.laneOut.get_first() != None:
            self.laneOut.remove_first()
            self.car_amount -= 1

        self.laneOut.step()
                                                    #   43 - 50:
                                                    #   Om grönt => kont. första & sista plats  Kör in bil.
                                                    #   aka kör förbi trafikljus
                                                    #   Stegar
        if self.light1.is_green() == True \
            and self.laneIN.get_first() != None \
            and self.laneOut.last_free() == True:
            self.laneOut.enter(self.laneIN.get_first())
            self.laneIN.remove_first()

        self.light1.step()
        self.laneIN.step()

                                                    #   55 - 77
                                                    #   Hämtar desitnation för bilar
                                                    #   Kollar om vi kan köra in bilar direkt eller om vi måste ställa
                                                    #   dem på kö. isf är det ledigt i laneIN eller ska vi köa dem?
                                                    #   är det ledigt i laneIN kör ut ur kön och ta bort bilen
                                                    #   Systemtid +1

        Stepdest = self.dest.step()

        if Stepdest != None and self.laneIN.last_free() == True and self.Queue == []:
            self.laneIN.enter(tc.Vehicle(Stepdest, self.time))
            self.carstats += 1
        elif Stepdest != None and self.laneIN.last_free() == True:
            self.Queue.append(Stepdest)
            self.laneIN.enter(tc.Vehicle(self.Queue[0], self.time))
            self.carstats += 1
            self.Queue.remove(self.Queue[0])
        elif Stepdest != None and self.laneIN.last_free() == False:
            self.Queue.append(Stepdest)
            self.carstats += 1
        elif Stepdest == None and self.Queue != [] and self.laneIN.last_free() == True:
            self.laneIN.enter(tc.Vehicle(self.Queue[0], self.time))
            self.Queue.remove(self.Queue[0])

        self.time += 1



    def print_statistics(self):
        """Print statistics about the run.
            -  statistik printsen per run"""
        self.insystem = self.carstats + self.car_amount
        print(f'Statistics after {self.time} timesteps:')
        print('')
        print(f'Created vehicles: {self.carstats}')
        print(f'In system       : {self.insystem}')


def main():
    ts = TrafficSystem()
    for i in range(33):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()