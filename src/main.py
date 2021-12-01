import asyncio
from DroneBlocksTelloSimulator import SimulatedDrone
from DroneBlocksTelloSimulator import Tello

# Define a drone mission to be executed by the simulator and then a real Tello drone
async def drone_mission():
    #drone = SimulatedDrone('64393f5f-e901-4b5e-a65a-69fe392b8e53')
    drone = Tello()

    # Tello only 
    # batt = drone.query_battery()
    # print('Battery is {}'.format(batt))

    # Connect to the drone
    await drone.connect()

    # Takeoff
    await drone.takeoff()

    # # Go fast
    # await drone.set_speed(100)

    # # Box pattern
    # await drone.fly_forward(30, 'in')
    # await drone.fly_left(30, 'in')
    # await drone.fly_backward(30, 'in')
    # await drone.fly_right(30, 'in')

    # # Slow down
    # await drone.set_speed(30)
    
    # # Fly up and down
    # await drone.fly_up(30, 'cm')
    # await drone.fly_down(30, 'cm')
    
    # Fly 3D coordinates from current position
    #await drone.fly_to_xyz(20, 20, 20, 'in')

    # Fly curve on x/y plane
    #await drone.fly_curve(25, 25, 0, 0, 25, 0, 'in')

    # Do some flips
    await drone.flip_forward()
    await drone.flip_backward()
    await drone.flip_left()
    await drone.flip_right()

    # Yaw right and left
    await drone.yaw_right(90)
    await drone.yaw_left(180)

    # Land
    await drone.land()

# Run the drone mission and wait for each command to complete before starting the next
asyncio.run(drone_mission())