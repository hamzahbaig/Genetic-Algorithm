# Genetic-Algorithm-
## Genetic algorithm has following steps:
• Initialization
• Selection
• Cross Over
• Mutation
• Stop if terminating condition meet
## Approach to the Wall following problem
In order to solve the wall following problem, I took the following steps:
  1) First of all, I generated a random string of 0,1,2 and 3 which shows the following
        movement:
        0 -> Do nothing
        1 -> Left Rotation
        2 -> Right Rotation
        3 -> Forward Movement
        
  2) Then I use this random string to traverse the grid and it returns the fitness of the random
generated string.

  3) Then I took the same approach and applied it on the population of
(50,100,200,500,700,100 -> graph attached below) and note the results.

  4) And save that population fitness in a class variable, and I sort it in descending order so
that the highest fitness chromosome and fitness value is at the index 0 of the array.

  5) Now create a new list, which would be the new generation.
  
  6) Now I took 10 percent of fittest population into the next generation and 90 percent of the
population I give to crossover function which will give me off springs. And I calculate
the fitness of new population

  7) Now I declare them as my new population and sort them again, So I get the highest
fitness chromosome at the top.

  8) I keep repeating this for either some generation Bound, or when it reaches the maximum
fitness which is 20 in this problem
