# twitter-intel
Twitter NLP intelligence

## Requirements

Download and unzip the latest stable [Apche Spark](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz) on your local machine.  Add the path to spark bin folder to your `PATH` environment variable.

## Setup your conda environment:

`conda create -n spark python=3.7`

## Activate conda env:

`conda activate spark`

## Run a simple Spark job locally (word count):

`spark-submit src/words.py`

## Run Twitter Spark job locally (device count):

`spark-submit src/process_tweets.py`

## Deactivate:

`conda deactivate`

