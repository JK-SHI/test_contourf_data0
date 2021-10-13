import numpy as np
import matplotlib.pyplot as plt


def main():
    z0 = np.array([[0., 0., 2.], [0., 0., 1.], [2., 1., 0.]])
    z1 = np.array([[0., 0., 2.], [0., 0., 1.], [2., 1., -1.7E-13]])

    fig = plt.figure(figsize=(2, 4))

    ax0 = fig.add_subplot(121)
    ax0.contourf(z0, cmap='jet')
    ax0.set_aspect('equal')

    ax1 = fig.add_subplot(122)
    ax1.contourf(z1, cmap='jet')
    ax1.set_aspect('equal')

    plt.show()


if __name__ == "__main__":
    main()
