import random
import pygame
from pygame.locals import *
import time
# from matplotlib import pyplot as plt



# Movements:
# 0 -> no_action
# 1 -> left_rotation
# 2 -> right_rotation
# 3 -> forward


#  Face Of Robot
# 
#     3
# 	  ^
# 	  |
# 2 <- -> 0
# 	  |
# 	  v
# 	  1


populationSize = 100
trailSize = 28
validMoves = "0123"
targetFitness = 20
generationBound = 1000

generationList = []
fitnessList = []


# def setup():
# 	size(800,600)


# def draw():
# 	grid = [ [-1,-1,-1,-1,-1,-1,-1,-1],
# 			 [-1, 1, 1, 1, 1, 1, 1,-1],
# 			 [-1, 1, 0, 0, 0, 0, 1,-1],
# 			 [-1, 1, 0, 0, 0, 1,-1,-1],
# 			 [-1, 1, 0, 0, 0, 1,-1,-1],
# 			 [-1, 1, 0, 0, 0, 0, 1,-1],
# 			 [-1, 1, 1, 1, 1, 1, 1,-1],
# 			 [-1,-1,-1,-1,-1,-1,-1,-1],
# 	]

# 	x,y = 0,0
# 	for row in grid:
# 		for col in row:
# 			rect(x,y,70,70)
# 			x = x + w
# 		y = y + w
# 		x = 0







def drawOptimalOnScreen(chromosome):
	grid = [ [-1,-1,-1,-1,-1,-1,-1,-1],
			 [-1, 1, 1, 1, 1, 1, 1,-1],
			 [-1, 1, 0, 0, 0, 0, 1,-1],
			 [-1, 1, 0, 0, 0, 1,-1,-1],
			 [-1, 1, 0, 0, 0, 1,-1,-1],
			 [-1, 1, 0, 0, 0, 0, 1,-1],
			 [-1, 1, 1, 1, 1, 1, 1,-1],
			 [-1,-1,-1,-1,-1,-1,-1,-1],
	]


	w = 70

	red = (230,50,50)
	blue = (0,0,255)
	x,y = 0,0

	done = False
	done1 = False
	face_of_robot = 0

	i = 1
	j = 1
	fitness = 1
	grid[i][j] = 2
	for move in chromosome:
		if (move == '0'):
			temp = "do nothing"
		elif (move == '1'):
			face_of_robot = (face_of_robot - 1) % 4
		elif (move == '2'):
			face_of_robot = (face_of_robot + 1) % 4
		else:

			if (face_of_robot == 0 and checkMove(i,j+1,grid)):
				j += 1
			elif (face_of_robot == 1 and checkMove(i+1,j,grid)):
				i += 1
			elif (face_of_robot == 2 and checkMove(i,j-1,grid)):
				j -= 1
			elif (face_of_robot == 3 and checkMove(i-1,j,grid)):
				i -= 1
			else:
				temp = 1


		if(grid[i][j] == 1):
			grid[i][j] = 2

	pygame.init()
	window = pygame.display.set_mode([550,600])
	window1 = pygame.display.set_mode([550,600])


	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()

		if done1 == False:
			for row in grid:
				for col in row:
					if col == -1:
						pygame.draw.rect(window,blue,(x,y,w,w))
					# elif col == 2:
					# 	time.sleep(1)
					# 	pygame.draw.rect(window,red,(x,y,w,w))
					# 	pygame.display.update()
					x = x + w
				y = y + w
				x = 0

		done1 = True
		pygame.display.update()

		x,y = 0,0
		if done == False:
			for row in grid:
				for col in row:
					if col == 2:
						time.sleep(0.5)
						pygame.draw.rect(window,red,(x,y,w,w))
						pygame.display.update()
					x = x + w
				y = y + w
				x = 0

		done = True
		pygame.display.update()





class IndiviualChromosome(object):
	def __init__(self,chromosome,fitness):
		self.chromosome = chromosome
		self.fitness = fitness


def crossOver(parent1,parent2):

	child = []
	for left, right in zip (parent1.chromosome,parent2.chromosome):

		prob = random.random()

		if prob < 0.6:
			child.append(left)

		elif prob < 0.9:
			child.append(right)
		else:
			child.append(random.choice(validMoves))

	return child

def crossover1(parent1,parent2):
	global trailSize

	pivot = random.randrange(trailSize)

	left = parent1.chromosome[0:pivot]
	right = parent1.chromosome[pivot:trailSize]

	left1 = parent2.chromosome[0:pivot]
	right1 = parent2.chromosome[pivot:trailSize]

	if(traverse_grid(left+right1) > traverse_grid(left1+ right)):
		return (left+right1)
	else:
		return(left1 + right)


