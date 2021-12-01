# DroneBlocks-Python-Simulator

```
pip install -i https://test.pypi.org/simple/ DroneBlocksTelloSimulator
```

```
import asyncio
from DroneBlocksTelloSimulator import SimulatedDrone

async def main():
    drone = SimulatedDrone('a5f921f4-f2f0-446d-b216-1a4e34ab4fa0')
    await drone.connect()
    await drone.takeoff()
    await drone.land()

asyncio.run(main())
```