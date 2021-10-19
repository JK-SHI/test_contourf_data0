import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(-1, 1, 21)
    y = np.linspace(-1, 1, 21)
    x, y = np.meshgrid(x, y)
    z0 = x * x + y * y

    for i in range(1, 5):
        for j in range(1, 5):
            z0[i, j] = 0.0

    for i in range(16, 19):
        for j in range(2, 5):
            z0[i, j] = np.nan

    z1 = z0.copy()
    for i in range(2, 5):
        for j in range(16, 19):
            z1[i, j] = -1.7E-13

    fig = plt.figure(figsize=(4, 8))

    ax0 = fig.add_subplot(121)
    ax0.contourf(x, y, z0, cmap='jet')
    ax0.set_aspect('equal')

    ax1 = fig.add_subplot(122)
    ax1.contourf(x, y, z1, cmap='jet')
    ax1.set_aspect('equal')

    plt.show()
    

if __name__ == "__main__":
    main()
