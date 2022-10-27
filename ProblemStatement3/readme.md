# Problem Statement 3: Centuries

List all the batsman who have hit centuries along with the count

## Map-Reduce Diagram

![Centuries Map Reduce](https://user-images.githubusercontent.com/3033681/197848995-2188c028-17d7-49f2-95a5-e3dd2c1cdbff.png)

## Pseudocode

### Mapper 1
Input: Dataset.csv
For each row
	Extract the matchID_Batsman and Runs
Output: matchID_Batsman		Runs

### Reducer 1
Input: Output of Mapper1
For each row
	Add the Batsman's score in a match
	return the batsman name and runs
Output: Batsman 	runsScored in a match

### Mapper 2
Input: Output of Reducer1
For each row
	Filter only the runs which is equal to or more than 100
	Return the batsman name and runs
Output: Batsman		Scores 100 and above

### Reducer 2
Input: Output of Mapper2
For each row
	return the batsman name and count of centuries
Output: Batsman		count of centuries

## Output Logs

### Part 1
```
[hadoop@master-node ProblemStatement3]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper1.py,reducer1.py -mapper "python mapper1.py" -reducer "python reducer1.py" -input /JayLab/dataset.csv -output /JayLab/3/Part1
packageJobJar: [/tmp/hadoop-unjar465896954426474357/] [] /tmp/streamjob5513865055299634528.jar tmpDir=null
2022-10-25 20:37:05,078 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:37:05,284 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:37:05,455 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0038
2022-10-25 20:37:05,789 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:37:05,862 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:37:05,994 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0038
2022-10-25 20:37:05,994 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:37:06,157 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:37:06,157 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:37:06,219 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0038
2022-10-25 20:37:06,253 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0038/
2022-10-25 20:37:06,255 INFO mapreduce.Job: Running job: job_1664524516236_0038
2022-10-25 20:37:12,325 INFO mapreduce.Job: Job job_1664524516236_0038 running in uber mode : false
2022-10-25 20:37:12,326 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:37:17,382 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:37:22,415 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:37:22,424 INFO mapreduce.Job: Job job_1664524516236_0038 completed successfully
2022-10-25 20:37:22,518 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=405019
		FILE: Number of bytes written=1639492
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=1597171
		HDFS: Number of bytes written=24590
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=6120
		Total time spent by all reduces in occupied slots (ms)=2228
		Total time spent by all map tasks (ms)=6120
		Total time spent by all reduce tasks (ms)=2228
		Total vcore-milliseconds taken by all map tasks=6120
		Total vcore-milliseconds taken by all reduce tasks=2228
		Total megabyte-milliseconds taken by all map tasks=6266880
		Total megabyte-milliseconds taken by all reduce tasks=2281472
	Map-Reduce Framework
		Map input records=17912
		Map output records=17912
		Map output bytes=369189
		Map output materialized bytes=405025
		Input split bytes=188
		Combine input records=0
		Combine output records=0
		Reduce input groups=1158
		Reduce shuffle bytes=405025
		Reduce input records=17912
		Reduce output records=1158
		Spilled Records=35824
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=268
		CPU time spent (ms)=2950
		Physical memory (bytes) snapshot=918786048
		Virtual memory (bytes) snapshot=8405823488
		Total committed heap usage (bytes)=743440384
		Peak Map Physical memory (bytes)=354332672
		Peak Map Virtual memory (bytes)=2801979392
		Peak Reduce Physical memory (bytes)=216440832
		Peak Reduce Virtual memory (bytes)=2803695616
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
		Bytes Written=24590
2022-10-25 20:37:22,518 INFO streaming.StreamJob: Output directory: /JayLab/3/Part1
```

### Part 2

```
[hadoop@master-node ProblemStatement3]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper2.py,reducer2.py -mapper "python mapper2.py" -reducer "python reducer2.py" -input /JayLab/3/Part1/part-00000 -output /JayLab/3/Part2
packageJobJar: [/tmp/hadoop-unjar3062617826671109710/] [] /tmp/streamjob4114936737137944790.jar tmpDir=null
2022-10-25 20:38:09,510 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:38:09,720 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:38:09,892 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0039
2022-10-25 20:38:10,213 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:38:10,282 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:38:10,427 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0039
2022-10-25 20:38:10,427 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:38:10,614 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:38:10,614 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:38:10,675 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0039
2022-10-25 20:38:10,709 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0039/
2022-10-25 20:38:10,710 INFO mapreduce.Job: Running job: job_1664524516236_0039
2022-10-25 20:38:16,783 INFO mapreduce.Job: Job job_1664524516236_0039 running in uber mode : false
2022-10-25 20:38:16,784 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:38:21,846 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:38:25,874 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:38:26,889 INFO mapreduce.Job: Job job_1664524516236_0039 completed successfully
2022-10-25 20:38:26,996 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=137
		FILE: Number of bytes written=829749
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=28888
		HDFS: Number of bytes written=49
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5572
		Total time spent by all reduces in occupied slots (ms)=2260
		Total time spent by all map tasks (ms)=5572
		Total time spent by all reduce tasks (ms)=2260
		Total vcore-milliseconds taken by all map tasks=5572
		Total vcore-milliseconds taken by all reduce tasks=2260
		Total megabyte-milliseconds taken by all map tasks=5705728
		Total megabyte-milliseconds taken by all reduce tasks=2314240
	Map-Reduce Framework
		Map input records=1158
		Map output records=8
		Map output bytes=115
		Map output materialized bytes=143
		Input split bytes=202
		Combine input records=0
		Combine output records=0
		Reduce input groups=4
		Reduce shuffle bytes=143
		Reduce input records=8
		Reduce output records=4
		Spilled Records=16
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=236
		CPU time spent (ms)=2100
		Physical memory (bytes) snapshot=907911168
		Virtual memory (bytes) snapshot=8398417920
		Total committed heap usage (bytes)=756547584
		Peak Map Physical memory (bytes)=339456000
		Peak Map Virtual memory (bytes)=2798317568
		Peak Reduce Physical memory (bytes)=229920768
		Peak Reduce Virtual memory (bytes)=2802774016
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=28686
	File Output Format Counters 
		Bytes Written=49
2022-10-25 20:38:26,996 INFO streaming.StreamJob: Output directory: /JayLab/3/Part2
```