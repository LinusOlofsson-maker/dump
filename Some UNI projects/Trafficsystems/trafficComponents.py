# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""
    
    def __init__(self, destinate, borntime):
        """Creates the vehicle with specified properties."""
        self.borntime = borntime
        self.destin = destinate
        
    def __str__(self):
        return str(f'Vehicle({self.destin}, {self.borntime})')


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.length = length
        self.rep = ''
        self.cars_inside = []
        self.lane_list = ['.' for i in range(self.length)]
        self.direction = ''

    def __str__(self):
        """String representation of lane contents."""
        self.lane_print = ''
        for i in range(len(self.lane_list)):
            self.lane_print += self.lane_list[i]
        return str(f'[{self.lane_print}]')

    def __repr__(self):
        """Compact representation of lane contents."""
        
        return self.cars_inside

    def enter(self, entervehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.car = entervehicle
        if self.last_free() == True:
            self.lane_list[len(self.lane_list)-1] = f'{self.car.destin}'
            self.cars_inside.append(self.car)
        else:
            pass
        
    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        if self.lane_list[len(self.lane_list)-1] == '.':
            self.free = True
        else:
            self.free = False
        return self.free

    def step(self):
        """Execute one time step."""
        self.s = 0
        for i in self.lane_list:
            if i == '.' and self.s < len(self.lane_list)-1:
                self.lane_list[self.s] = self.lane_list[self.s+1]
                self.lane_list[self.s+1] = '.'
            self.s += 1

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        if self.lane_list[0] == '.':
            self.first = None
        else:
            self.first = self.cars_inside[0]
        return self.first

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        if self.lane_list[0] == '.':
            self.remove = None
        else:
            self.remove = self.cars_inside[0]
            self.cars_inside.remove(self.cars_inside[0])
            self.lane_list[0] = '.'
        return self.remove

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        self.number_cars = len(self.cars_inside)
        return self.number_cars


def demo_lane():
    """"For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.Lane = Lane
        self.period = period
        self.green_period = green_period
        self.stepcount = 0
        self.red_period = self.period - self.green_period
        self.timer_list = []
        #RED = '\033[91m'
        #END = '\033[0m'
        #Green = '\33[4m'

        for i in range(self.green_period):
            self.timer_list.append('(\33[92mG\33[0m)')
        for i in range(self.red_period):
            self.timer_list.append('(\033[91mR\033[0m)')

    def __str__(self):
        """Report current state of the light."""
        return str(self.timer_list[self.stepcount%self.period])

    def step(self):
        """Take one light time step."""
        self.stepcount = self.stepcount + 1

    def is_green(self):
        """Return whether the light is currently green."""
        if self.stepcount%self.period < self.green_period:
            self.green = True
        else:
            self.green = False
        return self.green


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()