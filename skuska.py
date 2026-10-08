import pybullet as p
import time
import pybullet_data

# 1. Connect to the physics engine using the GUI
physicsClient = p.connect(p.GUI)

# 2. Set the path to built-in models
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 3. Apply gravity
p.setGravity(0, 0, -10)

# 4. Load a floor and an R2D2 robot
planeId = p.loadURDF("plane.urdf")
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
robotId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# 5. Run the simulation
for i in range(2400): # 10 seconds at 240Hz
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()