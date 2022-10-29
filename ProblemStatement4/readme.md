# Problem Statement 4: Extras bowled by a bowler in a match

List all the bowlers and the corresponding extras bowled by them in a match

## Map-Reduce Diagram

![ProblemStatement4_Mapper_Reducer_diagram](https://user-images.githubusercontent.com/3033681/198282292-2772a0f5-4b1a-4d81-a6cd-f93c7952d3a6.png)

## Pseudocode

### Mapper 1

<pre>
Input: Dataset.csv

For each row
    Extract the extra run given deliveries
    return the bowler name and the extra runs conceded

Output: matchID_bowler		extra runs conceded
</pre>

### Reducer 1

<pre>
Input: Output of Mapper1

For each row
    Add the runs conceded by the bowler

Output: matchID		bowler 	    total runs conceded
</pre>

## Output Logs
```
[hadoop@master-node Hadoop-Map-Reduce-main]$ hadoop jar /home/hadoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar -files mapper1.py,reducer1.py -mapper "python mapper1.py" -reducer "python reducer1.py" -input /JayLab/dataset.csv -output /JayLab/4/Part1
packageJobJar: [/tmp/hadoop-unjar1787392485175933963/] [] /tmp/streamjob9057633002761999937.jar tmpDir=null
2022-10-25 20:41:59,115 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:41:59,313 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at /172.16.24.215:8032
2022-10-25 20:41:59,484 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/hadoop/.staging/job_1664524516236_0040
2022-10-25 20:41:59,800 INFO mapred.FileInputFormat: Total input files to process : 1
2022-10-25 20:41:59,869 INFO mapreduce.JobSubmitter: number of splits:2
2022-10-25 20:41:59,999 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1664524516236_0040
2022-10-25 20:41:59,999 INFO mapreduce.JobSubmitter: Executing with tokens: []
2022-10-25 20:42:00,166 INFO conf.Configuration: resource-types.xml not found
2022-10-25 20:42:00,167 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2022-10-25 20:42:00,237 INFO impl.YarnClientImpl: Submitted application application_1664524516236_0040
2022-10-25 20:42:00,274 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1664524516236_0040/
2022-10-25 20:42:00,275 INFO mapreduce.Job: Running job: job_1664524516236_0040
2022-10-25 20:42:05,384 INFO mapreduce.Job: Job job_1664524516236_0040 running in uber mode : false
2022-10-25 20:42:05,385 INFO mapreduce.Job:  map 0% reduce 0%
2022-10-25 20:42:10,493 INFO mapreduce.Job:  map 100% reduce 0%
2022-10-25 20:42:15,520 INFO mapreduce.Job:  map 100% reduce 100%
2022-10-25 20:42:15,529 INFO mapreduce.Job: Job job_1664524516236_0040 completed successfully
2022-10-25 20:42:15,615 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=9474
		FILE: Number of bytes written=848294
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=1597171
		HDFS: Number of bytes written=3917
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=5221
		Total time spent by all reduces in occupied slots (ms)=2210
		Total time spent by all map tasks (ms)=5221
		Total time spent by all reduce tasks (ms)=2210
		Total vcore-milliseconds taken by all map tasks=5221
		Total vcore-milliseconds taken by all reduce tasks=2210
		Total megabyte-milliseconds taken by all map tasks=5346304
		Total megabyte-milliseconds taken by all reduce tasks=2263040
	Map-Reduce Framework
		Map input records=17912
		Map output records=650
		Map output bytes=8168
		Map output materialized bytes=9480
		Input split bytes=188
		Combine input records=0
		Combine output records=0
		Reduce input groups=157
		Reduce shuffle bytes=9480
		Reduce input records=650
		Reduce output records=157
		Spilled Records=1300
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=219
		CPU time spent (ms)=2090
		Physical memory (bytes) snapshot=903471104
		Virtual memory (bytes) snapshot=8400039936
		Total committed heap usage (bytes)=741867520
		Peak Map Physical memory (bytes)=344375296
		Peak Map Virtual memory (bytes)=2797801472
		Peak Reduce Physical memory (bytes)=217579520
		Peak Reduce Virtual memory (bytes)=2804768768
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
		Bytes Written=3917
2022-10-25 20:42:15,615 INFO streaming.StreamJob: Output directory: /JayLab/4/Part1
```