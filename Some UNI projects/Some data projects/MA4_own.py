"""
Solutions to module 4
Student: Linus Olofsson
Mail: Linus.Olofsson.4269@student.uu.se
Reviewed by: Martin Knebel
Reviewed date: 2022-10-25
"""


import math
import numpy as np
from matplotlib import pyplot as plt
import random
from time import perf_counter as pc
from time import sleep as pause
import multiprocessing as mp
import concurrent.futures as future

pi = math.pi
gamma = math.gamma


def pi_calc(n):
    nc_list = []  # Innanför cirkelen
    nk_list = []  # Utanför cirkelen i kvadraten
    for i in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            # print(f'Inside Circle: x = {x:.2f} y = {y:.2f}')
            nc_list.append((x, y))

        else:
            # print(f'Outside Circle: x = {x:.2f} y = {y:.2f}')
            nk_list.append((x, y))
    # print(f"len of circle list: {len(nc_list)}\n len of cube list: {len(nk_list)}\nfor n = {n}")
    return nc_list, nk_list


def inside(coord, r):
    length = sum([x ** 2 for x in coord])
    if length <= r:
        return True


def hyper(n, d):
    """

    :param n: Antal itterationer
    :param d: vilken dimension
    :return:
    """
    r = 1
    points = 0
    # Här bör vi göra
    # print('nu kör vi något! ')
    for i in range(n):
        # print(i)
        x = [random.uniform(-1, 1) for k in range(d)]  # The coordinates based on the dimension.
        if inside(x, r):
            points += 1

    sphereVol = points / n * 2 ** d  # To get the share of which points is inside the sphere insdie the cube.
    # a.e how much of the cube is filled by the sphere.

    theoretical = (pi ** (d / 2) / (gamma(d / 2 + 1))) * r ** d
    #print(f'Calculated sphere volume: {sphereVol} & Theoretical values: {theoretical}')
    return sphereVol, theoretical

def hyper_count(n, p, d):
    """
    :param n: antal itterationer
    :param p: antal processer
    :param d: vilket dimension
    :return:
    """
    with future.ProcessPoolExecutor() as ex:
        # n antal itterationer
        # t antal threads
        I = [n for _ in range(p)]
        D = [d for _ in range(p)]
        results_calc = ex.map(hyper, I, D)           # I , I , I , I , I,
                                                # D, D ,D , D , D ,D
    return results_calc

def sphere_plot():
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax1 = fig.add_subplot(projection='3d')
    r = 0.05
    u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
    x = np.cos(u) * np.sin(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(v)
    ax1.plot_surface(x, y, z, cmap='cividis')  # plt.cm.YlGnBu_r


def main():
    N = [1000, 10000, 100000]
    pie = []

    fig, ax = plt.subplots(1, 3)
    for n, a in zip(N, ax):
        # Find the inside and outside points and calculate the Pi's
        inside, outside = pi_calc(n)
        pie.append(4 * len(inside) / n)

        # Plot the Red Circle Blue box
        theta = np.linspace(0, 2 * pi, 360)
        r = 1
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        a.set_xlim(-1.5, 1.5)
        a.set_ylim(-1.5, 1.5)

        a.plot(x, y, 'r')
        a.set_aspect(1)

        a.plot((-1, 1), (-1, -1), 'b')
        a.plot((1, 1), (-1, 1), 'b')
        a.plot((-1, 1), (1, 1), 'b')
        a.plot((-1, -1), (1, -1), 'b')
        a.scatter([i[0] for i in inside], [i[1] for i in inside], color='r', s=0.9)
        a.scatter([o[0] for o in outside], [o[1] for o in outside], color='b', s=0.9)
        a.set_aspect(1)
        a.set_title(f'n = {n:,}')
    print(f'The PI values are: {pie}\n')


    #########################
    #### Spherical input ####
    #########################
    # sp_plot = sphere_plot()

    print(f'The values for the 11th dim hyper sphere:')
    high_order, high_order_theoretical = hyper(100000,11)
    print(f'Calculated values: {high_order}, Theoretical values: {high_order_theoretical}')
    print(' ')
    print('The values for the 2th dim hyper sphere:')
    lower_order, lower_order_theoretical =hyper(100000,2)
    print(f'Calculated values: {lower_order}, Theoretical values: {lower_order_theoretical}')
    print(' ')

    ##########################
    ####  Multithreading  ####
    ##########################

    d = 11
    print('Values for multithreading and its comparison:\n ')
    start = pc()
    count_hyp = hyper_count(1000000, 10, d)             # PARALLELL ,count_hyp_theo
    end = pc()
    print(f'Time with multithreading and n = 1000000 : {end - start} seconds ')
    #print(f'Calculated values: {count_hyp}, Theoretical values:')
    print(' ')
    start = pc()
    results,results_theo = hyper(10000000, d)                    # SINGULÄR
    end = pc()
    print(f'Time without multithreading and n = 10000000 : {end - start} seconds')
    print(f'Calculated values: {results}, Theoretical values: {results_theo}')
    plt.show()


if __name__ == '__main__':
    main()
