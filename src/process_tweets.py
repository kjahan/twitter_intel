from pyspark import SparkContext, SparkConf

def process(sc, filename):
    text_file = sc.textFile(filename)
    counts = text_file.filter(lambda line: len(line.split(";@;")) >= 6) \
    		 .map(lambda line: (line.split(";@;")[4],1)) \
             .reduceByKey(lambda a, b: a + b)
    counts.saveAsTextFile("device_counts")


if __name__ == '__main__':
    conf = SparkConf().setAppName("app")
    sc = SparkContext(conf=conf)
    filename = "data/us_election.txt"
    process(sc, filename)
