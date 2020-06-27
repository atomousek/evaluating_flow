import numpy as np
import path_finder_new as pf
from time import time

import pandas as pd
import pandas.io.common

class Tester:
    """
    Tester finds the shortest path for one scenario.
    """

    def __init__(self, radius_of_robot=1.0):
        self.radius_of_robot = radius_of_robot

    def test_model(self, path_model, path_data, testing_time, model_name, edges_of_cell=np.array([0.5, 0.5]), speed=1.0, weighted_encounters=False):
        """
        this script loads files,
                    calls methods from path_finder,
                    return values that will be saved into the text file.
        """

        ### the first part loads data

        # load part of test data
        try:
            test_data = pd.read_csv(path_data, sep=' ', header=None, engine='c', usecols=[0, 1, 2, 6, 7]).values
        except pandas.io.common.EmptyDataError:
            test_data = np.array([])
        # number of detections in test data
        if test_data.ndim == 2:
            number_of_detections = len(test_data)
        elif test_data.ndim == 1 and len(test_data) == 5:
            number_of_detections = 1
        else:
            number_of_detections = 0
        # define two possible routes
        route = np.array([(-5.0, 9.75), (2.0, 2.75), (-7.0, 0.75), (-5.0, 9.75)])  # clockwise route
        reverse_route = np.array([(-5.0, 9.75), (-7.0, 0.75), (2.0, 2.75), (-5.0, 9.75)])   # counter-clockwise route
        # define walls that cannot be crossed
        path_borders = '../data2/artificial_boarders_of_space_in_UTBM.txt'
        walls = pd.read_csv(path_borders, sep=' ', header=None, engine='c').values
        # load model, it can be txt or npy file
        if path_model.rsplit('.', 1)[1] == 'txt':
            Model = pd.read_csv(filepath_or_buffer=path_model, sep=' ', header=None, engine='c').values
        elif path_model.rsplit('.', 1)[1] == 'npy':
            Model = np.load(path_model)
        else:
            Model = None
            print('unknown file type')
        # initialisation of PathFinder
        path_finder = pf.PathFinder(model_data=Model, edges_of_cell=edges_of_cell)


        ### the second part calculates the shortest path for both routes

        path_finder.create_graph()
        path_finder.remove_walls(walls)

        # clockwise
        path_finder.find_shortest_path(route=route)
        weight_1 = path_finder.get_mean_path_weight()
        path_finder.extract_trajectory(testing_time, speed=speed, time_step=0.1/speed)
        result_1 = path_finder.extract_interactions(test_data, radius=self.radius_of_robot, weighted_encounters=weighted_encounters, time_step=0.1/speed)

        # counter-clockwise
        path_finder.find_shortest_path(route=reverse_route)
        weight_2 = path_finder.get_mean_path_weight()
        path_finder.extract_trajectory(testing_time, speed=speed, time_step=0.1/speed)
        result_2 = path_finder.extract_interactions(test_data, radius=self.radius_of_robot, weighted_encounters=weighted_encounters, time_step=0.1/speed)

        ### the third part creates an output
        
        results = []  # output that will be printed into the textfile
        results.append(int(testing_time))
        results.append(number_of_detections)
        results.append(result_1)
        results.append(result_2)
        results.append(weight_1)
        results.append(weight_2)

        if weight_1 < weight_2:
            results.append(result_1)
        else:
            results.append(result_2)
        
        return results


if __name__ == "__main__":

    start = time()
    tester = Tester(radius_of_robot=1.)
    finish = time()
    print(('zero part: ' + str(finish-start)))
    
    edges_of_cell = np.array([0.5, 0.5])
    start = time()
    print(tester.test_model('../models/1_cluster_9_periods/1554105994_model.txt', '../data/time_windows/1554105994_test_data.txt', testing_time=1554105994, model_name='WHyTeS', edges_of_cell=edges_of_cell, speed=1.0, weighted_encounters=False))
    finish = time()
    print(('first&second part: ' + str(finish-start)))
