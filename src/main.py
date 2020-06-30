from test_lot_of_models import test_models, test_with_different_params


def main():
    speed = 0.5
    radius_of_robot = 1.
    weighted_encounters = True

    #models = ['published_ral_3_clusters_3_periodicities', 'published_cliffmap_model_pq',
    #          'published_predictions_stef_euc_o2', 'model_daily_histogram',
    #          'model_segment_means', 'model_weekly_histogram', 'model_prophet']

    models = ['CLiFF', 'Means', 'occ_grid', 'Prophet', 'STeF', 'WHyTeS']

    #test_models(models=models, speed=speed, radius_of_robot=radius_of_robot, weighted_encounters=weighted_encounters)
    test_with_different_params('CLiFF',
                               #radii_of_robot=(0.7, 1.0, 1.3, 1.6, 1.9),
                               radii_of_robot=(1.0,),
                               #speeds=(0.5, 0.75, 1.0, 1.25),
                               speeds=(0.5,),
                               #weighted_encounters_opts=(True, False))
                               weighted_encounters_opts=(True,))


if __name__ == '__main__':
    main()
