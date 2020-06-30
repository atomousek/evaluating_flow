# Natural  Criteria  for  Pedestrian  Flow  Forecasting  Models  Comparison

This repository contains testing scripts and testing data used for model evaluation through social disturbance benchmark. Additionally, models evaluated in RAL paper are included.

The scripts enable to evaluate the models with different experiment parameters.

The scripts are written in python 3.7, with required packages listed in requirements.txt.

Run the following command to install the packages.

```
pip install -r ./requirements.txt
```

To set the parameters and run the experiment open: ./src/main.py 

The script contains two possible experiments. One tests many models using one set of parameters. The other tests one model using different parameter combinations.

The outputs of the experiment are: service disturbance cost for different servicing ratios in console and a figure showing service disturbance function of the different tested models. The figure should show after the test finishes and it is also saved in ./results/output/models.pdf