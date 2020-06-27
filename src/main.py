from test_lot_of_models import test_models, test_with_different_params


def main():
    speed = 1.
    radius_of_robot = 1.
    weighted_encounters = False

    models = ['published_ral_3_clusters_3_periodicities', 'published_cliffmap_model_pq',
              'published_predictions_stef_euc_o2', 'model_daily_histogram',
              'model_segment_means', 'model_weekly_histogram', 'model_prophet']

    # test_models(models=models, speed=speed, radius_of_robot=radius_of_robot, weighted_encounters=weighted_encounters)
    test_with_different_params('published_ral_3_clusters_3_periodicities',
                               radii_of_robot=(1., 2.),
                               speeds=(0.5, 1.),
                               weighted_encounters_opts=(False, ))


if __name__ == '__main__':
    main()