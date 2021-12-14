import paho.mqtt.client as mqtt
import asyncio
import uuid


class SimulatedDrone:

    def __init__(self, simulator_key):
        self.client = mqtt.Client()
        self.client.connect("159.65.187.41", 9999)
        self.simulator_key = simulator_key
        self.current_command_uuid = ""
        self.completed_command_uuid = ""
        self.command_in_progress = False

        # Listen for responses from simulator
        self.client.on_message = self.on_message

        # Necessary so on_message runs in a separate thread
        self.client.loop_start()

        # Handles response back from drone
        self.client.subscribe("/command_response/" + self.simulator_key)

    def on_message(self, client, data, message):
        self.completed_command_uuid = str(message.payload.decode("utf-8"))
        print("current command is: " + self.current_command_uuid)
        print("completed command is: " + self.completed_command_uuid)
        if self.current_command_uuid == self.completed_command_uuid:
            self.command_in_progress = False

    def connect(self):
        async def _connect():
            return

        return asyncio.run(_connect())

    def takeoff(self):
        async def _takeoff():
            await self.send_command("takeoff")

        return asyncio.run(_takeoff())

    def set_speed(self, speed):
        async def _set_speed(_speed):
            await self.send_command("speed," + str(speed) + ",cm/s")

        return asyncio.run(_set_speed(speed))

    def fly_forward(self, distance, units):
        async def _fly_forward(_distance, _units):
            await self.send_command("fly_forward," + str(_distance) + "," + _units)

        return asyncio.run(_fly_forward(distance, units))

    def fly_backward(self, distance, units):
        async def _fly_backwards(_distance, _units):
            await self.send_command("fly_backward," + str(_distance) + "," + _units)

        return asyncio.run(_fly_backwards(distance, units))

    def fly_left(self, distance, units):
        async def _fly_left(_distance, _units):
            await self.send_command("fly_left," + str(_distance) + "," + _units)

        return asyncio.run(_fly_left(distance, units))

    def fly_right(self, distance, units):
        async def _fly_right(_distance, _units):
            await self.send_command("fly_right," + str(_distance) + "," + _units)

        return asyncio.run(_fly_right(distance, units))

    def fly_up(self, distance, units):
        async def _fly_up(_distance, _units):
            await self.send_command("fly_up," + str(_distance) + "," + _units)

        return asyncio.run(_fly_up(distance, units))

    def fly_down(self, distance, units):
        async def _fly_down(_distance, _units):
            await self.send_command("fly_down," + str(_distance) + "," + _units)

        return asyncio.run(_fly_down(distance, units))

    def fly_to_xyz(self, x, y, z, units):
        async def _fly_to_xyz(_x, _y, _z, _units):
            await self.send_command("fly_xyz," + str(_x) + "," + str(_y) + "," + str(_z) + "," + _units)

        return asyncio.run(_fly_to_xyz(x, y, z, units))

    def fly_curve(self, x1, y1, z1, x2, y2, z2, units):
        async def _fly_curve(_x1, _y1, _z1, _x2, _y2, _z2, _units):
            await self.send_command(
                "curve," + str(_x1) + "," + str(_y1) + "," + str(_z1) + "," + str(_x2) + "," + str(_y2) + "," + str(
                    _z2) + "," + _units)

        return asyncio.run(_fly_curve(x1, y1, z1, x2, y2, z2, units))

    def flip_left(self):
        async def _flip_left():
            await self.send_command("flip_left")

        return asyncio.run(_flip_left())

    def flip_right(self):
        async def _flip_right():
            await self.send_command("flip_right")

        return asyncio.run(_flip_right())

    def flip_forward(self):
        async def _flip_forward():
            await self.send_command("flip_forward")

        return asyncio.run(_flip_forward())

    def flip_backward(self):
        async def _flip_backward():
            await self.send_command("flip_backward")

        return asyncio.run(_flip_backward())

    def yaw_right(self, degrees):
        async def _yaw_right(_degrees):
            await self.send_command("yaw_right," + str(_degrees))

        return asyncio.run(_yaw_right(degrees))

    def yaw_left(self, degrees):
        async def _yaw_left(_degrees):
            await self.send_command("yaw_left," + str(_degrees))

        return asyncio.run(_yaw_left(degrees))

    def land(self):
        async def _land():
            await self.send_command("land")

        return asyncio.run(_land())

    async def send_command(self, command):
        self.command_in_progress = True
        self.current_command_uuid = str(uuid.uuid4())
        self.current_command = command + "," + self.current_command_uuid
        print("publishing command: " + self.current_command)
        self.client.publish("/command/" + self.simulator_key, self.current_command)

        while True:
            if self.command_in_progress == False:
                return

    def disconnect(self):
        self.client.disconnect()
