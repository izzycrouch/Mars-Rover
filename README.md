# Mars-Rover

## Overview
 Rovers navigate the surface of Mars by following a sequence of commands. They can also use their cameras and robot arms to collect photographs and samples.

## Mars
 The surface of Mars is represented by a Plateau. For the purpose of this task, the Plateau is divided into a square/rectangular grid.

## The Rover Position
 A rover's position on the Plateau will be represented by x and y co-ordinates and the letters N, S, W, E which will represent the direction the rover is facing (North, South, West and East respectively).\
 For example: 4 2 E\
 This means the x co-ordinate is 4, the y co-ordinate is 2 and the rover is facing east.

## Program Inputs
    
### 1. Plateau Creation
 First define the size of the plateau.\
 e.g. 5 5 - this plateau would have maximum (x,y) co-ordinates of (5,5) and therefore has 6 possible x and y values (0 - 5 for each).\
 It is assumed that the lower left co-ordinate is (0,0)
    
### 2. Rover Creation 
 The Rover receives two lines of input.
 ```
 Line 1 - lands the Rover at a particular starting position. e.g. 1 2 N lands the Rover at position (1,2) facing North.
 Line 2 - a string input representing instructions to move the Rover around the Plateau.
 ```

## Instructions
The Rover can only be moved around the Plateau by a string of letters send to it.
```
 L -    Spins the Rover 90 degrees Left without moving from the current coordinate point.
 R -  	Spins the Rover 90 degrees Right without moving from the current coordinate point.
 M -    Moves the Rover forward by one grid point, maintaining the same heading/orientation.
```
All other letters are invalid.