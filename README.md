# DroneBlocksTelloSimulator

Welcome to the DroneBlocks Tello Simulator with Python. If you are looking for the JavaScript version you can check it out here.

The wonderful thing about this library is you can interact with a simulated Tello drone and take the same code and run it with a real Tello drone.

The first thing we recommend you do is set up a virtual environment for your project. This isn't a necessity but it helps keep your project clean.

```
python3 -m venv venv
```

or on some systems you may need to use the following:

```
python -m venv venv
```
Now that your virtual environment is up and running go ahead and activate it from the root of the project directory.

```
source venv/bin/activate
```
on Windows:
```
.\venv\Scripts\activate
```
Now install the DroneBlocksTelloSimulator Python package:

```
pip install DroneBlocksTelloSimulator
```
Installation is done! Now you need to create your first mission with the DroneBlocks Simulator. You can access the simulator at the link below:

[DroneBlocks Simulator Link](http://db-simulator-dev.web.app/)

You will need configure Chrome to "Allow Insecure Content" for the simulator. **This is not a security risk and will only be done for this domain.** This will allow the DroneBlocks simulator to receive commands from Python. Follow these steps:

1. Click on the lock icon next to the web address
2. Click on "Site settings"
3. Scroll to the bottom and look for "Insecure content"
4. Change "Block" to "Allow"
5. Close the tab and refresh the simulator

You can now move onto programming your first simulated drone mission in Python! Click the button in the top left of the DroneBlocks simulator that says "Get Drone Simulator Key". Copy this unique key to your clipboard as it will be used in your mission code below.

Create a simulated mission using the following code:

```
import asyncio
from DroneBlocksTelloSimulator import SimulatedDrone

async def mission():
    drone = SimulatedDrone('YOUR-SIMULATED-DRONE-KEY-GOES-HERE')
    await drone.connect()
    await drone.takeoff()
    await drone.fly_forward(100, 'in')
    await drone.fly_left(100, 'in')
    await drone.fly_backward(100, 'in')
    await drone.fly_right(100, 'in')
    await drone.flip_backward()
    await drone.land()

asyncio.run(mission())
```

Congrats on your first simulated mission! Now let's run the exact same code on a real Tello. We're assuming you know how to connect to Tello from your computer so go ahead and do that.

Once connected you'll run the exact same code above with two small difference. We're using a different import and constructor necessary to interface with the Tello drone.

```
import asyncio
from DroneBlocksTelloSimulator import Tello

async def mission():
    drone = Tello()
    await drone.connect()
    await drone.takeoff()
    await drone.fly_forward(100, 'in')
    await drone.fly_left(100, 'in')
    await drone.fly_backward(100, 'in')
    await drone.fly_right(100, 'in')
    await drone.flip_backward()
    await drone.land()

asyncio.run(mission())
```
Ta-da! Now you've run the same code in both the DroneBlocks simulator and on Tello! Let's take a look at all the commands available to both the Simulator and Tello:

```
drone.takeoff()
drone.fly_forward(20, 'in')
drone.fly_backward(20, 'in')
drone.fly_left(20, 'in')
drone.fly_right(20, 'in')
drone.fly_up(20, 'in')
drone.fly_down(20, 'in')
drone.fly_to_xyz(10, 20, 30, 'in')
drone.fly_curve(25, 25, 0, 0, 50, 0, 'in')
drone.flip_forward()
drone.flip_backward()
drone.flip_left()
drone.flip_right()
drone.land()
```
Give it a try and let us know what you think! If you run into any issues please open a [bug here](https://github.com/dbaldwin/DroneBlocks-Tello-Simulator-With-Python/issues).