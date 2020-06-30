import numpy as np
#from scipy.stats import chisquare
import warnings

list_of_times = np.loadtxt('../data2/test_times.txt')

dataset_dir = '../data2/time_windows/'
models_dir = '../models2/'

models = ['CLiFF', 'Histogram day', 'Histogram week', 'Means', 'occ_grid', 'Prophet', 'STeF', 'WHyTeS']
#models = ['WHyTeS']

angle_edges = np.array([0.5, 0.5, np.pi/4.0])
no_bins = np.array([24, 33, 8])
central_points = np.array([-9.5, 0.25, -3.0*np.pi/4.0])
lower_edge_points = central_points - (angle_edges * 0.5)
upper_edge_points = lower_edge_points + (angle_edges * (no_bins + 1.0))
for_range = ((lower_edge_points[0], upper_edge_points[0]), (lower_edge_points[1], upper_edge_points[1]), (lower_edge_points[2], upper_edge_points[2]),)

for model_name in models:
    model_path = models_dir + model_name + '/'
    chi2 = 0.0
    model_tmp = []
    data_tmp = []
    for one_time in list_of_times:
        if model_name != 'occ_grid':
            model = np.loadtxt(model_path + str(int(one_time)) + '_model.txt')[:, [0, 1, 2, 3]]
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            data = np.loadtxt(dataset_dir + str(int(one_time)) + '_test_data.txt')
        if len(np.shape(data)) == 1:
            if model_name != 'occ_grid':
                model_hist = np.histogramdd(model[:, [0, 1, 2]], bins=no_bins, range=for_range, weights=model[:, -1])[0]
            else:
                model_hist = np.zeros(no_bins)
            data_hist = np.ones_like(model_hist)*(1.0/8.0)
        else:
            #model_hist = np.histogramdd(model[:, :-1], bins=no_bins, range=for_range, weights=model[:, -1])[0]
            #model_hist = np.histogramdd(model[:, [0, 1, 2]], bins=no_bins, range=for_range, weights=model[:, -1])[0]
            if model_name != 'occ_grid':
                model_hist = np.histogramdd(model[:, [0, 1, 2]], bins=no_bins, range=for_range, weights=model[:, -1])[0]
            else:
                model_hist = np.zeros(no_bins)
            data_hist = np.histogramdd(data[:, [1,2,-2]], bins=no_bins, range=for_range)[0]
            indexes_where_zero = np.where(np.sum(data_hist, axis=2)==0)
            data_hist[indexes_where_zero[0], indexes_where_zero[1], :] = np.ones(8)/8.0
        indexes_where_zero = np.where(np.sum(model_hist, axis=2)==0)
        model_hist[indexes_where_zero[0], indexes_where_zero[1], :] = np.ones(8)/8.0

        model_hist = model_hist.astype(float)
        data_hist = data_hist.astype(float)
        #print(np.shape(model_hist))
        #print(np.sum(model_hist))
        #print(np.sum(data_hist))
        model_tmp.append(model_hist)
        data_tmp.append(data_hist)

        all_indexes = np.where(np.sum(model_hist, axis=2)!=None)
        A = model_hist[all_indexes[0], all_indexes[1], :]
        B = data_hist[all_indexes[0], all_indexes[1], :]
        #print(np.shape(A))
        #print(np.sum(A))
        #print(np.sum(B))
        
        A = A / np.sum(A, axis=1).reshape(-1,1)
        B = B / np.sum(B, axis=1).reshape(-1,1)
        #print(np.shape(A))
        #print(np.sum(A))
        #print(np.sum(B))
        #print('')
        # next defining 0/0=0
        #distances = np.divide((A-B)**2, (A+B), out=np.zeros_like(A), where=((A+B!=0)&(A-B!=0)))
        distances = np.divide((A-B)**2, (A+B), where=((A+B!=0)&(A-B!=0)))
        #distances = ((A-B)**2) / (A+B)
        chi2 += np.sum(distances)

    print(model_name + ' CHI2: ' + str(chi2))
    model_tmp = np.array(model_tmp)
    data_tmp = np.array(data_tmp)
    rmse = np.sqrt(np.mean(np.power((model_tmp/np.sum(model_tmp))-(data_tmp/np.sum(data_tmp)), 2)))
    print(model_name + ' RMSE: ' + str(rmse))
