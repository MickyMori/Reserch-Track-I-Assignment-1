Research Track I First Assignment
=================================

The assignment is based on a portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
In the assignment the robot is placed in an enviroment with six silver and six golden markers. The scope of the assignment was to write python code to make the robot pair each silver marker with a golden one.

Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

To run the program use the command:

```bash
$ python run.py assignment.py
```

Flowchart
---------

This is a flowchart that summarizes the key points of the program. The rectangular blocks rappresent the actions while the rhombuses rappresent the decisions. The image below, if clicked, will open the web page of the flowchart so that it can be viewed bigger and with higher resolution. 

[![Flowchart](/Images/flowchart.png "Flowchart")](https://cloud.smartdraw.com/share.aspx/?pubDocShare=94744E9FF2B39A0C7DEE78BF27810A626DA)

Possible improvements
---------------------

In this section will be desceibed some possible future improvements of the code. 
Sometimes when the robot is moving towards the next marker it hits and drag aroung another one that is in the way, so it could be added a piece of code that detects possible osbstacles on the path of the robot and that make so that it can avoid them.
When the robot is looking for the next marker it goes for the first one it sees, it would be better if it looked for the closer one so that it would save time.
The main body of the program is made of a while loop that calls the differnt functions that descript the behavior of the robot. The program breaks out of the loop, and thus ends, when the size of the list of the golden markers that have already been used is equal to six. The problem with this is that it works only when there are six of them. To make so that the program will work in an enviroment of any number of pairs of golden and silver markers it could be calculated the time that the robot takes to turn around with a given speed so that it can make a 360 degerees turn and if it doesn't see any unused silver markers the program ends.
 
