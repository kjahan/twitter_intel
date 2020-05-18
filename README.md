# twitter-intel
Twitter NLP intelligence

## Running Spark jobs locally

Download and unzip the latest stable [Apche Spark](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz) on your local machine.  Add the path to spark bin folder to your `PATH` environment variable.


## Setup your conda environment:

`conda create -n spark python=3.7`

## Activate conda env:

`conda activate spark`

## Run a spark job for word counts:

`spark-submit src/words.py`

## Run a spark job for twitter device count:

`spark-submit src/process_tweets.py`

## Deactivate:

`conda deactivate`

## Running Spark jobs on Amazon EMR

1. Login to your AWS account, open EMR under AWS services, and select `Create cluster`.
2. On the first page for creating an EMR clsuter, select `Go to advanced options` from top of the page.
3. Pick `emr-6.0.0` release version, and select `Hadoop 3.2.1` and `Spark 2.4.4` as applications to be installed on the cluster. Note that [Amazon EMR 6.x Release Versions](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-release-6x.html) comes with `Python 3` as default and that's what we want.
4. Keep the defaults on the "Hardware Configuratiosn" page (we use 1 Master and 2 Core nodes all of `m3.xlarge` instance type). Select Next.
6. Type `twitter-cluster` for your cluster name and go to the next page.
7. Select `hermes` for EC2 key pair option. Edit `EMR role`, `EC2 instance profile` and `Auto Scaling role` and add `AmazonS3FullAccess` permission to all of them. This is because we want to move data from S3 to Hadoop cluster.
8. Hit `Create cluster` button and wait for a few minutes for the cluster provisioning to be finished.
9. Copy how to ssh to master node from SSH link in `Master public DNS` section: `ssh -i ~/.ssh/hermes hadoop@YourMasterPublicName`
10. The instances are running `Amazon Linux release 2`. We need to install `git` on the Master node to checkout [twitter-intel project](https://github.com/kjahan/twitter-intel). Run: `sudo yum update -y` and then `sudo yum install git -y` commands to install `git` on the master node.
11. Clone the github project: `git clone https://github.com/kjahan/twitter-intel.git`. Change to `twitter-intel` path. 
12. Create a directory on HDFS to push the data to from S3: `hadoop fs -mkdir hdfs:///output`.
13. Download one of S3 files and move it to your master node local disk: `aws s3 cp s3://election.2016/tweets/election.2016-06-06-00:57:12.txt.gz data`.
14. Unzip your tweets data file: `gunzip data/election.2016-06-06-00\:57\:12.txt.gz` and rename it: `mv data/election.2016-06-06-00\:57\:12.txt data/election.txt`.
15. Push your election file to HDFS: `hadoop fs -put data/election.txt hdfs:///output/` before running the Spark job on the cluster.
14. Check if the file has been copied propely: `hadoop fs -ls hdfs:///output/`
16. Run your Spark job on the cluster: `spark-submit --master yarn --deploy-mode cluster src/process_tweets_on_cluster.py`
16. In case you want to check YARN logs: `yarn logs -applicationId application_1589746186574_0001`
18. Download your computation results from HDFS: `hadoop fs -get hdfs:///output/device_counts`.
19. When you are done DON'T FORGET to terminate your EMR cluster to not pay extra money :)
