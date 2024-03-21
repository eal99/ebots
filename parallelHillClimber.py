import copy

from solution import SOLUTION
import constants as c
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")
        # self.parent = SOLUTION()
        self.nextAvailableID = 0
        self.parents = {}

        for i in range(c.populationSize + 1):
            print(self.nextAvailableID)

            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):

        for parent in self.parents.values():
            parent.Start_Simulation("DIRECT")

        for parent in self.parents.values():
            parent.Wait_For_Simulation_To_End()
            print(parent.fitness)

        # self.parent.Evaluate("DIRECT")
        # self.Show_Best()
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        # self.Spawn()
        # self.Mutate()
        # self.child.Evaluate()
        # self.Select()
        # self.Print()
        pass

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child
        # print("Parent", self.parent.fitness)
        # print("Child", self.child.fitness)
        # exit()

    def Print(self):
        print("\n Parent Fitness:", str(self.parent.fitness), "\n Child Fitness:", str(self.child.fitness))

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass
