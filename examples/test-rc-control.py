from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
import time
if __name__ == '__main__':
    sim_key = '4cca2720-5b26-4e90-bcdd-7662950960b4'
    # sim_key = None
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.send_rc_control(0,0,50, 0)
        time.sleep(3)
        drone.send_rc_control(0,0,0,0)
        drone.land()


