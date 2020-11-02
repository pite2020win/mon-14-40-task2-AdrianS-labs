#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.
import random

class Plane:
    def __init__(self, yaw, roll, pitch , rate_of_correction):
        self.yaw = yaw
        self.roll = roll
        self.pitch = pitch
        self.rate_of_correction = rate_of_correction

    def simulate_turbulance(self):
        self.yaw += random.gauss(0, 4) 
        self.roll += random.gauss(0, 4)
        self.pitch += random.gauss(0, 4)
    
    def detect_current_orientation(self):
        orientation_dict = []
        orientation_dict.append(self.yaw)
        orientation_dict.append(self.roll)
        orientation_dict.append(self.pitch)
        return orientation_dict

    def correct_orientation(self):
        self.yaw -= random.gauss(0, 2*self.rate_of_correction)
        self.roll -= random.gauss(0, 2*self.rate_of_correction)
        self.pitch -= random.gauss(0, 2*self.rate_of_correction)



if __name__ == "__main__":
    simulation_step = 0
    simulated_plane = Plane(0, 0, 0, 2)
    while (simulation_step <= 1000):
        simulated_plane.simulate_turbulance()
        orientations = simulated_plane.detect_current_orientation()
        print(orientations)
        simulated_plane.correct_orientation()
        simulation_step += 1
