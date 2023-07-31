import numpy as np
import matplotlib.pyplot as plt
import socket

HOST = '192.168.0.106' 
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    
    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)  # adjust limits as necessary
    ax.set_ylim(0, 10)  # adjust limits as necessary
    lines = [ax.plot([], [], 'o')[0] for _ in range(6)]
    # plt.show(block=False)
    
    try:
        # Receive and plot data in real-time
        while True:
            data = conn.recv(1024)
            if not data:
                break
            coords = np.frombuffer(data, dtype=np.float64).reshape((-1, 2))
            for i in range(6):
                plt.scatter(coords[i, 0], coords[i, 1])
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.show()
            
    except KeyboardInterrupt:
        print("Exiting...")
