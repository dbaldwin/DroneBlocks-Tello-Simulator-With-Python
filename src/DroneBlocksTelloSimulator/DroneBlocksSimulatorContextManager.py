from DroneBlocksTelloSimulator import SimulatedDrone
from DroneBlocksTelloSimulator import Tello
import logging

class DroneBlocksSimulatorContextManager():
    """
    DroneBlocksSimulatorContextManager

    Class is used simplify using the DroneBlocks python simulator and running python code outside the simulator.
    """

    def __init__(self, simulator_key=None, log_level=logging.ERROR):
        """
        :param simulator_key: Default: None.  The simulator key from the DroneBlocks simulator and is used to
                              communicate with the simulator.  If not present, then the Tello class is used to
                              communicate with an actual Tello drone

        :param log_level: Default: ERROR Set
        """
        self.db_tello = None
        self.log_level = log_level
        self.simulator_key = simulator_key

    def __enter__(self):
        if self.simulator_key:
            self.db_tello = SimulatedDrone(self.simulator_key)
        else:
            self.db_tello = Tello()
            self.db_tello.LOGGER.setLevel(self.log_level)

            self.db_tello.connect()

        return self.db_tello

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Exception Type: {exc_type}")
        if exc_val:
            print(f"Exception Value: {exc_val}")

        if exc_tb:
            print(f"Exception Traceback: {exc_tb}")

        # if we are not running in the simulator, issue an 'end' command to
        # land and gracefully stop the Tello
        if self.simulator_key is None:
            self.db_tello.end()

