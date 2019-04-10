# stick-creatures-climbers

Simulates evolution of a population of virtual stick creatures.  
They learn to climb using a genetic algorithm / evolutionary algorithm.  
Uses pygame for graphics.

Each stick creature consists of the following:

  - A given number of segments that independently swing back and forth.
  - A head, represented by a larger green dot. 
  - A tail end, represented by a smaller green dot.
  - A white halo that appears around the head of the 'winner'.

In this scheme, 'breeding' occurs at static intervals.  Whichever
creature has come closest to the top of the screen is the winner, or stud.
The winner then breeds with the rest of the population.

Breeding consists of averaging out the rotation and rotation rates of each 
segment of each creature with the stud.  In addition there is a chance to 
mutate the rotation rate by a small amount.

Anthony Boratino 2013-1019


