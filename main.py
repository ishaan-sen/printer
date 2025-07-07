from time import sleep  # I'm sorry
import pickle

import cv2
import numpy as np
import matplotlib.pyplot as plt

from printer import move_gantry, set_abs_pos

cap = cv2.VideoCapture(0)


# for i in range(1000):
#     ret, frame = cap.read()
#     frame = frame[300:600, 300:600]
#     cv2.imshow("asdfg", frame)
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break




print(set_abs_pos())

# exit()
images = []
for x in np.linspace(90, 130, 160):
    images.append([])
    print("x=", x)
    print(move_gantry(x, 120))
    sleep(1)
    print(move_gantry(x, 80, f=5*60))
    # sleep(0.1)
    print("recording")
    for i in range(200): # idk how long this'll take
        ret, frame = cap.read()
        
        frame = frame[300:600, 300:600]
        
        frame = cv2.resize(frame, dsize=(100, 100), interpolation=cv2.INTER_CUBIC)
        images[-1].append((ret, frame))
        cv2.imshow("asdfg", frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    print("done")

cap.release()

# for seq in images:
#     for ret, frame in seq:
#         plt.imshow(frame)
#         plt.show()

file = open('asdfg', 'wb')

pickle.dump(images, file)

file.close()

