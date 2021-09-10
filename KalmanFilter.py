import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import real

from kf import KF

plt.ion()
plt.figure()

kf = KF(0, 1.0, 0.1)


DT = .1
NUM_STEPS = 1000
MEAS_STEPS = 20 

means = []
covars = []
real_xs = []
real_vs = []

real_x = 0.0
real_v = 0.9
meas_variance = 0.1 ** 2

for step in range(NUM_STEPS):

    covars.append(kf.getCovar)
    means.append(kf.getMean)

    real_x = real_x + DT * real_v

    kf.prediction(DT)

    if step != 0 and step %  MEAS_STEPS == 0:
        kf.update(real_x + np.random.randn() * np.sqrt(meas_variance), meas_variance)

    real_xs.append(real_x)
    real_vs.append(real_v)

plt.subplot(2, 1, 1)
plt.title('Position')
plt.plot([mean[0] for mean in means], 'r')
plt.plot(real_xs, 'b')
plt.plot([mean[0] - 2* np.sqrt(cov[0,0]) for mean, cov in zip(means, covars)], 'r--')
plt.plot([mean[0] + 2* np.sqrt(cov[0,0]) for mean, cov in zip(means, covars)], 'r--')


plt.subplot(2, 1, 2)
plt.title('Velocity')
plt.plot([mean[1] for mean in means], 'r')
plt.plot(real_vs, 'b')
plt.plot([mean[1] - 2* np.sqrt(cov[1,1]) for mean, cov in zip(means, covars)], 'r--')
plt.plot([mean[1] + 2* np.sqrt(cov[1,1]) for mean, cov in zip(means, covars)], 'r--')

plt.show()
plt.ginput(1)