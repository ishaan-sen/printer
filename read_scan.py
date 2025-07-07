import pickle
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
from scipy.signal import convolve2d


file = open(argv[2], 'rb')
images = pickle.load(file)
file.close()

frames = []

for seq in images:
    for ret, frame in seq:
        # frames.append(frame.dot(np.array([1, 1, 1]) / 3))
        frames.append(frame[:,:,2])



# print(frames[0].shape)
# for frame in frames:
#     frame = np.convolve(frame, np.ones((5, 5))/25)

maxes = [np.max(frame) for frame in frames]


z = int(argv[1])
# z = 20

out = np.array(maxes)[:z * (len(maxes) // z)].reshape(z, -1)

sharp = np.array([
                     [0, -1, 0],
                     [-1, 5, -1],
                     [0, -1, 0],
                 ])


out = convolve2d(out, sharp)
print(out.shape)
plt.imshow(out[2:-2, ::-1])
plt.show()




