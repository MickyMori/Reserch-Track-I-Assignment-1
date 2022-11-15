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

Robot API
---------

The API for controlling a simulated robot is designed to be as similar as possible to the [SR API][sr-api].

### Motors ###

The simulated robot has two motors configured for skid steering, connected to a two-output [Motor Board](https://studentrobotics.org/docs/kit/motor_board). The left motor is connected to output `0` and the right motor to output `1`.

The Motor Board API is identical to [that of the SR API](https://studentrobotics.org/docs/programming/sr/motors/), except that motor boards cannot be addressed by serial number. So, to turn on the spot at one quarter of full power, one might write the following:

```python
R.motors[0].m0.power = 25
R.motors[0].m1.power = -25
```

### The Grabber ###

The robot is equipped with a grabber, capable of picking up a token which is in front of the robot and within 0.4 metres of the robot's centre. To pick up a token, call the `R.grab` method:

```python
success = R.grab()
```

The `R.grab` function returns `True` if a token was successfully picked up, or `False` otherwise. If the robot is already holding a token, it will throw an `AlreadyHoldingSomethingException`.

To drop the token, call the `R.release` method.

Cable-tie flails are not implemented.

### Vision ###

To help the robot find tokens and navigate, each token has markers stuck to it, as does each wall. The `R.see` method returns a list of all the markers the robot can see, as `Marker` objects. The robot can only see markers which it is facing towards.

Each `Marker` object has the following attributes:

* `info`: a `MarkerInfo` object describing the marker itself. Has the following attributes:
  * `code`: the numeric code of the marker.
  * `marker_type`: the type of object the marker is attached to (either `MARKER_TOKEN_GOLD`, `MARKER_TOKEN_SILVER` or `MARKER_ARENA`).
  * `offset`: offset of the numeric code of the marker from the lowest numbered marker of its type. For example, token number 3 has the code 43, but offset 3.
  * `size`: the size that the marker would be in the real game, for compatibility with the SR API.
* `centre`: the location of the marker in polar coordinates, as a `PolarCoord` object. Has the following attributes:
  * `length`: the distance from the centre of the robot to the object (in metres).
  * `rot_y`: rotation about the Y axis in degrees.
* `dist`: an alias for `centre.length`
* `res`: the value of the `res` parameter of `R.see`, for compatibility with the SR API.
* `rot_y`: an alias for `centre.rot_y`
* `timestamp`: the time at which the marker was seen (when `R.see` was called).


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
 
