import numpy as np
import matplotlib.pyplot as plt
import random

def sir_model():
    beta = 0.0002
    delta = 0.0002
    alpha = 0.001
    f = 0.000005
    S = [500]
    I = [25]
    R = [0]
    t = [0]
    while t[-1] <= 200000:
        birth = beta * (S[-1] + I[-1] + R[-1])
        infection = f * S[-1] * I[-1]
        s_dies = delta * S[-1]
        recover = alpha * I[-1]
        i_dies = delta * I[-1]
        r_dies = delta * R[-1]
        time_to_event = []
        events = [[birth, S[-1] + 1, I[-1], R[-1]], [infection, S[-1] - 1, I[-1] + 1, R[-1]],
                  [s_dies, S[-1]-1, I[-1], R[-1]], [recover, S[-1], I[-1] - 1, R[-1] + 1],
                  [i_dies, S[-1], I[-1] - 1, R[-1]], [r_dies, S[-1], I[-1], R[-1] - 1]]
        for i in range(6):
            if events[i][0] != 0:
                time_to_event.append(-np.log(random.random())/events[i][0])
            else:
                time_to_event.append(99999999999999)
        min_time = 0
        for j in range(len(time_to_event)):
            if time_to_event[j]<time_to_event[min_time]:
                min_time = j
        S.append(events[min_time][1])
        I.append(events[min_time][2])
        R.append(events[min_time][3])
        t.append(t[-1]+time_to_event[min_time])
    plt.figure()
    plt.plot(t,S, label = 'S')
    plt.plot(t, I, label='I')
    plt.plot(t, R, label='R')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    sir_model()