# Defining the parent class
# Vehicles

# we have an understanding that one attribute that would be common in all types of vehicle is medium of commute/travel
# and also that this can be different for different types of vehicles, say Aerial Vehicles, Oceanic Vehicles and Land/Surface Vehicles

class Vehicles:
    def __init__(self):
        print('Main class vehicles')
    def print_vehicle_detail(self):
        print('"Calling from Parent calss: vehicles", the medium of travel for this vehicle is: ', self.medium)

# defining child classes after inheriting 'vehicles' as parent class

# Land(Vehicles) RC car, car, bike, bicycle, trucks, semi-trucks, etc...
# Water(Vehicles) can be ship, boat, raft, submerine, etc...
# Air(Vehicles) can have children as space-ships, UAV, etc...  
# Others(Vehicles) can be hovercraft, submersible cars, infact all hybrid category vehicles like seaplanes, etc...


class Land(Vehicles):
    def __init__(self):
        Vehicles.medium = 'Land'                # sets variable, medium of parent class, Vehicles
        print('\nIt can be any Land vehicle')
    def print_details(self):
        Vehicles.print_vehicle_detail(self)     # Technique 1, called from parent class, Vehicles (in case of overridden methods)
        print("This vehicle drives on the land")

class Water(Vehicles):
    def __init__(self):
        Vehicles.medium = 'Water'       # sets variable, medium of parent class, Vehicles
        print('\nIt can be any oceanic vehicles')
    def print_details(self):
        self.print_vehicle_detail()     # Technique 2, called from child class, Vehicles
        print('This vehicle commutes through water')

class Air(Vehicles):
    def __init__(self):
        Vehicles.medium = 'Air'         # sets variable, medium of parent class, Vehicles
        print('\nIt can be any flying vehicle')
    def print_details(self):
        print('The plane is flying in the air')

class Other(Vehicles):
    def __init__(self):
        # Vehicles.medium = 'Hybrid'
        print('\nIt can be any hybrid category vehicle')
    def print_details(self):
        print('This vehicle can have more than one medium of commute')



obj1  = Land()
obj1.print_details()

obj2 = Water()
obj2.print_details()

obj3 = Air()
obj3.print_vehicle_detail()     # Technique 3, called from child object class.
obj3.print_details()

obj4 = Other()
obj4.medium = 'Hybrid'
obj4.print_vehicle_detail()     # Technique 4. Update Parent variables and access parent methods from child object
obj4.print_details()