def mutate(child):
	global validMoves,trailSize

	pivot = random.randrange(trailSize)
	child[pivot] = random.choice(validMoves)
	return child




def traverse_grid(chromosome):

	grid = [ [-1,-1,-1,-1,-1,-1,-1,-1],
			 [-1, 1, 1, 1, 1, 1, 1,-1],
			 [-1, 1, 0, 0, 0, 0, 1,-1],
			 [-1, 1, 0, 0, 0, 1,-1,-1],
			 [-1, 1, 0, 0, 0, 1,-1,-1],
			 [-1, 1, 0, 0, 0, 0, 1,-1],
			 [-1, 1, 1, 1, 1, 1, 1,-1],
			 [-1,-1,-1,-1,-1,-1,-1,-1],
	]

	face_of_robot = 0

	i = 1
	j = 1
	fitness = 1
	grid[i][j] = 0
	for move in chromosome:
		if (move == '0'):
			temp = "do nothing"
		elif (move == '1'):
			face_of_robot = (face_of_robot - 1) % 4
		elif (move == '2'):
			face_of_robot = (face_of_robot + 1) % 4
		else:

			if (face_of_robot == 0 and checkMove(i,j+1,grid)):
				j += 1
			elif (face_of_robot == 1 and checkMove(i+1,j,grid)):
				i += 1
			elif (face_of_robot == 2 and checkMove(i,j-1,grid)):
				j -= 1
			elif (face_of_robot == 3 and checkMove(i-1,j,grid)):
				i -= 1
			else:
				temp = 1


		if(grid[i][j] == 1):
			fitness += 1
			grid[i][j] = 0

	return fitness


def checkMove(i,j,grid):
	if(grid[i][j] == -1):
		return False
	else:
		return True

# def createPlot():
# 	global generationList,fitnessList,populationSize

# 	plt.plot(generationList,fitnessList, color = 'g')
# 	plt.title("Generation VS Fitness\n Population: " + str(populationSize) )
# 	plt.xlabel("No. of Generations")
# 	plt.ylabel("Fitness")
# 	plt.show()

def main():
	global populationSize,targetFitness,generationList,fitnessList

	counter = 0
	generation = 1

	terminatingCondition = False
	population = []

	for _ in range(populationSize):
		chromosome = [random.choice(validMoves) for _ in range(trailSize)]
		fitness = traverse_grid(chromosome)
		population.append(IndiviualChromosome(chromosome,fitness))

	while (terminatingCondition != True and generation < generationBound):
#
		population.sort(key = lambda x:x.fitness,reverse = True)

		generationList.append(generation)
		fitnessList.append(population[0].fitness)

		if(population[0].fitness == targetFitness):
			terminatingCondition = True
			break


		mating_pool = []

		n = int((10*populationSize)/100)
		for x in range(n):
			# parent1 = random.choice(population[:10])
			# parent2 = random.choice(population[:10])
			# child = (crossOver(parent1,parent2))
			# mating_pool.append(IndiviualChromosome(child,traverse_grid(child)))
			mating_pool.append(population[x])
			

		n = int((90*populationSize)/100)
		for _ in range(n):
			parent1 = random.choice(population[:50])
			parent2 = random.choice(population[:50])
			child = mutate(crossover1(parent1,parent2))
			child = mutate(child)
			child = mutate(child)
			childFitness = traverse_grid(child)
			mating_pool.append(IndiviualChromosome(child,childFitness))

		



		population = mating_pool
		print("Generation: " + str(generation) + " Chromosome: " + 
			"".join(population[0].chromosome) + " Fitness: " + 
				str(population[0].fitness))

		generation += 1

	print("Generation: " + str(generation) + " Chromosome: " + 
			"".join(population[0].chromosome) + " Fitness: " + 
				str(population[0].fitness))

	
	# createPlot()
	print("\n\n----------------------------------------------------")
	print("-------------- OPTIMAL SOLUTION --------------------\n\n")
	print("Optimal Chromosome -> " + "".join(population[0].chromosome))
	print("Optimal Fitness -> " + str(population[0].fitness))
	print("Blue colour represent the wall")
	print("Red colour represent the optimal movement of robot")
	drawOptimalOnScreen(population[0].chromosome)

if __name__ == '__main__':
	main()



# Took bit guidance from internet plus friends!
















