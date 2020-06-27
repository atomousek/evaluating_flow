import numpy as np
from tester import Tester
from summarize_new import summarize, plot_all
import os

default_models = ['published_ral_3_clusters_3_periodicities', 'published_cliffmap_model_pq',
              'published_predictions_stef_euc_o2', 'model_daily_histogram',
              'model_segment_means', 'model_weekly_histogram', 'model_prophet']


def test_models(models=default_models, speed=1, radius_of_robot=1, weighted_encounters=False):
    model_dir = '../models2'
    test_dir = '../data2/time_windows/'
    times_path = '../data2/test_times.txt'

    tester = Tester(radius_of_robot=radius_of_robot)
    times = np.loadtxt(times_path, dtype='int')

    print('speed: ' + str(speed))
    print('radius_of_robot: ' + str(radius_of_robot))
    print('weighted_encounters: ' + str(weighted_encounters))

    result_dir = '../results/output'
    edges_of_cell = [0.5, 0.5]

    for model in models:
        print('testing  ' + model)
        try:
            os.mkdir(result_dir)
        except OSError as error:
            pass

        output_path = result_dir + '/' + str(model) + '_output.txt'
        if os.path.exists(output_path):
            os.remove(output_path)

        for time in times:
            path_model = model_dir + '/' + str(model) + '/' + str(time) + '_model.txt'
            test_data_path = test_dir + str(time) + '_test_data.txt'
            result = tester.test_model(path_model=path_model, path_data=test_data_path, testing_time=time, model_name=model, edges_of_cell=edges_of_cell, speed=speed, weighted_encounters=weighted_encounters)
            with open(output_path, 'a') as file:
                file.write(' '.join(str(value) for value in result) + '\n')

    for model in models:

        print('\n statistics of ' + model)
        output_path = result_dir + '/' + str(model) + '_output.txt'
        summarize(output_path)

    plot_all([result_dir + '/' + str(model) + '_output.txt' for model in models], models, result_dir + '/models.png')


def test_with_different_params(model, speeds=(1, ), radii_of_robot=(1, ), weighted_encounters_opts=(False, )):

    print('testing  ' + model)

    result_dir = '../results/output'
    edges_of_cell = [0.5, 0.5]

    try:
        os.mkdir(result_dir)
    except OSError as error:
        pass

    models = []
    outputs = []

    for speed in speeds:
        for radius_of_robot in radii_of_robot:
            for weighted_encounters in weighted_encounters_opts:

                current_model = "{}_{}_{}_{}".format(model, speed, radius_of_robot, weighted_encounters)
                models.append(current_model)

                model_dir = '../models2'
                test_dir = '../data2/time_windows/'
                times_path = '../data2/test_times.txt'

                tester = Tester(radius_of_robot=radius_of_robot)
                times = np.loadtxt(times_path, dtype='int')

                print('speed: ' + str(speed))
                print('radius_of_robot: ' + str(radius_of_robot))
                print('weighted_encounters: ' + str(weighted_encounters))

                output_path = result_dir + '/' + current_model + '_output.txt'
                outputs.append(output_path)

                if os.path.exists(output_path):
                    os.remove(output_path)
                
                for time in times:
                    path_model = model_dir + '/' + str(model) + '/' + str(time) + '_model.txt'
                    test_data_path = test_dir + str(time) + '_test_data.txt'
                    result = tester.test_model(path_model=path_model, path_data=test_data_path, testing_time=time,
                                               model_name=model, edges_of_cell=edges_of_cell, speed=speed,
                                               weighted_encounters=weighted_encounters)
                    with open(output_path, 'a') as file:
                        file.write(' '.join(str(value) for value in result) + '\n')
                
                print('\n statistics of {} with speed={}m/s, r={}m and weighted encounters set to {}.'.format(
                    model, speed, radius_of_robot, weighted_encounters))
                
                summarize(output_path)

    plot_all(outputs, models, result_dir + '/models.png')
