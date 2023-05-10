# Lab 6

For this lab we will be creating scheduled runs for our jobs and manipulating their run intervals.

## Getting Started

First clone the lab locally and install the dependencies like so:

```bash
git clone git@github.com:TPL-515/Lab6.git
cd Lab6/
pip install -e ".[dev]"
```

This should install all of the required dependencies for the lab.

## Running the Lab

In order to run the lab just run the following command:

```bash
dagster dev
```

From here you should be able to navigate to the UI hosted at: http://localhost:3000

## Lab Tasks

For this lab you will be asked to perform the following tasks

1) Look in the U.I. and find the "generate data" asset. This will generate 10 rows and insert them into the dsdemo table.

2) Next run the "train model" asset that trains the model. The output of this is a finished model that can be reused later on. 

3) Lastly run the "predict" asset that shows off the predictions and logs a scatter plot of the two features colored by the label as well as a confusion matrix for predictions.

4) Write a scheduled job that appends more data to the database every 1 min.

5) Write a scheduled job that when this job runs updates the retrains the model and makes a prediction.

6) Notice how over time our model performance changes.