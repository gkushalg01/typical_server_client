import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import socket

HOST = '192.168.0.106' 
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    print("Receiving coordinates: ")
    
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)  # adjust limits as necessary
    ax.set_ylim(0, 10)  # adjust limits as necessary
    lines = [ax.plot([], [], 'o')[0] for _ in range(6)]
    # plt.show(block=False)
    
    def plotter(i):
        try:
            # Receive and plot data in real-time
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                coords = np.frombuffer(data, dtype=np.float64).reshape((-1, 2))
                print("[", end=" ")
                for i in range(6):
                    print("(", str(coords[i, 0]), " ,", str(coords[i, 1]), ")", end=" ")
                    plt.scatter(coords[i, 0], coords[i, 1])
                print("]")
                fig.canvas.draw()
                fig.canvas.flush_events()

        except KeyboardInterrupt:
            print("Exiting...")

    ani = FuncAnimation(fig, plotter, interval=10)
    plt.show()
