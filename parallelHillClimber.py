import copy

from solution import SOLUTION
import constants as c
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        self.Show_Best()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for key in self.parents.keys():
            self.children[key] = copy.deepcopy(self.parents[key])
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents.keys():
            if self.parents[key].fitness > self.children[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print("\n")
        for key in self.parents.keys():
            print("Parent Fitness:", str(self.parents[key].fitness), "Child Fitness:", str(self.children[key].fitness))
        print("\n")

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        lowestFitness = {}
        minFitness = self.parents[0]
        for key in self.parents.keys():
            current = self.parents[key]
            if current.fitness < minFitness.fitness:
                minFitness = current
                print("\nUpdated minFitness with new value: " + str(minFitness.fitness))
        print("\nBest Self Identified \n")
        print("New value is " + str(minFitness.fitness) + "Generating visual representation")
        minFitness.Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")

        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()
