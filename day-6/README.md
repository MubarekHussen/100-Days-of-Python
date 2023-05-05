# Hurdles race
![Screenshot from 2023-05-05 18-44-05](https://user-images.githubusercontent.com/96715809/236520846-f63ada72-4107-4320-9d51-f663b555eb6f.png)
Reeborg has entered a hurdles race. Make him run the course, following the path shown.
### What you need to know
- The functions move() and turn_left().
Difficulty level

### More advanced
You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.

Difficulty level

### [visit](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
## To pass the challenge put the following code to the python code section and run it.

- def turn_right():
   - turn_left()
   - turn_left()
   - turn_left()
- def jump():
   - move()
   - turn_left()
   - move()
   - turn_right()
   - move()
   - turn_right()
   - move()
   - turn_left()
- for i in range(0,6):
   - jump()
