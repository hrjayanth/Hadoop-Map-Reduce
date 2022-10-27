# Problem Statement 2: Top 10 wicket takers

List the top 10 wicket takers of the tournament along with the wickets taken

## Map-Reduce Diagram

![ProblemStatement2_Mapper_Reducer_diagram](https://user-images.githubusercontent.com/3033681/198283900-e998c729-13b4-4536-b83d-e17fafdce120.png)

## Pseudocode

### Mapper 1
<pre>
Input: Dataset.csv
For each row
	Extract the Bowler and wickets
Output: bowler		wickets
</pre>

### Reducer 1
<pre>
Input: Output of Mapper1
For each row
	Add the Bowler's wickets
	return the Bowler name and wickets
Output: Bowler 	wickets taken
</pre>

### Mapper 2
<pre>
Input: Output of Reducer1
For each row
	Sort as per the wickets taken in ascending Order
	Extract only top 10 wicket takers
Output: Bowler		 wickets taken
</pre>

### Reducer 2
<pre>
Input: Output of Mapper2
For each row
	Sort as per the wickets taken in ascending Order
	Extract only top 10 wicket takers
Output: Bowler		 wickets taken
</pre>

## Output Logs

### Part 1

```
[hadoop@master-node ProblemStatement2]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper1.py,reducer1.py -mapper "python mapper1.py" -reducer "python reducer1.py" -input /JayLab/dataset.csv -output /JayLab/2/Part1
packageJobJar: [/tmp/hadoop-unjar359422602379915819/] [] /tmp/streamjob189147907643851539.jar tmpDir=null
2022-10-25 20:25:33,897 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:25:34,096 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:25:34,268 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0035
2022-10-25 20:25:34,592 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:25:34,663 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:25:34,792 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0035
2022-10-25 20:25:34,792 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:25:34,973 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:25:34,973 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:25:35,036 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0035
2022-10-25 20:25:35,073 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0035/
2022-10-25 20:25:35,074 INFO mapreduce.Job: Running job: job_1664524516236_0035
2022-10-25 20:25:41,146 INFO mapreduce.Job: Job job_1664524516236_0035 running in uber mode : false
2022-10-25 20:25:41,147 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:25:45,242 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:25:50,274 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:25:50,283 INFO mapreduce.Job: Job job_1664524516236_0035 completed successfully
2022-10-25 20:25:50,370 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=13988
		FILE: Number of bytes written=857427
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=1597171
		HDFS: Number of bytes written=1403
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5220
		Total time spent by all reduces in occupied slots (ms)=2110
		Total time spent by all map tasks (ms)=5220
		Total time spent by all reduce tasks (ms)=2110
		Total vcore-milliseconds taken by all map tasks=5220
		Total vcore-milliseconds taken by all reduce tasks=2110
		Total megabyte-milliseconds taken by all map tasks=5345280
		Total megabyte-milliseconds taken by all reduce tasks=2160640
	Map-Reduce Framework
		Map input records=17912
		Map output records=912
		Map output bytes=12158
		Map output materialized bytes=13994
		Input split bytes=188
		Combine input records=0
		Combine output records=0
		Reduce input groups=105
		Reduce shuffle bytes=13994
		Reduce input records=912
		Reduce output records=104
		Spilled Records=1824
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=237
		CPU time spent (ms)=2170
		Physical memory (bytes) snapshot=937807872
		Virtual memory (bytes) snapshot=8398974976
		Total committed heap usage (bytes)=744488960
		Peak Map Physical memory (bytes)=361345024
		Peak Map Virtual memory (bytes)=2797686784
		Peak Reduce Physical memory (bytes)=218529792
		Peak Reduce Virtual memory (bytes)=2804658176
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=1596983
	File Output Format Counters 
		Bytes Written=1403
2022-10-25 20:25:50,370 INFO streaming.StreamJob: Output directory: /JayLab/2/Part1
```

### Part 2:

```
[hadoop@master-node ProblemStatement2]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper2.py,reducer2.py -mapper "python mapper2.py" -reducer "python reducer2.py" -input /JayLab/2/Part1/part-00000 -output /JayLab/2/Part2
packageJobJar: [/tmp/hadoop-unjar3785706011925002164/] [] /tmp/streamjob6359430048171873258.jar tmpDir=null
2022-10-25 20:29:55,241 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:29:55,446 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:29:55,622 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0037
2022-10-25 20:29:55,955 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:29:56,032 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:29:56,160 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0037
2022-10-25 20:29:56,160 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:29:56,340 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:29:56,340 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:29:56,406 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0037
2022-10-25 20:29:56,442 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0037/
2022-10-25 20:29:56,443 INFO mapreduce.Job: Running job: job_1664524516236_0037
2022-10-25 20:30:02,516 INFO mapreduce.Job: Job job_1664524516236_0037 running in uber mode : false
2022-10-25 20:30:02,517 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:30:06,596 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:30:11,626 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:30:11,636 INFO mapreduce.Job: Job job_1664524516236_0037 completed successfully
2022-10-25 20:30:11,717 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=334
		FILE: Number of bytes written=830143
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2307
		HDFS: Number of bytes written=154
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5029
		Total time spent by all reduces in occupied slots (ms)=2241
		Total time spent by all map tasks (ms)=5029
		Total time spent by all reduce tasks (ms)=2241
		Total vcore-milliseconds taken by all map tasks=5029
		Total vcore-milliseconds taken by all reduce tasks=2241
		Total megabyte-milliseconds taken by all map tasks=5149696
		Total megabyte-milliseconds taken by all reduce tasks=2294784
	Map-Reduce Framework
		Map input records=104
		Map output records=20
		Map output bytes=288
		Map output materialized bytes=340
		Input split bytes=202
		Combine input records=0
		Combine output records=0
		Reduce input groups=20
		Reduce shuffle bytes=340
		Reduce input records=20
		Reduce output records=10
		Spilled Records=40
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=203
		CPU time spent (ms)=1880
		Physical memory (bytes) snapshot=864178176
		Virtual memory (bytes) snapshot=8397783040
		Total committed heap usage (bytes)=745013248
		Peak Map Physical memory (bytes)=339836928
		Peak Map Virtual memory (bytes)=2797289472
		Peak Reduce Physical memory (bytes)=234184704
		Peak Reduce Virtual memory (bytes)=2804183040
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=2105
	File Output Format Counters 
		Bytes Written=154
2022-10-25 20:30:11,717 INFO streaming.StreamJob: Output directory: /JayLab/2/Part2
```