import string
import random
import datetime
import math

# Background

# Parking lots have open spaces for vehicles to park in. 
# Vehicles can be of different sizes, e.g. cars, limos, trucks, etc.

# In some cases, parking spots can be numbered. 
# For large venues, parking lots may have multiple levels, i.e. parking garages.

# Sometimes parking is free, but in other cases customers have to pay. 
# So parking lots can have a payment system to keep track of parked vehicles.

# Requirements

# Some possible questions to ask:

# Will there be multiple levels in the parking lot?
# What kinds of vehicles will be parked? Will their sizes differ?
# Will there be special spots for certain vehicles?
# Will the parking lot have a payment system? If so, how will it work?
# Will parking spots be reserved or can the driver choose any spot?
# How much functionality will the driver have beyond parking and paying?
# Basics

# Multiple levels in the parking lot
# Possible vehicle types: car, limo, semi-truck
# We will have a payment system, with a single entrance and exit
# Drivers will be assigned a parking spot after paying
# Vehicles and Parking Spots

# Vehicles can be of different sizes (car = 1, limo = 2, truck = 3)
# Each parking spot will have a size of 1
# A vehicle must fully take up each spot assigned to it (no fractional spots)
# Vehicles will automatically be assigned the next available parking spot on the lowest floor
# Payment System

# Drivers will pay for parking and be assigned the next available spot on the lowest floor
# Drivers can pay for a variable number of hours and they are charged after they remove their vehicle based on an hourly rate
# We can assume vehicles can be parked for a variable number of hours
# If there is no capacity, the system should not assign a spot and should notify the driver


class Vehicle:
    def __init__(self, spot_size):
        self._spot_size = spot_size

    def get_spot_size(self):
        return self._spot_size

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__(1)

class Limo(Vehicle):
    def __init__(self) -> None:
        super().__init__(2)

class Semi(Vehicle):
    def __init__(self) -> None:
         super().__init__(3)
    
class Driver(Vehicle):
    def __init__(self, vehicle) -> None:
         self._id = ''.join(random.choices(string.digits, 16))
         self._vehicle = vehicle
         self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle
    
    def get_id(self):
        return self._id 
    
    def charge(self, amount):
        self._payment_due += amount 


class ParkingFloor:
    def __init__(self, spot_count):
        self._spots = [0] * spot_count
        self._vehicle_map = {}

    def park_vehicle(self, vehicle):
        size = vehicle.get_spot_size()
        l, r = 0, 0
        while r < len(self._spots):
            if self._spots[r] != 0:
                l = r + 1
            if r - l + 1 == size:
                # we found enough spots, park the vehicle
                for k in range(l, r+1):
                    self._spots[k] = 1
                self._vehicle_map[vehicle] = [l, r]
                return True
            r += 1
        return False
    
    def remove_vehicle(self, vehicle):
        start, end = self._vehicle_map[vehicle]
        for i in range(start, end + 1):
            self._spots[i] = 0
        del self._vehicle_map[vehicle]

    def get_parking_spots(self):
        return self._spots

    def get_vehicle_spots(self, vehicle):
        return self._vehicle_map.get(vehicle)

class ParkingGarage:
    def __init__(self, floor_count, spots_per_floor):
        self._parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]

    def park_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False
    
class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):
        self._parkingGarage = parkingGarage
        self._hourlyRate = hourlyRate
        self._timeParked = {} # map driverId to time that they parked

    def park_vehicle(self, driver):
        currentHour = datetime.datetime.now().hour
        isParked = self._parkingGarage.park_vehicle(driver.get_vehicle())
        if isParked:
            self._timeParked[driver.get_id()] = currentHour
        return isParked
    
    def remove_vehicle(self, driver):
        if driver.get_id() not in self._timeParked:
            return False
        currentHour = datetime.datetime.now().hour
        timeParked = math.ceil(currentHour - self._timeParked[driver.get_id()])
        driver.charge(timeParked * self._hourlyRate)

        del self._timeParked[driver.get_id()]
        return self._parkingGarage.remove_vehicle(driver.get_vehicle())
    
parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(Car())
driver2 = Driver(Limo())
driver3 = Driver(Semi())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false