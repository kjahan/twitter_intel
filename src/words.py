from pyspark import SparkContext, SparkConf

def process(sc):
    words = sc.textFile("/usr/share/dict/words")
    spar_words = words.filter(lambda w: w.startswith("spar")).take(5)
    print(spar_words)


if __name__ == '__main__':
    conf = SparkConf().setAppName("app")
    sc = SparkContext(conf=conf)
    process(sc)
