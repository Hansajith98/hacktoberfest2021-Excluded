# Colored Hexagons Turtle Design
// We will be learning about a very cool Colored Hexagons Turtle Design in Python.

# First Part:

 In the first part of this Colored Hexagons Turtle Design code, import the turtle module and the random module. The random module will be used to generate a random number and we will be drawing pentagons in the same pattern of color which we will be discussing below. Then, let the variable “x” be 20 and the variable “muller” also be 20. Now, set the speed to 100 and color mode to 255.


# Second Part with Functions:

 Create a function move() with the parameters l and a. In the the function we will be moving the turtle right at an angle of a and moving the turtle forward at a value of l with the code above. Similarly, We will also be creating a function hex(). In this function, first we will be call the pendown() function and setting the color from (radinint(0, 255), randint(0, 255), randint(0, 255)). Likewise, we will be calling the function begin_fill() and create a for loop with the range of 6. In this for loop, we will move from (x, -60). Lastly, we will call the end_fill() function and the penup() function.


# Last Part with a large Loop:

 Accordingly, we will be creating a for loop with the range of the value of the “muller” variable. Then, create an if statement which will run if “max” is equal to 0. Similarly, call the hex() function and move in the (x, -60) pattern three times and lastly move in (0, 180). Coming out of the if statement, create a for loop with the range of 6 and move (0, 60). moreover, we will be creating another for loop with the range of (max + 1). In this nested loop, call the hex() function and move (x, -60) and (x, 60) respectively. Coming out of two for loops, write the following code.

move(-x,60)
move(x,-120)
move(0,60)


# Ending the code:

 Lastly, call the exitonclick() function and end the code.
