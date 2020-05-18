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

1. Login to your AWS account, open EMR under AWS services, and select `Create cluster` button.
2. On the first page for creating an EMR clsuter, select `Go to advanced options` from the top.
3. Pick `emr-5.30.0` release version, and select `Hadoop 2.8.5` and `Spark 2.4.5` as applications to be installed on the cluster.
4. Add the following for the configuration box, and click on Next button:
`[
  {
   "Classification": "spark-env",
   "Properties": {},
   "Configurations": [
       {
         "Classification": "export",
         "Properties": {
             "PYSPARK_PYTHON": "/user/bin/python3",
         }
       }
   ]
 }
]`
5. Keep the defaults on the "Hardware Configuratiosn" page (we use 1 Mater and 2 Core nodes all of `m3.xlarge` instance type) and select Next.
6. Pick `twitter-cluster` for your cluster name and go to the next page.
7. Select `hermes` for EC2 key pair option. Also, edit EMR role, EC2 instance profile and Auto Scaling role and add `AmazonS3FullAccess` to all of them.
8. Hit `Create cluster` button! You need to wait for a few minutes for the cluster resource provisioning to be finished.
9. Copy how to ssh to master node from SSH link in `Master public DNS` section: `ssh -i ~/hermes.pem hadoop@YourMasterPublicName`
10. The instances are running `Amazon Linux release 2`. We need to install `git` on the Master node to checkout our code. So, run: `sudo yum update -y` and then `sudo yum install git -y` commands to get `git`.
11. Clone the Twitter project: `git clone https://github.com/kjahan/twitter-intel.git`. Switch to `twitter-intel` folder. 
12. Create a directory on HDFS: `hadoop fs -mkdir hdfs:///output`.
13. Push your election file to HDFS: `hadoop fs -put data/election.txt hdfs:///output/`.
14. Check if the file has been copied propely: `hadoop fs -ls hdfs:///output/`
15.     filename = "hdfs:///output/election.txt"
16. `yarn logs -applicationId application_1589746186574_0001`
17. spark-submit --master yarn --deploy-mode cluster src/process_tweets.py
