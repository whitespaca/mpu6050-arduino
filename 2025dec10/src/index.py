import serial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

PORT = 'COM8'
BAUD = 115200

ser = serial.Serial(PORT, BAUD)

plt.ion()
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# 초기 설정
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

point, = ax.plot([0], [0], [0], 'bo', markersize=10)

def scale(val):
    return max(min(val / 2000.0, 10), -10)

while True:
    try:
        if ser.in_waiting:
            line = ser.readline().decode().strip()
            parts = line.split(",")

            if len(parts) == 3:
                ax_val = scale(int(parts[0]))
                ay_val = scale(int(parts[1]))
                az_val = scale(int(parts[2]))

                point.set_data([ax_val], [ay_val])
                point.set_3d_properties([az_val])

                plt.draw()
                plt.pause(0.01)

    except Exception as e:
        print("Error:", e)