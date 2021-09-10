from kf import KF
import numpy as np
import unittest

class TestStringMethods(unittest.TestCase):

    def test_can_construct_with_x_and_v(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x, initial_v=v, accel_variance=1.2)
        self.assertAlmostEqual(kf.getPos, x)
        self.assertAlmostEqual(kf.getVel, v)

    def test_can_predict_rightShape(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x, initial_v=v, accel_variance=1.2)
        kf.prediction(dt=0.1)

        self.assertAlmostEqual(kf.getCovar.shape, (2,2))
        self.assertAlmostEqual(kf.getMean.shape, (2,))

    def test_can_predict_state_uncertainty(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x, initial_v=v, accel_variance=1.2)

        for i in range(10):
            det_before = np.linalg.det(kf.getCovar)
            kf.prediction(dt=0.1)
            det_after = np.linalg.det(kf.getCovar)
            self.assertGreater(det_after, det_before)
            print(det_before, det_after)

    def test_can_update_state_uncertainty(self):
        x = 0.2
        v = 2.3
        kf = KF(initial_x=x, initial_v=v, accel_variance=1.2)

        det_before = np.linalg.det(kf.getCovar)
        kf.update(0.1, 0.01)
        det_after = np.linalg.det(kf.getCovar)
        self.assertLess(det_after, det_before)