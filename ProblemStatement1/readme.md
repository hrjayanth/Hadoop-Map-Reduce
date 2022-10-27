# Problem Statement 1: Top 10 run scorers in the tournament

Calcaulate the top 10 run scorers in the tournament

## Map-Reduce Diagram

![ProblemStatement1_Map_Reduce_Diagram](https://user-images.githubusercontent.com/3033681/197775936-f24234fb-d145-42af-bbb6-c1ac56a7f30b.png)

## Pseudocode

### Mapper 1
Input: Dataset.csv
For each row
	Extract the Batsman and Runs
Output: Batsman		Runs

### Reducer 1
Input: Output of Mapper1
For each row
	Add the Batsman's score in a match
	return the batsman name and runs
Output: Batsman 	runsScored in a match

### Mapper 2
Input: Output of Reducer1
For each row
	Sort the batsman in descending order as per the runs scored
	Extract top 10 run scorers
Output: Batsman		runs scored

### Reducer 2
Input: Output of Mapper2
For each row
	Sort the batsman in descending order as per the runs scored
	Extract top 10 run scorers
Output: Batsman		runs scored

## Output Logs

### Part 1

```
[hadoop@master-node ProblemStatement1]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper1.py,reducer1.py -mapper "python mapper1.py" -reducer "python reducer1.py" -input /JayLab/dataset.csv -output /JayLab/1/Part1
packageJobJar: [/tmp/hadoop-unjar4658169538935593650/] [] /tmp/streamjob5901346350540241303.jar tmpDir=null
2022-10-25 20:14:29,501 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:14:29,706 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:14:29,883 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0032
2022-10-25 20:14:30,204 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:14:30,279 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:14:30,421 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0032
2022-10-25 20:14:30,421 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:14:30,600 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:14:30,600 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:14:30,668 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0032
2022-10-25 20:14:30,705 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0032/
2022-10-25 20:14:30,706 INFO mapreduce.Job: Running job: job_1664524516236_0032
2022-10-25 20:14:36,777 INFO mapreduce.Job: Job job_1664524516236_0032 running in uber mode : false
2022-10-25 20:14:36,778 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:14:40,847 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:14:45,877 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:14:45,887 INFO mapreduce.Job: Job job_1664524516236_0032 completed successfully
2022-10-25 20:14:45,968 INFO mapreduce.Job: Counters: 55
	File System Counters
		FILE: Number of bytes read=261723
		FILE: Number of bytes written=1352900
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=1597171
		HDFS: Number of bytes written=2462
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Killed map tasks=1
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5351
		Total time spent by all reduces in occupied slots (ms)=2548
		Total time spent by all map tasks (ms)=5351
		Total time spent by all reduce tasks (ms)=2548
		Total vcore-milliseconds taken by all map tasks=5351
		Total vcore-milliseconds taken by all reduce tasks=2548
		Total megabyte-milliseconds taken by all map tasks=5479424
		Total megabyte-milliseconds taken by all reduce tasks=2609152
	Map-Reduce Framework
		Map input records=17912
		Map output records=17912
		Map output bytes=225893
		Map output materialized bytes=261729
		Input split bytes=188
		Combine input records=0
		Combine output records=0
		Reduce input groups=174
		Reduce shuffle bytes=261729
		Reduce input records=17912
		Reduce output records=174
		Spilled Records=35824
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=189
		CPU time spent (ms)=2920
		Physical memory (bytes) snapshot=918667264
		Virtual memory (bytes) snapshot=8397361152
		Total committed heap usage (bytes)=754974720
		Peak Map Physical memory (bytes)=343416832
		Peak Map Virtual memory (bytes)=2796998656
		Peak Reduce Physical memory (bytes)=232030208
		Peak Reduce Virtual memory (bytes)=2803683328
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
		Bytes Written=2462
2022-10-25 20:14:45,969 INFO streaming.StreamJob: Output directory: /JayLab/1/Part1
```

### Part 2

```
[hadoop@master-node ProblemStatement1]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper2.py,reducer2.py -mapper "python mapper2.py" -reducer "python reducer2.py" -input /JayLab/1/Part1/part-00000 -output /JayLab/1/Part2
packageJobJar: [/tmp/hadoop-unjar6956988432589894522/] [] /tmp/streamjob3737005604872614622.jar tmpDir=null
2022-10-25 20:19:55,855 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:19:56,085 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:19:56,265 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0034
2022-10-25 20:19:56,583 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:19:56,658 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:19:56,798 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0034
2022-10-25 20:19:56,799 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:19:56,992 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:19:56,992 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:19:57,050 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0034
2022-10-25 20:19:57,092 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0034/
2022-10-25 20:19:57,093 INFO mapreduce.Job: Running job: job_1664524516236_0034
2022-10-25 20:20:03,172 INFO mapreduce.Job: Job job_1664524516236_0034 running in uber mode : false
2022-10-25 20:20:03,173 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:20:08,232 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:20:12,257 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:20:12,265 INFO mapreduce.Job: Job job_1664524516236_0034 completed successfully
2022-10-25 20:20:12,352 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=342
		FILE: Number of bytes written=830159
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=3895
		HDFS: Number of bytes written=144
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5188
		Total time spent by all reduces in occupied slots (ms)=2142
		Total time spent by all map tasks (ms)=5188
		Total time spent by all reduce tasks (ms)=2142
		Total vcore-milliseconds taken by all map tasks=5188
		Total vcore-milliseconds taken by all reduce tasks=2142
		Total megabyte-milliseconds taken by all map tasks=5312512
		Total megabyte-milliseconds taken by all reduce tasks=2193408
	Map-Reduce Framework
		Map input records=174
		Map output records=20
		Map output bytes=296
		Map output materialized bytes=348
		Input split bytes=202
		Combine input records=0
		Combine output records=0
		Reduce input groups=20
		Reduce shuffle bytes=348
		Reduce input records=20
		Reduce output records=10
		Spilled Records=40
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=199
		CPU time spent (ms)=1790
		Physical memory (bytes) snapshot=862785536
		Virtual memory (bytes) snapshot=8401317888
		Total committed heap usage (bytes)=735051776
		Peak Map Physical memory (bytes)=304414720
		Peak Map Virtual memory (bytes)=2799472640
		Peak Reduce Physical memory (bytes)=258834432
		Peak Reduce Virtual memory (bytes)=2804510720
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=3693
	File Output Format Counters 
		Bytes Written=144
2022-10-25 20:20:12,352 INFO streaming.StreamJob: Output directory: /JayLab/1/Part2
```