from test_lot_of_models import test_models, test_with_different_params


def test_many_models():
    # choose parameters
    speed = 0.5
    radius_of_robot = 1.
    weighted_encounters = True

    # choose models
    models = ['CLiFF', 'Histogram day', 'Histogram week', 'Means', 'occ_grid', 'Prophet', 'STeF', 'WHyTeS']

    # run the tests
    test_models(models=models, speed=speed, radius_of_robot=radius_of_robot, weighted_encounters=weighted_encounters)


def test_different_parameters():
    # choose model and parameters
    model = 'CLiFF'
    radii_of_robot = (0.7, 1.0, 1.3, 1.6, 1.9)
    speeds = (0.5, 0.75, 1.0, 1.25)
    weighted_encounters_opts = (True, False)

    # run the tests
    test_with_different_params(model=model,
                               radii_of_robot=radii_of_robot,
                               speeds=speeds,
                               weighted_encounters_opts=weighted_encounters_opts)


if __name__ == '__main__':
    """
    Choose the test
    Specify the desired parameters and models in the functions called below
    """
    test_many_models()
    test_different_parameters()
