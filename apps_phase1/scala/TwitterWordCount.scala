val lines = sc.textFile("hdfs://localhost:9000/usr/hadoop/twitter/cricket_twitter.txt")
val words = lines.flatMap(_.split("\\s+"))
val wc = words.map(w => (w, 1)).reduceByKey(_ + _)
wc.saveAsTextFile("README.count")
