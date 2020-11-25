# SparkStreaming
Udacity spark streaming course project

How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
The most direct impact is on the processedRowsPerSecond, more rows processed per second means higher throughput and low latency and vice versa.

What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
According to https://spark.apache.org/docs/latest/streaming-programming-guide.html, below parameters could affect the performance:
  spark.default.parallelism
  spark.streaming.kafka.maxRatePerPartition
  spark.sql.shuffle.partitions
  
spark.default.parallelism is directly related to the cluster machine number and CPU core of each machine. The more cores available in a machine/cluster, the more parallelism it can achieve. Similarly, if spark stream could have the same partition number as kafka partition number, the ingest performance will be good.
The way to find optimal combinations of above params are through enumeration and measure processedRowsPerSecond.
