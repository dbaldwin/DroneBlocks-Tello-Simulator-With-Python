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

[DroneBlocks Simulator Link](http://coding-sim.droneblocks.io/)

You will need configure Chrome to "Allow Insecure Content" for the simulator. **This is not a security risk and will only be done for this domain.** This will allow the DroneBlocks simulator to receive commands from Python. Follow these steps:

1. Click on the lock icon next to the web address
2. Click on "Site settings"
3. Scroll to the bottom and look for "Insecure content"
4. Change "Block" to "Allow"
5. Close the tab and refresh the simulator

You can now move onto programming your first simulated drone mission in Python! Click the button in the top left of the DroneBlocks simulator that says "Get Drone Simulator Key". Copy this unique key to your clipboard as it will be used in your mission code below.

Create a simulated mission using the following code:

```
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = 'YOUR_SIM_KEY_GOES_HERE'
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_forward(distance, 'in')
        drone.fly_left(distance, 'in')
        drone.fly_backward(distance, 'in')
        drone.fly_right(distance, 'in')
        drone.flip_backward()
        drone.land()
```

Congrats on your first simulated mission! Now let's run the exact same code on a real Tello. We're assuming you know how to connect to Tello from your computer so go ahead and do that.

Once connected you'll run the exact same code above with one small difference. We've changed the sim_key to **None** and Python now knows to send the same commands to your real Tello, Tello EDU, or Tello Talent!

```
from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = None
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_forward(distance, 'in')
        drone.fly_left(distance, 'in')
        drone.fly_backward(distance, 'in')
        drone.fly_right(distance, 'in')
        drone.flip_backward()
        drone.land()
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