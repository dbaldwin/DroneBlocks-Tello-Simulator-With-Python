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

    async def connect(self):
        return
        
    async def takeoff(self):
        await self.send_command("takeoff")

    async def set_speed(self, speed):
        await self.send_command("speed," + str(speed) + ",cm/s")

    async def fly_forward(self, distance, units):
        await self.send_command("fly_forward," + str(distance) + "," + units)

    async def fly_backward(self, distance, units):
        await self.send_command("fly_backward," + str(distance) + "," + units)

    async def fly_left(self, distance, units):
        await self.send_command("fly_left," + str(distance) + "," + units)

    async def fly_right(self, distance, units):
        await self.send_command("fly_right," + str(distance) + "," + units)
    
    async def fly_up(self, distance, units):
        await self.send_command("fly_up," + str(distance) + "," + units)

    async def fly_down(self, distance, units):
        await self.send_command("fly_down," + str(distance) + "," + units)

    async def fly_to_xyz(self, x, y, z, units):
        await self.send_command("fly_xyz," + str(x) + "," + str(y) + "," + str(z) + "," + units)

    async def fly_curve(self, x1, y1, z1, x2, y2, z2, units):
        await self.send_command("curve," + str(x1) + "," + str(y1) + "," + str(z1) + ","  + str(x2) + "," + str(y2) + "," + str(z2) + "," + units)

    async def flip_left(self):
        await self.send_command("flip_left")

    async def flip_right(self):
        await self.send_command("flip_right")

    async def flip_forward(self):
        await self.send_command("flip_forward")

    async def flip_backward(self):
        await self.send_command("flip_backward")

    async def yaw_right(self, degrees):
        await self.send_command("yaw_right," + str(degrees))

    async def yaw_left(self, degrees):
        await self.send_command("yaw_left," + str(degrees))

    async def land(self):
        await self.send_command("land")

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