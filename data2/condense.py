import numpy as np
import os


model_orig_dir = "/home/filip/Documents/evaluating_flow/models/"
model_new_dir = "/home/filip/Documents/evaluating_flow/models2/"
test_dir = "/home/filip/Documents/evaluating_flow/data2/time_windows/"

times = np.loadtxt("test_times_full.txt")
models = ["cost_F_3_clusters_3_periodicities",
            "model_daily_histogram",
            "model_prophet",
            "model_segment_means",
            "model_weekly_histogram",
            "occ_grid",
            "published_cliffmap_model_pq",
            "published_predictions_stef_euc_o2",
            "published_ral_3_clusters_3_periodicities"]

# # condense models
# for model in models:
#     for i in range(len(times) // 2):
#         t1 = times[2*i]
#         t2 = times[2*i + 1]

#         a1 = np.loadtxt(model_orig_dir + model + "/{}_model.txt".format(int(t1)))
#         a2 = np.loadtxt(model_orig_dir + model + "/{}_model.txt".format(int(t2)))

#         a1[:, 3] = a1[:, 3] + a2[:, 3]
#         np.savetxt(model_new_dir + model + "/{}_model.txt".format(int(t1)), a1)

# condense testing data
for i in range(len(times) // 2):
    t1 = times[2*i]
    t2 = times[2*i + 1]

    with open(test_dir + "{}_test_data.txt".format(int(t1)), "a") as f1:
        with open(test_dir + "{}_test_data.txt".format(int(t2)), "r") as f2:
            if os.path.getsize(test_dir + "{}_test_data.txt".format(int(t2))):
                if os.path.getsize(test_dir + "{}_test_data.txt".format(int(t1))):
                    f1.write('\n')
                    f1.write(f2.read())
                else:
                    f1.write(f2.read())
    
    os.remove(test_dir + "{}_test_data.txt".format(int(t2)))


