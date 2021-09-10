import numpy as np

class KF:
    
    def __init__(self, initial_x: float, 
                       initial_v: float,
                       accel_variance: float) -> None:
        
        self._x = np.array([initial_x, initial_v])
        self._accel_variance = accel_variance
        self._P = np.eye(2)

    def prediction(self, dt: float):
        F = np.array([[1, dt], [0,1]])
        G = np.array([.5 * dt**2, dt]).reshape((2,1))

        new_x = F.dot(self._x)
        new_P = F.dot(self._P).dot(F.T) + G.dot(G.T) * self._accel_variance
        self._x = new_x
        self._P = new_P

    def update(self, means: float, measures: float):
        z = np.array([means])
        R = np.array([measures])
        H = np.array([1, 0]).reshape(1,2)
        y = z - H.dot(self._x)
        S = H.dot(self._P).dot(H.T) + R
        K = self._P.dot(H.T).dot(np.linalg.inv(S))

        new_x = self._x + K.dot(y)
        I = np.eye(2)
        new_P = (I - K.dot(H)).dot(self._P)
        self._x = new_x
        self._P = new_P


    @property
    def getCovar(self):
        return self._P

    @property
    def getMean(self):
        return self._x

    @property
    def getPos(self) -> float:
        return self._x[0]

    @property
    def getVel(self) -> float:
        return self._x[1]
