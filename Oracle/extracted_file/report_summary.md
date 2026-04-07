#  WORKLOAD REPOSITORY report for 

DB Name| DB Id| Instance| Inst num| Startup Time| Release| RAC  
---|---|---|---|---|---|---  
ORCL| 1539058184| orcl2| 2| 02-Feb-21 02:02| 11.2.0.4.0| YES  
  
Host Name| Platform| CPUs| Cores| Sockets| Memory (GB)  
---|---|---|---|---|---  
his02| Linux x86 64-bit|  112|  56|  4|  251.08  
  
| Snap Id| Snap Time| Sessions| Cursors/Session| Instances  
---|---|---|---|---|---  
Begin Snap:| 73343| 20-Jan-25 08:00:22| 493|  2.1| 2  
End Snap:| 73349| 20-Jan-25 11:00:59| 560|  1.9| 2  
Elapsed:|  |  180.61 (mins)|  |  |   
DB Time:|  |  710.67 (mins)|  |  |   
  
### Report Summary

Load Profile

| Per Second| Per Transaction| Per Exec| Per Call  
---|---|---|---|---  
DB Time(s):|  3.9|  0.1|  0.00|  0.00  
DB CPU(s):|  2.6|  0.1|  0.00|  0.00  
Redo size (bytes):|  516,290.8|  11,613.0|  |   
Logical read (blocks):|  295,008.8|  6,635.7|  |   
Block changes:|  2,520.9|  56.7|  |   
Physical read (blocks):|  67,416.6|  1,516.4|  |   
Physical write (blocks):|  57.0|  1.3|  |   
Read IO requests:|  1,268.1|  28.5|  |   
Write IO requests:|  30.4|  0.7|  |   
Read IO (MB):|  526.7|  11.9|  |   
Write IO (MB):|  0.5|  0.0|  |   
Global Cache blocks received:|  114.6|  2.6|  |   
Global Cache blocks served:|  64.4|  1.5|  |   
User calls:|  895.8|  20.2|  |   
Parses (SQL):|  327.0|  7.4|  |   
Hard parses (SQL):|  9.2|  0.2|  |   
SQL Work Area (MB):|  34.4|  0.8|  |   
Logons:|  0.9|  0.0|  |   
Executes (SQL):|  1,254.6|  28.2|  |   
Rollbacks:|  0.7|  0.0|  |   
Transactions:|  44.5|  |  |   
  
Instance Efficiency Percentages (Target 100%) 

Buffer Nowait %:|  100.00| Redo NoWait %:|  100.00  
---|---|---|---  
Buffer Hit %:|  99.98| In-memory Sort %:|  100.00  
Library Hit %:|  98.19| Soft Parse %:|  97.19  
Execute to Parse %:|  73.94| Latch Hit %:|  99.99  
Parse CPU to Parse Elapsd %:|  79.00| % Non-Parse CPU:|  99.19  
  
Top 10 Foreground Events by Total Wait Time


Event| Waits| Total Wait Time (sec)| Wait Avg(ms)| % DB time| Wait Class  
---|---|---|---|---|---  
DB CPU|  | 27.9K|  | 65.5|   
control file sequential read| 1,437,851| 511.8| 0| 1.2| System I/O  
log file sync| 224,920| 258.1| 1| .6| Commit  
gc cr block busy| 107,095| 214.3| 2| .5| Cluster  
db file sequential read| 503,183| 202| 0| .5| User I/O  
gc current block 2-way| 578,238| 188| 0| .4| Cluster  
SQL*Net message from dblink| 60,038| 187.9| 3| .4| Network  
gc current grant busy| 134,466| 161.9| 1| .4| Cluster  
gc cr block 2-way| 312,763| 136.9| 0| .3| Cluster  
SQL*Net more data to client| 4,522,962| 47| 0| .1| Network  
  
Wait Classes by Total Wait Time


Wait Class| Waits| Total Wait Time (sec)| Avg Wait (ms)| % DB time| Avg Active Sessions  
---|---|---|---|---|---  
DB CPU|  | 27,929|  | 65.5| 2.6  
System I/O| 2,292,871| 1,068| 0| 2.5| 0.1  
Cluster| 1,231,689| 841| 1| 2.0| 0.1  
Network| 12,731,469| 265| 0| .6| 0.0  
Commit| 224,934| 258| 1| .6| 0.0  
User I/O| 566,190| 212| 0| .5| 0.0  
Other| 653,324| 122| 0| .3| 0.0  
Application| 116,338| 31| 0| .1| 0.0  
Concurrency| 73,086| 18| 0| .0| 0.0  
Configuration| 8,319| 3| 0| .0| 0.0  
  
Host CPU 

CPUs| Cores| Sockets| Load Average Begin| Load Average End| %User| %System| %WIO| %Idle  
---|---|---|---|---|---|---|---|---  
112|  56|  4|  3.12|  3.85|  2.3|  0.3|  1.1|  97.4  
  
Instance CPU 

%Total CPU| %Busy CPU| %DB time waiting for CPU (Resource Manager)  
---|---|---  
2.4|  90.2|  0.0  
  
IO Profile

| Read+Write Per Second| Read per Second| Write Per Second  
---|---|---|---  
Total Requests:|  1,534.8|  1,422.1|  112.7  
Database Requests:|  1,298.5|  1,268.1|  30.4  
Optimized Requests:|  0.0|  0.0|  0.0  
Redo Requests:|  94.8|  15.8|  78.9  
Total (MB):|  532.8|  530.8|  2.0  
Database (MB):|  527.1|  526.7|  0.5  
Optimized Total (MB):|  0.0|  0.0|  0.0  
Redo (MB):|  3.0|  1.9|  1.0  
Database (blocks):|  67,473.5|  67,416.6|  57.0  
Via Buffer Cache (blocks):|  87.4|  40.7|  46.7  
Direct (blocks):|  67,386.1|  67,375.9|  10.2  
  
Memory Statistics 

| Begin| End  
---|---|---  
Host Mem (MB):|  257,104.9|  257,104.9  
SGA use (MB):|  153,600.0|  153,600.0  
PGA use (MB):|  3,843.1|  4,122.7  
% Host Mem used for SGA+PGA:|  61.24|  61.35  
  
Cache Sizes 

| Begin| End| |   
---|---|---|---|---  
Buffer Cache:|  123,392M|  123,392M| Std Block Size:|  8K  
Shared Pool Size:|  20,887M|  20,908M| Log Buffer:|  344,184K  
  
Shared Pool Statistics 

| Begin| End  
---|---|---  
Memory Usage %:|  63.25|  63.36  
% SQL with executions>1:|  97.65|  90.88  
% Memory for SQL w/exec>1:|  97.56|  91.41  
  
##  Main Report 

  * Report Summary
  * Wait Events Statistics
  * SQL Statistics
  * Instance Activity Statistics
  * IO Stats
  * Buffer Pool Statistics
  * Advisory Statistics
  * Wait Statistics
  * Undo Statistics
  * Latch Statistics
  * Segment Statistics
  * Dictionary Cache Statistics
  * Library Cache Statistics
  * Memory Statistics
  * Streams Statistics
  * Resource Limit Statistics
  * Shared Server Statistics
  * init.ora Parameters



##  RAC Statistics 

  * RAC Report Summary
  * Global Messaging Statistics
  * Global CR Served Stats
  * Global CURRENT Served Stats
  * Global Cache Transfer Stats
  * Interconnect Stats
  * Dynamic Remastering Statistics

  
Back to Top

* * *

##  Wait Events Statistics 

  * Time Model Statistics
  * Operating System Statistics
  * Operating System Statistics - Detail
  * Foreground Wait Class
  * Foreground Wait Events
  * Background Wait Events
  * Wait Event Histogram
  * Wait Event Histogram Detail (64 msec to 2 sec)
  * Wait Event Histogram Detail (4 sec to 2 min)
  * Wait Event Histogram Detail (4 min to 1 hr)
  * Service Statistics
  * Service Wait Class Stats

Back to Top

### Time Model Statistics

  * Total time in database user-calls (DB Time): 42639.9s
  * Statistics including the word "background" measure background process time, and so do not contribute to the DB time statistic
  * Ordered by % or DB time desc, Statistic name

Statistic Name| Time (s)| % of DB Time  
---|---|---  
sql execute elapsed time| 41,466.14| 97.25  
DB CPU| 27,929.36| 65.50  
parse time elapsed| 397.25| 0.93  
hard parse elapsed time| 315.54| 0.74  
PL/SQL execution elapsed time| 107.39| 0.25  
connection management call elapsed time| 36.30| 0.09  
hard parse (sharing criteria) elapsed time| 12.02| 0.03  
failed parse elapsed time| 7.18| 0.02  
sequence load elapsed time| 2.66| 0.01  
PL/SQL compilation elapsed time| 1.85| 0.00  
inbound PL/SQL rpc elapsed time| 0.36| 0.00  
repeated bind elapsed time| 0.19| 0.00  
hard parse (bind mismatch) elapsed time| 0.07| 0.00  
DB time| 42,639.94|   
background elapsed time| 1,204.52|   
background cpu time| 946.74|   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Operating System Statistics

  * *TIME statistic values are diffed. All others display actual values. End Value is displayed if different 
  * ordered by statistic type (CPU Use, Virtual Memory, Hardware Config), Name

Statistic| Value| End Value  
---|---|---  
BUSY_TIME| 3,200,240|   
IDLE_TIME| 117,904,255|   
IOWAIT_TIME| 1,278,668|   
NICE_TIME| 1|   
SYS_TIME| 375,141|   
USER_TIME| 2,807,367|   
LOAD| 3| 4  
RSRC_MGR_CPU_WAIT_TIME| 0|   
VM_IN_BYTES| 0|   
VM_OUT_BYTES| 0|   
PHYSICAL_MEMORY_BYTES| 269,593,985,024|   
NUM_CPUS| 112|   
NUM_CPU_CORES| 56|   
NUM_CPU_SOCKETS| 4|   
GLOBAL_RECEIVE_SIZE_MAX| 4,194,304|   
GLOBAL_SEND_SIZE_MAX| 1,048,586|   
TCP_RECEIVE_SIZE_DEFAULT| 87,380|   
TCP_RECEIVE_SIZE_MAX| 6,291,456|   
TCP_RECEIVE_SIZE_MIN| 4,096|   
TCP_SEND_SIZE_DEFAULT| 16,384|   
TCP_SEND_SIZE_MAX| 4,194,304|   
TCP_SEND_SIZE_MIN| 4,096|   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Operating System Statistics - Detail


Snap Time| Load| %busy| %user| %sys| %idle| %iowait  
---|---|---|---|---|---|---  
20-Jan 08:00:22| 3.12|  |  |  |  |   
20-Jan 08:30:28| 3.63| 2.43| 2.11| 0.30| 97.57| 1.00  
20-Jan 09:00:34| 3.15| 2.67| 2.35| 0.31| 97.33| 1.09  
20-Jan 09:30:40| 3.34| 2.53| 2.21| 0.30| 97.47| 1.04  
20-Jan 10:00:46| 3.71| 2.73| 2.41| 0.31| 97.27| 1.07  
20-Jan 10:30:52| 3.31| 2.88| 2.54| 0.32| 97.12| 1.10  
20-Jan 11:00:59| 3.85| 2.61| 2.28| 0.31| 97.39| 1.03  
  
* * *

Back to Wait Events Statistics   
Back to Top

### Foreground Wait Class

  * s - second, ms - millisecond - 1000th of a second 
  * ordered by wait time desc, waits desc 
  * %Timeouts: value of 0 indicates value was < .5%. Value of null is truly 0
  * Captured Time accounts for 70.6% of Total DB time 42,639.94 (s)
  * Total FG Wait Time: 2,173.89 (s) DB CPU time: 27,929.36 (s)

Wait Class| Waits| %Time -outs| Total Wait Time (s)| Avg wait (ms)| %DB time  
---|---|---|---|---|---  
DB CPU|  |  | 27,929|  | 65.50  
Cluster| 1,223,441| 0| 834| 1| 1.96  
System I/O| 1,494,095| 0| 537| 0| 1.26  
Commit| 224,920| 0| 258| 1| 0.61  
Network| 12,308,365| 0| 248| 0| 0.58  
User I/O| 562,602| 0| 212| 0| 0.50  
Other| 243,519| 25| 39| 0| 0.09  
Application| 116,104| 0| 31| 0| 0.07  
Concurrency| 30,473| 0| 11| 0| 0.03  
Configuration| 8,282| 99| 3| 0| 0.01  
  
* * *

Back to Wait Events Statistics   
Back to Top

### Foreground Wait Events

  * s - second, ms - millisecond - 1000th of a second 
  * Only events with Total Wait Time (s) >= .001 are shown 
  * ordered by wait time desc, waits desc (idle events last) 
  * %Timeouts: value of 0 indicates value was < .5%. Value of null is truly 0

Event| Waits| %Time -outs| Total Wait Time (s)| Avg wait (ms)| Waits /txn| % DB time  
---|---|---|---|---|---|---  
control file sequential read| 1,437,851| 0| 512| 0| 2.98| 1.20  
log file sync| 224,920| 0| 258| 1| 0.47| 0.61  
gc cr block busy| 107,095| 0| 214| 2| 0.22| 0.50  
db file sequential read| 503,183| 0| 202| 0| 1.04| 0.47  
gc current block 2-way| 578,238| 0| 188| 0| 1.20| 0.44  
SQL*Net message from dblink| 60,038| 0| 188| 3| 0.12| 0.44  
gc current grant busy| 134,466| 0| 162| 1| 0.28| 0.38  
gc cr block 2-way| 312,763| 0| 137| 0| 0.65| 0.32  
SQL*Net more data to client| 4,522,962| 0| 47| 0| 9.39| 0.11  
gc cr failure| 5,086| 0| 44| 9| 0.01| 0.10  
gc cr multi block request| 20,630| 0| 33| 2| 0.04| 0.08  
gc buffer busy acquire| 13,673| 0| 32| 2| 0.03| 0.08  
log file sequential read| 56,244| 0| 25| 0| 0.12| 0.06  
enq: TX - row lock contention| 191| 0| 18| 95| 0.00| 0.04  
rdbms ipc reply| 114,637| 0| 16| 0| 0.24| 0.04  
SQL*Net more data from dblink| 15,215| 0| 10| 1| 0.03| 0.02  
DFS lock handle| 23,060| 0| 9| 0| 0.05| 0.02  
SQL*Net break/reset to client| 113,045| 0| 9| 0| 0.23| 0.02  
gc current grant 2-way| 19,170| 0| 8| 0| 0.04| 0.02  
gc cr grant 2-way| 15,528| 0| 7| 0| 0.03| 0.02  
enq: SV - contention| 2,324| 0| 4| 2| 0.00| 0.01  
library cache pin| 15,801| 0| 4| 0| 0.03| 0.01  
reliable message| 1,331| 0| 4| 3| 0.00| 0.01  
Disk file operations I/O| 47,931| 0| 4| 0| 0.10| 0.01  
enq: KO - fast object checkpoint| 2,377| 0| 4| 2| 0.00| 0.01  
direct path write| 4,109| 0| 3| 1| 0.01| 0.01  
library cache lock| 8,287| 0| 3| 0| 0.02| 0.01  
enq: HW - contention| 8,239| 100| 3| 0| 0.02| 0.01  
SQL*Net message to client| 7,573,432| 0| 3| 0| 15.72| 0.01  
name-service call wait| 34| 0| 3| 78| 0.00| 0.01  
gc cr disk read| 6,322| 0| 2| 0| 0.01| 0.01  
enq: TX - index contention| 569| 0| 2| 4| 0.00| 0.01  
gc current block congested| 4,447| 0| 2| 0| 0.01| 0.00  
gc cr block congested| 3,003| 0| 2| 1| 0.01| 0.00  
gc current block busy| 1,014| 0| 2| 1| 0.00| 0.00  
local write wait| 732| 0| 1| 2| 0.00| 0.00  
SQL*Net more data from client| 77,448| 0| 1| 0| 0.16| 0.00  
row cache lock| 4,502| 0| 1| 0| 0.01| 0.00  
db file scattered read| 918| 0| 1| 1| 0.00| 0.00  
os thread startup| 8| 0| 1| 102| 0.00| 0.00  
gc buffer busy release| 175| 0| 1| 4| 0.00| 0.00  
enq: IV - contention| 1,509| 6| 1| 0| 0.00| 0.00  
gc current multi block request| 1,103| 0| 1| 1| 0.00| 0.00  
direct path read| 2,613| 0| 1| 0| 0.01| 0.00  
IPC send completion sync| 252| 0| 1| 2| 0.00| 0.00  
enq: RO - fast object reuse| 470| 0| 0| 1| 0.00| 0.00  
enq: JQ - contention| 715| 100| 0| 0| 0.00| 0.00  
enq: FB - contention| 484| 0| 0| 0| 0.00| 0.00  
gc current grant congested| 401| 0| 0| 0| 0.00| 0.00  
ASM file metadata operation| 36,595| 0| 0| 0| 0.08| 0.00  
gc cr grant congested| 310| 0| 0| 1| 0.00| 0.00  
log file switch completion| 8| 0| 0| 17| 0.00| 0.00  
CSS initialization| 84| 0| 0| 1| 0.00| 0.00  
latch: shared pool| 36| 0| 0| 3| 0.00| 0.00  
db file parallel read| 3,003| 0| 0| 0| 0.01| 0.00  
enq: PS - contention| 105| 26| 0| 1| 0.00| 0.00  
buffer busy waits| 1,117| 0| 0| 0| 0.00| 0.00  
CSS operation: action| 84| 0| 0| 0| 0.00| 0.00  
undo segment extension| 5| 100| 0| 8| 0.00| 0.00  
asynch descriptor resize| 60,122| 100| 0| 0| 0.12| 0.00  
enq: TT - contention| 77| 0| 0| 0| 0.00| 0.00  
read by other session| 113| 0| 0| 0| 0.00| 0.00  
SQL*Net message to dblink| 59,270| 0| 0| 0| 0.12| 0.00  
library cache load lock| 9| 0| 0| 2| 0.00| 0.00  
cursor: pin S wait on X| 1| 0| 0| 20| 0.00| 0.00  
library cache: mutex X| 12| 0| 0| 2| 0.00| 0.00  
PX Deq: Slave Session Stats| 137| 0| 0| 0| 0.00| 0.00  
KJC: Wait for msg sends to complete| 278| 0| 0| 0| 0.00| 0.00  
latch free| 21| 0| 0| 1| 0.00| 0.00  
enq: MS - contention| 72| 0| 0| 0| 0.00| 0.00  
cursor: pin S| 2| 0| 0| 5| 0.00| 0.00  
CSS operation: query| 252| 0| 0| 0| 0.00| 0.00  
enq: JI - contention| 18| 0| 0| 0| 0.00| 0.00  
enq: TM - contention| 14| 100| 0| 0| 0.00| 0.00  
enq: SQ - contention| 27| 0| 0| 0| 0.00| 0.00  
PX Deq: reap credit| 1,088| 100| 0| 0| 0.00| 0.00  
latch: ges resource hash list| 105| 0| 0| 0| 0.00| 0.00  
PX Deq: Signal ACK RSG| 40| 0| 0| 0| 0.00| 0.00  
PX Deq: Signal ACK EXT| 40| 0| 0| 0| 0.00| 0.00  
gc current split| 8| 0| 0| 0| 0.00| 0.00  
enq: PI - contention| 8| 100| 0| 0| 0.00| 0.00  
latch: cache buffers chains| 106| 0| 0| 0| 0.00| 0.00  
gc current retry| 9| 0| 0| 0| 0.00| 0.00  
enq: UL - contention| 7| 100| 0| 0| 0.00| 0.00  
SQL*Net message from client| 7,573,372| 0| 7,039,641| 930| 15.72|   
jobq slave wait| 57,591| 96| 28,348| 492| 0.12|   
Streams capture: waiting for archive log| 25,699| 100| 12,842| 500| 0.05|   
KSV master wait| 73,190| 0| 20| 0| 0.15|   
single-task message| 768| 0| 14| 18| 0.00|   
PX Deq: Execution Msg| 388| 0| 0| 1| 0.00|   
PX Deq: Parse Reply| 40| 0| 0| 2| 0.00|   
PX Deq: Join ACK| 40| 0| 0| 1| 0.00|   
PX Deq: Execute Reply| 45| 0| 0| 1| 0.00|   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Background Wait Events

  * ordered by wait time desc, waits desc (idle events last) 
  * Only events with Total Wait Time (s) >= .001 are shown 
  * %Timeouts: value of 0 indicates value was < .5%. Value of null is truly 0

Event| Waits| %Time -outs| Total Wait Time (s)| Avg wait (ms)| Waits /txn| % bg time  
---|---|---|---|---|---|---  
log file parallel write| 416,440| 0| 370| 1| 0.86| 30.73  
db file parallel write| 187,865| 0| 113| 1| 0.39| 9.40  
Streams AQ: qmn coordinator waiting for slave to start| 6| 100| 36| 5917| 0.00| 2.95  
control file sequential read| 58,375| 0| 25| 0| 0.12| 2.11  
ASM file metadata operation| 115,266| 0| 19| 0| 0.24| 1.58  
control file parallel write| 15,546| 0| 17| 1| 0.03| 1.44  
LNS wait on SENDREQ| 400,869| 0| 16| 0| 0.83| 1.35  
DFS lock handle| 17,650| 100| 9| 1| 0.04| 0.75  
gcs log flush sync| 8,939| 0| 7| 1| 0.02| 0.61  
log file sequential read| 3,657| 0| 5| 1| 0.01| 0.41  
enq: WF - contention| 114| 0| 5| 40| 0.00| 0.38  
os thread startup| 165| 0| 4| 23| 0.00| 0.31  
gc current grant busy| 581| 0| 3| 6| 0.00| 0.27  
enq: TX - index contention| 10| 0| 2| 226| 0.00| 0.19  
name-service call wait| 18| 0| 1| 83| 0.00| 0.12  
enq: CO - master slave det| 3,603| 100| 1| 0| 0.01| 0.12  
ges lms sync during dynamic remastering and reconfig| 48| 67| 1| 26| 0.00| 0.10  
gc current block 2-way| 3,084| 0| 1| 0| 0.01| 0.09  
gc cr multi block request| 1,748| 0| 1| 1| 0.00| 0.08  
gc cr block 2-way| 2,336| 0| 1| 0| 0.00| 0.07  
CGS wait for IPC msg| 96,762| 100| 1| 0| 0.20| 0.06  
reliable message| 716| 0| 1| 1| 0.00| 0.05  
enq: CF - contention| 1,100| 90| 0| 0| 0.00| 0.04  
enq: TM - contention| 6| 0| 0| 63| 0.00| 0.03  
db file sequential read| 537| 0| 0| 0| 0.00| 0.02  
ksxr poll remote instances| 36,768| 100| 0| 0| 0.08| 0.02  
row cache lock| 633| 0| 0| 0| 0.00| 0.02  
row cache process| 62,909| 0| 0| 0| 0.13| 0.02  
gc cr block busy| 95| 0| 0| 2| 0.00| 0.01  
library cache pin| 516| 0| 0| 0| 0.00| 0.01  
enq: IV - contention| 500| 0| 0| 0| 0.00| 0.01  
LGWR wait for redo copy| 2,185| 0| 0| 0| 0.00| 0.01  
CSS initialization| 28| 0| 0| 4| 0.00| 0.01  
gc current block busy| 62| 0| 0| 2| 0.00| 0.01  
enq: TT - contention| 370| 29| 0| 0| 0.00| 0.01  
CSS operation: action| 124| 0| 0| 1| 0.00| 0.01  
gc current grant 2-way| 195| 0| 0| 0| 0.00| 0.01  
library cache lock| 221| 73| 0| 0| 0.00| 0.01  
libcache interrupt action by LCK| 41,020| 0| 0| 0| 0.09| 0.01  
row cache cleanup| 48,805| 0| 0| 0| 0.10| 0.01  
latch free| 160| 0| 0| 0| 0.00| 0.00  
direct path write| 88| 0| 0| 1| 0.00| 0.00  
SQL*Net more data from client| 4| 0| 0| 12| 0.00| 0.00  
db file async I/O submit| 116,748| 0| 0| 0| 0.24| 0.00  
latch: shared pool| 5| 0| 0| 8| 0.00| 0.00  
Log archive I/O| 72| 0| 0| 1| 0.00| 0.00  
asynch descriptor resize| 7,646| 100| 0| 0| 0.02| 0.00  
ges inquiry response| 137| 0| 0| 0| 0.00| 0.00  
ADR block file read| 57| 0| 0| 1| 0.00| 0.00  
log file single write| 40| 0| 0| 1| 0.00| 0.00  
Disk file operations I/O| 2,942| 0| 0| 0| 0.01| 0.00  
kfk: async disk IO| 30| 0| 0| 1| 0.00| 0.00  
enq: RO - fast object reuse| 139| 0| 0| 0| 0.00| 0.00  
CSS group registration| 16| 0| 0| 2| 0.00| 0.00  
PX Deq: reap credit| 4,597| 100| 0| 0| 0.01| 0.00  
enq: US - contention| 151| 0| 0| 0| 0.00| 0.00  
log file sync| 14| 0| 0| 2| 0.00| 0.00  
latch: messages| 394| 0| 0| 0| 0.00| 0.00  
enq: TA - contention| 71| 0| 0| 0| 0.00| 0.00  
enq: KO - fast object checkpoint| 83| 0| 0| 0| 0.00| 0.00  
gc current block congested| 26| 0| 0| 1| 0.00| 0.00  
gc current multi block request| 32| 0| 0| 1| 0.00| 0.00  
enq: PS - contention| 55| 33| 0| 0| 0.00| 0.00  
gc cr grant 2-way| 47| 0| 0| 0| 0.00| 0.00  
enq: FB - contention| 36| 0| 0| 0| 0.00| 0.00  
enq: JQ - contention| 59| 100| 0| 0| 0.00| 0.00  
SQL*Net message to client| 22,223| 0| 0| 0| 0.05| 0.00  
IPC send completion sync| 43| 0| 0| 0| 0.00| 0.00  
PX Deq: Slave Session Stats| 56| 0| 0| 0| 0.00| 0.00  
wait for scn ack| 13| 0| 0| 1| 0.00| 0.00  
latch: call allocation| 91| 0| 0| 0| 0.00| 0.00  
gc buffer busy release| 7| 0| 0| 1| 0.00| 0.00  
gc cr block congested| 13| 0| 0| 0| 0.00| 0.00  
CSS operation: data query| 32| 0| 0| 0| 0.00| 0.00  
direct path read| 20| 0| 0| 0| 0.00| 0.00  
PX Deq: Signal ACK RSG| 56| 0| 0| 0| 0.00| 0.00  
enq: HW - contention| 10| 10| 0| 0| 0.00| 0.00  
gc current split| 8| 0| 0| 0| 0.00| 0.00  
enq: PW - flush prewarm buffers| 6| 100| 0| 0| 0.00| 0.00  
gc current grant congested| 4| 0| 0| 1| 0.00| 0.00  
rdbms ipc reply| 2| 0| 0| 1| 0.00| 0.00  
enq: TX - contention| 2| 50| 0| 1| 0.00| 0.00  
enq: WL - contention| 5| 100| 0| 0| 0.00| 0.00  
enq: WR - contention| 5| 100| 0| 0| 0.00| 0.00  
enq: MW - contention| 6| 0| 0| 0| 0.00| 0.00  
latch: redo writing| 26| 0| 0| 0| 0.00| 0.00  
CSS operation: query| 68| 0| 0| 0| 0.00| 0.00  
rdbms ipc message| 1,200,976| 25| 423,492| 353| 2.49|   
gcs remote message| 4,135,026| 29| 54,030| 13| 8.58|   
class slave wait| 41,061| 0| 45,106| 1099| 0.09|   
wait for unread message on broadcast channel| 23,329| 92| 21,670| 929| 0.05|   
DIAG idle wait| 353,094| 100| 21,590| 61| 0.73|   
Space Manager: slave idle wait| 418,240| 0| 19,506| 47| 0.87|   
Streams AQ: qmn slave idle wait| 427| 1| 12,127| 28401| 0.00|   
dispatcher timer| 181| 100| 10,862| 60011| 0.00|   
ASM background timer| 73,822| 0| 10,834| 147| 0.15|   
shared server idle wait| 361| 100| 10,834| 30011| 0.00|   
PING| 4,465| 19| 10,831| 2426| 0.01|   
smon timer| 2,184| 0| 10,830| 4959| 0.00|   
pmon timer| 3,632| 99| 10,829| 2982| 0.01|   
ges remote message| 280,682| 26| 10,826| 39| 0.58|   
GCR sleep| 2,164| 100| 10,819| 5000| 0.00|   
Streams AQ: qmn coordinator idle wait| 754| 50| 10,809| 14336| 0.00|   
LNS ASYNC end of log| 416,062| 0| 10,799| 26| 0.86|   
PX Idle Wait| 115| 0| 9,657| 83978| 0.00|   
SQL*Net message from client| 29,685| 0| 79| 3| 0.06|   
KSV master wait| 8,387| 78| 2| 0| 0.02|   
PX Deq: Join ACK| 56| 0| 0| 1| 0.00|   
PX Deq: Parse Reply| 56| 0| 0| 0| 0.00|   
Streams AQ: RAC qmn coordinator idle wait| 773| 100| 0| 0| 0.00|   
PX Deq: Execute Reply| 56| 0| 0| 0| 0.00|   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Wait Event Histogram

  * Units for Total Waits column: K is 1000, M is 1000000, G is 1000000000 
  * % of Waits: value of .0 indicates value was <.05%; value of null is truly 0 
  * % of Waits: column heading of <=1s is truly <1024ms, >1s is truly >=1024ms 
  * Ordered by Event (idle events last)

|  | % of Waits  
---|---|---  
Event| Total Waits|  <1ms|  <2ms|  <4ms|  <8ms| <16ms| <32ms|  <=1s|  >1s  
ADR block file read| 57| 94.7|  |  |  | 5.3|  |  |   
ADR block file write| 15| 100.0|  |  |  |  |  |  |   
ADR file lock| 18| 100.0|  |  |  |  |  |  |   
ARCH wait for archivelog lock| 10| 100.0|  |  |  |  |  |  |   
ASM file metadata operation| 151.8K| 99.9| .1| .0| .0| .0| .0| .0|   
CGS wait for IPC msg| 96.8K| 100.0|  |  |  |  |  |  |   
CSS group registration| 16|  | 100.0|  |  |  |  |  |   
CSS initialization| 112| 42.9|  | 37.5| 19.6|  |  |  |   
CSS operation: action| 208| 84.6| 14.4| 1.0|  |  |  |  |   
CSS operation: data query| 32| 100.0|  |  |  |  |  |  |   
CSS operation: query| 320| 100.0|  |  |  |  |  |  |   
DFS lock handle| 40.7K| 96.6| 1.0| 1.4| .9| .0| .0| .0|   
Disk file operations I/O| 50.9K| 100.0|  |  |  |  |  |  |   
IPC send completion sync| 295| 91.9| 1.4| 1.4| 1.0| .3| 2.4| 1.7|   
KJC: Wait for msg sends to complete| 281| 99.3|  | .7|  |  |  |  |   
LGWR wait for redo copy| 2185| 100.0|  |  |  |  |  |  |   
LNS wait on SENDREQ| 400.8K| 100.0| .0| .0| .0|  | .0| .0|   
Log archive I/O| 72| 77.8| 13.9| 8.3|  |  |  |  |   
PX Deq: Signal ACK EXT| 96| 99.0|  | 1.0|  |  |  |  |   
PX Deq: Signal ACK RSG| 96| 99.0| 1.0|  |  |  |  |  |   
PX Deq: Slave Session Stats| 193| 99.0|  | .5| .5|  |  |  |   
PX Deq: reap credit| 5686| 100.0|  |  |  |  |  |  |   
SQL*Net break/reset to client| 113K| 99.7| .3| .0| .0|  |  |  |   
SQL*Net message from dblink| 60K| 76.5| 16.7| 3.3| 1.6| .3| .5| 1.0| .0  
SQL*Net message to client| 7594.8K| 100.0|  |  |  |  |  |  |   
SQL*Net message to dblink| 59.3K| 100.0|  |  |  |  |  |  |   
SQL*Net more data from client| 77.5K| 99.8| .1| .1| .0|  |  | .0|   
SQL*Net more data from dblink| 15.2K| 99.1| .7| .1| .0| .0|  | .1|   
SQL*Net more data to client| 4522.2K| 100.0| .0| .0| .0| .0| .0| .0|   
Streams AQ: qmn coordinator waiting for slave to start| 6|  |  |  |  |  |  |  | 100.0  
asynch descriptor resize| 67.8K| 100.0|  |  |  |  |  |  |   
buffer busy waits| 1144| 99.9| .1|  |  |  |  |  |   
buffer deadlock| 32| 100.0|  |  |  |  |  |  |   
control file parallel write| 15.5K| 39.7| 59.8| .5| .1| .0|  |  |   
control file sequential read| 1496.2K| 99.6| .3| .1| .0| .0|  | .0|   
cursor: pin S| 2| 50.0|  |  |  | 50.0|  |  |   
cursor: pin S wait on X| 1|  |  |  |  |  | 100.0|  |   
db file async I/O submit| 116.7K| 100.0|  |  |  |  |  |  |   
db file parallel read| 3004| 100.0|  |  |  |  |  |  |   
db file parallel write| 187.8K| 81.1| 18.6| .3| .0| .0| .0|  |   
db file scattered read| 919| 69.6| 15.8| 13.6| 1.0|  |  |  |   
db file sequential read| 503.8K| 99.6| .3| .1| .0| .0|  |  |   
direct path read| 2633| 100.0| .0|  |  |  |  |  |   
direct path write| 4197| 81.9| 18.0| .1|  |  |  |  |   
enq: AF - task serialization| 3| 100.0|  |  |  |  |  |  |   
enq: CF - contention| 1099| 96.5| 1.0| 2.5| .1|  |  |  |   
enq: CO - master slave det| 3603| 96.2| 1.4| 2.3| .1|  |  |  |   
enq: CR - block range reuse ckpt| 4| 100.0|  |  |  |  |  |  |   
enq: FB - contention| 516| 97.9| 1.4| .8|  |  |  |  |   
enq: FU - contention| 1| 100.0|  |  |  |  |  |  |   
enq: HW - contention| 8251| 97.8| .7| 1.4| .0|  |  |  |   
enq: IV - contention| 2009| 96.5| 2.1| 1.0| .3|  |  | .0|   
enq: JI - contention| 18| 100.0|  |  |  |  |  |  |   
enq: JQ - contention| 773| 97.3| .5| 1.9| .3|  |  |  |   
enq: JS - job run lock - synchronize| 3| 100.0|  |  |  |  |  |  |   
enq: KO - fast object checkpoint| 2460| 61.0| 20.0| 18.3| .6| .0|  | .1|   
enq: MS - contention| 72| 100.0|  |  |  |  |  |  |   
enq: MW - contention| 6| 100.0|  |  |  |  |  |  |   
enq: PI - contention| 8| 87.5|  | 12.5|  |  |  |  |   
enq: PS - contention| 160| 95.0| 1.3| 3.1| .6|  |  |  |   
enq: PW - flush prewarm buffers| 6| 83.3| 16.7|  |  |  |  |  |   
enq: RO - fast object reuse| 609| 79.5| 2.8| 13.6| 3.9|  | .2|  |   
enq: SQ - contention| 27| 100.0|  |  |  |  |  |  |   
enq: SV - contention| 2326| 96.6| 1.2| 1.6| .1|  | .0| .5|   
enq: TA - contention| 71| 98.6|  | 1.4|  |  |  |  |   
enq: TD - KTF dump entries| 1| 100.0|  |  |  |  |  |  |   
enq: TM - contention| 20| 70.0|  |  |  |  |  | 30.0|   
enq: TT - contention| 447| 97.5| .2| 2.0| .2|  |  |  |   
enq: TX - allocate ITL entry| 3| 100.0|  |  |  |  |  |  |   
enq: TX - contention| 2| 50.0| 50.0|  |  |  |  |  |   
enq: TX - index contention| 578| 94.1| 2.4| 1.7| .2|  |  | 1.6|   
enq: TX - row lock contention| 191| 48.2| 3.1| 16.8| 7.3| 2.1| 3.1| 17.8| 1.6  
enq: UL - contention| 7| 100.0|  |  |  |  |  |  |   
enq: US - contention| 151| 100.0|  |  |  |  |  |  |   
enq: WF - contention| 114| 83.3| 5.3| 1.8|  |  | .9| 8.8|   
enq: WL - contention| 5| 100.0|  |  |  |  |  |  |   
enq: WR - contention| 5| 100.0|  |  |  |  |  |  |   
gc buffer busy acquire| 13.7K| 52.8| 41.9| 4.4| .2| .2| .1| .4|   
gc buffer busy release| 183| 59.6| 30.6| 7.1| .5| 1.6|  | .5|   
gc cr block 2-way| 315.1K| 94.3| 4.0| 1.6| .0| .0| .0|  |   
gc cr block busy| 106.4K| .9| 58.0| 40.3| .8| .0|  |  |   
gc cr block congested| 3017| 89.6| 7.0| 3.1| .3|  |  |  |   
gc cr disk read| 6322| 97.7| .4| 1.9|  |  |  |  |   
gc cr failure| 5087| 1.3| 8.4| 8.1| 9.1| 73.1|  |  |   
gc cr grant 2-way| 15.6K| 96.3| 1.2| 2.4| .1|  |  |  |   
gc cr grant congested| 311| 94.2| 1.6| 4.2|  |  |  |  |   
gc cr multi block request| 22.4K| 84.0| 2.9| 3.0| 7.8| .0| 2.1| .3|   
gc current block 2-way| 581.4K| 98.3| .7| 1.0| .0| .0| .0| .0|   
gc current block busy| 1084| 33.8| 49.4| 14.4| 1.2| 1.2|  |  |   
gc current block congested| 4474| 97.3| 1.2| 1.4| .1|  |  |  |   
gc current grant 2-way| 19.4K| 97.8| .9| 1.2| .0|  |  |  |   
gc current grant busy| 135.1K| 97.4| 1.0| 1.3| .1| .0| .0| .2|   
gc current grant congested| 405| 98.3| 1.0| .7|  |  |  |  |   
gc current multi block request| 1131| 98.3| 1.2| .4| .1|  |  |  |   
gc current retry| 9| 100.0|  |  |  |  |  |  |   
gc current split| 17| 94.1| 5.9|  |  |  |  |  |   
gcs log flush sync| 8952| 69.9| 28.1| 1.9| .0| .0|  |  |   
ges inquiry response| 137| 98.5|  | 1.5|  |  |  |  |   
ges lms sync during dynamic remastering and reconfig| 48| 16.7| 16.7|  |  |  | 33.3| 33.3|   
ges2 LMON to wake up LMD - mrcvr| 4| 100.0|  |  |  |  |  |  |   
global enqueue expand wait| 1| 100.0|  |  |  |  |  |  |   
kfk: async disk IO| 30| 73.3| 26.7|  |  |  |  |  |   
ksxr poll remote instances| 36.8K| 100.0|  |  |  |  |  |  |   
latch free| 181| 96.1|  |  | 3.3| .6|  |  |   
latch: active service list| 1| 100.0|  |  |  |  |  |  |   
latch: cache buffers chains| 122| 100.0|  |  |  |  |  |  |   
latch: cache buffers lru chain| 2| 100.0|  |  |  |  |  |  |   
latch: call allocation| 92| 100.0|  |  |  |  |  |  |   
latch: checkpoint queue latch| 1| 100.0|  |  |  |  |  |  |   
latch: enqueue hash chains| 4| 100.0|  |  |  |  |  |  |   
latch: gc element| 2| 100.0|  |  |  |  |  |  |   
latch: gcs resource hash| 9| 100.0|  |  |  |  |  |  |   
latch: ges resource hash list| 112| 100.0|  |  |  |  |  |  |   
latch: messages| 394| 100.0|  |  |  |  |  |  |   
latch: redo allocation| 4| 100.0|  |  |  |  |  |  |   
latch: redo writing| 26| 100.0|  |  |  |  |  |  |   
latch: row cache objects| 23| 100.0|  |  |  |  |  |  |   
latch: shared pool| 41| 68.3| 4.9| 4.9| 4.9| 7.3| 9.8|  |   
libcache interrupt action by LCK| 41K| 100.0|  |  |  |  |  |  |   
library cache load lock| 9| 22.2|  | 55.6| 22.2|  |  |  |   
library cache lock| 8508| 97.2| 1.1| 1.4| .2| .0|  |  |   
library cache pin| 16.3K| 97.8| .8| 1.4| .1|  |  |  |   
library cache: mutex X| 12| 83.3|  |  |  | 16.7|  |  |   
local write wait| 732|  | 67.2| 32.8|  |  |  |  |   
log file parallel write| 416.4K| 77.6| 21.1| 1.2| .1| .0| .0| .0|   
log file sequential read| 59.9K| 91.6| 5.3| 2.8| .3|  |  |  |   
log file single write| 40| 82.5| 17.5|  |  |  |  |  |   
log file switch completion| 8|  | 25.0|  |  | 25.0| 50.0|  |   
log file sync| 224.9K| 49.4| 46.3| 4.1| .2| .0| .0| .0|   
name-service call wait| 52| 1.9|  |  | 1.9| 3.8| 1.9| 90.4|   
os thread startup| 173|  |  |  |  | 17.3| 72.3| 10.4|   
rdbms ipc reply| 114.6K| 99.4| .2| .1| .3| .0| .0| .0|   
read by other session| 113| 99.1| .9|  |  |  |  |  |   
reliable message| 2047| 30.8| 53.8| 9.6| 1.5| .3| 2.9| 1.1|   
row cache cleanup| 48.8K| 100.0|  | .0|  |  |  |  |   
row cache lock| 5132| 98.7| .7| .5| .1|  |  |  |   
row cache process| 62.9K| 100.0|  |  |  |  |  |  |   
undo segment extension| 5| 40.0|  |  |  | 40.0| 20.0|  |   
wait for scn ack| 13| 100.0|  |  |  |  |  |  |   
ASM background timer| 73.8K| 86.0| 3.8| .1| .0| .0| .0| 4.3| 5.7  
DIAG idle wait| 353.1K| .1| .0| .0| .0| 2.0| 80.2| 17.7|   
GCR sleep| 2165|  |  |  |  |  |  |  | 100.0  
KSV master wait| 81.6K| 99.8| .1| .0| .0| .0| .0| .0|   
LNS ASYNC end of log| 416K| 16.4| 16.0| 13.3| 14.8| 11.2| 9.3| 19.0|   
PING| 4465| 79.2| .2| .5|  | .1| .9| .1| 19.0  
PX Deq: Execute Reply| 101| 83.2|  | 16.8|  |  |  |  |   
PX Deq: Execution Msg| 388| 90.2| 7.2| 1.0| .8| .3| .3| .3|   
PX Deq: Join ACK| 96| 58.3| 31.3| 7.3|  | 2.1| 1.0|  |   
PX Deq: Parse Reply| 96| 86.5| 9.4| 2.1| 1.0|  |  | 1.0|   
PX Idle Wait| 97| 11.3| 4.1| 2.1| 6.2| 8.2| 20.6| 7.2| 40.2  
SQL*Net message from client| 7602.6K| 66.8| 11.5| 5.0| 2.0| 1.4| 2.0| 9.5| 1.8  
Space Manager: slave idle wait| 418.2K| 15.1| 16.6| 13.5| 15.0| 11.2| 9.3| 19.0| .4  
Streams AQ: RAC qmn coordinator idle wait| 773| 100.0|  |  |  |  |  |  |   
Streams AQ: qmn coordinator idle wait| 754| 50.0|  |  |  |  |  |  | 50.0  
Streams AQ: qmn slave idle wait| 427|  |  |  |  |  |  |  | 100.0  
Streams capture: waiting for archive log| 25.7K|  |  |  |  |  |  | 100.0|   
class slave wait| 41.1K| 3.7| 6.1| 12.7| 2.4| .7| .2| 32.8| 41.5  
dispatcher timer| 181|  |  |  |  |  |  |  | 100.0  
gcs remote message| 4133.1K| 23.8| 7.1| 8.4| 13.2| 11.2| 36.2| .1|   
ges remote message| 280.7K| 36.9| 3.2| 3.0| 3.6| 5.9| 6.8| 40.6|   
jobq slave wait| 57.6K| .5| .2| .1| .0| .0| .0| 99.2|   
pmon timer| 3633| .4|  |  |  |  |  | .2| 99.3  
rdbms ipc message| 1200.1K| 41.4| 4.0| 5.0| 4.4| 4.5| 3.9| 27.7| 9.2  
shared server idle wait| 361|  |  |  |  |  |  |  | 100.0  
single-task message| 768|  |  |  |  | 16.0| 84.0|  |   
smon timer| 2182|  |  |  |  |  |  | .3| 99.7  
wait for unread message on broadcast channel| 23.3K| 7.1| .0|  |  | .0|  | 92.9|   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Wait Event Histogram Detail (64 msec to 2 sec)

  * Units for Total Waits column: K is 1000, M is 1000000, G is 1000000000 
  * Units for % of Total Waits: ms is milliseconds s is 1024 milliseconds (approximately 1 second) 
  * % of Total Waits: total waits for all wait classes, including Idle 
  * % of Total Waits: value of .0 indicates value was <.05%; value of null is truly 0 
  * Ordered by Event (only non-idle events are displayed)

|  | % of Total Waits  
---|---|---  
Event| Waits 64ms to 2s| <32ms| <64ms| <1/8s| <1/4s| <1/2s|  <1s|  <2s| >=2s  
ASM file metadata operation| 17| 100.0| .0| .0| .0|  |  |  |   
DFS lock handle| 10| 100.0| .0| .0|  |  |  |  |   
IPC send completion sync| 5| 98.3| 1.7|  |  |  |  |  |   
LNS wait on SENDREQ| 6| 100.0| .0| .0|  |  |  |  |   
SQL*Net message from dblink| 642| 98.9| .4| .3| .2| .1| .1| .0| .0  
SQL*Net more data from client| 1| 100.0| .0|  |  |  |  |  |   
SQL*Net more data from dblink| 9| 99.9|  |  |  | .0| .0|  |   
SQL*Net more data to client| 110| 100.0| .0| .0| .0| .0| .0|  |   
control file sequential read| 1| 100.0| .0|  |  |  |  |  |   
enq: IV - contention| 1| 100.0| .0|  |  |  |  |  |   
enq: KO - fast object checkpoint| 2| 99.9|  |  |  | .0| .0|  |   
enq: SV - contention| 11| 99.5| .0| .0| .1| .2| .0|  |   
enq: TM - contention| 6| 70.0| 10.0| 20.0|  |  |  |  |   
enq: TX - index contention| 9| 98.4|  | .2|  | .7| .7|  |   
enq: TX - row lock contention| 37| 80.6| 1.0| 2.6| 4.2| 3.1| 6.8| 1.6|   
enq: WF - contention| 10| 91.2| .9| 1.8|  | 2.6| 3.5|  |   
gc buffer busy acquire| 54| 99.6| .1| .0| .1| .1| .1|  |   
gc buffer busy release| 1| 99.5|  |  |  |  | .5|  |   
gc cr multi block request| 62| 99.7| .2| .1| .0| .0|  |  |   
gc current block 2-way| 1| 100.0| .0|  |  |  |  |  |   
gc current grant busy| 287| 99.8| .0| .0| .1| .1| .1|  |   
ges lms sync during dynamic remastering and reconfig| 16| 66.7| 33.3|  |  |  |  |  |   
log file parallel write| 1| 100.0| .0|  |  |  |  |  |   
log file sync| 2| 100.0| .0|  |  |  |  |  |   
name-service call wait| 47| 9.6| 11.5| 78.8|  |  |  |  |   
os thread startup| 18| 89.6|  | 10.4|  |  |  |  |   
rdbms ipc reply| 3| 100.0| .0| .0|  |  |  |  |   
reliable message| 23| 98.9| .9| .2|  |  |  |  |   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Wait Event Histogram Detail (4 sec to 2 min)

  * Units for Total Waits column: K is 1000, M is 1000000, G is 1000000000 
  * Units for % of Total Waits: s is 1024 milliseconds (approximately 1 second) m is 64*1024 milliseconds (approximately 67 seconds or 1.1 minutes) 
  * % of Total Waits: total waits for all wait classes, including Idle 
  * % of Total Waits: value of .0 indicates value was <.05%; value of null is truly 0 
  * Ordered by Event (only non-idle events are displayed)

|  | % of Total Waits  
---|---|---  
Event| Waits 4s to 2m| <2s|  <4s|  <8s| <16s| <32s| < 1m| < 2m| >=2m  
SQL*Net message from dblink| 5| 100.0| .0|  |  |  |  |  |   
Streams AQ: qmn coordinator waiting for slave to start| 6|  |  | 100.0|  |  |  |  |   
  
* * *

Back to Wait Events Statistics   
Back to Top

### Wait Event Histogram Detail (4 min to 1 hr)

No data exists for this section of the report. 

Back to Wait Events Statistics   
Back to Top

### Service Statistics

  * ordered by DB Time

Service Name| DB Time (s)| DB CPU (s)| Physical Reads (K)| Logical Reads (K)  
---|---|---|---|---  
orcl| 41,307| 27,392| 730,473| 3,057,607  
SYS$USERS| 1,333| 538| 17| 138,121  
SYS$BACKGROUND| 0| 0| 2| 1,063  
orclXDB| 0| 0| 0| 0  
  
* * *

Back to Wait Events Statistics   
Back to Top

### Service Wait Class Stats

  * Wait Class info for services in the Service Statistics section. 
  * Total Waits and Time Waited displayed for the following wait classes: User I/O, Concurrency, Administrative, Network 
  * Time Waited (Wt Time) in seconds

Service Name| User I/O Total Wts| User I/O Wt Time| Concurcy Total Wts| Concurcy Wt Time| Admin Total Wts| Admin Wt Time| Network Total Wts| Network Wt Time  
---|---|---|---|---|---|---|---|---  
orcl | 515275| 202| 23985| 9| 0| 0| 11938460| 101  
SYS$USERS | 47327| 10| 6488| 2| 0| 0| 370631| 147  
SYS$BACKGROUND | 3588| 0| 42617| 7| 0| 0| 400876| 16  
  
* * *

Back to Wait Events Statistics   
Back to Top

##  SQL Statistics 

  * SQL ordered by Elapsed Time
  * SQL ordered by CPU Time
  * SQL ordered by User I/O Wait Time
  * SQL ordered by Gets
  * SQL ordered by Reads
  * SQL ordered by Physical Reads (UnOptimized)
  * SQL ordered by Executions
  * SQL ordered by Parse Calls
  * SQL ordered by Sharable Memory
  * SQL ordered by Version Count
  * SQL ordered by Cluster Wait Time
  * Complete List of SQL Text

Back to Top

### SQL ordered by Elapsed Time

  * Resources reported for PL/SQL code includes the resources used by all SQL statements called by the code. 
  * % Total DB Time is the Elapsed Time of the SQL statement divided into the Total Database Time multiplied by 100 
  * %Total - Elapsed Time as a percentage of Total DB time 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Captured SQL account for 88.0% of Total DB Time (s): 42,640
  * Captured PL/SQL account for 3.2% of Total DB Time (s): 42,640

Elapsed Time (s)| Executions | Elapsed Time per Exec (s) | %Total| %CPU| %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---  
10,836.38| 0|  | 25.41| 55.70| 0.00| 48v6k1d4s1txt |  JDBC Thin Client  | select * from qyhYzkbOpIncomeC...  
8,184.03| 352| 23.25| 19.19| 34.22| 0.00| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
3,531.25| 735| 4.80| 8.28| 99.74| 0.00| 8nbhkyycmx838 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
2,498.29| 352| 7.10| 5.86| 21.98| 0.00| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
1,368.34| 2,477| 0.55| 3.21| 99.67| 0.00| 5965cwv3r2tz3 |  JDBC Thin Client  | select obsettleac0_.ID as ID10...  
1,265.90| 114| 11.10| 2.97| 99.75| 0.00| 2u395bhfbhg99 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
1,228.85| 324| 3.79| 2.88| 99.71| 0.01| g1mygga3s3mcz |  | select pat_index_no, treat_car...  
1,003.61| 481| 2.09| 2.35| 99.40| 0.00| cdxqhvdmm89mb |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT "ELECTRONIC_CARD_NO", "...  
962.65| 19,991| 0.05| 2.26| 98.46| 0.00| 11523cnuz91yv |  JDBC Thin Client  | select bedallrese0_.uuid as uu...  
726.56| 44,658| 0.02| 1.70| 97.46| 0.00| caz5v85xqv2nr |  JDBC Thin Client  | BEGIN PG_HIS_ELECTRONICBILLS.p...  
627.85| 1,050| 0.60| 1.47| 99.72| 0.00| dvhc0bwbs7q52 |  JDBC Thin Client  | SELECT COUNT(1) FROM T_OB_SETT...  
573.59| 78,823| 0.01| 1.35| 91.62| 0.00| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
483.10| 2,855| 0.17| 1.13| 95.69| 0.00| 12nd0kqpvd8xn |  JDBC Thin Client  | select visit0_.ID as ID160_, v...  
471.64| 46,841| 0.01| 1.11| 17.07| 9.17| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by CPU Time

  * Resources reported for PL/SQL code includes the resources used by all SQL statements called by the code. 
  * %Total - CPU Time as a percentage of Total DB CPU 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Captured SQL account for 84.1% of Total CPU Time (s): 27,929
  * Captured PL/SQL account for 4.4% of Total CPU Time (s): 27,929

CPU Time (s)| Executions | CPU per Exec (s)| %Total| Elapsed Time (s)| %CPU| %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---|---  
6,036.31| 0|  | 21.61| 10,836.38| 55.70| 0.00| 48v6k1d4s1txt |  JDBC Thin Client  | select * from qyhYzkbOpIncomeC...  
3,522.03| 735| 4.79| 12.61| 3,531.25| 99.74| 0.00| 8nbhkyycmx838 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
2,800.60| 352| 7.96| 10.03| 8,184.03| 34.22| 0.00| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
1,363.80| 2,477| 0.55| 4.88| 1,368.34| 99.67| 0.00| 5965cwv3r2tz3 |  JDBC Thin Client  | select obsettleac0_.ID as ID10...  
1,262.73| 114| 11.08| 4.52| 1,265.90| 99.75| 0.00| 2u395bhfbhg99 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
1,225.32| 324| 3.78| 4.39| 1,228.85| 99.71| 0.01| g1mygga3s3mcz |  | select pat_index_no, treat_car...  
997.58| 481| 2.07| 3.57| 1,003.61| 99.40| 0.00| cdxqhvdmm89mb |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT "ELECTRONIC_CARD_NO", "...  
947.82| 19,991| 0.05| 3.39| 962.65| 98.46| 0.00| 11523cnuz91yv |  JDBC Thin Client  | select bedallrese0_.uuid as uu...  
708.14| 44,658| 0.02| 2.54| 726.56| 97.46| 0.00| caz5v85xqv2nr |  JDBC Thin Client  | BEGIN PG_HIS_ELECTRONICBILLS.p...  
626.07| 1,050| 0.60| 2.24| 627.85| 99.72| 0.00| dvhc0bwbs7q52 |  JDBC Thin Client  | SELECT COUNT(1) FROM T_OB_SETT...  
549.07| 352| 1.56| 1.97| 2,498.29| 21.98| 0.00| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
525.55| 78,823| 0.01| 1.88| 573.59| 91.62| 0.00| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
462.29| 2,855| 0.16| 1.66| 483.10| 95.69| 0.00| 12nd0kqpvd8xn |  JDBC Thin Client  | select visit0_.ID as ID160_, v...  
400.68| 335| 1.20| 1.43| 402.08| 99.65| 0.00| 84aqh3u98gdk2 |  JDBC Thin Client  | select mtinspecta0_.apply_id a...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by User I/O Wait Time

  * Resources reported for PL/SQL code includes the resources used by all SQL statements called by the code. 
  * %Total - User I/O Time as a percentage of Total User I/O Wait time 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Captured SQL account for 79.2% of Total User I/O Wait Time (s): 212
  * Captured PL/SQL account for 0.5% of Total User I/O Wait Time (s): 212

User I/O Time (s)| Executions | UIO per Exec (s)| %Total| Elapsed Time (s)| %CPU| %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---|---  
78.60| 8| 9.82| 37.07| 198.50| 60.53| 39.60| 5qnpb11bzakp0 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
43.24| 46,841| 0.00| 20.39| 471.64| 17.07| 9.17| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
15.75| 33,801| 0.00| 7.43| 134.21| 26.09| 11.73| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
13.85| 10| 1.38| 6.53| 16.19| 16.56| 85.53| 2mdx9t6xxn3x6 |  JDBC Thin Client  | select SUM(IMPORT_QUANTITY) AS...  
10.23| 16| 0.64| 4.82| 14.50| 17.10| 70.55| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
5.01| 1| 5.01| 2.37| 8.83| 22.48| 56.79| gjm43un5cy843 |  | SELECT SUM(USED), SUM(TOTAL) F...  
0.61| 241| 0.00| 0.29| 74.33| 6.51| 0.83| d45qmb31zqpch |  | DECLARE job BINARY_INTEGER := ...  
0.38| 416| 0.00| 0.18| 43.97| 81.27| 0.87| dz7vaztm8008c |  JDBC Thin Client  | BEGIN PG_HIS_SQ.occupyNumberSo...  
0.28| 676| 0.00| 0.13| 1.89| 25.68| 14.69| 9af3pdtxg6jvt |  | INSERT INTO WOPB.DPB_OP_DISPEN...  
0.23| 4,616| 0.00| 0.11| 9.95| 9.68| 2.29| 2rajyj0wtnxgg |  JDBC Thin Client  | insert into T_ODW_ORDERBILLING...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Gets

  * Resources reported for PL/SQL code includes the resources used by all SQL statements called by the code. 
  * %Total - Buffer Gets as a percentage of Total Buffer Gets 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Total Buffer Gets: 3,196,935,601
  * Captured SQL account for 80.4% of Total

Buffer Gets | Executions| Gets per Exec | %Total| Elapsed Time (s)|  %CPU|  %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---|---  
495,708,302| 352| 1,408,262.22| 15.51| 8,184.03| 34.2| 0| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
341,044,916| 735| 464,006.69| 10.67| 3,531.25| 99.7| 0| 8nbhkyycmx838 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
316,699,730| 2,855| 110,928.10| 9.91| 483.10| 95.7| 0| 12nd0kqpvd8xn |  JDBC Thin Client  | select visit0_.ID as ID160_, v...  
241,605,863| 2,477| 97,539.71| 7.56| 1,368.34| 99.7| 0| 5965cwv3r2tz3 |  JDBC Thin Client  | select obsettleac0_.ID as ID10...  
170,541,946| 352| 484,494.16| 5.33| 2,498.29| 22| 0| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
169,378,214| 2,341| 72,352.93| 5.30| 245.91| 98.5| 0| d3uu56jx39a2j |  JDBC Thin Client  | select * from urm.esb_pm_dr_re...  
153,251,880| 19,991| 7,666.04| 4.79| 962.65| 98.5| 0| 11523cnuz91yv |  JDBC Thin Client  | select bedallrese0_.uuid as uu...  
113,051,557| 44,658| 2,531.50| 3.54| 726.56| 97.5| 0| caz5v85xqv2nr |  JDBC Thin Client  | BEGIN PG_HIS_ELECTRONICBILLS.p...  
102,458,035| 1,050| 97,579.08| 3.20| 627.85| 99.7| 0| dvhc0bwbs7q52 |  JDBC Thin Client  | SELECT COUNT(1) FROM T_OB_SETT...  
69,189,041| 78,823| 877.78| 2.16| 573.59| 91.6| 0| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
55,572,622| 9| 6,174,735.78| 1.74| 125.24| 99.7| 0| f0czvj8ah7dtt |  JDBC Thin Client  | SELECT * FROM ( SELECT TMP_PAG...  
45,154,506| 14| 3,225,321.86| 1.41| 117.48| 99.1| 0| 6gdn0m2zkmbz7 |  | DECLARE job BINARY_INTEGER := ...  
42,219,389| 1,084| 38,947.78| 1.32| 322.67| 75.7| .1| 8hs1qzm4j4zqk |  JDBC Thin Client  | select reg_id, visit_id, card_...  
41,828,756| 324| 129,101.10| 1.31| 1,228.85| 99.7| 0| g1mygga3s3mcz |  | select pat_index_no, treat_car...  
41,456,826| 481| 86,188.83| 1.30| 1,003.61| 99.4| 0| cdxqhvdmm89mb |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT "ELECTRONIC_CARD_NO", "...  
39,642,321| 35| 1,132,637.74| 1.24| 192.65| 99.7| 0| 6744kvtnv7utw |  JDBC Thin Client  | select q.invoice_id, q.YYJB, (...  
35,761,526| 14| 2,554,394.71| 1.12| 121.11| 98.6| 0| ggd2znk56cwt0 |  | DECLARE job BINARY_INTEGER := ...  
33,582,392| 2,999| 11,197.86| 1.05| 41.39| 95.9| 0| 3mbzwp1hudumm |  JDBC Thin Client  | SELECT * FROM ( SELECT TMP_PAG...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Reads

  * %Total - Physical Reads as a percentage of Total Disk Reads 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Total Disk Reads: 730,576,196
  * Captured SQL account for 99.9% of Total

Physical Reads| Executions| Reads per Exec | %Total| Elapsed Time (s)| %CPU| %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---|---  
469,146,040| 352| 1,332,801.25| 64.22| 8,184.03| 34.22| 0.00| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
169,794,990| 352| 482,372.13| 23.24| 2,498.29| 21.98| 0.00| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
53,030,118| 0|  | 7.26| 10,836.38| 55.70| 0.00| 48v6k1d4s1txt |  JDBC Thin Client  | select * from qyhYzkbOpIncomeC...  
19,696,244| 23| 856,358.43| 2.70| 309.34| 14.72| 0.00| 7tsw7k06q9x42 |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT "ID", "IDENTIFIER_ID", ...  
13,345,248| 16| 834,078.00| 1.83| 219.14| 15.64| 0.00| g56xnb42pv9t4 |  JDBC Thin Client  | select A.ID as ROWKEY , A.* fr...  
4,206,268| 12| 350,522.33| 0.58| 216.45| 73.65| 0.00| a0kfc05k3nz99 |  | select doctavaila0_.fda_id as ...  
207,329| 8| 25,916.13| 0.03| 198.50| 60.53| 39.60| 5qnpb11bzakp0 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
114,906| 46,841| 2.45| 0.02| 471.64| 17.07| 9.17| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
38,978| 33,801| 1.15| 0.01| 134.21| 26.09| 11.73| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
35,931| 10| 3,593.10| 0.00| 16.19| 16.56| 85.53| 2mdx9t6xxn3x6 |  JDBC Thin Client  | select SUM(IMPORT_QUANTITY) AS...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Physical Reads (UnOptimized)

  * UnOptimized Read Reqs = Physical Read Reqts - Optimized Read Reqs 
  * %Opt - Optimized Reads as percentage of SQL Read Requests 
  * %Total - UnOptimized Read Reqs as a percentage of Total UnOptimized Read Reqs
  * Total Physical Read Requests: 13,742,520
  * Captured SQL account for 104.5% of Total
  * Total UnOptimized Read Requests: 13,742,520
  * Captured SQL account for 104.5% of Total
  * Total Optimized Read Requests: 1
  * Captured SQL account for 0.0% of Total

UnOptimized Read Reqs| Physical Read Reqs| Executions| UnOptimized Reqs per Exec| %Opt| %Total|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---  
7,871,846| 7,871,846| 0|  | 0.00| 57.28| 48v6k1d4s1txt |  JDBC Thin Client  | select * from qyhYzkbOpIncomeC...  
3,681,663| 3,681,663| 352| 10,459.27| 0.00| 26.79| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
1,334,478| 1,334,478| 352| 3,791.13| 0.00| 9.71| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
997,264| 997,264| 16,256| 61.35| 0.00| 7.26| dr97hbjraumrm |  OGG-HISEA0-OCI_META_THREAD  | SELECT 1 FROM V$LOGFILE WHERE(...  
207,010| 207,010| 8| 25,876.25| 0.00| 1.51| 5qnpb11bzakp0 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
154,624| 154,624| 23| 6,722.78| 0.00| 1.13| 7tsw7k06q9x42 |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT "ID", "IDENTIFIER_ID", ...  
104,768| 104,768| 16| 6,548.00| 0.00| 0.76| g56xnb42pv9t4 |  JDBC Thin Client  | select A.ID as ROWKEY , A.* fr...  
2,459| 2,459| 33,801| 0.07| 0.00| 0.02| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
1,638| 1,638| 416| 3.94| 0.00| 0.01| dz7vaztm8008c |  JDBC Thin Client  | BEGIN PG_HIS_SQ.occupyNumberSo...  
1,348| 1,348| 241| 5.59| 0.00| 0.01| d45qmb31zqpch |  | DECLARE job BINARY_INTEGER := ...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Executions

  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time
  * Total Executions: 13,595,239
  * Captured SQL account for 25.3% of Total

Executions | Rows Processed| Rows per Exec| Elapsed Time (s)|  %CPU|  %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---  
388,908| 2,439,216| 6.27| 50.16| 97.2| 0| 7ahdc26dxpwfu |  | UPDATE WDP.DPC_STORAGE_DRUG G ...  
388,908| 388,908| 1.00| 32.49| 99.7| 0| f72rtznv1afds |  | SELECT COUNT(*) FROM WDP.DPC_S...  
300,580| 300,580| 1.00| 27.61| 99.5| 0| 39vzujk1r12gw |  | SELECT COUNT(1) FROM T_SM_PARA...  
294,296| 253,076| 0.86| 13.11| 47.3| 0| 0jyvx0fff62jb |  JDBC Thin Client  | select paraitem0_.ID as ID255_...  
240,464| 240,464| 1.00| 2.58| 102.2| 0| gsnna7vkctvdp |  | SELECT P.ID FROM T_SM_PARAITEM...  
237,839| 0| 0.00| 5.24| 36.8| 0| 13j5ux5tz7kws |  JDBC Thin Client  | select emrbedlist0_.bed_id as ...  
229,388| 229,375| 1.00| 8.43| 40.5| 0| bgnt3bpd2b04f |  JDBC Thin Client  | select CURRENT_TIMESTAMP as co...  
180,348| 180,348| 1.00| 15.88| 98| 0| 5nz3dctx1y13j |  | SELECT COUNT(1) FROM T_SM_PARA...  
80,387| 78,820| 0.98| 227.41| 92.4| 0| 1hhg7sfy5d46f |  JDBC Thin Client  | select 1 from USER_TABLES t wh...  
78,823| 172,284| 2.19| 573.59| 91.6| 0| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Parse Calls

  * Total Parse Calls: 3,543,284
  * Captured SQL account for 62.6% of Total

Parse Calls| Executions | % Total Parses|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---  
300,580| 300,580| 8.48| 39vzujk1r12gw |  | SELECT COUNT(1) FROM T_SM_PARA...  
294,299| 294,296| 8.31| 0jyvx0fff62jb |  JDBC Thin Client  | select paraitem0_.ID as ID255_...  
240,464| 240,464| 6.79| gsnna7vkctvdp |  | SELECT P.ID FROM T_SM_PARAITEM...  
229,394| 229,388| 6.47| bgnt3bpd2b04f |  JDBC Thin Client  | select CURRENT_TIMESTAMP as co...  
180,348| 180,348| 5.09| 5nz3dctx1y13j |  | SELECT COUNT(1) FROM T_SM_PARA...  
80,388| 80,387| 2.27| 1hhg7sfy5d46f |  JDBC Thin Client  | select 1 from USER_TABLES t wh...  
78,823| 78,823| 2.22| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
64,931| 64,930| 1.83| 6pqru4undjfj5 |  JDBC Thin Client  | select version from t_sm_dbloc...  
62,417| 62,417| 1.76| cwvq44dwhaw9j |  JDBC Thin Client  | SELECT * FROM TABLE(PG_JSONUTI...  
59,545| 59,545| 1.68| 97a6ts33jd0ba |  ISServerExec.exe  | INSERT INTO "HISUSER"."BI_FACT...  
53,200| 53,200| 1.50| 4bd22u3q0p7mp |  JDBC Thin Client  | update t_sm_dblock set version...  
46,840| 46,841| 1.32| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
46,663| 46,663| 1.32| d642fkkxqhs98 |  JDBC Thin Client  | select ID from T_SM_EXTERNAL_S...  
46,527| 46,527| 1.31| 9qc6r0wu94sqg |  JDBC Thin Client  | select externalsy0_.ID as ID17...  
44,659| 44,658| 1.26| caz5v85xqv2nr |  JDBC Thin Client  | BEGIN PG_HIS_ELECTRONICBILLS.p...  
36,937| 36,832| 1.04| cm5vu20fhtnq1 |  | select /*+ connect_by_filterin...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Sharable Memory

  * Only Statements with Sharable Memory greater than 1048576 are displayed

Sharable Mem (b)| Executions | % Total|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---  
534,420,771| 19,991| 2.44| 11523cnuz91yv |  JDBC Thin Client  | select bedallrese0_.uuid as uu...  
286,908,888| 237,839| 1.31| 13j5ux5tz7kws |  JDBC Thin Client  | select emrbedlist0_.bed_id as ...  
43,641,633| 118| 0.20| dw9qd5d0pn687 |  JDBC Thin Client  | SELECT X.SUBOR_WARD_ID, X.SUBO...  
40,151,400|  | 0.18| 68vcxdwvu2g0z |  | /* MV_REFRESH (INS) */ INSERT ...  
38,655,568|  | 0.18| 7sccjnr8zm8ht |  | /* MV_REFRESH (INS) */ INSERT ...  
29,633,160|  | 0.14| a8kmz6qtudcmn |  | /* MV_REFRESH (INS) */ INSERT ...  
11,469,718| 16| 0.05| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
10,452,318| 16| 0.05| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
10,378,374| 16| 0.05| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
10,333,294| 16| 0.05| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
8,659,202| 46,841| 0.04| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
8,500,623| 649| 0.04| 97d6ah8gw4f6u |  JDBC Thin Client  | update bab_bed_allocation set ...  
4,616,411| 7,679| 0.02| az33m61ym46y4 |  JDBC Thin Client  | SELECT NULL AS table_cat, o.ow...  
3,346,169| 41| 0.02| gxn6jnu7qx2vw |  JDBC Thin Client  | select t.* from hisuser.add_zy...  
3,200,740| 40| 0.01| g2cqspstx3awz |  JDBC Thin Client  | insert into bab_bed_allocation...  
2,699,683| 3,274| 0.01| dv474vaz39154 |  JDBC Thin Client  | select patName, visitId, deptI...  
2,638,766| 33,801| 0.01| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
2,182,151| 1| 0.01| f1jpfkf5c955q |  JDBC Thin Client  | select idworderbi0_.id as id27...  
2,116,251| 550| 0.01| 8xwunw9vbjc5t |  JDBC Thin Client  | update cure_apply set created_...  
2,098,024| 262| 0.01| 4nh3ub5zdrbbf |  JDBC Thin Client  | select interlist0_.FINTER_ID a...  
2,093,811| 262| 0.01| 9m5ur86a3v85h |  JDBC Thin Client  | select interoutwa0_.FOUT_WAY_I...  
1,711,685| 1,862| 0.01| f2xfzfr3pjh3q |  JDBC Thin Client  | select t.* from hisuser.dgby_o...  
1,668,362| 7| 0.01| 9m82p8p2d7z84 |  | select OBJOID, CLSOID, RUNTIME...  
1,564,556| 676| 0.01| 5x20uhxy5qbjf |  | INSERT INTO WOPB.DPT_EMR_PRESP...  
1,445,857| 676| 0.01| 9af3pdtxg6jvt |  | INSERT INTO WOPB.DPB_OP_DISPEN...  
1,400,368| 37| 0.01| 98vc0ayk19rbk |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
1,348,594| 3| 0.01| 47zf852ccf4qd |  JDBC Thin Client  | SELECT t.* FROM (select * from...  
1,232,228| 50| 0.01| 2ftuy4q1xa9md |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
1,151,476| 21| 0.01| 2x9u0gw4gh4x6 |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
1,134,190| 211| 0.01| 7ng34ruy5awxq |  | select i.obj#, i.ts#, i.file#,...  
1,073,512| 69| 0.00| b4nc4nnx3fhf5 |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Version Count

  * Only Statements with Version Count greater than 20 are displayed

Version Count | Executions |  SQL Id| SQL Module| SQL Text  
---|---|---|---|---  
550| 46,841| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
504|  | a8kmz6qtudcmn |  | /* MV_REFRESH (INS) */ INSERT ...  
471|  | 68vcxdwvu2g0z |  | /* MV_REFRESH (INS) */ INSERT ...  
465|  | 7sccjnr8zm8ht |  | /* MV_REFRESH (INS) */ INSERT ...  
342| 33,801| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
61| 757| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
61| 757| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
61| 757| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
61| 757| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
61| 757| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
54| 55| 47rjnu9vtspmy |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
54| 12| 69k5bhm12sz98 |  | SELECT dbin.instance_number, d...  
53| 42| 5r5pa47z6zauj |  JDBC Thin Client  | INSERT INTO BAC_SHEDLOCK(name,...  
52| 21| 2x9u0gw4gh4x6 |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
49| 228| 150m85pbj62gc |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
49| 25| 720d7u76g8wjr |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
45| 16| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
45| 16| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
45| 16| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
45| 16| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
45| 211| 7ng34ruy5awxq |  | select i.obj#, i.ts#, i.file#,...  
43| 649| 97d6ah8gw4f6u |  JDBC Thin Client  | update bab_bed_allocation set ...  
42| 50| 2ftuy4q1xa9md |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
42| 37| 98vc0ayk19rbk |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
42| 69| b4nc4nnx3fhf5 |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
40| 757| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
40| 757| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
40| 757| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
40| 757| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
40| 757| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
39| 314| 1krt4fdxy59ds |  JDBC Thin Client  | UPDATE BAC_SHEDLOCK SET lock_u...  
25| 30| awa8nszb02q6p |  JDBC Thin Client  | SELECT column_name as Field , ...  
25| 30| awa8nszb02q6p |  JDBC Thin Client  | SELECT column_name as Field , ...  
22| 7,679| az33m61ym46y4 |  JDBC Thin Client  | SELECT NULL AS table_cat, o.ow...  
22| 3,274| dv474vaz39154 |  JDBC Thin Client  | select patName, visitId, deptI...  
22| 41| gxn6jnu7qx2vw |  JDBC Thin Client  | select t.* from hisuser.add_zy...  
21| 550| 8xwunw9vbjc5t |  JDBC Thin Client  | update cure_apply set created_...  
  
* * *

Back to SQL Statistics   
Back to Top

### SQL ordered by Cluster Wait Time

  * %Total - Cluster Time as a percentage of Total Cluster Wait Time 
  * %Clu - Cluster Time as a percentage of Elapsed Time 
  * %CPU - CPU Time as a percentage of Elapsed Time 
  * %IO - User I/O Time as a percentage of Elapsed Time 
  * Only SQL with Cluster Wait Time > .005 seconds is reported
  * Total Cluster Wait Time (s): 841
  * Captured SQL account for 61.7% of Total

Cluster Wait Time (s)| Executions| %Total| Elapsed Time(s)| %Clu| %CPU| %IO|  SQL Id| SQL Module| SQL Text  
---|---|---|---|---|---|---|---|---|---  
285.13| 46,841| 33.91| 471.64| 60.46| 17.07| 9.17| 0j9d1baynxk9z |  JDBC Thin Client  | update T_SM_EXTERNAL_SYS_LOGGE...  
73.61| 33,801| 8.75| 134.21| 54.84| 26.09| 11.73| 51ny34wxhrzv4 |  JDBC Thin Client  | insert into T_SM_EXTERNAL_SYS_...  
39.65| 1| 4.72| 43.25| 91.68| 18.69| 0.00| 5t4gc4s91q44p |  JDBC Thin Client  | SELECT count(0) FROM (SELECT D...  
20.99| 2,855| 2.50| 483.10| 4.34| 95.69| 0.00| 12nd0kqpvd8xn |  JDBC Thin Client  | select visit0_.ID as ID160_, v...  
15.82| 46,527| 1.88| 26.25| 60.28| 39.49| 0.58| 9qc6r0wu94sqg |  JDBC Thin Client  | select externalsy0_.ID as ID17...  
13.62| 7,125| 1.62| 16.63| 81.88| 22.38| 0.00| bfnzd8q7d2z0m |  JDBC Thin Client  | update t_sm_client_socket set ...  
13.58| 1| 1.61| 15.72| 86.40| 23.28| 0.01| 4pbn1pv4kucsv |  w3wp.exe  | select ͳƿ , placer_code , ...  
8.46| 4,616| 1.01| 9.95| 85.05| 9.68| 2.29| 2rajyj0wtnxgg |  JDBC Thin Client  | insert into T_ODW_ORDERBILLING...  
5.90| 53,200| 0.70| 23.31| 25.31| 14.89| 0.00| 4bd22u3q0p7mp |  JDBC Thin Client  | update t_sm_dblock set version...  
5.78| 64,930| 0.69| 9.70| 59.56| 36.20| 0.67| 6pqru4undjfj5 |  JDBC Thin Client  | select version from t_sm_dbloc...  
5.39| 44,658| 0.64| 726.56| 0.74| 97.46| 0.00| caz5v85xqv2nr |  JDBC Thin Client  | BEGIN PG_HIS_ELECTRONICBILLS.p...  
5.25| 46,663| 0.62| 8.65| 60.69| 48.86| 0.00| d642fkkxqhs98 |  JDBC Thin Client  | select ID from T_SM_EXTERNAL_S...  
4.20| 241| 0.50| 74.33| 5.64| 6.51| 0.83| d45qmb31zqpch |  | DECLARE job BINARY_INTEGER := ...  
2.51| 16| 0.30| 14.50| 17.35| 17.10| 70.55| 6z7g6p5vzf8c2 |  op_dispense_print.exe  |  SELECT note.DISPENSE_NOTE_ID ...  
2.47| 1| 0.29| 8.83| 27.98| 22.48| 56.79| gjm43un5cy843 |  | SELECT SUM(USED), SUM(TOTAL) F...  
2.47| 29,805| 0.29| 4.33| 56.97| 20.99| 0.00| c5uhk705rt3v1 |  JDBC Thin Client  | select clientsock0_.ID as ID22...  
2.37| 1,084| 0.28| 322.67| 0.74| 75.67| 0.06| 8hs1qzm4j4zqk |  JDBC Thin Client  | select reg_id, visit_id, card_...  
2.13| 416| 0.25| 43.97| 4.85| 81.27| 0.87| dz7vaztm8008c |  JDBC Thin Client  | BEGIN PG_HIS_SQ.occupyNumberSo...  
2.08| 14| 0.25| 114.06| 1.82| 98.21| 0.00| dvd0axaxt81h9 |  | DECLARE job BINARY_INTEGER := ...  
1.96| 352| 0.23| 8,184.03| 0.02| 34.22| 0.00| 4mpkm9h0x47uu |  HIS_Oracle.exe  | select A.* from V_DATA_PRESCRI...  
1.59| 388,908| 0.19| 50.16| 3.16| 97.17| 0.00| 7ahdc26dxpwfu |  | UPDATE WDP.DPC_STORAGE_DRUG G ...  
1.55| 24,861| 0.18| 3.56| 43.38| 36.08| 0.00| 2x81947q6ruys |  JDBC Thin Client  | select visit0_.ID as ID160_, v...  
1.47| 19,991| 0.17| 962.65| 0.15| 98.46| 0.00| 11523cnuz91yv |  JDBC Thin Client  | select bedallrese0_.uuid as uu...  
1.47| 14| 0.17| 121.11| 1.21| 98.56| 0.00| ggd2znk56cwt0 |  | DECLARE job BINARY_INTEGER := ...  
1.43| 2,999| 0.17| 41.39| 3.46| 95.94| 0.01| 3mbzwp1hudumm |  JDBC Thin Client  | SELECT * FROM ( SELECT TMP_PAG...  
1.36| 16| 0.16| 264.49| 0.51| 99.29| 0.00| 4yf3t9abkd8f2 |  ISServerExec.exe  | delete from BI_Fact_Visit_Regi...  
1.24| 676| 0.15| 1.89| 65.63| 25.68| 14.69| 9af3pdtxg6jvt |  | INSERT INTO WOPB.DPB_OP_DISPEN...  
1.13| 4,959| 0.13| 71.90| 1.57| 96.49| 0.00| gs22bnjq55v3q |  JDBC Thin Client  | select count(*) as prespSum, c...  
1.13| 1,862| 0.13| 3.31| 34.13| 58.53| 0.36| f2xfzfr3pjh3q |  JDBC Thin Client  | select t.* from hisuser.dgby_o...  
1.07| 11,748| 0.13| 1.77| 60.56| 24.88| 0.00| 787skx2f5ffyg |  JDBC Thin Client  | select account0_.ID as ID158_,...  
0.92| 184| 0.11| 50.92| 1.82| 98.08| 0.03| acvzqsugt0vma |  JDBC Thin Client  | BEGIN PG_DPB_DISPENSE_BATCH.hp...  
0.81| 2,477| 0.10| 1,368.34| 0.06| 99.67| 0.00| 5965cwv3r2tz3 |  JDBC Thin Client  | select obsettleac0_.ID as ID10...  
0.72| 3,274| 0.09| 3.04| 23.50| 49.31| 0.29| dv474vaz39154 |  JDBC Thin Client  | select patName, visitId, deptI...  
0.71| 59,545| 0.08| 5.33| 13.29| 36.09| 0.09| 97a6ts33jd0ba |  ISServerExec.exe  | INSERT INTO "HISUSER"."BI_FACT...  
0.62| 14| 0.07| 117.48| 0.52| 99.11| 0.00| 6gdn0m2zkmbz7 |  | DECLARE job BINARY_INTEGER := ...  
0.49| 95| 0.06| 15.08| 3.27| 96.66| 0.21| dh5nf6qw9sycm |  JDBC Thin Client  | BEGIN PG_DPB_DISPENSE_BATCH.hp...  
0.39| 5| 0.05| 13.86| 2.78| 97.32| 0.01| 912j26wh9n2k6 |  JDBC Thin Client  | SELECT * FROM ( SELECT TMP_PAG...  
0.36| 324| 0.04| 1,228.85| 0.03| 99.71| 0.01| g1mygga3s3mcz |  | select pat_index_no, treat_car...  
0.34| 182| 0.04| 0.73| 47.00| 47.91| 0.04| gdp34xjtzz19w |  JDBC Thin Client  | \--շѸ֪ select o.org_name, --Ժ...  
0.31| 118| 0.04| 2.21| 13.92| 82.16| 0.00| dw9qd5d0pn687 |  JDBC Thin Client  | SELECT X.SUBOR_WARD_ID, X.SUBO...  
0.30| 47| 0.04| 55.87| 0.54| 99.24| 0.02| 9yzygm67qqk86 |  JDBC Thin Client  | BEGIN PG_HIS_SQ.realeaseNumber...  
0.30| 1,050| 0.04| 627.85| 0.05| 99.72| 0.00| dvhc0bwbs7q52 |  JDBC Thin Client  | SELECT COUNT(1) FROM T_OB_SETT...  
0.27| 2,999| 0.03| 36.10| 0.74| 97.05| 0.00| 1jv192g5rhnhu |  JDBC Thin Client  | SELECT count(0) FROM VDPB_WAIT...  
0.25| 335| 0.03| 402.08| 0.06| 99.65| 0.00| 84aqh3u98gdk2 |  JDBC Thin Client  | select mtinspecta0_.apply_id a...  
0.21| 8| 0.02| 198.50| 0.11| 60.53| 39.60| 5qnpb11bzakp0 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
0.21| 18,702| 0.02| 1.10| 18.71| 49.11| 0.43| 3hz06j9b5j1rf |  JDBC Thin Client  | select chargeitem0_.ID as ID22...  
0.20| 649| 0.02| 0.50| 39.41| 65.96| 3.05| 97d6ah8gw4f6u |  JDBC Thin Client  | update bab_bed_allocation set ...  
0.19| 735| 0.02| 3,531.25| 0.01| 99.74| 0.00| 8nbhkyycmx838 |  JDBC Thin Client  | select r.* from sq_esb_pm_dr_r...  
0.18| 2,341| 0.02| 245.91| 0.07| 98.49| 0.00| d3uu56jx39a2j |  JDBC Thin Client  | select * from urm.esb_pm_dr_re...  
0.16| 78,823| 0.02| 573.59| 0.03| 91.62| 0.00| 7bqavhxqu996b |  JDBC Thin Client  | select clientmess0_.id as id32...  
0.15| 228| 0.02| 0.49| 30.92| 55.51| 2.06| 150m85pbj62gc |  oracle@DZBL-EMRS-SQL1 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
0.15| 10| 0.02| 16.19| 0.92| 16.56| 85.53| 2mdx9t6xxn3x6 |  JDBC Thin Client  | select SUM(IMPORT_QUANTITY) AS...  
0.12| 352| 0.01| 2,498.29| 0.00| 21.98| 0.00| 4ua10u4pbtsqp |  HIS_Oracle.exe  | select * from V_DATA_PRESCRIPT...  
0.11| 757| 0.01| 34.08| 0.33| 99.24| 0.00| bb19k370m2b2t |  JDBC Thin Client  | SELECT X.PHARMACY_WIN_ID FROM ...  
0.11| 69| 0.01| 0.25| 43.52| 51.47| 1.03| b4nc4nnx3fhf5 |  oracle@DZBL-EMRS-SQL2 (TNS V1-V3)  | SELECT DISTINCT "A1"."ITEM_COD...  
0.09| 30| 0.01| 26.23| 0.35| 8.44| 0.20| 16ppcycdazapw |  | DECLARE job BINARY_INTEGER := ...  
0.09| 5,263| 0.01| 1.40| 6.43| 16.73| 0.00| 652v2j6y7uk5j |  JDBC Thin Client  | update t_sm_dblock set version...  
0.09| 114| 0.01| 131.66| 0.07| 99.65| 0.00| f8hq4t3wdkwfp |  JDBC Thin Client  | select mtinspecta0_.apply_id a...  
0.09| 757| 0.01| 3.73| 2.37| 95.28| 0.00| 4bnr0k0nxykf2 |  JDBC Thin Client  | SELECT COUNT(*) FROM WOP.VDPB_...  
0.07| 637| 0.01| 61.74| 0.12| 99.33| 0.00| 3y1uhvddtzucs |  JDBC Thin Client  | select * from urm.esb_pm_dr_re...  
0.07| 314| 0.01| 0.14| 49.47| 33.53| 0.00| 1krt4fdxy59ds |  JDBC Thin Client  | UPDATE BAC_SHEDLOCK SET lock_u...  
0.06| 5| 0.01| 14.77| 0.44| 78.89| 0.01| 8142bgxafa240 |  JDBC Thin Client  | select a.id as ROWKEY , a.* fr...  
0.06| 40| 0.01| 0.11| 58.72| 43.13| 5.27| g2cqspstx3awz |  JDBC Thin Client  | insert into bab_bed_allocation...  
0.06| 211| 0.01| 0.22| 27.05| 49.89| 1.16| 7ng34ruy5awxq |  | select i.obj#, i.ts#, i.file#,...  
  
* * *

Back to SQL Statistics   
Back to Top

### Complete List of SQL Text

SQL Id| SQL Text  
---|---  
0j9d1baynxk9z| update T_SM_EXTERNAL_SYS_LOGGER set MSG_ID=:1 , FUNC_ID=:2 , FUNC_NAME=:3 , METHOD_TYPE=:4 , REQUESTXML=:5 , RESPONSEXML=:6 , START_TIME=:7 , END_TIME=:8 , SEND_STATUS=:9 , CONSUMER=:10 , PROVIDER=:11 , CREATE_DATETIME=:12 , LAST_UDP_TIME=:13 where ID=:14   
0jyvx0fff62jb| select paraitem0_.ID as ID255_0_, paraitem0_.CATALOG_ID as CATALOG2_255_0_, paraitem0_.PARENT_ID as PARENT3_255_0_, paraitem0_.ABBREVIATION_NAME as ABBREVIA4_255_0_, paraitem0_.DESCRIPTION as DESCRIPT5_255_0_, paraitem0_.PINYIN_CODE as PINYIN6_255_0_, paraitem0_.WUBI_CODE as WUBI7_255_0_, paraitem0_.MEMORY_CODE as MEMORY8_255_0_, paraitem0_.SPELING_CODE as SPELING9_255_0_, paraitem0_.ACTIVE_FLAG as ACTIVE10_255_0_, paraitem0_.SEQ_NO as SEQ11_255_0_, paraitem0_.ITEM_VALUE as ITEM12_255_0_, paraitem0_.KEY_VALUE as KEY13_255_0_, paraitem0_.CONFIG_ENABLED as CONFIG14_255_0_, paraitem0_.VERSION_NO as VERSION15_255_0_ from T_SM_PARAITEM paraitem0_ where paraitem0_.ID=:1   
11523cnuz91yv|  select bedallrese0_.uuid as uuid1_69_, bedallrese0_.admit_date as admit_date2_69_, bedallrese0_.age as age3_69_, bedallrese0_.allocation_dept_name as allocation_dept_na4_69_, bedallrese0_.allocation_no as allocation_no5_69_, bedallrese0_.bed_card_title as bed_card_title6_69_, bedallrese0_.bed_code as bed_code7_69_, bedallrese0_.bed_code_abbr as bed_code_abbr8_69_, bedallrese0_.bed_descr as bed_descr9_69_, bedallrese0_.bed_id as bed_id10_69_, bedallrese0_.bed_level_icon as bed_level_icon11_69_, bedallrese0_.bed_level_id as bed_level_id12_69_, bedallrese0_.bed_level_name as bed_level_name13_69_, bedallrese0_.bed_name as bed_name14_69_, bedallrese0_.bed_sort as bed_sort15_69_, bedallrese0_.bed_state as bed_state16_69_, bedallrese0_.bed_type_icon as bed_type_icon17_69_, bedallrese0_.bed_type_id as bed_type_id18_69_, bedallrese0_.bed_type_name as bed_type_name19_69_, bedallrese0_.bed_type_tag as bed_type_tag20_69_, bedallrese0_.borrow_bed as borrow_bed21_69_, bedallrese 0_.discharge_date as discharge_date22_69_, bedallrese0_.discharge_hour as discharge_hour23_69_, bedallrese0_.inhosp_id as inhosp_id24_69_, bedallrese0_.inhosp_no as inhosp_no25_69_, bedallrese0_.is_allow_reserve as is_allow_reserve26_69_, bedallrese0_.is_cross_dept as is_cross_dept27_69_, bedallrese0_.is_keep_bed as is_keep_bed28_69_, bedallrese0_.is_need_quarantine as is_need_quarantin29_69_, bedallrese0_.is_pat_cross_dept as is_pat_cross_dept30_69_, bedallrese0_.is_reserve_discharge as is_reserve_discha31_69_, bedallrese0_.is_window_bed as is_window_bed32_69_, bedallrese0_.iswc as iswc33_69_, bedallrese0_.keep_bed_descr as keep_bed_descr34_69_, bedallrese0_.keep_bed_type_id as keep_bed_type_id35_69_, bedallrese0_.keep_bed_type_name as keep_bed_type_nam36_69_, bedallrese0_.keep_date as keep_date37_69_, bedallrese0_.keep_doctor_name as keep_doctor_name38_69_, bedallrese0_.keep_end_date as keep_end_date39_69_, bedallrese0_.keep_pat_idnumber as keep_pat_idnumber40_69_, bedallrese0_.keep_pat_name as keep_pat_name41_69_, bedallrese0_.keep_pat_phone_num as keep_pat_phone_nu42_69_, bedallrese0_.keep_user_id as keep_user_id43_69_, bedallrese0_.keep_user_name as keep_user_name44_69_, bedallrese0_.last_state_tag as last_state_tag45_69_, bedallrese0_.medical_group_all as medical_group_all46_69_, bedallrese0_.medical_group_id as medical_group_id47_69_, bedallrese0_.medical_group_show as medical_group_sho48_69_, bedallrese0_.medical_ward_id as medical_ward_id49_69_, bedallrese0_.medical_ward_name as medical_ward_name50_69_, bedallrese0_.pat_name as pat_name51_69_, bedallrese0_.reserve_admit_date as reserve_admit_dat52_69_, bedallrese0_.sex_code as sex_code53_69_, bedallrese0_.sex_name as sex_name54_69_, bedallrese0_.sickroom_descr as sickroom_descr55_69_, bedallrese0_.sickroom_sex_state as sickroom_sex_stat56_69_, bedallrese0_.sickroom_sex_tag as sickroom_sex_tag57_69_, bedallrese0_.sr_is_need_quarantine as sr_is_need_quaran58_69_, bedallres e0_.subor_branch_id as subor_branch_id59_69_, bedallrese0_.subor_dept_id as subor_dept_id60_69_, bedallrese0_.subor_dept_name as subor_dept_name61_69_, bedallrese0_.subor_sickroom_code as subor_sickroom_co62_69_, bedallrese0_.subor_sickroom_id as subor_sickroom_id63_69_, bedallrese0_.subor_sickroom_name as subor_sickroom_na64_69_, bedallrese0_.subor_ward_code as subor_ward_code65_69_, bedallrese0_.subor_ward_id as subor_ward_id66_69_, bedallrese0_.subor_ward_name as subor_ward_name67_69_, bedallrese0_.visit_card_no as visit_card_no68_69_ from bav_bed_all_reserve_detail bedallrese0_ where bedallrese0_.bed_code=:1   
12nd0kqpvd8xn|  select visit0_.ID as ID160_, visit0_.PID as PID160_, visit0_.VISIT_ID as VISIT3_160_, visit0_.CARD_ID as CARD4_160_, visit0_.NAME_PINYIN_CODE as NAME5_160_, visit0_.NAME_WUBI_CODE as NAME6_160_, visit0_.NAME_SPELLING_CODE as NAME7_160_, visit0_.NAME as NAME160_, visit0_.GENDER as GENDER160_, visit0_.BIRTHDAY as BIRTHDAY160_, visit0_.DEPT_ID as DEPT11_160_, visit0_.CONTACT as CONTACT160_, visit0_.PHONE as PHONE160_, visit0_.ADDRESS as ADDRESS160_, visit0_.PATIENT_CLASS as PATIENT15_160_, visit0_.ADMISSION_TYPE as ADMISSION16_160_, visit0_.ATTENDING_DOCTOR_ID as ATTENDING17_160_, visit0_.ATTENDING_DOCTOR_VER_ID as ATTENDING18_160_, visit0_.ATTENDING_DOCTOR_NAME as ATTENDING19_160_, visit0_.ATTENDING_DOCTOR_CODE as ATTENDING20_160_, visit0_.HOSPITAL_SERVICE as HOSPITAL21_160_, visit0_.PRE_ADMITTEST_INDICATOR as PRE22_160_, visit0_.READMISSION_INDICATOR as READMIS23_160_, visit0_.ADMIT_SOURCE as ADMIT24_160_, visit0_.AMBULATORY_STATUS as AMBULATORY25_160_, visit0_. VIP_INDICATOR as VIP26_160_, visit0_.SPECIAL_PATIENT_TYPE as SPECIAL27_160_, visit0_.COURTESY_CODE as COURTESY28_160_, visit0_.DISCHARGE_DISPOSITION as DISCHARGE29_160_, visit0_.BED_STATUS as BED30_160_, visit0_.SEQ_NO as SEQ31_160_, visit0_.NOON as NOON160_, visit0_.SEQ_NO_NOON as SEQ33_160_, visit0_.ACTIVE_FLAG as ACTIVE34_160_, visit0_.REFUND_FLAG as REFUND35_160_, visit0_.ADMIT_FLAG as ADMIT36_160_, visit0_.ADMIT_TYPE as ADMIT37_160_, visit0_.ADMIT_DATETIME as ADMIT38_160_, visit0_.DISCHARGE_DATETIME as DISCHARGE39_160_, visit0_.CALL_FLAG as CALL40_160_, visit0_.REGISTER_WAY as REGISTER41_160_, visit0_.BOOKING_WAY as BOOKING42_160_, visit0_.DSCH_ID as DSCH43_160_, visit0_.SOURCE_TYPE as SOURCE44_160_, visit0_.SOURCE_ID as SOURCE45_160_, visit0_.SPECIALITY as SPECIALITY160_, visit0_.LOCATION as LOCATION160_, visit0_.APPOINTMENT_ID as APPOINT48_160_, visit0_.VISIT_DATETIME as VISIT49_160_, visit0_.ORG_ID as ORG50_160_, visit0_.CREATOR_ID as CREATOR51_160_, v isit0_.CREATOR_VER_ID as CREATOR52_160_, visit0_.CREATE_TIME as CREATE53_160_, visit0_.LAST_UPD_USER as LAST54_160_, visit0_.LAST_UPD_USER_VER_ID as LAST55_160_, visit0_.LAST_UPD_TIME as LAST56_160_, visit0_.CREATOR_USER_CODE as CREATOR57_160_, visit0_.LAST_UPD_USER_CODE as LAST58_160_, visit0_.ARRANGEMENT_SEQ_NO as ARRANGE59_160_, visit0_.DBTT_ID as DBTT60_160_, visit0_.AGE as AGE160_, visit0_.IS_RESCUE as IS62_160_, visit0_.RESCUE_TIMES as RESCUE63_160_, visit0_.RESCUE_SUCCESS_TIMES as RESCUE64_160_, visit0_.DEATH_INDICATOR as DEATH65_160_, visit0_.DEATH_DATETIME as DEATH66_160_, visit0_.IS_SURGERY as IS67_160_, visit0_.MAJOR_DEPT_ID as MAJOR68_160_, visit0_.LATER_PAYMENT as LATER69_160_, visit0_.VISIT_TIME as VISIT70_160_, visit0_.ISREGISTMI_FLAG as ISREGISTMI71_160_, visit0_.FIRST_ADMIT_FLAG as FIRST72_160_, visit0_.VISIT_START_DATETIME as VISIT73_160_, visit0_.VISIT_END_DATETIME as VISIT74_160_, visit0_.SEND_STATUS as SEND75_160_, visit0_.TAKE_NO_FLAG as TA KE76_160_, visit0_.DOCTOR_BIND_ID as DOCTOR77_160_, visit0_.OVERTIME_FLAG as OVERTIME78_160_, visit0_.ISPREGNANT as ISPREGNANT160_, visit0_.ISBREASTFEEDING as ISBREAS80_160_, visit0_.PE_SEQ_NO as PE81_160_, visit0_.SPECIALIST_DEPT_CODE as SPECIALIST82_160_, visit0_.SPECIALIST_DEPT_NAME as SPECIALIST83_160_, visit0_.NOON_CODE as NOON84_160_, visit0_.NOON_NAME as NOON85_160_, visit0_.CALCULATOR_MARKER as CALCULATOR86_160_, visit0_.REMARK as REMARK160_, visit0_.DOCTOR_TITLE as DOCTOR88_160_, visit0_.ATTENDING_DOCTOR_DEPT_ID as ATTENDING89_160_ from T_OR_VISIT visit0_ where visit0_.CARD_ID=:1 and visit0_.REFUND_FLAG='N' and (exists (select orderbilli1_.ID from T_ODW_ORDERBILLING orderbilli1_, T_OR_ACCOUNT account2_ where orderbilli1_.ACCOUNT_ID=account2_.ACCOUNT_ID and account2_.VISIT_ID=visit0_.VISIT_ID and orderbilli1_.ACTIVE_FLAG='Y' and orderbilli1_.ACCOUNT_FLAG='N' and orderbilli1_.CREATE_DATETIME>=trunc(to_date(:2 , 'yyyy-MM-dd hh24:mi:ss')) and orderbilli1_.CREATE_ DATETIME<trunc(to_date(:3 , 'yyyy-MM-dd hh24:mi:ss'))+1 and (orderbilli1_.ORDER_GROUP_ID is null or orderbilli1_.ORDER_GROUP_ID in (select ordergroup3_.ID from T_ODW_ORDERGROUP ordergroup3_ where ordergroup3_.ID=orderbilli1_.ORDER_GROUP_ID and ordergroup3_.ACCOUNT_ID=orderbilli1_.ACCOUNT_ID and ordergroup3_.ORDER_GROUP_SOURCE<>-308754)))) and visit0_.ADMIT_FLAG='Y'  
13j5ux5tz7kws|  select emrbedlist0_.bed_id as bed_id1_51_0_, emrbedlist0_.admit_date as admit_date2_51_0_, emrbedlist0_.admit_time as admit_time3_51_0_, emrbedlist0_.age as age4_51_0_, emrbedlist0_.bed_code as bed_code5_51_0_, emrbedlist0_.bed_level_code as bed_level_code6_51_0_, emrbedlist0_.bed_level_name as bed_level_name7_51_0_, emrbedlist0_.bed_name as bed_name8_51_0_, emrbedlist0_.bed_type as bed_type9_51_0_, emrbedlist0_.bed_type_code as bed_type_code10_51_0_, emrbedlist0_.bed_type_name as bed_type_name11_51_0_, emrbedlist0_.bed_type_tag as bed_type_tag12_51_0_, emrbedlist0_.bed_zybz as bed_zybz13_51_0_, emrbedlist0_.borrow_bed as borrow_bed14_51_0_, emrbedlist0_.contact_phone_no as contact_phone_no15_51_0_, emrbedlist0_.create_date as create_date16_51_0_, emrbedlist0_.create_user as create_user17_51_0_, emrbedlist0_.date_birth as date_birth18_51_0_, emrbedlist0_.diag_code as diag_code19_51_0_, emrbedlist0_.diag_name as diag_name20_51_0_, emrbedlist0_.discharge_date as disch arge_date21_51_0_, emrbedlist0_.discharge_hour as discharge_hour22_51_0_, emrbedlist0_.id_number as id_number23_51_0_, emrbedlist0_.inhosp_id as inhosp_id24_51_0_, emrbedlist0_.inhosp_no as inhosp_no25_51_0_, emrbedlist0_.inward_time as inward_time26_51_0_, emrbedlist0_.is_curr_occupy as is_curr_occupy27_51_0_, emrbedlist0_.is_reserve_bed as is_reserve_bed28_51_0_, emrbedlist0_.is_reserve_discharge as is_reserve_discha29_51_0_, emrbedlist0_.medical_group_id as medical_group_id30_51_0_, emrbedlist0_.medical_group_name as medical_group_nam31_51_0_, emrbedlist0_.medical_ward_id as medical_ward_id32_51_0_, emrbedlist0_.medical_ward_name as medical_ward_name33_51_0_, emrbedlist0_.pat_id as pat_id34_51_0_, emrbedlist0_.pat_name as pat_name35_51_0_, emrbedlist0_.pat_phone_no as pat_phone_no36_51_0_, emrbedlist0_.reserve_no as reserve_no37_51_0_, emrbedlist0_.sex_code as sex_code38_51_0_, emrbedlist0_.sex_name as sex_name39_51_0_, emrbedlist0_.stay_in_bed as stay_in_bed40_51 _0_, emrbedlist0_.subor_branch_id as subor_branch_id41_51_0_, emrbedlist0_.subor_dept_code as subor_dept_code42_51_0_, emrbedlist0_.subor_dept_id as subor_dept_id43_51_0_, emrbedlist0_.subor_dept_name as subor_dept_name44_51_0_, emrbedlist0_.subor_sickroom_code as subor_sickroom_co45_51_0_, emrbedlist0_.subor_sickroom_id as subor_sickroom_id46_51_0_, emrbedlist0_.subor_sickroom_name as subor_sickroom_na47_51_0_, emrbedlist0_.subor_ward_code as subor_ward_code48_51_0_, emrbedlist0_.subor_ward_id as subor_ward_id49_51_0_, emrbedlist0_.subor_ward_name as subor_ward_name50_51_0_, emrbedlist0_.transfer_ward_date as transfer_ward_dat51_51_0_, emrbedlist0_.update_date as update_date52_51_0_, emrbedlist0_.update_user as update_user53_51_0_ from bai_emr_bed_list emrbedlist0_ where emrbedlist0_.bed_id=:1   
150m85pbj62gc| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
16ppcycdazapw| DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN PG_SYN_WIP_SEND.pp_job_batch; :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END;   
1hhg7sfy5d46f| select 1 from USER_TABLES t where lower(t.TABLE_NAME)=lower(:1 )  
1jv192g5rhnhu| SELECT count(0) FROM VDPB_WAIT_DELIVER d LEFT JOIN wpub.p_decoct_agent_way w ON d.herbal_is_decoct_hospital = w.decoct_agent_way_code WHERE d.is_deliver = 'N' AND d.is_dispense = 'Y' AND d.is_cancel_confirm = 'N' AND d.pharmacy_id = :1 AND d.actual_win_id = :2 AND d.dispense_time >= :3 AND d.dispense_time <= :4   
1krt4fdxy59ds| UPDATE BAC_SHEDLOCK SET lock_until = :1 , locked_at = :2 , locked_by = :3 WHERE name = :4 AND lock_until <= :5   
2ftuy4q1xa9md| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003 OR "A1"."ITEM_CODE"=:V00004 OR "A1"."ITEM_CODE"=:V00005 OR "A1"."ITEM_CODE"=:V00006 OR "A1"."ITEM_CODE"=:V00007) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
2mdx9t6xxn3x6| select SUM(IMPORT_QUANTITY) AS IMPORT_SUM_QUANTITY, SUM(EXPORT_QUANTITY) AS EXPORT_SUM_QUANTITY, SUM(IMPORT_SALE_AMOUNT) AS IMPORT_SUM_SALE_AMOUNT, SUM(EXPORT_SALE_AMOUNT) AS EXPORT_SUM_SALE_AMOUNT from ( select DECODE(OPERATE_TYPE, 'IMPORT', OPERATE_MIN_QUANTITY, 0) AS IMPORT_QUANTITY, DECODE(OPERATE_TYPE, 'EXPORT', OPERATE_MIN_QUANTITY * -1, 0) AS EXPORT_QUANTITY, DECODE(OPERATE_TYPE, 'IMPORT', OPERATE_SALE_AMOUNT, 0) AS IMPORT_SALE_AMOUNT, DECODE(OPERATE_TYPE, 'EXPORT', OPERATE_SALE_AMOUNT * -1, 0) AS EXPORT_SALE_AMOUNT from PHB_STOCK_ITEM_DETAIL WHERE OPERATE_TIME >= :1 AND OPERATE_TIME <= :2 + 1 AND PHARMACY_ID = :3 AND ITEM_ID = :4 )T  
2rajyj0wtnxgg|  insert into T_ODW_ORDERBILLING (ACCOUNT_ID, BILLING_TYPE, ORDER_GROUP_ID, ORDER_GROUP_CODE, ORDER_ID, TC_ID, ORDER_NAME, ITEM_ID, ITEM_CODE, ITEM_NAME, ACTUAL_ITEM_ID, UNIT_PRICE, ACTUAL_DISPENSE_AMOUNT, DISPENSE_UNITS, AMOUNT, ACTUAL_AMOUNT, INDIVIDUAL_PAYMENT, ACCOUNT_DEBTED, PAY_SCALE, DISCOUNT_SCALE, PERFORMING_DEPT_ID, PLACER_ID, PLACER_NAME, PLACER_DEPT_ID, PLACER_CODE, DEPT_ID, CREATE_DATETIME, CHARGE_DATETIME, EXECUTIVE_DATETIME, ACTIVE_FLAG, ACCOUNT_FLAG, PAYMENT_INACTIVE_FLAG, ACCOUNT_TYPE, DRUG_STORE_ID, ISDISPENSING, ORG_ID, FINANCIAL_CLASSIFICATION, ITEM_TYPE, ACCOUNT_DEBTED_AMOUNT, SPECIFICATION, DOSAGE_FORM, DISPENSE_AMOUNT_EVERYTIMES, BILLING_CLASSIFY, DM_DRUGSTORE_ID, PURCHASE_PRICE, DISPENSED_INDICATOR, EXTERNAL_BILLING_XH, MEDICAL_REGISTRATION_NO, FEE_BATCH, INVOICE_CODE, EXTERNAL_PRES_NO, MEMORY_CODE, YIBAO_FLAG, TC_CODE, REFUND_TP_FLAG, SPECIAL_DRUG_DEBTED, LIMITING_DRUG, IP_ACCOUNT_DEBTED_AMOUNT, USAGE_NAME , USAGE_DAYS, FREQUENCY_NAME, DOSAGE, DOSAGE_UNIT, TC_NAME, SICK_OR_WOUNDED, ATTACHED_CHARGE_FLAG, PRE_DIAG_CODE, SPECIFIC_DISEASE_CODE, PRIC_UPLMT_AMT, SELFPAY_PROP, FULAMT_OWNPAY_AMT, OVERLMT_AMT, PRESELFPAY_AMT, INSCP_SCP_AMT, MED_CHRGITM_TYPE, CHRGITM_LV, DET_ITEM_FEE_SUMAMT, PRIC, ACCT_USED_FLAG, STATISTICS_MII_ITEM_CODE, ORIGNAL_ACTUAL_AMOUNT, MEDICAL_GROUP_NO, ANTIBIOTIC_LEVEL, DOCTOR_TITLE, ACCOUNT_ORG_ID, ACCOUNT_ORG_NAME, ID) values (:1 , :2 , :3 , :4 , :5 , :6 , :7 , :8 , :9 , :10 , :11 , :12 , :13 , :14 , :15 , :16 , :17 , :18 , :19 , :20 , :21 , :22 , :23 , :24 , :25 , :26 , :27 , :28 , :29 , :30 , :31 , :32 , :33 , :34 , :35 , :36 , :37 , :38 , :39 , :40 , :41 , :42 , :43 , :44 , :45 , :46 , :47 , :48 , :49 , :50 , :51 , :52 , :53 , :54 , :55 , :56 , :57 , :58 , :59 , :60 , :61 , :62 , :63 , :64 , :65 , :66 , :67 , :68 , :69 , :70 , :71 , :72 , :73 , :74 , :75 , :76 , : 77 , :78 , :79 , :80 , :81 , :82 , :83 , :84 , :85 , :86 , :87 )  
2u395bhfbhg99| select r.* from sq_esb_pm_dr_regist_time_infor r where 1=1 and schedule_no =:1 and OUT_CALL_STATUS =:2 and QUOTA_USAGE =:3 order by start_time asc   
2x81947q6ruys|  select visit0_.ID as ID160_, visit0_.PID as PID160_, visit0_.VISIT_ID as VISIT3_160_, visit0_.CARD_ID as CARD4_160_, visit0_.NAME_PINYIN_CODE as NAME5_160_, visit0_.NAME_WUBI_CODE as NAME6_160_, visit0_.NAME_SPELLING_CODE as NAME7_160_, visit0_.NAME as NAME160_, visit0_.GENDER as GENDER160_, visit0_.BIRTHDAY as BIRTHDAY160_, visit0_.DEPT_ID as DEPT11_160_, visit0_.CONTACT as CONTACT160_, visit0_.PHONE as PHONE160_, visit0_.ADDRESS as ADDRESS160_, visit0_.PATIENT_CLASS as PATIENT15_160_, visit0_.ADMISSION_TYPE as ADMISSION16_160_, visit0_.ATTENDING_DOCTOR_ID as ATTENDING17_160_, visit0_.ATTENDING_DOCTOR_VER_ID as ATTENDING18_160_, visit0_.ATTENDING_DOCTOR_NAME as ATTENDING19_160_, visit0_.ATTENDING_DOCTOR_CODE as ATTENDING20_160_, visit0_.HOSPITAL_SERVICE as HOSPITAL21_160_, visit0_.PRE_ADMITTEST_INDICATOR as PRE22_160_, visit0_.READMISSION_INDICATOR as READMIS23_160_, visit0_.ADMIT_SOURCE as ADMIT24_160_, visit0_.AMBULATORY_STATUS as AMBULATORY25_160_, visit0_. VIP_INDICATOR as VIP26_160_, visit0_.SPECIAL_PATIENT_TYPE as SPECIAL27_160_, visit0_.COURTESY_CODE as COURTESY28_160_, visit0_.DISCHARGE_DISPOSITION as DISCHARGE29_160_, visit0_.BED_STATUS as BED30_160_, visit0_.SEQ_NO as SEQ31_160_, visit0_.NOON as NOON160_, visit0_.SEQ_NO_NOON as SEQ33_160_, visit0_.ACTIVE_FLAG as ACTIVE34_160_, visit0_.REFUND_FLAG as REFUND35_160_, visit0_.ADMIT_FLAG as ADMIT36_160_, visit0_.ADMIT_TYPE as ADMIT37_160_, visit0_.ADMIT_DATETIME as ADMIT38_160_, visit0_.DISCHARGE_DATETIME as DISCHARGE39_160_, visit0_.CALL_FLAG as CALL40_160_, visit0_.REGISTER_WAY as REGISTER41_160_, visit0_.BOOKING_WAY as BOOKING42_160_, visit0_.DSCH_ID as DSCH43_160_, visit0_.SOURCE_TYPE as SOURCE44_160_, visit0_.SOURCE_ID as SOURCE45_160_, visit0_.SPECIALITY as SPECIALITY160_, visit0_.LOCATION as LOCATION160_, visit0_.APPOINTMENT_ID as APPOINT48_160_, visit0_.VISIT_DATETIME as VISIT49_160_, visit0_.ORG_ID as ORG50_160_, visit0_.CREATOR_ID as CREATOR51_160_, v isit0_.CREATOR_VER_ID as CREATOR52_160_, visit0_.CREATE_TIME as CREATE53_160_, visit0_.LAST_UPD_USER as LAST54_160_, visit0_.LAST_UPD_USER_VER_ID as LAST55_160_, visit0_.LAST_UPD_TIME as LAST56_160_, visit0_.CREATOR_USER_CODE as CREATOR57_160_, visit0_.LAST_UPD_USER_CODE as LAST58_160_, visit0_.ARRANGEMENT_SEQ_NO as ARRANGE59_160_, visit0_.DBTT_ID as DBTT60_160_, visit0_.AGE as AGE160_, visit0_.IS_RESCUE as IS62_160_, visit0_.RESCUE_TIMES as RESCUE63_160_, visit0_.RESCUE_SUCCESS_TIMES as RESCUE64_160_, visit0_.DEATH_INDICATOR as DEATH65_160_, visit0_.DEATH_DATETIME as DEATH66_160_, visit0_.IS_SURGERY as IS67_160_, visit0_.MAJOR_DEPT_ID as MAJOR68_160_, visit0_.LATER_PAYMENT as LATER69_160_, visit0_.VISIT_TIME as VISIT70_160_, visit0_.ISREGISTMI_FLAG as ISREGISTMI71_160_, visit0_.FIRST_ADMIT_FLAG as FIRST72_160_, visit0_.VISIT_START_DATETIME as VISIT73_160_, visit0_.VISIT_END_DATETIME as VISIT74_160_, visit0_.SEND_STATUS as SEND75_160_, visit0_.TAKE_NO_FLAG as TA KE76_160_, visit0_.DOCTOR_BIND_ID as DOCTOR77_160_, visit0_.OVERTIME_FLAG as OVERTIME78_160_, visit0_.ISPREGNANT as ISPREGNANT160_, visit0_.ISBREASTFEEDING as ISBREAS80_160_, visit0_.PE_SEQ_NO as PE81_160_, visit0_.SPECIALIST_DEPT_CODE as SPECIALIST82_160_, visit0_.SPECIALIST_DEPT_NAME as SPECIALIST83_160_, visit0_.NOON_CODE as NOON84_160_, visit0_.NOON_NAME as NOON85_160_, visit0_.CALCULATOR_MARKER as CALCULATOR86_160_, visit0_.REMARK as REMARK160_, visit0_.DOCTOR_TITLE as DOCTOR88_160_, visit0_.ATTENDING_DOCTOR_DEPT_ID as ATTENDING89_160_ from T_OR_VISIT visit0_ where visit0_.VISIT_ID=:1   
2x9u0gw4gh4x6| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003 OR "A1"."ITEM_CODE"=:V00004 OR "A1"."ITEM_CODE"=:V00005 OR "A1"."ITEM_CODE"=:V00006 OR "A1"."ITEM_CODE"=:V00007 OR "A1"."ITEM_CODE"=:V00008 OR "A1"."ITEM_CODE"=:V00009) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
39vzujk1r12gw| SELECT COUNT(1) FROM T_SM_PARAITEM P WHERE 1 = 1 AND P.CATALOG_ID = '070111' AND P.ITEM_VALUE = :B1   
3hz06j9b5j1rf|  select chargeitem0_.ID as ID222_, chargeitem0_.ITEM_ID as ITEM2_222_, chargeitem0_.MII_ITEM_CODE as MII3_222_, chargeitem0_.MII_ITEM_NAME as MII4_222_, chargeitem0_.MI_CODE as MI5_222_, chargeitem0_.MI_CATALOG_ID as MI6_222_, chargeitem0_.ACCOUNT_TYPE as ACCOUNT7_222_, chargeitem0_.ITEM_TYPE as ITEM8_222_, chargeitem0_.PAY_SCALE as PAY9_222_, chargeitem0_.CLASSIFICATION_CODE as CLASSIF10_222_, chargeitem0_.REMARK as REMARK222_, chargeitem0_.QUESTION_TYPE as QUESTION12_222_, chargeitem0_.QUESTION_INFO as QUESTION13_222_, chargeitem0_.REPLY_YES as REPLY14_222_, chargeitem0_.REPLY_NO as REPLY15_222_, chargeitem0_.CREATOR_ID as CREATOR16_222_, chargeitem0_.CREATOR_VER_ID as CREATOR17_222_, chargeitem0_.CREATE_TIME as CREATE18_222_, chargeitem0_.CREATOR_CODE as CREATOR19_222_, chargeitem0_.LAST_UPD_USER as LAST20_222_, chargeitem0_.LAST_UPD_USER_VER_ID as LAST21_222_, chargeitem0_.LAST_UPD_TIME as LAST22_222_, chargeitem0_.LAST_UPD_USER_CODE as LAST23_222_, chargeitem 0_.CONFIRM_FLAG as CONFIRM24_222_, chargeitem0_.IP_PAY_SCALE as IP25_222_, chargeitem0_.TRANS_CODE as TRANS26_222_, chargeitem0_.IP_ACCOUNT_TYPE as IP27_222_, chargeitem0_.PEDIATRICS_ACCOUNT_TYPE as PEDIATRICS28_222_, chargeitem0_.IP_OWN_PAY_FIRST as IP29_222_, chargeitem0_.IP_ACCOUNT_DEBTED_AMOUNT as IP30_222_, chargeitem0_.IP_TRANS_CODE as IP31_222_, chargeitem0_.IP_MII_ITEM_CODE as IP32_222_ from T_MII_CHARGEITEM chargeitem0_ where chargeitem0_.ITEM_ID=:1 and chargeitem0_.MI_CODE=:2 and chargeitem0_.ITEM_TYPE=:3   
3mbzwp1hudumm|  SELECT * FROM ( SELECT TMP_PAGE.*, ROWNUM ROW_ID FROM ( select d.dispense_note_id, d.pat_id, d.pat_name, d.visit_id, d.is_dispense, d.is_deliver, d.is_cancel, d.is_breakoff, d.queue_time, d.med_card_no, d.pharmacy_win_code, d.pharmacy_win_name, d.last_state_sort, d.last_state_id, d.check_in_time, d.dispense_time, d.is_checked_in, d.invoice_id, d.invoice_no, d.dispense_proc_type, d.check_in_proc_type, d.pre_queue_num, d.herbal_is_decoct_hospital, d.is_confirm, d.id_number, d.presp_id, d.charge_user_name, d.is_push, d.visit_flag, d.is_express, (SELECT COUNT(1) FROM wopb.dpb_op_dispense_detail t, wpub.p_drug drug WHERE t.dispense_note_id = d.dispense_note_id and drug.item_id = t.item_id AND drug.ANTIBIOTIC_GRADE != 0 ) AS ANTIBIOTIC_GRADE, (SELECT (case when count(1) > 0 then 'Y' else 'N' end) FROM wopb.dpb_op_dispense_detail t, wpub.p_drug drug WHERE t.dispense_note_id = d.dispense_note_id and drug.item_id = t.item_id and drug.Is_Poison = 'Y' ) AS IS_ POISON, (SELECT (case when count(1) > 0 then 'Y' else 'N' end) FROM wopb.dpb_op_dispense_detail t, wpub.p_drug drug WHERE t.dispense_note_id = d.dispense_note_id and drug.item_id = t.item_id and drug.is_narcotic_drug = 'Y' ) AS IS_NARCOTIC_DRUG, (SELECT (case when count(1) > 0 then 'Y' else 'N' end) FROM wopb.dpb_op_dispense_detail t, wpub.p_drug drug WHERE t.dispense_note_id = d.dispense_note_id and drug.item_id = t.item_id and drug.drug_poison_flag != 'N' ) AS DRUG_POISON_FLAG, w.decoct_agent_way_name as HERBAL_ISDECOCTHOSPITALNAME, w.decoct_agent_way_enname as HERBAL_IS_DECOCTHOSPITALENNAME from VDPB_WAIT_DELIVER d LEFT JOIN wpub.p_decoct_agent_way w ON d.herbal_is_decoct_hospital = w.decoct_agent_way_code where d.is_deliver = 'N' and d.is_dispense = 'Y' and d.is_cancel_confirm = 'N' and d.pharmacy_id = :1 and d.actual_win_id = :2 and d.dispense_time >= :3 and d.dispense_time <= :4 ) TMP_PAGE) WHERE ROW_ID <= :5 AND ROW_ID > :6   
3y1uhvddtzucs| select * from urm.esb_pm_dr_regist_infors where 1=1 and OUT_CALL_STATUS = '0' and SUBOR_HOSPITAL_DISTRICT = :1 and SCHEDUL_DATE >= to_date(:2 , 'yyyy/mm/dd') and SCHEDUL_DATE <= to_date(:3 , 'yyyy/mm/dd') and DR_CODE = :4 and DEPT_CODES = :5   
47rjnu9vtspmy| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND "A1"."ITEM_CODE"=:V00002 AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
47zf852ccf4qd| SELECT t.* FROM (select * from ESB_PA_INHOSP_REG_INFOR where 1=1 and VISIT_CARD_NO = '1100995745') t WHERE ROWNUM < 1000  
48v6k1d4s1txt| select * from qyhYzkbOpIncomeCharge t where t.DATEID = :1 and t.ORGID = :2   
4bd22u3q0p7mp| update t_sm_dblock set version=version+1, lock_time=sysdate where operation=:1 and key=:2 and version=:3 and (locked='N' or lock_time<sysdate-:4 /24/60/60)  
4bnr0k0nxykf2| SELECT COUNT(*) FROM WOP.VDPB_QUEUE_COUNT T WHERE T.PHARMACY_ID = :B2 AND T.PHARMACY_WIN_CLASS = :B1   
4mpkm9h0x47uu| select A.* from V_DATA_PRESCRIPTION_DETAIL A , V_DATA_PRESCRIPTION B where A.ID=B.ID AND B.PRESCRIBE_TIME >= to_date('2025-01-20 00:00:00', 'yyyy-MM-dd hh24:mI:ss') AND B.PRESCRIBE_TIME <= to_date('2025-01-21 00:00:00', 'yyyy-MM-dd hh24:mI:ss')  
4nh3ub5zdrbbf| select interlist0_.FINTER_ID as FINTER_ID1_5_, interlist0_.FVERSION as FVERSION2_5_, interlist0_.FINTER_NAME as FINTER_NAME3_5_, interlist0_.FINTER_CODE as FINTER_CODE4_5_, interlist0_.FXML_HEAD as FXML_HEAD5_5_, interlist0_.FWX_APP_ID as FWX_APP_ID6_5_, interlist0_.FWX_APP_NAME as FWX_APP_NAME7_5_, interlist0_.FINTER_WAY as FINTER_WAY8_5_, interlist0_.FINTER_WAY_CONTENT as FINTER_WAY_CONTENT9_5_, interlist0_.FIS_CIRC_XML as FIS_CIRC_XML10_5_, interlist0_.FIS_XML_PARAM as FIS_XML_PARAM11_5_, interlist0_.FXML_CONTENT as FXML_CONTENT12_5_, interlist0_.FIS_OPEN as FIS_OPEN13_5_, interlist0_.FORDER_NUMBER as FORDER_NUMBER14_5_, interlist0_.FIN_PARAMS as FIN_PARAMS15_5_, interlist0_.FCURSOR as FCURSOR16_5_ from PS_INTER_LIST interlist0_ where interlist0_.FINTER_CODE=:1   
4pbn1pv4kucsv|  select ͳƿ , placer_code , ҽ, ְ, count(*) , sum(ܷ) ܷ, sum(ҩ) ҩ, sum(Ϸ) Ϸ, roundsum(ҩ)/decode(sum(ܷ), 0, 1, sum(ܷ)), 4)*100||'%' ҩ, roundsum(Ϸ)/decode(sum(ܷ), 0, 1, sum(ܷ)), 4)*100||'%' ϱ, roundsum(ܷ) /count(*), 2 ˾ from (select to_char(i.charge_datetime, 'yyyy-MM-dd') շ, k.ks ͳƿ, i.patient_name , odw.account_id, i.card_id, pg_his_dict_mapping.get_dept_code_from_id(odw.dept_id) ƺ, pg_his_dict_mapping.get_dept_name_from_id(odw.dept_id) , odw.placer_code, odw.placer_name ҽ, (select doc.FTITLE_NAME from urm.doctor doc where doc.fdr_code=odw.placer_code and rownum=1) ְ, sum(odw.actual_amount) ܷ, sum(case when odw.invoice_code in ('4830', '4831', '4832') then odw.actual_amount else 0 end ) ҩ, sum(case when odw.invoice_code in ('242413') then odw.actual_amount else 0 end ) Ϸ, i.active_flag Ʊ״̬ from t_ob_invoice i inner join t_ob_payment p on i.payment_id = p.id inner join t_ob_paymentitems ps on i.id = p s.invoice_id inner join t_odw_orderbilling odw on odw.id = ps.order_billing_id left join unicorn.EZS_KS_YS@emr_link k on k.ysh = odw.placer_code where 1=1 and i.charge_datetime >= to_date('2025-01-15 00:00:00', 'yyyy-mm-dd hh24:mi:ss') and i.charge_datetime < to_date('2025-01-15', 'yyyy-mm-dd') + 1 and i.invoice_no is not null and i.active_flag = 'Y' and odw.placer_code in (select ysh from unicorn.EZS_KS_YS@emr_link where ks in ( 'ۺϲ')) group by k.ks, to_char(i.charge_datetime, 'yyyy-MM-dd'), odw.account_id, i.patient_name, i.card_id, odw.placer_code, odw.placer_name, i.active_flag, odw.dept_id) group by ͳƿ, placer_code, ҽ, ְ  
4ua10u4pbtsqp| select * from V_DATA_PRESCRIPTION where PRESCRIBE_TIME >= to_date('2025-01-20 00:00:00', 'yyyy-MM-dd hh24:mI:ss') AND PRESCRIBE_TIME <= to_date('2025-01-21 00:00:00', 'yyyy-MM-dd hh24:mI:ss')  
4yf3t9abkd8f2| delete from BI_Fact_Visit_Register_Time where to_number(to_char(Regist_Time, 'yyyymmdd'))>=to_number(to_char(sysdate, 'yyyymmdd'))  
51ny34wxhrzv4| insert into T_SM_EXTERNAL_SYS_LOGGER (MSG_ID, FUNC_ID, FUNC_NAME, METHOD_TYPE, REQUESTXML, RESPONSEXML, START_TIME, END_TIME, SEND_STATUS, CONSUMER, PROVIDER, CREATE_DATETIME, LAST_UDP_TIME, ID) values (:1 , :2 , :3 , :4 , :5 , :6 , :7 , :8 , :9 , :10 , :11 , :12 , :13 , :14 )  
5965cwv3r2tz3|  select obsettleac0_.ID as ID108_, obsettleac0_.VISIT_ID as VISIT2_108_, obsettleac0_.ACCOUNT_ID as ACCOUNT3_108_, obsettleac0_.INDI_ID as INDI4_108_, obsettleac0_.MEDICAL_REGISTRATION_NO as MEDICAL5_108_, obsettleac0_.FEE_BATCH as FEE6_108_, obsettleac0_.ACTIVE_FLAG as ACTIVE7_108_, obsettleac0_.ACCOUNT_FLAG as ACCOUNT8_108_, obsettleac0_.TREATMENT_TYPE as TREATMENT9_108_, obsettleac0_.HOSPITAL_ID as HOSPITAL10_108_, obsettleac0_.ZYZJE as ZYZJE108_, obsettleac0_.SBZFJE as SBZFJE108_, obsettleac0_.ZHZFJE as ZHZFJE108_, obsettleac0_.BFXMZFJE as BFXMZFJE108_, obsettleac0_.QFJE as QFJE108_, obsettleac0_.GRZFJE1 as GRZFJE16_108_, obsettleac0_.GRZFJE2 as GRZFJE17_108_, obsettleac0_.GRZFJE3 as GRZFJE18_108_, obsettleac0_.CXZFJE as CXZFJE108_, obsettleac0_.YYFDJE as YYFDJE108_, obsettleac0_.CASH_PAY_COM as CASH21_108_, obsettleac0_.ACCT_PAY_COM as ACCT22_108_, obsettleac0_.CASH_PAY_OWN as CASH23_108_, obsettleac0_.ACCT_PAY_OWN as ACCT24_108_, obsettleac0_.OUTPAT_OR_INPA T as OUTPAT25_108_, obsettleac0_.CREATE_TIME as CREATE26_108_, obsettleac0_.CREATOR_ID as CREATOR27_108_, obsettleac0_.CREATOR_CODE as CREATOR28_108_, obsettleac0_.LAST_UPD_TIME as LAST29_108_, obsettleac0_.LAST_UPD_USER_ID as LAST30_108_, obsettleac0_.LAST_UPD_USER_CODE as LAST31_108_, obsettleac0_.INVOICE_ID as INVOICE32_108_, obsettleac0_.SETTLE_SOURCE as SETTLE33_108_, obsettleac0_.IS_CHANGE as IS34_108_, obsettleac0_.PAT_NAME as PAT35_108_, obsettleac0_.YIBAO_TYPE as YIBAO36_108_, obsettleac0_.ORG_ID as ORG37_108_, obsettleac0_.REFUND_FLAG as REFUND38_108_, obsettleac0_.IN_DISEASE as IN39_108_, obsettleac0_.PATIENT_ID as PATIENT40_108_, obsettleac0_.RELOAD_TYPE as RELOAD41_108_, obsettleac0_.SETTLE_FLAG as SETTLE42_108_, obsettleac0_.ECBX_MEDI_NO as ECBX43_108_, obsettleac0_.ECBX_JZZE as ECBX44_108_, obsettleac0_.ECBX_BUSINESS_TYPE as ECBX45_108_, obsettleac0_.THIRD_MEDICARD_ORDER_NO as THIRD46_108_, obsettleac0_.OTHER_ACCOUNT_DEBTED1 as OTHER47_108_, obsett leac0_.OTHER_ACCOUNT_DEBTED2 as OTHER48_108_, obsettleac0_.OTHER_ACCOUNT_DEBTED3 as OTHER49_108_, obsettleac0_.OTHER_ACCOUNT_DEBTED4 as OTHER50_108_, obsettleac0_.OTHER_ACCOUNT_DEBTED5 as OTHER51_108_, obsettleac0_.OTHER_ACCOUNT_DEBTED6 as OTHER52_108_, obsettleac0_.YIBAO_SETTLE_NO as YIBAO53_108_, obsettleac0_.MI_CODE as MI54_108_, obsettleac0_.YB_BALANCE_STATUS as YB55_108_, obsettleac0_.YB_INSU_TYPE_CODE as YB56_108_, obsettleac0_.YB_INSU_TYPE_NAME as YB57_108_, obsettleac0_.YB_DISE_CODG as YB58_108_, obsettleac0_.YB_DISE_NAME as YB59_108_, obsettleac0_.PSN_TYPE as PSN60_108_, obsettleac0_.INSU_OPTINS as INSU61_108_, obsettleac0_.EMP_NAME as EMP62_108_, obsettleac0_.INSCP_SCP_AMT as INSCP63_108_, obsettleac0_.POOL_PROP_SELFPAY as POOL64_108_, obsettleac0_.CVLSERV_PAY as CVLSERV65_108_, obsettleac0_.OTH_PAY as OTH66_108_, obsettleac0_.CASH_PAYAMT as CASH67_108_, obsettleac0_.BALC as BALC108_, obsettleac0_.ACCT_MULAID_PAY as ACCT69_108_, obsettleac0_.BEFORE_SETTL EMENT_BALC as BEFORE70_108_, obsettleac0_.CALCULATOR_MARKER as CALCULATOR71_108_, obsettleac0_.HIFDM_PAY as HIFDM72_108_, obsettleac0_.PAY_ORDID as PAY73_108_, obsettleac0_.PAY_TOKEN as PAY74_108_, obsettleac0_.PAY_AUTH_NO as PAY75_108_, obsettleac0_.CRTF_RULE_CODE as CRTF76_108_, obsettleac0_.MED_SUMFEE as MED77_108_, obsettleac0_.PSN_PART_AMT as PSN78_108_, obsettleac0_.YB_MDTRT_CERT_NO as YB79_108_, obsettleac0_.YB_MDTRT_CERT_TYPE as YB80_108_, obsettleac0_.IN_DISEASE_NAME as IN81_108_, obsettleac0_.SETTLE_SEQ_YEAR as SETTLE82_108_, obsettleac0_.YB_EXP_CONTENT as YB83_108_, obsettleac0_.HMB_INSU_FLAG as HMB84_108_, obsettleac0_.FUND_PAY_SUMAMT as FUND85_108_, obsettleac0_.YB_CVLSERV_FLAG as YB86_108_, obsettleac0_.YB_CLR_OPTINS as YB87_108_, obsettleac0_.YB_CLR_WAY as YB88_108_, obsettleac0_.YB_CLR_TYPE as YB89_108_, obsettleac0_.HIFOB_PAY as HIFOB90_108_, obsettleac0_.HIFMI_PAY as HIFMI91_108_, obsettleac0_.HIFES_PAY as HIFES92_108_, obsettleac0_.MAF_PAY as M AF93_108_, obsettleac0_.HIFP_PAY as HIFP94_108_, obsettleac0_.PLATFORM_SEQ_ID as PLATFORM95_108_, obsettleac0_.THIRD_PARTY_REF_NO as THIRD96_108_, obsettleac0_.UNIONPAY_SEQ_NO as UNIONPAY97_108_, obsettleac0_.UPLOAD_STAS_TYPE as UPLOAD98_108_, obsettleac0_.SETTLE_CHANNEL as SETTLE99_108_ from T_OB_SETTLEACCOUNT obsettleac0_ where 1=1 and obsettleac0_.INVOICE_ID=:1 and obsettleac0_.ACTIVE_FLAG='Y' and obsettleac0_.REFUND_FLAG='N'  
5nz3dctx1y13j| SELECT COUNT(1) FROM T_SM_PARAITEM P WHERE P.CATALOG_ID = '070111' AND P.ITEM_VALUE = :B1   
5qnpb11bzakp0| select r.* from sq_esb_pm_dr_regist_infor r where 1=1 and r.SCHEDUL_DATE >=to_date(:1 , 'yyyy-MM-dd') and r.SCHEDUL_DATE < to_date(:2 , 'yyyy-MM-dd')+1 and r.SUBOR_HOSPITAL_DISTRICT = :3 order by r.OUT_CALL_STATUS desc, to_date(to_char(r.SCHEDUL_DATE, 'yyyy-mm-dd') || ' ' ||r.start_Time, 'yyyy-mm-dd hh24:mi:ss') asc, r.quota_Usage desc, nvl(r.REGIST_NUMBER, 0) asc   
5r5pa47z6zauj| INSERT INTO BAC_SHEDLOCK(name, lock_until, locked_at, locked_by) VALUES(:1 , :2 , :3 , :4 )  
5t4gc4s91q44p| SELECT count(0) FROM (SELECT DISTINCT IPPAT_NO, PAT_NAME, PAT_SEX_NAME, FULL_AGE, WARD_ID, WARD_NAME, PRESP_NOTE_ID, DISPENSE_NOTE_ID, BED_CODE, DISPENSE_TIME, is_deliver FROM VDPB_DP_PRESP_DRUG_DETAIL v WHERE 1 = 1 AND v.dispense_time >= to_date(:1 , 'yyyy-MM-dd HH24:mi:ss') AND v.dispense_time <= to_date(:2 , 'yyyy-MM-dd HH24:mi:ss') AND v.pharmacy_id = :3 AND v.is_dispense = :4 ) table_count  
5x20uhxy5qbjf|  INSERT INTO WOPB.DPT_EMR_PRESP_DETAIL (DISPENSE_DETAIL_ID, PAT_ID, VISIT_ID, PAT_NAME, INVOICE_ID, CHARGE_TIME, PRESP_ID, PRESP_TYPE, PRESP_TIME, BRANCH_ID, OP_DEPT_ID, OP_DEPT_NAME, OP_DOCTOR_ID, OP_DOCTOR_NAME, DIAGNOSIS_CODE, DIAGNOSIS_DESC, DIAGNOSIS_DESC_CN, PAT_WEIGHT, PHARMACY_ID, PHARMACY_NAME, ORDER_TYPE, IS_SUB_ORDER, ORDER_NO, ORDER_GROUP_NO, ORDER_SORT_NO, PARENT_ORDER_NO, PARENT_ORDER_FLAG, ITEM_ID, ITEM_NAME, ITEM_SPEC, ITEM_PRICE, PKG_UNIT, PKG_UNIT_RATIO, MIN_PKG_UNIT, ITEMPKG_ID, ORDER_DOSAGE, DOSAGE_UNIT, MIN_DOSAGE, MIN_DOSAGE_UNIT, IS_PRINTDOSA, DOSE_WAY_ID, DOSE_WAY_NAME, FREQUENCY_ID, FREQUENCY_NAME, FREQUENCY_DAY_NUM, FREQUENCY_EXEC_TIME, PRES_DAYS, ORDER_ADVICE, QUANTITY, SUM_CHARGE, ORDER_DESC, HERBAL_REPETITION, HERBAL_DECOCT_NAME, HERBAL_DOSE_WAY_CODE, HERBAL_DOSE_WAY_NAME, HERBAL_FREQ_DAY_NUM, DECOCT_ORDER, IS_AVAILABLE, CREATE_USER, CREATE_DATE, UPDATE_USER, UPDATE_DATE) SELECT SYS_GUID() AS DISPE NSE_DETAIL_ID, T.PATIENT_ID AS PAT_ID, T.VISIT_ID AS VISIT_ID, T.PAT_NAME AS PAT_NAME, :B8 AS INVOICE_ID, :B7 AS CHARGE_TIME, T.PRES_NOTE_ID AS PRESP_ID, '1' AS PRESP_TYPE, T.PRES_TIME AS PRESP_TIME, T.BRANCH_ID AS BRANCH_ID, T.DEPT_ID AS OP_DEPT_ID, T.DEPT_NAME AS OP_DEPT_NAME, T.DOCTOR_ID AS OP_DOCTOR_ID, T.DOCTOR_NAME AS OP_DOCTOR_NAME, :B6 AS DIAGNOSIS_CODE, :B5 AS DIAGNOSIS_DESC, :B4 AS DIAGNOSIS_DESC_CN, NULL AS PAT_WEIGHT, 'null' AS PHARMACY_ID, 'null' AS PHARMACY_NAME, DECODE(T.PRES_TYPE, '3', 'CY', 'XY') AS ORDER_TYPE, DECODE(T.ORDER_ID, T.ORDER_NO, 'N', 'Y') AS IS_SUB_ORDER, T.ORDER_ID AS ORDER_NO, T.ORDER_NO AS ORDER_GROUP_NO, T.ORDER_SUB_NO AS ORDER_SORT_NO, T.ORDER_NO AS PARENT_ORDER_NO, NULL AS PARENT_ORDER_FLAG, NVL(T.ITEM_ID, 'null') AS ITEM_ID, NVL(T.ITEM_NAME, 'null') AS ITEM_NAME, NVL(T.ITEM_SPEC, 'null') AS ITEM_SPEC, NVL(T.ITEM_PRICE, 0) AS ITEM_PRICE, NVL(T.DISPENSE_UNIT, 'null') AS PKG_UNIT, 1 AS PKG_UNIT_RATIO, NULL AS MIN_PKG_UNIT, NULL AS ITEMPKG_ID, T.DOSAGE AS ORDER_DOSAGE, T.DOSAGE_UNIT AS DOSAGE_UNIT, NULL AS MIN_DOSAGE, T.DOSAGE_UNIT AS MIN_DOSAGE_UNIT, 'Y' AS IS_PRINTDOSA, T.DOSE_WAY_ID AS DOSE_WAY_ID, T.DOSE_WAY_NAME AS DOSE_WAY_NAME, T.FREQUENCY_ID AS FREQUENCY_ID, T.FREQUENCY_NAME AS FREQUENCY_NAME, T.FREQUENCY_EXECUTE AS FREQUENCY_DAY_NUM, T.FREQ_SUM AS FREQUENCY_EXEC_TIME, T.DAYS AS PRES_DAYS, SUBSTR(TRIM(T.PRES_DESCR), 1, 25) AS ORDER_ADVICE, T.QUANTITY AS QUANTITY, T.AMOUNT AS SUM_CHARGE, SUBSTR(TRIM(T.PRES_DESCR), 1, 25) AS ORDER_DESC, (T.DAYS * T.FREQUENCY_EXECUTE) AS HERBAL_REPETITION, T.HERBAL_DOSE_WAY_NAME AS HERBAL_DECOCT_NAME, T.DOSE_WAY_ID AS HERBAL_DOSE_WAY_CODE, T.DOSE_WAY_NAME AS HERBAL_DOSE_WAY_NAME, T.FREQUENCY_EXECUTE AS HERBAL_FREQ_DAY_NUM, T.DECOCTORDER_NAME AS DECOCT_ORDER, 'Y' AS IS_AVAILABLE, 'admin' AS CREATE_USER, SYSDATE AS CREATE_DATE, 'admin' AS UPDATE_USER, SYSDATE AS UPDATE_DATE FROM COMM.WOP_EMR_PRES_DETAIL@EMR_VIEW_LINK T WHE RE T.PATIENT_ID = :B3 AND T.VISIT_ID = :B2 AND T.PRES_NOTE_ID = :B1   
652v2j6y7uk5j| update t_sm_dblock set version=version+1, locked=:1 , lock_time=sysdate where operation=:2 and key=:3 and version=:4 and (locked=:5 or lock_time<sysdate-:6 /24/60/60)  
6744kvtnv7utw|  select q.invoice_id, q.YYJB, (case when q.dept_id='63710' and q.mi_code='4796' then '' end) "ҽ", nvl((select k.amount from t_ob_chargetype k where k.charge_type='254254' and k.invoice_id=q.invoice_id), 0) ҽԺŻ, (select to_char(wm_concat(j.item_value)) from t_sm_paraitem j where j.id in( select k.charge_type from t_ob_chargetype k where k.invoice_id=q.invoice_id)) ʾ֧, q.AMOUNT_01, q.AMOUNT_02, q.AMOUNT_03, q.AMOUNT_04, q.AMOUNT_05, q.AMOUNT_06, q.AMOUNT_07, q.AMOUNT_08, q.AMOUNT_09, q.AMOUNT_10, q.AMOUNT_11, q.AMOUNT_12, q.refund_zcf, q.org_id, q.dept_id, q.atdr_code, q.cashier_code, q.cashier_name, q.dr_code, q.ass_win, q.tips, q.pre_pay, q.precharge, q.PRECHARGESTR from (select h.*, i.mi_code, i.org_id, (select k.attending_doctor_code from t_or_visit k where k.visit_id||'-1'=:1 ) atdr_code, dep.id dept_id, dep.dept_name, i.cashier_code, i.cashier_name, nvl((select odw.placer_name from t_odw_orderbilling odw, t_ob_paymentitems ps where ro wnum=1 and odw.id=ps.order_billing_id and ps.payment_id=i.payment_id and odw.placer_name not in (select u.user_name from t_sm_userbaseinfo u where u.remark='xn')), '') as dr_code, i.ass_win, '뵽'|| nvl(i.ass_win, 'ҩ') ||'Ŷȡҩ' as tips, case when instr(i.remark, '')>0 then substr(i.remark, instr(i.remark, '')) else null end as pre_pay, nvl(i.precharge, 0) as precharge, i.remark as PRECHARGESTR from (select T_OB_FC_AMOUNT.INVOICE_ID, '' YYJB, sum(case when d.id=15989 then AMOUNT else NULL end) AMOUNT_01, --ҩ sum(case when d.id=14987 then AMOUNT else NULL end) AMOUNT_02, --гҩ sum(case when d.id=23006 then AMOUNT else NULL end) AMOUNT_03, --вҩ sum(case when d.id=23509 then AMOUNT else NULL end) AMOUNT_04, -- sum(case when d.id=15992 then AMOUNT else NULL end) AMOUNT_05, -- sum(case when d.id=15993 then AMOUNT else NULL end) AMOUNT_06, -- sum(case when d.id=15994 then AMOUNT else NULL end) AMOUNT_07, --Ʒ sum(case when d.id=15995 then AMOUNT else NULL end) AMOUNT_08, -- sum(case when d.id=15996 then AMOUNT else NULL end) AMOUNT_09, --Ϸ sum(case when d.id=15997 then AMOUNT else NULL end) AMOUNT_10, -- sum(case when d.id=15998 then AMOUNT else NULL end) AMOUNT_11, --λ sum(case when d.id=15999 then AMOUNT else NULL end) AMOUNT_12, -- sum(case when d.id=23509 then nvl(AMOUNT, 0)-nvl(T_OB_FC_AMOUNT.NO_DEBTED, 0) else 0 end) refund_zcf from T_OB_FC_AMOUNT, t_fm_reportindex_d d , t_fm_reportindexitem item, t_ob_invoice where d.id = item.rid_id and T_OB_FC_AMOUNT.INVOICE_CLASSIFICATION= item.index_item_id and T_OB_FC_AMOUNT.INVOICE_ID= :2 and T_OB_FC_AMOUNT.INVOICE_ID=t_ob_invoice.id group by T_OB_FC_AMOUNT.INVOICE_ID)h, t_ob_invoice i, t_sm_department dep where h.invoice_id=i.id and i.dept_id=dep.id)q  
68vcxdwvu2g0z|  /* MV_REFRESH (INS) */ INSERT /*+ NOAPPEND */ INTO "HISUSER"."MV_SM_3CATALOG_ORG" SELECT /*+ NO_MERGE("JV$") */ "JV$"."RID$", "MAS$1".ROWID, "MAS$0".ROWID, "MAS$1"."ID", "MAS$1"."PRODUCTID", "MAS$1"."PRODUCT_NAME", "JV$"."COMMON_NAME", "JV$"."PINYIN_CODE", "JV$"."WUBI_CODE", "JV$"."SPELLING_CODE", "JV$"."COMMON_ENG_NAME", "MAS$1"."PRODUCT_ENG_NAME", (-1), "JV$"."SINGLE_DOSE_SPEC", "JV$"."STORE_UNIT", "MAS$1"."PINYIN_CODE", "MAS$1"."WUBI_CODE", "MAS$1"."SPELLING_CODE", "MAS$1"."MEMORY_CODE", "JV$"."FINANCE_CODE", "JV$"."OP_INVOICE_CODE", "JV$"."IP_INVOICE_CODE", (- 1), ROUND("MAS$1"."RETAIL_PRICE"/"JV$"."STOREHOUSE_UNIT_TO_STORE_UNIT", 5), '030301', "MAS$1"."VERSION_NO", "JV$"."DOSAGE_FORM", "JV$"."LABEL_UNIT", "JV$"."STORE_UNIT_TO_LABEL_UNIT", "JV$"."OP_DISPENSE_UNIT", "JV$"."OP_DISPENSE_UNIT_TO_STORE_UNIT", "JV$"."USE_OF", "JV$"."PACKAGE_SPEC", "JV$"."ON_ONE_PX", "JV$"."ACCUMULATION_FLAG", "JV$"."IP_DISPENSE_UNIT", "JV$"."IP_DISPENSE_UNIT_TO_STORE_UNIT", ' ', ' ', ' ', ' ', ' ', "JV$"."ACTIVE_FLAG", "MAS$1"."ACTIVE_FLAG", "JV$"."DRUNK_DRUGS_FLAG", "JV$"."TOXIC_DRUGS_FLAG", 'Y', 'Y' FROM ( SELECT "MAS$"."ROWID" "RID$" , "MAS$".* FROM "HISUSER "."T_DM_DRUGDICT" "MAS$" WHERE ROWID IN (SELECT /*+ HASH_SJ */ CHARTOROWID("MAS$"."M_ROW$$") RID$ FROM "HISUSER"."MLOG$_T_DM_DRUGDICT1" "MAS$" WHERE "MAS$".SNAPTIME$$ > :B_ST2 )) "JV$", "T_SM_ORGANIZATION" AS OF SNAPSHOT(:B_SCN) "MAS$0", "T_DM_DRUGLIST" "MAS$1" WHERE "JV$"."ID"="MAS$1"."DM_DRUGDICT_ID" AND "MAS$0"."ID"<>0  
69k5bhm12sz98|  SELECT dbin.instance_number, dbin.db_name, dbin.instance_name, dbin.host_name, dbin.version, CASE WHEN s1.startup_time = s2.startup_time THEN 0 ELSE 1 END as bounce, CAST(s1.end_interval_time AS DATE) as begin_time, CAST(s2.end_interval_time AS DATE) as end_time, ROUND((cast( (case when s2.end_interval_time > s1.end_interval_time then s2.end_interval_time else s1.end_interval_time end) as date) - cast(s1.end_interval_time as date)) * 86400) as int_secs, CASE WHEN (s1.status <> 0 OR s2.status <> 0) THEN 1 ELSE 0 END as err_detect, round( greatest( (extract(day from s2.flush_elapsed) * 86400) + (extract(hour from s2.flush_elapsed) * 3600) + (extract(minute from s2.flush_elapsed) * 60) + extract(second from s2.flush_elapsed), (extract(day from s1.flush_elapsed) * 86400) + (extract(hour from s1.flush_elapsed) * 3600) + (extract(minute from s1.flush_elapsed) * 60) + extract(second from s1.flush_elapsed), 0 )) as max_flush_secs FROM WRM$_SNAPSHOT s1 , WRM$_DATABASE _INSTANCE dbin , WRM$_SNAPSHOT s2 WHERE s1.dbid = :dbid AND s2.dbid = :dbid AND s1.instance_number = s2.instance_number AND dbin.instance_number = s1.instance_number AND s1.snap_id = :bid AND s2.snap_id = :eid AND dbin.dbid = s1.dbid AND dbin.startup_time = s1.startup_time and dbin.instance_number = :inst  
6gdn0m2zkmbz7| DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN hisuser.PG_HIS_WMD.pf_wmd_ms; :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END;   
6pqru4undjfj5| select version from t_sm_dblock where operation=:1 and key=:2   
6z7g6p5vzf8c2|  SELECT note.DISPENSE_NOTE_ID as DISPENSE_NOTE_ID, note.PAT_NAME as PAT_NAME, note.PAT_SEX_NAME as PAT_SEX_NAME, note.MED_CARD_NO as MED_CARD_NO, note.INVOICE_NO as INVOICE_NO, note.PRESP_NO as PRESP_NO, note.OP_DEPT_NAME as OP_DEPT_NAME, note.OP_DOCTOR_NAME as OP_DOCTOR_NAME, note.CHARGE_TIME as CHARGE_TIME, note.dispense_note_type as dispense_note_type, note.pre_queue_num as pre_queue_num, note.is_printed as is_printed, win.pharmacy_win_code as pharmacy_win_code, trunc(note.CHARGE_TIME) as charge_date, note.last_state_name as last_state_name, note.is_cancel as is_cancel, note.herbal_repetition as herbal_repetition, note.herbal_dose_way_name as herbal_dose_way_name, note.herbal_freq_day_num as herbal_freq_day_num, note.pharmacy_id as pharmacy_id FROM wopb.DPB_OP_DISPENSE_NOTE note, wop.dpc_pharmacy_win win WHERE note.actual_win_id = win.pharmacy_win_id AND note.CHARGE_TIME >= :adt_begin AND note.CHARGE_TIME < :adt_end and note.pharmacy_id = :as_pharmacy_id an d note.actual_win_id like :as_pharmacy_win_id and (note.pat_name like :as_query or note.med_card_no like :as_query )   
720d7u76g8wjr| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003 OR "A1"."ITEM_CODE"=:V00004 OR "A1"."ITEM_CODE"=:V00005 OR "A1"."ITEM_CODE"=:V00006) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
787skx2f5ffyg|  select account0_.ID as ID158_, account0_.ACCOUNT_ID as ACCOUNT2_158_, account0_.VISIT_ID as VISIT3_158_, account0_.MI_CODE as MI4_158_, account0_.PAY_SCALE as PAY5_158_, account0_.MF_SCALE as MF6_158_, account0_.DRUGS_LIMIT as DRUGS7_158_, account0_.TREATMENT_LIMIT as TREATMENT8_158_, account0_.DISEASE_CODE as DISEASE9_158_, account0_.SPECIAL_DISEASE_ID as SPECIAL10_158_, account0_.PID as PID158_, account0_.FIRM_CODE as FIRM12_158_, account0_.MI_CARD_ID as MI13_158_, account0_.CREATOR_ID as CREATOR14_158_, account0_.CREATOR_VER_ID as CREATOR15_158_, account0_.CREATE_TIME as CREATE16_158_, account0_.LAST_UPD_USER as LAST17_158_, account0_.LAST_UPD_USER_VER_ID as LAST18_158_, account0_.LAST_UPD_TIME as LAST19_158_, account0_.MATERIAL_LIMIT as MATERIAL20_158_, account0_.OP_QUOTA_TYPE as OP21_158_, account0_.OP_DEBTED_QUOTA as OP22_158_, account0_.OP_QUOTA_DURATION as OP23_158_, account0_.TIME_STAMP as TIME24_158_, account0_.ACCOUNT_DEBT_COUNT as ACCOUNT25_158_ from T_OR_ACCOUNT account0_ where account0_.ACCOUNT_ID=:1   
7ahdc26dxpwfu| UPDATE WDP.DPC_STORAGE_DRUG G SET G.ITEM_CNNAME = :B7 , G.ITEM_CNALIAS = :B6 , G.ITEM_SPEC = :B5 , G.PKG_UNIT = :B4 , G.PKG_UNIT_RATIO = :B3 , G.MIN_PKG_UNIT = :B2 , G.IS_AVAILABLE = 'Y' WHERE G.ITEM_ID = :B1   
7bqavhxqu996b|  select clientmess0_.id as id321_, clientmess0_.action_flag as action2_321_, clientmess0_.active_flag as active3_321_, clientmess0_.callback as callback321_, clientmess0_.client_key as client5_321_, clientmess0_.client_model as client6_321_, clientmess0_.handle_time as handle7_321_, clientmess0_.handle_user as handle8_321_, clientmess0_.key as key321_, clientmess0_.message as message321_, clientmess0_.only_active as only11_321_, clientmess0_.org_id as org12_321_, clientmess0_.params as params321_, clientmess0_.result as result321_, clientmess0_.send_time as send15_321_, clientmess0_.send_to_all as send16_321_, clientmess0_.show_time as show17_321_, clientmess0_.status as status321_, clientmess0_.title as title321_, clientmess0_.type as type321_, clientmess0_.user_id as user21_321_ from T_SM_CLIENT_MESSAGE clientmess0_ where ( clientmess0_.active_flag = 'Y') and clientmess0_.status='NEW' and (clientmess0_.client_key=:1 or clientmess0_.user_id=:2 or clientmess0_.send_t o_all='Y') order by clientmess0_.send_time  
7ng34ruy5awxq| select i.obj#, i.ts#, i.file#, i.block#, i.intcols, i.type#, i.flags, i.property, i.pctfree$, i.initrans, i.maxtrans, i.blevel, i.leafcnt, i.distkey, i.lblkkey, i.dblkkey, i.clufac, i.cols, i.analyzetime, i.samplesize, i.dataobj#, nvl(i.degree, 1), nvl(i.instances, 1), i.rowcnt, mod(i.pctthres$, 256), i.indmethod#, i.trunccnt, nvl(c.unicols, 0), nvl(c.deferrable#+c.valid#, 0), nvl(i.spare1, i.intcols), i.spare4, i.spare2, i.spare6, decode(i.pctthres$, null, null, mod(trunc(i.pctthres$/256), 256)), ist.cachedblk, ist.cachehit, ist.logicalread from ind$ i, ind_stats$ ist, (select enabled, min(cols) unicols, min(to_number(bitand(defer, 1))) deferrable#, min(to_number(bitand(defer, 4))) valid# from cdef$ where obj#=:1 and enabled > 1 group by enabled) c where i.obj#=c.enabled(+) and i.obj# = ist.obj#(+) and i.bo#=:1 order by i.obj#  
7sccjnr8zm8ht|  /* MV_REFRESH (INS) */ INSERT /*+ NOAPPEND */ INTO "HISUSER"."MV_SM_3CATALOG_ORG" SELECT /*+ NO_MERGE("JV$") */ "MAS$2".ROWID, "JV$"."RID$", "MAS$0".ROWID, "JV$"."ID", "JV$"."PRODUCTID", "JV$"."PRODUCT_NAME", "MAS$2"."COMMON_NAME", "MAS$2"."PINYIN_CODE", "MAS$2"."WUBI_CODE", "MAS$2"."SPELLING_CODE", "MAS$2"."COMMON_ENG_NAME", "JV$"."PRODUCT_ENG_NAME", (-1), "MAS$2"."SINGLE_DOSE_SPEC", "MAS$2"."STORE_UNIT", "JV$"."PINYIN_CODE", "JV$"."WUBI_CODE", "JV$"."SPELLING_CODE", "JV$"."MEMORY_CODE", "MAS$2"."FINANCE_CODE", "MAS$2"."OP_INVOICE_CODE", "MAS$2"."IP_INVOICE_CODE" , (-1), ROUND("JV$"."RETAIL_PRICE"/"MAS$2"."STOREHOUSE_UNIT_TO_STORE_UNIT", 5), '030301', "JV$"."VERSION_NO", "MAS$2"."DOSAGE_FORM", "MAS$2"."LABEL_UNIT", "MAS$2"."STORE_UNIT_TO_LABEL_UNIT", "MAS$2"."OP_DISPENSE_UNIT", "MAS$2"."OP_DISPENSE_UNIT_TO_STORE_UNIT", "MAS$2"."USE_OF", "MAS$2"."PACKAGE_SPEC", "MAS$2"."ON_ONE_PX", "MAS$2"."ACCUMULATION_FLAG", "MAS$2"."IP_DISPENSE_UNIT", "MAS$2"."IP_DISPENSE_UNIT_TO_STORE_UNIT", ' ', ' ', ' ', ' ', ' ', "MAS$2"."ACTIVE_FLAG", "JV$"."ACTIVE_FLAG", "MAS$2"."DRUNK_DRUGS_FLAG", "MAS$2"."TOXIC_DRUGS_FLAG", 'Y', 'Y' FROM ( SELECT "MAS$"."ROWID" "RID$" , "MAS$ ".* FROM "HISUSER"."T_DM_DRUGLIST" "MAS$" WHERE ROWID IN (SELECT /*+ HASH_SJ */ CHARTOROWID("MAS$"."M_ROW$$") RID$ FROM "HISUSER"."MLOG$_T_DM_DRUGLIST1" "MAS$" WHERE "MAS$".SNAPTIME$$ > :B_ST1 )) "JV$", "T_SM_ORGANIZATION" AS OF SNAPSHOT(:B_SCN) "MAS$0", "T_DM_DRUGDICT" "MAS$2" WHERE "MAS$2"."ID"="JV$"."DM_DRUGDICT_ID" AND "MAS$0"."ID"<>0  
7tsw7k06q9x42| SELECT "ID", "IDENTIFIER_ID", "CREATE_TIME" FROM "T_PA_PERSON" "P" WHERE "CREATE_TIME">:1-180 AND "CREATE_TIME">=:2  
8142bgxafa240| select a.id as ROWKEY , a.* from T_ODW_ORDERBILLING a where a.create_datetime>=sysdate-7  
84aqh3u98gdk2|  select mtinspecta0_.apply_id as apply_id1_34_, mtinspecta0_.address as address2_34_, mtinspecta0_.age as age3_34_, mtinspecta0_.anaesthesia as anaesthesia4_34_, mtinspecta0_.apply_check_state as apply_check_state5_34_, mtinspecta0_.apply_dept_code as apply_dept_code6_34_, mtinspecta0_.apply_dept_id as apply_dept_id7_34_, mtinspecta0_.apply_dept_name as apply_dept_name8_34_, mtinspecta0_.apply_doctor_code as apply_doctor_code9_34_, mtinspecta0_.apply_doctor_id as apply_doctor_id10_34_, mtinspecta0_.apply_doctor_name as apply_doctor_name11_34_, mtinspecta0_.apply_doctor_type as apply_doctor_type12_34_, mtinspecta0_.apply_item_count as apply_item_count13_34_, mtinspecta0_.apply_no as apply_no14_34_, mtinspecta0_.apply_pay_amount as apply_pay_amount15_34_, mtinspecta0_.apply_pay_state as apply_pay_state16_34_, mtinspecta0_.apply_source as apply_source17_34_, mtinspecta0_.apply_time as apply_time18_34_, mtinspecta0_.appt_remark as appt_remark19_34_, mtinspecta0_.appt_stat e as appt_state20_34_, mtinspecta0_.area_id as area_id21_34_, mtinspecta0_.area_name as area_name22_34_, mtinspecta0_.automatic_reservation as automatic_reserva23_34_, mtinspecta0_.bed_no as bed_no24_34_, mtinspecta0_.branch_id as branch_id25_34_, mtinspecta0_.branch_name as branch_name26_34_, mtinspecta0_.date_birth as date_birth27_34_, mtinspecta0_.db_flag as db_flag28_34_, mtinspecta0_.dcheck_rec as dcheck_rec29_34_, mtinspecta0_.dept_code as dept_code30_34_, mtinspecta0_.dept_id as dept_id31_34_, mtinspecta0_.dept_name as dept_name32_34_, mtinspecta0_.diag as diag33_34_, mtinspecta0_.digital_age as digital_age34_34_, mtinspecta0_.dmed_rec as dmed_rec35_34_, mtinspecta0_.dphyexam as dphyexam36_34_, mtinspecta0_.dtell as dtell37_34_, mtinspecta0_.emr_phone as emr_phone38_34_, mtinspecta0_.exampurpose as exampurpose39_34_, mtinspecta0_.examination as examination40_34_, mtinspecta0_.fcalmflag as fcalmflag41_34_, mtinspecta0_.flow_num as flow_num42_34_, mtinspecta 0_.gender as gender43_34_, mtinspecta0_.health_code as health_code44_34_, mtinspecta0_.id_number as id_number45_34_, mtinspecta0_.infecthistory as infecthistory46_34_, mtinspecta0_.inhosp_num as inhosp_num47_34_, mtinspecta0_.insp_type_code as insp_type_code48_34_, mtinspecta0_.insp_type_id as insp_type_id49_34_, mtinspecta0_.insp_type_name as insp_type_name50_34_, mtinspecta0_.internet as internet51_34_, mtinspecta0_.ip_patient_id as ip_patient_id52_34_, mtinspecta0_.isavailable as isavailable53_34_, mtinspecta0_.list_print_date as list_print_date54_34_, mtinspecta0_.list_print_flag as list_print_flag55_34_, mtinspecta0_.logcby as logcby56_34_, mtinspecta0_.logcdate as logcdate57_34_, mtinspecta0_.logluby as logluby58_34_, mtinspecta0_.logludate as logludate59_34_, mtinspecta0_.manual_add_flag as manual_add_flag60_34_, mtinspecta0_.multiresisbact as multiresisbact61_34_, mtinspecta0_.new_ip_patient as new_ip_patient62_34_, mtinspecta0_.op_patient_id as op_patient_i d63_34_, mtinspecta0_.order_num as order_num64_34_, mtinspecta0_.original_area as original_area65_34_, mtinspecta0_.other_remark as other_remark66_34_, mtinspecta0_.pacs_state as pacs_state67_34_, mtinspecta0_.patient_id as patient_id68_34_, mtinspecta0_.patient_name as patient_name69_34_, mtinspecta0_.patient_num as patient_num70_34_, mtinspecta0_.phone as phone71_34_, mtinspecta0_.print_date as print_date72_34_, mtinspecta0_.print_flag as print_flag73_34_, mtinspecta0_.print_times as print_times74_34_, mtinspecta0_.print_user_name as print_user_name75_34_, mtinspecta0_.priority as priority76_34_, mtinspecta0_.relate_apply as relate_apply77_34_, mtinspecta0_.remark as remark78_34_, mtinspecta0_.specialinfection as specialinfection79_34_, mtinspecta0_.special_requirements as special_requireme80_34_, mtinspecta0_.state as state81_34_, mtinspecta0_.sync_remark as sync_remark82_34_, mtinspecta0_.sync_state as sync_state83_34_, mtinspecta0_.transportmode as transportmo de84_34_, mtinspecta0_.valid_end_date as valid_end_date85_34_ from mt_inspect_apply mtinspecta0_ where (mtinspecta0_.patient_num=:1 or mtinspecta0_.patient_name=:2 or mtinspecta0_.patient_id=:3 or mtinspecta0_.op_patient_id=:4 or mtinspecta0_.ip_patient_id=:5 or mtinspecta0_.apply_no=:6 or mtinspecta0_.flow_num=:7 or mtinspecta0_.health_code=:8 or mtinspecta0_.id_number=:9) and mtinspecta0_.isavailable='Y' and mtinspecta0_.state='ZC' and to_char(apply_time, 'yyyy-MM-dd')>=:10  
8hs1qzm4j4zqk| select reg_id, visit_id, card_no, patient_name, sex, patient_id, contact_addr, dob, height, weight, age, identity_no, phone_no, remark, que_no, dept_code, dept_name, doctor_code, doctor_name, reg_time, area_code, area_name, reg_status, reg_period, treat_status, treat_time , treat_doctor_code, treat_doctor_name, patient_source, seq_code, seq_name, que_type, app_start_time, app_end_time, his_doctor_leave, section_code, site_type, his_room_name from v_lianfan_clinic_calls where clinic_time >= :1 and clinic_time<:2   
8nbhkyycmx838| select r.* from sq_esb_pm_dr_regist_infor r where 1=1 and r.SCHEDUL_DATE >=to_date(:1 , 'yyyy-MM-dd') and r.SCHEDUL_DATE < to_date(:2 , 'yyyy-MM-dd')+1 and to_date(to_char(r.SCHEDUL_DATE, 'yyyy-mm-dd') || ' ' || r.end_Time, 'yyyy-mm-dd hh24:mi:ss') >= TO_DATE(:3 , 'YYYYMMDDHH24MI') and r.SUBOR_HOSPITAL_DISTRICT = :4 order by r.OUT_CALL_STATUS desc, to_date(to_char(r.SCHEDUL_DATE, 'yyyy-mm-dd') || ' ' ||r.start_Time, 'yyyy-mm-dd hh24:mi:ss') asc, r.quota_Usage desc, nvl(r.REGIST_NUMBER, 0) asc   
8xwunw9vbjc5t|  update cure_apply set created_time=:1 , creator=:2 , mend_time=:3 , mender=:4 , address=:5 , admit_state=:6 , admit_time=:7 , age=:8 , anesthesia_method_code=:9 , anesthesia_method_name=:10 , apply_check_state=:11 , apply_dept_code=:12 , apply_dept_id=:13 , apply_dept_name=:14 , apply_doctor_code=:15 , apply_doctor_id=:16 , apply_doctor_name=:17 , apply_doctor_type=:18 , apply_item_count=:19 , apply_no=:20 , apply_pay_amount=:21 , apply_pay_state=:22 , apply_source=:23 , apply_time=:24 , apply_ward_id=:25 , apply_ward_name=:26 , appt_remark=:27 , appt_state=:28 , available=:29 , bed_no=:30 , branch_id=:31 , branch_name=:32 , check_state=:33 , cure_state=:34 , date_birth=:35 , dcheck_rec=:36 , dept_code=:37 , dept_id=:38 , dept_name=:39 , diag=:40 , diag_code=:41 , digital_age=:42 , discharge_time=:43 , dmed_rec=:44 , dphyexam=:45 , dtell=:46 , emr_flag=:47 , emr_phone=:48 , examination=:49 , exampurpose=:50 , executive_group=:51 , expe ct_hour=:52 , expect_time=:53 , flow_num=:54 , gender=:55 , id_number=:56 , infecthistory=:57 , inhosp_num=:58 , ip_patient_id=:59 , is_paid=:60 , item_id=:61 , item_name=:62 , item_type_code=:63 , item_type_id=:64 , item_type_name=:65 , manual_add_flag=:66 , merge=:67 , multiresisbact=:68 , op_patient_id=:69 , patient_id=:70 , patient_name=:71 , patient_num=:72 , phone=:73 , pre_admit_state=:74 , print_date=:75 , print_flag=:76 , print_times=:77 , print_user_name=:78 , priority=:79 , remark=:80 , shipping=:81 , special_flag=:82 , special_requirements=:83 , specialinfection=:84 , state=:85 , surgeon_doctor_code=:86 , surgeon_doctor_id=:87 , surgeon_doctor_name=:88 , surgeon_doctor_type=:89 , surgery_type=:90 , surgical_state=:91 , sync_remark=:92 , transportmode=:93 where apply_id=:94   
912j26wh9n2k6| SELECT * FROM ( SELECT TMP_PAGE.*, ROWNUM ROW_ID FROM ( SELECT null as PH_CONSUMPTION, null as ST_EXPORT, Z.*, H.phbStockMinQuantity as phbStockQuantity FROM vstb_stock_item Z LEFT JOIN ( select item_id, sum(round(stock_min_quantity/pkg_unit_ratio, 3)) as phbStockMinQuantity from wdp.VPHB_STOCK_ITEM where IS_AVAILABLE='Y' group by item_id ) H ON H.item_id=Z.item_id WHERE Z.STORAGE_ID = :1 and Z.MIN_STOCK > Z.STOCK_QUANTITY + ROUND(Z.STOCK_MIN_QUANTITY/z.pkg_unit_ratio, 2) order by Z.ITEM_ID ) TMP_PAGE) WHERE ROW_ID <= :2 AND ROW_ID > :3   
97a6ts33jd0ba| INSERT INTO "HISUSER"."BI_FACT_VISIT_REGISTER_TIME"( "REGIST_TIME", "REGISTER_TIME", "CALL_SIGN_TIME", "RECORD_NO", "VISIT_DEPT_CODE", "VISIT_DR_CODE", "PATIENT_NAME", "PATIENT_CODE", "FIRST_FLAG", "REGISTER_FLAG", "OVERCOLON_FLAG", "ABANDON_FLAG", "FIRST_REGISTER_TIME", "FIRST_CALL_SIGN_TIME") VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14) RETURNING ROWID INTO :15  
97d6ah8gw4f6u|  update bab_bed_allocation set accounting_status=:1 , admit_method_id=:2 , admit_method_name=:3 , admit_purpose=:4 , admit_status_id=:5 , admit_status_name=:6 , admit_status_tag=:7 , admit_type_id=:8 , admit_type_name=:9 , admit_way_id=:10 , admit_way_name=:11 , age=:12 , allocation_admit_date=:13 , allocation_admit_hour=:14 , allocation_bed_code=:15 , allocation_bed_descr=:16 , allocation_bed_id=:17 , allocation_bed_level_name=:18 , allocation_bed_name=:19 , allocation_bed_time=:20 , allocation_bed_type_name=:21 , allocation_bed_type_tag=:22 , allocation_branch_id=:23 , allocation_dept_id=:24 , allocation_dept_name=:25 , allocation_medical_group_id=:26 , allocation_medical_group_name=:27 , allocation_sickroom_id=:28 , allocation_sickroom_name=:29 , allocation_sickroom_sex_tag=:30 , allocation_type=:31 , allocation_user_id=:32 , allocation_user_name=:33 , allocation_ward_id=:34 , allocation_ward_name=:35 , antigen_type=:36 , apply_admit_dept_code=:37 , apply_admit_dept_name=:38 , apply_resource=:39 , apply_user_id=:40 , apply_user_name=:41 , bed_type_id=:42 , bed_type_name=:43 , birth_addr=:44 , birth_city=:45 , birth_city_code=:46 , birth_district=:47 , birth_district_code=:48 , birth_postcode=:49 , birth_province=:50 , birth_province_code=:51 , birth_street=:52 , birth_street_code=:53 , cancel_bed_descr=:54 , company_addr=:55 , company_phone_no=:56 , company_postcode=:57 , confirm_apply_time=:58 , confirmed_state=:59 , contact_addr=:60 , contact_city=:61 , contact_city_code=:62 , contact_credential_type_id=:63 , contact_credential_type_name=:64 , contact_district=:65 , contact_district_code=:66 , contact_fail_times=:67 , contact_id_number=:68 , contact_name=:69 , contact_phone_no=:70 , contact_postcode=:71 , contact_province=:72 , contact_province_code=:73 , contact_relation_id=:74 , contact_relation_name=:75 , contact_street=:76 , contact_street_code=:77 , create_date=:78 , create_user=: 79 , credential_type_id=:80 , credential_type_name=:81 , cross_dept_type_id=:82 , cross_dept_type_name=:83 , cross_dept_type_tag=:84 , curr_addr=:85 , curr_city=:86 , curr_city_code=:87 , curr_district=:88 , curr_district_code=:89 , curr_postcode=:90 , curr_province=:91 , curr_province_code=:92 , curr_street=:93 , curr_street_code=:94 , customer_state=:95 , data_source=:96 , date_birth=:97 , diag_code=:98 , diag_name=:99 , discharge_date=:100 , disease_history=:101 , diseases_class_id=:102 , diseases_class_name=:103 , diseases_class_tag=:104 , emergency_treatment=:105 , emr_pre_in_dept_id=:106 , emr_pre_in_dept_name=:107 , estimate_pros_pay=:108 , fever=:109 , guardian_credential_type_id=:110 , guardian_credential_type_name=:111 , guardian_id_number=:112 , guardian_name=:113 , his_admit_time=:114 , his_in_ward_time=:115 , hosp_dept_code=:116 , hosp_dept_name=:117 , household_addr=:118 , household_city=:119 , household_city_code=:120 , household _district=:121 , household_district_code=:122 , household_postcode=:123 , household_province=:124 , household_province_code=:125 , household_street=:126 , household_street_code=:127 , id_number=:128 , infectious_disease_id=:129 , infectious_disease_name=:130 , inhosp_id=:131 , inhosp_no=:132 , inhosp_times=:133 , is_accompany=:134 , is_allocationd_bed=:135 , is_appointment=:136 , is_bac_examination=:137 , is_fasting=:138 , is_icu_bed=:139 , is_need_quarantine=:140 , is_pat_cross_dept=:141 , is_retired_staff=:142 , is_window_bed=:143 , last_desc=:144 , last_state=:145 , last_state_tag=:146 , last_time=:147 , last_user_id=:148 , last_user_name=:149 , marital_status_id=:150 , marital_status_name=:151 , medical_cross_dept_descr=:152 , medicare_categ_code=:153 , medicare_categ_name=:154 , nation_id=:155 , nation_name=:156 , nationality_id=:157 , nationality_name=:158 , native_city=:159 , native_city_code=:160 , native_province=:161 , native_province_ code=:162 , nucleic_acid_date=:163 , nucleic_acid_result=:164 , occupation_id=:165 , occupation_name=:166 , other_id=:167 , outhosp_no=:168 , pat_id=:169 , pat_name=:170 , pat_phone_no=:171 , pat_source_id=:172 , pat_source_name=:173 , physi_sex_code=:174 , physi_sex_name=:175 , pre_in_bed_code=:176 , pre_in_branch_id=:177 , pre_in_dept_id=:178 , pre_in_dept_name=:179 , pre_in_medical_group_id=:180 , pre_in_medical_group_name=:181 , pre_in_ward_id=:182 , pre_in_ward_name=:183 , recept_treat_dr_code=:184 , recept_treat_dr_id=:185 , recept_treat_dr_name=:186 , reserve_admit_date=:187 , reserve_apply_date=:188 , reserve_descr=:189 , reserve_no=:190 , revise_reg_msg_num=:191 , sickroom_type_id=:192 , sickroom_type_name=:193 , sync_pre_in_dept_id=:194 , sync_pre_in_dept_name=:195 , test_results=:196 , transfer_out_bed_code=:197 , transfer_out_branch_id=:198 , transfer_out_dept_id=:199 , transfer_out_dept_name=:200 , transfer_out_ward_id=:201 , transfe r_out_ward_name=:202 , update_date=:203 , update_user=:204 , visit_card_no=:205 , wait_bed_flag=:206 where allocation_no=:207   
98vc0ayk19rbk| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003 OR "A1"."ITEM_CODE"=:V00004 OR "A1"."ITEM_CODE"=:V00005 OR "A1"."ITEM_CODE"=:V00006 OR "A1"."ITEM_CODE"=:V00007 OR "A1"."ITEM_CODE"=:V00008 OR "A1"."ITEM_CODE"=:V00009 OR "A1"."ITEM_CODE"=:V00010) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
9af3pdtxg6jvt|  INSERT INTO WOPB.DPB_OP_DISPENSE_NOTE (DISPENSE_NOTE_ID, PAT_NAME, PAT_SEX_ID, PAT_SEX_NAME, BIRTH_DATE, ID_TYPE, ID_NUMBER, PAT_AGE, MED_CARD_NO, CONTACT_ADDR, CONTACT_PHONE_NO, ALERGY_DRUG, PARENT_NAME, PAT_ID, VISIT_ID, VISIT_NO, VISIT_FLAG, REG_DATE, REGCLASS_ID, REGCLASS_NAME, SETMETH_ID, SETMETH_NAME, INVOICE_ID, INVOICE_NO, CHARGE_TIME, CHARGE_USER_ID, CHARGE_USER_NAME, PRESP_ID, PRESP_NO, PRESP_TYPE, PRESP_TIME, BRANCH_ID, OP_DEPT_ID, OP_DEPT_NAME, OP_DOCTOR_ID, OP_DOCTOR_NAME, DIAGNOSIS_CODE, DIAGNOSIS_DESC, DIAGNOSIS_DESC_CN, PAT_WEIGHT, HERBAL_REPETITION, HERBAL_DECOCT_NAME, HERBAL_DOSE_WAY_CODE, HERBAL_DOSE_WAY_NAME, HERBAL_FREQ_DAY_NUM, DISPENSE_NOTE_TYPE, SUM_TOTAL, PHARMACY_ID, PHARMACY_NAME, PRE_WIN_ID, PRE_QUEUE_NUM, ACTUAL_WIN_ID, QUEUE_TIME, LAST_STATE_ID, LAST_STATE_NAME, LAST_TIME, LAST_USER_ID, LAST_USER_NAME, LAST_DESC, IS_CHECKED_IN, CHECK_IN_TIME, IS_PRINTED, PRINT_TIME, PRINT_USER_ID, IS_DISPENSE, DISPENSE_TIME, DISPENSE_USER_ID, DISPENSE_USER_NAME, IS_DELIVER, DELIVER_TIME, DELIVER_USER_ID, DELIVER_USER_NAME, IS_BREAKOFF, IS_CANCEL, CANCEL_TYPE, CANCEL_TIME, CANCEL_USER_ID, CANCEL_USER_NAME, IS_CANCEL_CONFIRM, CANCEL_CONFIRM_NODE, CANCEL_CONFIRM_TIME, CANCEL_CONFIRM_USER_ID, CANCEL_CONFIRM_USER_NAME, IS_AVAILABLE, CREATE_USER, CREATE_DATE, UPDATE_USER, UPDATE_DATE, PRESP_INV_ORDER, PRESP_INV_COUNT, IS_PICKED, PICKED_TIME, PICKED_USER_ID, PICKED_USER_NAME, DISPENSE_PROC_TYPE, CHECK_IN_PROC_TYPE) SELECT :B13 AS DISPENSE_NOTE_ID, NVL(Y.PAT_NAME, T.PAT_NAME) AS PAT_NAME, T.PAT_SEX_ID AS PAT_SEX_ID, T.PAT_SEX_NAME AS PAT_SEX_NAME, T.BIRTH_DATE AS BIRTH_DATE, NULL AS ID_TYPE, T.ID_NUMBER AS ID_NUMBER, T.PAT_AGE AS PAT_AGE, T.MED_CARD_NO AS MED_CARD_NO, T.CONTACT_ADDR AS CONTACT_ADDR, T.CONTACT_PHONE_NO AS CONTACT_PHONE_NO, NULL AS ALERGY_DRUG, NULL AS PARENT_NAME, T.PAT_ID AS PAT_ID, T.VISIT_ID AS VISIT_ID, T.VISIT_ID AS VISIT_NO, NULL AS VISIT_FLAG, T.REG_DATE AS REG_DATE, NULL AS REGCLASS_ID, NULL AS REGCLASS_NAME, NULL AS SETMETH_ID, NULL AS SETMETH_NAME, Y.INVOICE_ID AS INVOICE_ID, Y.INVOICE_ID AS INVOICE_NO, Y.CHARGE_TIME AS CHARGE_TIME, :B12 , :B11 , Y.PRESP_ID AS PRESP_ID, Y.PRESP_ID AS PRESP_NO, Y.PRESP_TYPE AS PRESP_TYPE, Y.PRESP_TIME AS PRESP_TIME, Y.BRANCH_ID AS BRANCH_ID, Y.OP_DEPT_ID AS OP_DEPT_ID, Y.OP_DEPT_NAME AS OP_DEPT_NAME, Y.OP_DOCTOR_ID AS OP_DOCTOR_ID, Y.OP_DOCTOR_NAME AS OP_DOCTOR_NAME, Y.DIAGNOSIS_CODE AS DIAGNOSIS_CODE, Y.DIAGNOSIS_DESC AS DIAGNOSIS_DESC, Y.DIAGNOSIS_DESC_CN AS DIAGNOSIS_DESC_CN, Y.PAT_WEIGHT AS PAT_WEIGHT, Y.HERBAL_REPETITION AS HERBAL_REPETITION, Y.HERBAL_DECOCT_NAME AS HERBAL_DECOCT_NAME, Y.HERBAL_DOSE_WAY_CODE AS HERBAL_DOSE_WAY_CODE, Y.HERBAL_DOSE_WAY_NAME AS HERBAL_DOSE_WAY_NAME, Y.HERBAL_FREQ_DAY_NUM AS HERBAL_FREQ_DAY_NUM, Y.ORDER_TYPE AS DISPENSE_NOTE_TYPE, :B10 AS SUM_TOTAL, :B9 AS PHARMACY_ID, :B8 AS PHARMACY_NAME, :B6 AS PRE_WIN_I D, :B7 AS PRE_QUEUE_NUM, :B6 AS ACTUAL_WIN_ID, SYSDATE AS QUEUE_TIME, 'CHECKED_IN' AS LAST_STATE_ID, 'ѱ' AS LAST_STATE_NAME, SYSDATE AS LAST_TIME, NVL(Y.OP_DOCTOR_ID, 'null') AS LAST_USER_ID, NVL(Y.OP_DOCTOR_NAME, 'null') AS LAST_USER_NAME, NULL AS LAST_DESC, 'Y' AS IS_CHECKED_IN, SYSDATE AS CHECK_IN_TIME, 'N' AS IS_PRINTED, NULL AS PRINT_TIME, NULL AS PRINT_USER_ID, 'N' AS IS_DISPENSE, NULL AS DISPENSE_TIME, NULL AS DISPENSE_USER_ID, NULL AS DISPENSE_USER_NAME, 'N' AS IS_DELIVER, NULL AS DELIVER_TIME, NULL AS DELIVER_USER_ID, NULL AS DELIVER_USER_NAME, 'N' AS IS_BREAKOFF, 'N' AS IS_CANCEL, NULL AS CANCEL_TYPE, NULL AS CANCEL_TIME, NULL AS CANCEL_USER_ID, NULL AS CANCEL_USER_NAME, 'N' AS IS_CANCEL_CONFIRM, NULL AS CANCEL_CONFIRM_NODE, NULL AS CANCEL_CONFIRM_TIME, NULL AS CANCEL_CONFIRM_USER_ID, NULL AS CANCEL_CONFIRM_USER_NAME, 'Y' AS IS_AVAILABLE, 'admin' AS CREATE_USER, SYSDATE AS CREATE_DATE, 'admin' AS UPDATE_USER, SYSDATE AS UPDATE_DATE, :B5 AS PRESP_INV_ORDER, :B4 AS PRESP_INV_COUNT, 'N' AS IS_PICKED, NULL AS PICKED_TIME, NULL AS PICKED_USER_ID, NULL AS PICKED_USER_NAME, 'NORMAL' AS DISPENSE_PROC_TYPE, 'NORMAL' AS CHECK_IN_PROC_TYPE FROM WOP.VDPB_OP_VISIT T, WOPB.DPT_EMR_PRESP_DETAIL Y WHERE T.VISIT_ID = :B3 AND Y.PRESP_ID = :B2 AND Y.INVOICE_ID = :B1 AND ROWNUM = 1  
9m5ur86a3v85h| select interoutwa0_.FOUT_WAY_ID as FOUT_WAY_ID1_6_, interoutwa0_.FVERSION as FVERSION2_6_, interoutwa0_.FINTER_NAME as FINTER_NAME3_6_, interoutwa0_.FINTER_CODE as FINTER_CODE4_6_, interoutwa0_.FSOURCE_CODE as FSOURCE_CODE5_6_, interoutwa0_.FTARGET_CODE as FTARGET_CODE6_6_, interoutwa0_.FCODE_DESC as FCODE_DESC7_6_, interoutwa0_.FNOTE_TYPE as FNOTE_TYPE8_6_, interoutwa0_.FDEFAULT_NAME as FDEFAULT_NAME9_6_, interoutwa0_.FCONVER_VALUE as FCONVER_VALUE10_6_, interoutwa0_.FORDER_NUMBER as FORDER_NUMBER11_6_ from PS_INTER_OUT_WAY interoutwa0_ where interoutwa0_.FINTER_CODE=:1 order by interoutwa0_.FORDER_NUMBER asc  
9m82p8p2d7z84|  select OBJOID, CLSOID, RUNTIME, PRI, JOBTYPE, SCHLIM, WT, INST, RUNNOW, ENQ_SCHLIM from ( select a.obj# OBJOID, a.class_oid CLSOID, decode(bitand(a.flags, 16384), 0, a.next_run_date, a.last_enabled_time) RUNTIME, (2*a.priority + decode(bitand(a.job_status, 4), 0, 0, decode(a.running_instance, :1, -1, 1))) PRI, 1 JOBTYPE, decode(a.schedule_limit, NULL, decode(bitand(a.flags, 4194304), 4194304, p.schedule_limit, NULL), a.schedule_limit) SCHLIM, a.job_weight WT, decode(a.running_instance, NULL, 0, a.running_instance) INST, decode(bitand(a.flags, 16384), 0, 0, 1) RUNNOW, decode(bitand(a.job_status, 8388608), 0, 0, 1) ENQ_SCHLIM from sys.scheduler$_job a, sys.scheduler$_program p, v$database v, v$instance i where a.program_oid = p.obj#(+) and bitand(a.job_status, 515) = 1 and bitand(a.flags, 1048576) = 0 and ((bitand(a.flags, 134217728 + 268435456) = 0) or (bitand(a.job_status, 1024) <> 0)) and bitand(a.flags, 4096) = 0 and (a.nex t_run_date <= :2 or bitand(a.flags, 16384) <> 0) and a.instance_id is null and (a.class_oid is null or (a.class_oid is not null and a.class_oid in (select b.obj# from sys.scheduler$_class b where b.affinity is null))) and (a.database_role = v.database_role or (a.database_role is null and v.database_role = 'PRIMARY')) and ( i.logins = 'ALLOWED' or bitand(a.flags, 17179869184) <> 0 ) union all select l.obj#, l.class_oid, decode(bitand(l.flags, 16384), 0, l.next_run_date, l.last_enabled_time), (2*decode(bitand(l.flags, 8589934592), 0, q.priority, pj.priority) + decode(bitand(l.job_status, 4), 0, 0, decode(l.running_instance, :3, -1, 1))), 1, decode(bitand(l.flags, 8589934592), 0, q.schedule_limit, decode(pj.schedule_limit, NULL, q.schedule_limit, pj.schedule_limit)), decode(bitand(l.flags, 8589934592), 0, q.job_weight, pj.job_weight), decode(l.running_instance, NULL, 0, l.running_instance), decode(bitand(l.flags, 16384), 0, 0, 1), decode(bitand(l.job_status, 8388608), 0, 0, 1) from sys.scheduler$_lightweight_job l, sys.scheduler$_program q, (select sl.obj# obj#, decode(bitand(sl.flags, 8589934592), 0, sl.program_oid, spj.program_oid) program_oid, decode(bitand(sl.flags, 8589934592), 0, NULL, spj.priority) priority, decode(bitand(sl.flags, 8589934592), 0, NULL, spj.job_weight) job_weight, decode(bitand(sl.flags, 8589934592), 0, NULL, spj.schedule_limit) schedule_limit from sys.scheduler$_lightweight_job sl, scheduler$_job spj where sl.program_oid = spj.obj#(+)) pj , v$instance i where pj.obj# = l.obj# and pj.program_oid = q.obj#(+) and (:4 = 0 or l.running_instance = :5) and bitand(l.job_status, 515) = 1 and ((bitand(l.flags, 134217728 + 268435456) = 0) or (bitand(l.job_status, 1024) <> 0)) and bitand(l.flags, 4096) = 0 and (l.next_run_date <= :6 or bitand(l.flags, 16384) <> 0) and l.instance_id is null and (l.class_oid is null or (l.class_oid is not null and l.cla ss_oid in (select w.obj# from sys.scheduler$_class w where w.affinity is null))) and ( i.logins = 'ALLOWED' or bitand(l.flags, 17179869184) <> 0 ) union all select c.obj#, 0, c.next_start_date, 0, 2, c.duration, 1, 0, 0, 0 from sys.scheduler$_window c , v$instance i where bitand(c.flags, 1) <> 0 and bitand(c.flags, 2) = 0 and bitand(c.flags, 64) = 0 and c.next_start_date <= :7 and i.logins = 'ALLOWED' union all select d.obj#, 0, d.next_start_date + d.duration, 0, 4, numtodsinterval(0, 'minute'), 1, 0, 0, 0 from sys.scheduler$_window d , v$instance i where bitand(d.flags, 1) <> 0 and bitand(d.flags, 2) = 0 and bitand(d.flags, 64) = 0 and d.next_start_date <= :8 and i.logins = 'ALLOWED' union all select f.obj#, 0, e.attr_tstamp, 0, decode(bitand(e.flags, 131072), 0, 2, 3), e.attr_intv, 1, 0, 0, 0 from sys.scheduler$_global_attribute e, sys.obj$ f, sys.obj$ g, v$instance i where e.obj# = g.obj# and g.owner# = 0 and f.owner # = 0 and g.name = 'CURRENT_OPEN_WINDOW' and e.value = f.name and f.type# = 69 and e.attr_tstamp is not null and e.attr_intv is not null and i.logins = 'ALLOWED' union all select i.obj#, 0, h.attr_tstamp + h.attr_intv, 0, decode(bitand(h.flags, 131072), 0, 4, 5), numtodsinterval(0, 'minute'), 1, 0, 0, 0 from sys.scheduler$_global_attribute h, sys.obj$ i, sys.obj$ j, v$instance ik where h.obj# = j.obj# and j.owner# = 0 and i.owner# = 0 and j.name = 'CURRENT_OPEN_WINDOW' and h.value = i.name and i.type# = 69 and h.attr_tstamp is not null and h.attr_intv is not null and ik.logins = 'ALLOWED') order by RUNTIME, JOBTYPE, CLSOID, PRI, WT DESC, OBJOID  
9qc6r0wu94sqg| select externalsy0_.ID as ID17_0_, externalsy0_.MSG_ID as MSG2_17_0_, externalsy0_.FUNC_ID as FUNC3_17_0_, externalsy0_.FUNC_NAME as FUNC4_17_0_, externalsy0_.METHOD_TYPE as METHOD5_17_0_, externalsy0_.REQUESTXML as REQUESTXML17_0_, externalsy0_.RESPONSEXML as RESPONSE7_17_0_, externalsy0_.START_TIME as START8_17_0_, externalsy0_.END_TIME as END9_17_0_, externalsy0_.SEND_STATUS as SEND10_17_0_, externalsy0_.CONSUMER as CONSUMER17_0_, externalsy0_.PROVIDER as PROVIDER17_0_, externalsy0_.CREATE_DATETIME as CREATE13_17_0_, externalsy0_.LAST_UDP_TIME as LAST14_17_0_ from T_SM_EXTERNAL_SYS_LOGGER externalsy0_ where externalsy0_.ID=:1   
9yzygm67qqk86| BEGIN PG_HIS_SQ.realeaseNumberSource001(:1 , :2 ) ; END;  
a0kfc05k3nz99|  select doctavaila0_.fda_id as fda_id1_20_, doctavaila0_.add_num as add_num2_20_, doctavaila0_.add_num_ocp as add_num_ocp3_20_, doctavaila0_.appt_num as appt_num4_20_, doctavaila0_.appt_num_ocp as appt_num_ocp5_20_, doctavaila0_.fassist_schedule as fassist_schedule6_20_, doctavaila0_.fbooking_open as fbooking_open7_20_, doctavaila0_.fbranch_id as fbranch_id8_20_, doctavaila0_.fdate as fdate9_20_, doctavaila0_.fday_of_week as fday_of_week10_20_, doctavaila0_.fday_of_week_num as fday_of_week_num11_20_, doctavaila0_.fdept_code as fdept_code12_20_, doctavaila0_.fdept_id as fdept_id13_20_, doctavaila0_.fdept_name as fdept_name14_20_, doctavaila0_.fdept_order_num as fdept_order_num15_20_, doctavaila0_.fdr_code as fdr_code16_20_, doctavaila0_.fdr_gender as fdr_gender17_20_, doctavaila0_.fgood_at as fgood_at18_20_, doctavaila0_.fgood_at_desc as fgood_at_desc19_20_, doctavaila0_.fdr_id as fdr_id20_20_, doctavaila0_.fdr_name as fdr_name21_20_, doctavaila0_.fdr_order_num as fd r_order_num22_20_, doctavaila0_.fdr_phone as fdr_phone23_20_, doctavaila0_.fdr_photo as fdr_photo24_20_, doctavaila0_.fend_time as fend_time25_20_, doctavaila0_.fhis_dept_code as fhis_dept_code26_20_, doctavaila0_.fhis_dept_id as fhis_dept_id27_20_, doctavaila0_.fhis_dept_name as fhis_dept_name28_20_, doctavaila0_.fifshare as fifshare29_20_, doctavaila0_.fis_temporary as fis_temporary30_20_, doctavaila0_.flogluby as flogluby31_20_, doctavaila0_.flogludate as flogludate32_20_, doctavaila0_.fold_dept_name as fold_dept_name33_20_, doctavaila0_.fold_doct_name as fold_doct_name34_20_, doctavaila0_.fold_his_dept_code as fold_his_dept_cod35_20_, doctavaila0_.fold_his_dept_id as fold_his_dept_id36_20_, doctavaila0_.fold_his_dept_name as fold_his_dept_nam37_20_, doctavaila0_.online_type as online_type38_20_, doctavaila0_.freg_fee as freg_fee39_20_, doctavaila0_.freg_type_id as freg_type_id40_20_, doctavaila0_.freg_type_name as freg_type_name41_20_, doctavaila0_.fremark as fr emark42_20_, doctavaila0_.freplace_flag as freplace_flag43_20_, doctavaila0_.room_name as room_name44_20_, doctavaila0_.schd_remark as schd_remark45_20_, doctavaila0_.fschd_type as fschd_type46_20_, doctavaila0_.shft_num as shft_num47_20_, doctavaila0_.shft_num_ocp as shft_num_ocp48_20_, doctavaila0_.fsb_id as fsb_id49_20_, doctavaila0_.fshift_id as fshift_id50_20_, doctavaila0_.fshift_name as fshift_name51_20_, doctavaila0_.fshft_order_num as fshft_order_num52_20_, doctavaila0_.fsm_sent as fsm_sent53_20_, doctavaila0_.fspec_dept_code as fspec_dept_code54_20_, doctavaila0_.fspec_dept_id as fspec_dept_id55_20_, doctavaila0_.fspec_dept_name as fspec_dept_name56_20_, doctavaila0_.fstaff_id as fstaff_id57_20_, doctavaila0_.fstart_time as fstart_time58_20_, doctavaila0_.fstate as fstate59_20_, doctavaila0_.ftitle_name as ftitle_name60_20_, doctavaila0_.ftreat_fee as ftreat_fee61_20_, doctavaila0_.vip_num as vip_num62_20_, doctavaila0_.vip_num_ocp as vip_num_ocp63_20_ fr om doct_available doctavaila0_ where doctavaila0_.fda_id=:1  
a8kmz6qtudcmn|  /* MV_REFRESH (INS) */ INSERT /*+ NOAPPEND */ INTO "HISUSER"."MV_SM_3CATALOG_ORG" SELECT /*+ NO_MERGE("JV$") */ "MAS$2".ROWID, "JV$"."RID$", "MAS$0".ROWID, "MAS$2"."ID", "MAS$2"."ITEM_CODE", "MAS$2"."ITEM_NAME", "MAS$2"."COMMON_NAME", "MAS$2"."COMMON_PINYIN_CODE", "MAS$2"."COMMON_WUBI_CODE", "MAS$2"."COMMON_SPELLING_CODE", ' ', ' ', "MAS$2"."DOSAGE_UNITS", "MAS$2"."SPECIFICATION", "MAS$2"."UNITS_ID", "MAS$2"."PINYIN_CODE", "MAS$2"."WUBI_CODE", "MAS$2"."SPELLING_CODE", "MAS$2"."MEMORY_CODE", "MAS$2"."FINANCIAL_CLASSIFICATION", "MAS$2"."OP_INVOICE_CODE", "MAS$2"."IP_INVOICE_CODE", "JV$"."PRICE_TYPE", "JV$"."PRICE", '030302', (-1), (-1), "MAS$2"."UNITS_ID", 1, "MAS$2"."UNITS_ID", 1, CAST(5211 AS number(16)), "MAS$2"."SPECIFICATION", 'N', 'N', "MAS$2"."UNITS_ID", 1, ' ', ' ', ' ', ' ', ' ', DECODE("MAS$2"."DISABLE_FLAG", 'N', 'Y', 'N'), DECODE("MAS$2"."DISABLE_FLAG", 'N', 'Y', 'N'), 'N', 'N', "MAS$2"."IS_INDEPENDENT", "MAS$2"."ISGB" FROM ( SELECT "MAS$"."ROWID" "RID$" , "MAS$".* FROM "HISUSER"."T_SM_MEDICALSERVICESPRICE" "MAS$" WHERE ROWID IN (SELECT /*+ HASH_SJ */ CHARTOROWID("MAS$"."M_ROW$$") RID$ FROM "HISUSER"."MLOG$_T_SM_MEDICALSERVICES2" "MAS$" WHERE "MAS$".SNAPTIME$$ > :B_ST1 )) "JV$", "T_SM_ORGANIZATION" AS OF SNAPSHOT(:B_SCN) "MAS$0", "T_SM_MEDICALSERVICES" "MAS$2" WHERE "MAS$2"."ID"="JV$"."ITEM_ID" AND "MAS$0"."ID"="JV$"."ORG_ID"  
acvzqsugt0vma| BEGIN PG_DPB_DISPENSE_BATCH.hp_get_dispense_detail( :1 , :2 , :3 , :4 , :5 , :6 , :7 , :8 ) ; END;  
awa8nszb02q6p| SELECT column_name as Field , data_type as Type FROM all_tab_cols WHERE lower(table_name) = 'lb_patient'  
az33m61ym46y4| SELECT NULL AS table_cat, o.owner AS table_schem, o.object_name AS table_name, o.object_type AS table_type, NULL AS remarks FROM all_objects o WHERE o.owner LIKE :1 ESCAPE '/' AND o.object_name LIKE :2 ESCAPE '/' AND o.object_type IN ('xxx', 'TABLE') ORDER BY table_type, table_schem, table_name   
b4nc4nnx3fhf5| SELECT DISTINCT "A1"."ITEM_CODE", "A1"."STOCK_MIN_QUANTITY", "A1"."LOWEST_STOCK", "A1"."DRUG_SPEC" FROM "WDP"."VEMR_DEPT_PHARMACY" "A2", "WDP"."VEMR_STOCK_ITEM" "A1" WHERE "A2"."DEPT_ID"=:V00001 AND ("A1"."ITEM_CODE"=:V00002 OR "A1"."ITEM_CODE"=:V00003 OR "A1"."ITEM_CODE"=:V00004 OR "A1"."ITEM_CODE"=:V00005 OR "A1"."ITEM_CODE"=:V00006 OR "A1"."ITEM_CODE"=:V00007 OR "A1"."ITEM_CODE"=:V00008) AND "A2"."PHARMACY_ID"="A1"."PHARMACY_ID"  
bb19k370m2b2t| SELECT X.PHARMACY_WIN_ID FROM (SELECT T.* FROM WOP.VDPB_QUEUE_COUNT T WHERE T.PHARMACY_ID = :B2 AND T.PHARMACY_WIN_CLASS = :B1 ORDER BY T.COUNT_VISIT, T.PXH ASC) X WHERE ROWNUM = 1  
bfnzd8q7d2z0m| update t_sm_client_socket set last_active_time=sysdate where client_ip=:1 and clinet_port=:2   
bgnt3bpd2b04f| select CURRENT_TIMESTAMP as col_0_0_ from dual dual0_  
c5uhk705rt3v1| select clientsock0_.ID as ID224_, clientsock0_.CLIENT_ID as CLIENT2_224_, clientsock0_.USER_ID as USER3_224_, clientsock0_.ORG_ID as ORG4_224_, clientsock0_.CLIENT_IP as CLIENT5_224_, clientsock0_.CLINET_PORT as CLINET6_224_, clientsock0_.ACTIVE_MODEL as ACTIVE7_224_, clientsock0_.CURRENT_MODELS as CURRENT8_224_, clientsock0_.USER_KEYS as USER9_224_, clientsock0_.active_Flag as active10_224_ from T_SM_CLIENT_SOCKET clientsock0_ where nvl(clientsock0_.active_Flag, 'Y')='Y' and clientsock0_.ORG_ID=:1 and (clientsock0_.USER_KEYS like :2 ) and (clientsock0_.CURRENT_MODELS like :3 )  
caz5v85xqv2nr| BEGIN PG_HIS_ELECTRONICBILLS.pf_main_check(:1 , :2 , :3 ) ; END;  
cdxqhvdmm89mb| SELECT "ELECTRONIC_CARD_NO", "CARD_NO", "PAT_INDEX_NO" FROM "ESB_PA_ELECTRONICCARD" "T"  
cm5vu20fhtnq1| select /*+ connect_by_filtering */ privilege#, level from sysauth$ connect by grantee#=prior privilege# and privilege#>0 start with grantee#=:1 and privilege#>0  
cwvq44dwhaw9j| SELECT * FROM TABLE(PG_JSONUTIL.FUNC_SPLIT(:B1 , ':'))  
d3uu56jx39a2j| select * from urm.esb_pm_dr_regist_infors where 1=1 and SUBOR_HOSPITAL_DISTRICT = :1 and SCHEDUL_DATE >= to_date(:2 , 'yyyy/mm/dd') and SCHEDUL_DATE <= to_date(:3 , 'yyyy/mm/dd') and SUPERIOR_DEPT_CODE = :4 and OUT_CALL_STATUS = 0  
d45qmb31zqpch| DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN pg_syn_emr_presp.pp_job_batch; :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END;   
d642fkkxqhs98| select ID from T_SM_EXTERNAL_SYS_LOGGER where ID =:1   
dh5nf6qw9sycm| BEGIN PG_DPB_DISPENSE_BATCH.hp_get_ward_list( :1 , :2 , :3 , :4 , :5 , :6 ) ; END;  
dr97hbjraumrm| SELECT 1 FROM V$LOGFILE WHERE(STATUS NOT IN ('STALE', 'INVALID') OR STATUS IS NULL) AND MEMBER <> :log_name AND EXISTS ( SELECT 1 FROM V$LOG WHERE GROUP# = V$LOGFILE.GROUP# AND THREAD# = :ora_thread AND SEQUENCE# = :ora_seq_no ) AND ROWNUM = 1  
dv474vaz39154|  select patName, visitId, deptId, deptCode, deptName, source_id, docCode, docName, sum(payAmount), settleMethodId, settleMethodName, org_id, ISREGISTMI_FLAG, account_id, sum(accountDebted) from ( select v.name patName, v.visit_id visitId, v.dept_id deptId, (select d.dept_code from t_sm_department d where d.id = v.dept_id) deptCode, (select d.dept_name from t_sm_department d where d.id = v.dept_id) deptName, v.source_id, (select u.user_code from t_sm_userbaseinfo u where u.id = v.attending_doctor_id) docCode, (select u.user_name from t_sm_userbaseinfo u where u.id = v.attending_doctor_id) docName, sum(ob.ACTUAL_AMOUNT * 100) payAmount, a.mi_code settleMethodId, (select t.item_value from t_sm_paraitem t where t.id = a.mi_code) settleMethodName, v.org_id, v.ISREGISTMI_FLAG, a.account_id, sum(ob.ACCOUNT_DEBTED * 100) accountDebted from T_ODW_ORDERBILLING ob, t_odw_ordergroup og, t_or_account a, t_or_visit v where ob.order_group_id = og.id and a.account_id = ob.account_id and v.visit_i d = a.visit_id and ob.active_flag = 'Y' and ob.account_flag = 'N' and og.active_flag = 'Y' and og.account_flag = 'N' and og.original_order_group_id is null and og.order_group_source<>-308754 and v.visit_id = :1 and v.card_id=:2 group by v.name, v.visit_id, v.dept_id, v.attending_doctor_id, v.source_id, a.mi_code, v.org_id, v.ISREGISTMI_FLAG, a.account_id union all select v.name patName, v.visit_id visitId, v.dept_id deptId, (select d.dept_code from t_sm_department d where d.id = v.dept_id) deptCode, (select d.dept_name from t_sm_department d where d.id = v.dept_id) deptName, v.source_id, (select u.user_code from t_sm_userbaseinfo u where u.id = v.attending_doctor_id) docCode, (select u.user_name from t_sm_userbaseinfo u where u.id = v.attending_doctor_id) docName, sum(ob.ACTUAL_AMOUNT * 100) payAmount, a.mi_code settleMethodId, (select t.item_value from t_sm_paraitem t where t.id = a.mi_code) settleMethodName, v.org_id, v.ISREGISTMI_FLAG, a.account_id, sum(ob.ACCOUNT_DEBTED * 100) accountDebted from T_ODW_ORDERBILLING ob, t_or_account a, t_or_visit v where ob.order_group_id is null and ob.active_flag = 'Y' and ob.account_flag = 'N' and a.account_id = ob.account_id and v.visit_id = a.visit_id and ob.financial_classification <> 241962 and v.visit_id = :3 and v.card_id=:4 group by v.name, v.visit_id, v.dept_id, v.attending_doctor_id, v.source_id, a.mi_code, v.org_id, v.ISREGISTMI_FLAG, a.account_id ) group by patName, visitId, deptId, deptCode, deptName, source_id, docCode, docName, settleMethodId, settleMethodName, org_id, ISREGISTMI_FLAG, account_id order by account_id asc  
dvd0axaxt81h9| DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN PG_WDP_STOCK.pp_job_normal; :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END;   
dvhc0bwbs7q52| SELECT COUNT(1) FROM T_OB_SETTLEACCOUNT A WHERE A.INVOICE_ID = :B1 AND A.OTH_PAY > 1  
dw9qd5d0pn687| SELECT X.SUBOR_WARD_ID, X.SUBOR_SICKROOM_ID, X.BED_CODE, NVL(Y.PAT_NAME, Z.PAT_NAME) PAT_NAME, NVL(Y.PHYSI_SEX_NAME, Z.SEX_NAME) SEX_NAME FROM BAV_BED_ALL X, BAB_BED_RESERVE Y, BAI_EMR_BED_LIST Z WHERE X.BED_ID = Y.BED_ID(+) AND X.SUBOR_WARD_ID = Z.SUBOR_WARD_ID(+) AND X.BED_CODE = Z.BED_CODE(+) AND NVL(Y.PHYSI_SEX_NAME, Z.SEX_NAME) IS NOT NULL ORDER BY X.SUBOR_WARD_ID, X.SUBOR_SICKROOM_ID  
dz7vaztm8008c| BEGIN PG_HIS_SQ.occupyNumberSource001(:1 , :2 ) ; END;  
f0czvj8ah7dtt| SELECT * FROM ( SELECT TMP_PAGE.*, ROWNUM ROW_ID FROM ( SELECT v.*, round((v.STOCK_QUANTITY + v.STOCK_MIN_QUANTITY/v.PKG_UNIT_RATIO)*v.BUY_PRICE, 2) as STOCK_BUY_AMOUNT , s.SUPPLIER_ID as lastSupplierId, s.SUPPLIER_NAME as lastSupplierName FROM VSTB_STOCK_ITEM v, STC_IMPORT_DEFAULT s WHERE v.ITEM_ID=s.ITEM_ID(+) AND v.STORAGE_ID=:1 ORDER BY v.ITEM_ID ASC ) TMP_PAGE) WHERE ROW_ID <= :2 AND ROW_ID > :3   
f1jpfkf5c955q|  select idworderbi0_.id as id273_, idworderbi0_.account_debted as account2_273_, idworderbi0_.account_debted_amount as account3_273_, idworderbi0_.account_debted_amount2 as account4_273_, idworderbi0_.account_debted_flag as account5_273_, idworderbi0_.account_flag as account6_273_, idworderbi0_.account_id as account7_273_, idworderbi0_.account_type as account8_273_, idworderbi0_.active_flag as active9_273_, idworderbi0_.actual_amount as actual10_273_, idworderbi0_.actual_dispense_amount as actual11_273_, idworderbi0_.actual_item_id as actual12_273_, idworderbi0_.adi_id as adi13_273_, idworderbi0_.adi_ver_no as adi14_273_, idworderbi0_.amount as amount273_, idworderbi0_.attached_charge_flag as attached16_273_, idworderbi0_.barcode as barcode273_, idworderbi0_.base_type as base18_273_, idworderbi0_.bed_no as bed19_273_, idworderbi0_.billing_classify as billing20_273_, idworderbi0_.billing_type as billing21_273_, idworderbi0_.bir_id as bir22_273_, idworderbi0_.cancel_ chargeable_datetime as cancel23_273_, idworderbi0_.cancel_confirmor_id as cancel24_273_, idworderbi0_.charge_datetime as charge25_273_, idworderbi0_.chargeable_datetime as chargeable26_273_, idworderbi0_.chargeable_indicator as chargeable27_273_, idworderbi0_.chargeable_status as chargeable28_273_, idworderbi0_.chrgitm_lv as chrgitm29_273_, idworderbi0_.confirmor_id as confirmor30_273_, idworderbi0_.conjunction as conjunc31_273_, idworderbi0_.conjunction_seq_no as conjunc32_273_, idworderbi0_.create_datetime as create33_273_, idworderbi0_.creator_id as creator34_273_, idworderbi0_.creator_user_code as creator35_273_, idworderbi0_.creator_ver_id as creator36_273_, idworderbi0_.dept_id as dept37_273_, idworderbi0_.det_item_fee_sumamt as det38_273_, idworderbi0_.discount_scale as discount39_273_, idworderbi0_.dispense_amount_everytimes as dispense40_273_, idworderbi0_.dispense_units as dispense41_273_, idworderbi0_.dispensed_amount as dispensed42_273_, idworderbi0_.dis pensed_indicator as dispensed43_273_, idworderbi0_.dm_drugstore_id as dm44_273_, idworderbi0_.dosage as dosage273_, idworderbi0_.drip_rate as drip46_273_, idworderbi0_.drug_store_id as drug47_273_, idworderbi0_.executable as executable273_, idworderbi0_.executable_datetime as executable49_273_, idworderbi0_.executable_group as executable50_273_, idworderbi0_.executable_user_code as executable51_273_, idworderbi0_.executable_user_id as executable52_273_, idworderbi0_.executable_user_name as executable53_273_, idworderbi0_.executable_user_ver_id as executable54_273_, idworderbi0_.executive_datetime as executive55_273_, idworderbi0_.executive_times as executive56_273_, idworderbi0_.external_billing_xh as external57_273_, idworderbi0_.financial_classification as financial58_273_, idworderbi0_.fulamt_ownpay_amt as fulamt59_273_, idworderbi0_.inactive_datetime as inactive60_273_, idworderbi0_.inactive_user_id as inactive61_273_, idworderbi0_.individual_payment as individua l62_273_, idworderbi0_.inscp_scp_amt as inscp63_273_, idworderbi0_.interval as interval273_, idworderbi0_.invoice_code as invoice65_273_, idworderbi0_.ip_account_debted_amount as ip66_273_, idworderbi0_.ip_dept_id as ip67_273_, idworderbi0_.ip_own_pay_first as ip68_273_, idworderbi0_.is_immediately_dispense as is69_273_, idworderbi0_.isaccumulation as isaccum70_273_, idworderbi0_.isdispensing as isdispe71_273_, idworderbi0_.isfirst as isfirst273_, idworderbi0_.item_code as item73_273_, idworderbi0_.item_group_code as item74_273_, idworderbi0_.item_id as item75_273_, idworderbi0_.item_name as item76_273_, idworderbi0_.item_type as item77_273_, idworderbi0_.label_dosage as label78_273_, idworderbi0_.limiting_drug as limiting79_273_, idworderbi0_.med_chrgitm_type as med80_273_, idworderbi0_.medical_group_id as medical81_273_, idworderbi0_.memory_code as memory82_273_, idworderbi0_.order_dosage as order83_273_, idworderbi0_.order_generated_no as order84_273_, idworde rbi0_.order_id as order85_273_, idworderbi0_.order_name as order86_273_, idworderbi0_.order_times as order87_273_, idworderbi0_.org_id as org88_273_, idworderbi0_.origin_external_billing_xh as origin89_273_, idworderbi0_.orignal_actual_amount as orignal90_273_, idworderbi0_.overlmt_amt as overlmt91_273_, idworderbi0_.pay_scale as pay92_273_, idworderbi0_.pay_scale2 as pay93_273_, idworderbi0_.payment_account_id as payment94_273_, idworderbi0_.payment_inactive_flag as payment95_273_, idworderbi0_.performing_dept_id as performing96_273_, idworderbi0_.performing_ward_id as performing97_273_, idworderbi0_.placer_code as placer98_273_, idworderbi0_.placer_dept_id as placer99_273_, idworderbi0_.placer_id as placer100_273_, idworderbi0_.placer_name as placer101_273_, idworderbi0_.preselfpay_amt as preselfpay102_273_, idworderbi0_.pric as pric273_, idworderbi0_.pric_uplmt_amt as pric104_273_, idworderbi0_.purchase_price as purchase105_273_, idworderbi0_.px_id as px106_273_ , idworderbi0_.refund_flag as refund107_273_, idworderbi0_.refund_id as refund108_273_, idworderbi0_.remark as remark273_, idworderbi0_.route_name as route110_273_, idworderbi0_.selfpay_prop as selfpay111_273_, idworderbi0_.settleaccount_id as settle112_273_, idworderbi0_.sick_or_wounded as sick113_273_, idworderbi0_.special_drug_debted as special114_273_, idworderbi0_.specification as specif115_273_, idworderbi0_.statistics_mii_item_code as statistics116_273_, idworderbi0_.tc_id as tc117_273_, idworderbi0_.tc_name as tc118_273_, idworderbi0_.times as times273_, idworderbi0_.trans_flag as trans120_273_, idworderbi0_.unit_price as unit121_273_, idworderbi0_.usage as usage273_, idworderbi0_.used_account_debted as used123_273_, idworderbi0_.used_account_debted_amount as used124_273_, idworderbi0_.used_actual_amount as used125_273_, idworderbi0_.used_individual_payment as used126_273_, idworderbi0_.ward as ward273_ from t_idw_orderbilling idworderbi0_ where idworderbi0 _.id in (:1 , :2 , :3 , :4 , :5 , :6 , :7 , :8 , :9 , :10 , :11 , :12 , :13 , :14 , :15 , :16 , :17 , :18 , :19 , :20 , :21 , :22 , :23 , :24 , :25 , :26 , :27 , :28 , :29 , :30 , :31 , :32 , :33 , :34 , :35 , :36 , :37 , :38 , :39 , :40 , :41 , :42 , :43 , :44 , :45 , :46 , :47 , :48 , :49 , :50 , :51 , :52 , :53 , :54 , :55 , :56 , :57 , :58 , :59 , :60 , :61 , :62 , :63 , :64 , :65 , :66 , :67 , :68 , :69 , :70 , :71 , :72 , :73 , :74 , :75 , :76 , :77 , :78 , :79 , :80 , :81 , :82 , :83 , :84 , :85 , :86 , :87 , :88 , :89 , :90 , :91 , :92 , :93 , :94 , :95 , :96 , :97 , :98 , :99 , :100 , :101 , :102 , :103 , :104 , :105 , :106 , :107 , :108 , :109 , :110 , :111 , :112 , :113 , :114 , :115 , :116 , :117 , :118 , :119 , :120 , :121 , :122 , :123 , :124 , :125 , :126 , :127 , :128 , :129 , :130 , :131 , :132 , :133 , :134 , :135 , :136 , :137 , :13 8 , :139 , :140 , :141 , :142 , :143 , :144 , :145 , :146 , :147 , :148 , :149 , :150 , :151 , :152 , :153 , :154 , :155 , :156 , :157 , :158 , :159 , :160 , :161 , :162 , :163 , :164 , :165 , :166 , :167 , :168 , :169 , :170 , :171 , :172 , :173 , :174 , :175 , :176 , :177 , :178 , :179 , :180 , :181 , :182 , :183 , :184 , :185 , :186 , :187 , :188 , :189 , :190 , :191 , :192 , :193 , :194 , :195 , :196 , :197 , :198 , :199 , :200 , :201 , :202 , :203 , :204 , :205 , :206 , :207 , :208 , :209 , :210 , :211 , :212 , :213 , :214 , :215 , :216 , :217 , :218 , :219 , :220 , :221 , :222 , :223 , :224 , :225 , :226 , :227 , :228 , :229 , :230 , :231 , :232 , :233 , :234 , :235 , :236 , :237 , :238 , :239 , :240 , :241 , :242 , :243 , :244 , :245 , :246 , :247 , :248 , :249 , :250 , :251 , :252 , :253 , :254 , :255 , :256 , :257 , :258 , :259 , :260 , :261 , :262 , :26 3 , :264 , :265 , :266 , :267 , :268 , :269 , :270 , :271 , :272 , :273 , :274 , :275 , :276 , :277 , :278 , :279 , :280 , :281 , :282 , :283 , :284 , :285 , :286 , :287 , :288 , :289 , :290 , :291 , :292 , :293 , :294 , :295 , :296 , :297 , :298 , :299 , :300 , :301 , :302 , :303 , :304 , :305 , :306 , :307 , :308 , :309 , :310 , :311 , :312 , :313 , :314 , :315 , :316 , :317 , :318 , :319 , :320 , :321 , :322 , :323 , :324 , :325 , :326 , :327 , :328 , :329 , :330 , :331 , :332 , :333 , :334 , :335 , :336 , :337 , :338 , :339 , :340 , :341 , :342 , :343 , :344 , :345 , :346 , :347 , :348 , :349 , :350 , :351 , :352 , :353 , :354 , :355 , :356 , :357 , :358 , :359 , :360 , :361 , :362 , :363 , :364 , :365 , :366 , :367 , :368 , :369 , :370 , :371 , :372 , :373 , :374 , :375 , :376 , :377 , :378 , :379 , :380 , :381 , :382 , :383 , :384 , :385 , :386 , :387 , :38 8 , :389 , :390 , :391 , :392 , :393 , :394 , :395 , :396 , :397 , :398 , :399 , :400 , :401 , :402 , :403 , :404 , :405 , :406 , :407 , :408 , :409 , :410 , :411 , :412 , :413 , :414 , :415 , :416 , :417 , :418 , :419 , :420 , :421 , :422 , :423 , :424 , :425 , :426 , :427 , :428 , :429 , :430 , :431 , :432 , :433 , :434 , :435 , :436 , :437 , :438 , :439 , :440 , :441 , :442 , :443 , :444 , :445 , :446 , :447 , :448 , :449 , :450 , :451 , :452 , :453 , :454 , :455 , :456 , :457 , :458 , :459 , :460 , :461 , :462 , :463 , :464 , :465 , :466 , :467 , :468 , :469 , :470 , :471 , :472 , :473 , :474 , :475 , :476 , :477 , :478 , :479 , :480 , :481 , :482 , :483 , :484 , :485 , :486 , :487 , :488 , :489 , :490 , :491 , :492 , :493 , :494 , :495 , :496 , :497 , :498 , :499 , :500 , :501 , :502 , :503 , :504 , :505 , :506 , :507 , :508 , :509 , :510 , :511 , :512 , :51 3 , :514 , :515 , :516 , :517 , :518 , :519 , :520 , :521 , :522 , :523 , :524 , :525 , :526 , :527 , :528 , :529 , :530 , :531 , :532 , :533 , :534 , :535 , :536 , :537 , :538 , :539 , :540 , :541 , :542 , :543 , :544 , :545 , :546 , :547 , :548 , :549 , :550 , :551 , :552 , :553 , :554 , :555 , :556 , :557 , :558 , :559 , :560 , :561 , :562 , :563 , :564 , :565 , :566 , :567 , :568 , :569 , :570 , :571 , :572 , :573 , :574 , :575 , :576 , :577 , :578 , :579 , :580 , :581 , :582 , :583 , :584 , :585 , :586 , :587 , :588 , :589 , :590 , :591 , :592 , :593 , :594 , :595 , :596 , :597 , :598 , :599 , :600 , :601 , :602 , :603 , :604 , :605 , :606 , :607 , :608 , :609 , :610 , :611 , :612 , :613 , :614 , :615 , :616 , :617 , :618 , :619 , :620 , :621 , :622 , :623 , :624 , :625 , :626 , :627 , :628 , :629 , :630 , :631 , :632 , :633 , :634 , :635 , :636 , :637 , :63 8 , :639 , :640 , :641 , :642 , :643 , :644 , :645 , :646 , :647 , :648 , :649 , :650 , :651 , :652 , :653 , :654 , :655 , :656 , :657 , :658 , :659 , :660 , :661 , :662 , :663 , :664 , :665 , :666 , :667 , :668 , :669 , :670 , :671 , :672 , :673 , :674 , :675 , :676 , :677 , :678 , :679 , :680 , :681 , :682 , :683 , :684 , :685 , :686 , :687 , :688 , :689 , :690 , :691 , :692 , :693 , :694 , :695 , :696 , :697 , :698 , :699 , :700 , :701 , :702 , :703 , :704 , :705 , :706 , :707 , :708 , :709 , :710 , :711 , :712 , :713 , :714 , :715 , :716 , :717 , :718 , :719 , :720 , :721 , :722 , :723 , :724 , :725 , :726 , :727 , :728 , :729 , :730 , :731 , :732 , :733 , :734 , :735 , :736 , :737 , :738 , :739 , :740 , :741 , :742 , :743 , :744 , :745 , :746 , :747 , :748 , :749 , :750 , :751 , :752 , :753 , :754 , :755 , :756 , :757 , :758 , :759 , :760 , :761 , :762 , :76 3 , :764 , :765 , :766 , :767 , :768 , :769 , :770 , :771 , :772 , :773 , :774 , :775 , :776 , :777 , :778 , :779 , :780 , :781 , :782 , :783 , :784 , :785 , :786 , :787 , :788 , :789 , :790 , :791 , :792 , :793 , :794 , :795 , :796 , :797 , :798 , :799 , :800 , :801 , :802 , :803 , :804 , :805 , :806 , :807 , :808 , :809 , :810 , :811 , :812 , :813 , :814 , :815 , :816 , :817 , :818 , :819 , :820 , :821 , :822 , :823 , :824 , :825 , :826 , :827 , :828 , :829 , :830 , :831 , :832 , :833 , :834 , :835 , :836 , :837 , :838 , :839 , :840 , :841 , :842 , :843 , :844 , :845 , :846 , :847 , :848 , :849 , :850 , :851 , :852 , :853 , :854 , :855 , :856 , :857 , :858 , :859 , :860 , :861 , :862 , :863 , :864 , :865 , :866 , :867 , :868 , :869 , :870 , :871 , :872 , :873 , :874 , :875 , :876 , :877 , :878 , :879 , :880 , :881 , :882 , :883 , :884 , :885 , :886 , :887 , :88 8 , :889 , :890 , :891 , :892 , :893 , :894 , :895 , :896 , :897 , :898 , :899 , :900 , :901 , :902 , :903 , :904 , :905 , :906 , :907 , :908 , :909 , :910 , :911 , :912 , :913 , :914 , :915 , :916 , :917 , :918 , :919 , :920 , :921 , :922 , :923 , :924 , :925 , :926 , :927 , :928 , :929 , :930 , :931 , :932 , :933 , :934 , :935 , :936 , :937 , :938 , :939 , :940 , :941 , :942 , :943 , :944 , :945 , :946 , :947 , :948 , :949 , :950 , :951 , :952 , :953 , :954 , :955 , :956 , :957 , :958 , :959 , :960 , :961 , :962 , :963 , :964 , :965 , :966 , :967 , :968 , :969 , :970 , :971 , :972 , :973 , :974 , :975 , :976 , :977 , :978 , :979 , :980 , :981 , :982 , :983 , :984 , :985 , :986 , :987 , :988 , :989 , :990 , :991 , :992 , :993 , :994 , :995 , :996 , :997 , :998 , :999 , :1000 ) or idworderbi0_.id in (:1001 , :1002 , :1003 , :1004 , :1005 , :1006 , :1007 , :1008 , :100 9 , :1010 , :1011 , :1012 , :1013 , :1014 , :1015 , :1016 , :1017 , :1018 , :1019 , :1020 , :1021 , :1022 , :1023 , :1024 , :1025 , :1026 , :1027 , :1028 , :1029 , :1030 , :1031 , :1032 , :1033 , :1034 , :1035 , :1036 , :1037 , :1038 , :1039 , :1040 , :1041 , :1042 , :1043 , :1044 , :1045 , :1046 , :1047 , :1048 , :1049 , :1050 , :1051 , :1052 , :1053 , :1054 , :1055 , :1056 , :1057 , :1058 , :1059 , :1060 , :1061 , :1062 , :1063 , :1064 , :1065 , :1066 , :1067 , :1068 , :1069 , :1070 , :1071 , :1072 , :1073 , :1074 , :1075 , :1076 , :1077 , :1078 , :1079 , :1080 , :1081 , :1082 , :1083 , :1084 , :1085 , :1086 , :1087 , :1088 , :1089 , :1090 , :1091 , :1092 , :1093 , :1094 , :1095 , :1096 , :1097 , :1098 , :1099 , :1100 , :1101 , :1102 , :1103 , :1104 , :1105 , :1106 , :1107 , :1108 , :1109 , :1110 , :1111 , :1112 , :1113 , :1114 , :1115 , :1116 , :1117 , :1118 , :1119 , :1120 , :1121 , :1122 , :1123 , :1124 , :1125 , :1126 , :1127 , :1128 , :1129 , :1130 , :1131 , :1132 , :1133 , :1134 , :1135 , :1136 , :1137 , :1138 , :1139 , :1140 , :1141 , :1142 , :1143 , :1144 , :1145 , :1146 , :1147 , :1148 , :1149 , :1150 , :1151 , :1152 , :1153 , :1154 , :1155 , :1156 , :1157 , :1158 , :1159 , :1160 , :1161 , :1162 , :1163 , :1164 , :1165 , :1166 , :1167 , :1168 , :1169 , :1170 , :1171 , :1172 , :1173 , :1174 , :1175 , :1176 , :1177 , :1178 , :1179 , :1180 , :1181 , :1182 , :1183 , :1184 , :1185 , :1186 , :1187 , :1188 , :1189 , :1190 , :1191 , :1192 , :1193 , :1194 , :1195 , :1196 , :1197 , :1198 , :1199 , :1200 , :1201 , :1202 , :1203 , :1204 , :1205 , :1206 , :1207 , :1208 , :1209 , :1210 , :1211 , :1212 , :1213 , :1214 , :1215 , :1216 , :1217 , :1218 , :1219 , :1220 , :1221 , :1222 , :1223 , :1224 , :1225 , :1226 , :1227 , :1228 , :1229 , :1230 , :1231 , :1232 , :1233 , :1234 , :1235 , :1236 , :1237 , :1238 , :1239 , :1240 , :1241 , :1242 , :1243 , :1244 , :1245 , :1246 , :1247 , :1248 , :1249 , :1250 , :1251 , :1252 , :1253 , :1254 , :1255 , :1256 , :1257 , :1258 , :1259 , :1260 , :1261 , :1262 , :1263 , :1264 , :1265 , :1266 , :1267 , :1268 , :1269 , :1270 , :1271 , :1272 , :1273 , :1274 , :1275 , :1276 , :1277 , :1278 , :1279 , :1280 , :1281 , :1282 , :1283 , :1284 , :1285 , :1286 , :1287 , :1288 , :1289 , :1290 , :1291 , :1292 , :1293 , :1294 , :1295 , :1296 , :1297 , :1298 , :1299 , :1300 , :1301 , :1302 , :1303 , :1304 , :1305 , :1306 , :1307 , :1308 , :1309 , :1310 , :1311 , :1312 , :1313 , :1314 , :1315 , :1316 , :1317 , :1318 , :1319 , :1320 , :1321 , :1322 , :1323 , :1324 , :1325 , :1326 , :1327 , :1328 , :1329 , :1330 , :1331 , :1332 , :1333 , :1334 , :1335 , :1336 , :1337 , :1338 , :1339 , :1340 , :1341 , :1342 , :1343 , :1344 , :1345 , :1346 , :1347 , :1348 , :1349 , :1350 , :1351 , :1352 , :1353 , :1354 , :1355 , :1356 , :1357 , :1358 , :1359 , :1360 , :1361 , :1362 , :1363 , :1364 , :1365 , :1366 , :1367 , :1368 , :1369 , :1370 , :1371 , :1372 , :1373 , :1374 , :1375 , :1376 , :1377 , :1378 , :1379 , :1380 , :1381 , :1382 , :1383 , :1384 , :1385 , :1386 , :1387 , :1388 , :1389 , :1390 , :1391 , :1392 , :1393 , :1394 , :1395 , :1396 , :1397 , :1398 , :1399 , :1400 , :1401 , :1402 , :1403 , :1404 , :1405 , :1406 , :1407 , :1408 , :1409 , :1410 , :1411 , :1412 , :1413 , :1414 , :1415 , :1416 , :1417 , :1418 , :1419 , :1420 , :1421 , :1422 , :1423 , :1424 , :1425 , :1426 , :1427 , :1428 , :1429 , :1430 , :1431 , :1432 , :1433 , :1434 , :1435 , :1436 , :1437 , :1438 , :1439 , :1440 , :1441 , :1442 , :1443 , :1444 , :1445 , :1446 , :1447 , :1448 , :1449 , :1450 , :1451 , :1452 , :1453 , :1454 , :1455 , :1456 , :1457 , :1458 , :1459 , :1460 , :1461 , :1462 , :1463 , :1464 , :1465 , :1466 , :1467 , :1468 , :1469 , :1470 , :1471 , :1472 , :1473 , :1474 , :1475 , :1476 , :1477 , :1478 , :1479 , :1480 , :1481 , :1482 , :1483 , :1484 , :1485 , :1486 , :1487 , :1488 , :1489 , :1490 , :1491 , :1492 , :1493 , :1494 , :1495 , :1496 , :1497 , :1498 , :1499 , :1500 , :1501 , :1502 , :1503 , :1504 , :1505 , :1506 , :1507 , :1508 , :1509 , :1510 , :1511 , :1512 , :1513 , :1514 , :1515 , :1516 , :1517 , :1518 , :1519 , :1520 , :1521 , :1522 , :1523 , :1524 , :1525 , :1526 , :1527 , :1528 , :1529 , :1530 , :1531 , :1532 , :1533 , :1534 , :1535 , :1536 , :1537 , :1538 , :1539 , :1540 , :1541 , :1542 , :1543 , :1544 , :1545 , :1546 , :1547 , :1548 , :1549 , :1550 , :1551 , :1552 , :1553 , :1554 , :1555 , :1556 , :1557 , :1558 , :1559 , :1560 , :1561 , :1562 , :1563 , :1564 , :1565 , :1566 , :1567 , :1568 , :1569 , :1570 , :1571 , :1572 , :1573 , :1574 , :1575 , :1576 , :1577 , :1578 , :1579 , :1580 , :1581 , :1582 , :1583 , :1584 , :1585 , :1586 , :1587 , :1588 , :1589 , :1590 , :1591 , :1592 , :1593 , :1594 , :1595 , :1596 , :1597 , :1598 , :1599 , :1600 , :1601 , :1602 , :1603 , :1604 , :1605 , :1606 , :1607 , :1608 , :1609 , :1610 , :1611 , :1612 , :1613 , :1614 , :1615 , :1616 , :1617 , :1618 , :1619 , :1620 , :1621 , :1622 , :1623 , :1624 , :1625 , :1626 , :1627 , :1628 , :1629 , :1630 , :1631 , :1632 , :1633 , :1634 , :1635 , :1636 , :1637 , :1638 , :1639 , :1640 , :1641 , :1642 , :1643 , :1644 , :1645 , :1646 , :1647 , :1648 , :1649 , :1650 , :1651 , :1652 , :1653 , :1654 , :1655 , :1656 , :1657 , :1658 , :1659 , :1660 , :1661 , :1662 , :1663 , :1664 , :1665 , :1666 , :1667 , :1668 , :1669 , :1670 , :1671 , :1672 , :1673 , :1674 , :1675 , : 1676 , :1677 , :1678 , :1679 , :1680 , :1681 , :1682 , :1683 , :1684 , :1685 , :1686 , :1687 , :1688 , :1689 , :1690 , :1691 , :1692 , :1693 , :1694 , :1695 , :1696 , :1697 , :1698 , :1699 , :1700 , :1701 , :1702 , :1703 , :1704 , :1705 , :1706 , :1707 , :1708 , :1709 , :1710 , :1711 , :1712 , :1713 , :1714 , :1715 , :1716 , :1717 , :1718 , :1719 , :1720 , :1721 , :1722 , :1723 , :1724 , :1725 , :1726 , :1727 , :1728 , :1729 , :1730 , :1731 , :1732 , :1733 , :1734 , :1735 , :1736 , :1737 , :1738 , :1739 , :1740 , :1741 , :1742 , :1743 , :1744 , :1745 , :1746 , :1747 , :1748 , :1749 , :1750 , :1751 , :1752 , :1753 , :1754 , :1755 , :1756 , :1757 , :1758 , :1759 , :1760 , :1761 , :1762 , :1763 , :1764 , :1765 , :1766 , :1767 , :1768 , :1769 , :1770 , :1771 , :1772 , :1773 , :1774 , :1775 , :1776 , :1777 , :1778 , :1779 , :1780 , :1781 , :1782 , :1783 , :1784 , :1785 , :1786 , :1 787 , :1788 , :1789 , :1790 , :1791 , :1792 , :1793 , :1794 , :1795 , :1796 , :1797 , :1798 , :1799 , :1800 , :1801 , :1802 , :1803 , :1804 , :1805 , :1806 , :1807 , :1808 , :1809 , :1810 , :1811 , :1812 , :1813 , :1814 , :1815 , :1816 , :1817 , :1818 , :1819 , :1820 , :1821 , :1822 , :1823 , :1824 , :1825 , :1826 , :1827 , :1828 , :1829 , :1830 , :1831 , :1832 , :1833 , :1834 , :1835 , :1836 , :1837 , :1838 , :1839 , :1840 , :1841 , :1842 , :1843 , :1844 , :1845 , :1846 , :1847 , :1848 , :1849 , :1850 , :1851 , :1852 , :1853 , :1854 , :1855 , :1856 , :1857 , :1858 , :1859 , :1860 , :1861 , :1862 , :1863 , :1864 , :1865 , :1866 , :1867 , :1868 , :1869 , :1870 , :1871 , :1872 , :1873 , :1874 , :1875 , :1876 , :1877 , :1878 , :1879 , :1880 , :1881 , :1882 , :1883 , :1884 , :1885 , :1886 , :1887 , :1888 , :1889 , :1890 , :1891 , :1892 , :1893 , :1894 , :1895 , :1896 , :1897 , :18 98 , :1899 , :1900 , :1901 , :1902 , :1903 , :1904 , :1905 , :1906 , :1907 , :1908 , :1909 , :1910 , :1911 , :1912 , :1913 , :1914 , :1915 , :1916 , :1917 , :1918 , :1919 , :1920 , :1921 , :1922 , :1923 , :1924 , :1925 , :1926 , :1927 , :1928 , :1929 , :1930 , :1931 , :1932 , :1933 , :1934 , :1935 , :1936 , :1937 , :1938 , :1939 , :1940 , :1941 , :1942 , :1943 , :1944 , :1945 , :1946 , :1947 , :1948 , :1949 , :1950 , :1951 , :1952 , :1953 , :1954 , :1955 , :1956 , :1957 , :1958 , :1959 , :1960 , :1961 , :1962 , :1963 , :1964 , :1965 , :1966 , :1967 , :1968 , :1969 , :1970 , :1971 , :1972 , :1973 , :1974 , :1975 , :1976 , :1977 , :1978 , :1979 , :1980 , :1981 , :1982 , :1983 , :1984 , :1985 , :1986 , :1987 , :1988 , :1989 , :1990 , :1991 , :1992 , :1993 , :1994 , :1995 , :1996 , :1997 , :1998 , :1999 , :2000 ) or idworderbi0_.id in (:2001 , :2002 , :2003 , :2004 , :2005 , :2006 , :2007 , :2008 , :2009 , :2010 , :2011 , :2012 , :2013 , :2014 , :2015 , :2016 , :2017 , :2018 , :2019 , :2020 , :2021 , :2022 , :2023 , :2024 , :2025 , :2026 , :2027 , :2028 , :2029 , :2030 , :2031 , :2032 , :2033 , :2034 , :2035 , :2036 , :2037 , :2038 , :2039 , :2040 , :2041 , :2042 , :2043 , :2044 , :2045 , :2046 , :2047 , :2048 , :2049 , :2050 , :2051 , :2052 , :2053 , :2054 , :2055 , :2056 , :2057 , :2058 , :2059 , :2060 , :2061 , :2062 , :2063 , :2064 , :2065 , :2066 , :2067 , :2068 , :2069 , :2070 , :2071 , :2072 , :2073 , :2074 , :2075 , :2076 , :2077 , :2078 , :2079 , :2080 , :2081 , :2082 , :2083 , :2084 , :2085 , :2086 , :2087 , :2088 , :2089 , :2090 , :2091 , :2092 , :2093 , :2094 , :2095 , :2096 , :2097 , :2098 , :2099 , :2100 , :2101 , :2102 , :2103 , :2104 , :2105 , :2106 , :2107 , :2108 , :2109 , :2110 , :2111 , :2112 , :2113 , :2114 , :2115 , :2116 , :2117 , : 2118 , :2119 , :2120 , :2121 , :2122 , :2123 , :2124 , :2125 , :2126 , :2127 , :2128 , :2129 , :2130 , :2131 , :2132 , :2133 , :2134 , :2135 , :2136 , :2137 , :2138 , :2139 , :2140 , :2141 , :2142 , :2143 , :2144 , :2145 , :2146 , :2147 , :2148 , :2149 , :2150 , :2151 , :2152 , :2153 , :2154 , :2155 , :2156 , :2157 , :2158 , :2159 , :2160 , :2161 , :2162 , :2163 , :2164 , :2165 , :2166 , :2167 , :2168 , :2169 , :2170 , :2171 , :2172 , :2173 , :2174 , :2175 , :2176 , :2177 , :2178 , :2179 , :2180 , :2181 , :2182 , :2183 , :2184 , :2185 , :2186 , :2187 , :2188 , :2189 , :2190 , :2191 , :2192 , :2193 , :2194 , :2195 , :2196 , :2197 , :2198 , :2199 , :2200 , :2201 , :2202 , :2203 , :2204 , :2205 , :2206 , :2207 , :2208 , :2209 , :2210 , :2211 , :2212 , :2213 , :2214 , :2215 , :2216 , :2217 , :2218 , :2219 , :2220 , :2221 , :2222 , :2223 , :2224 , :2225 , :2226 , :2227 , :2228 , :2 229 , :2230 , :2231 , :2232 , :2233 , :2234 , :2235 , :2236 , :2237 , :2238 , :2239 , :2240 , :2241 , :2242 , :2243 , :2244 , :2245 , :2246 , :2247 , :2248 , :2249 , :2250 , :2251 , :2252 , :2253 , :2254 , :2255 , :2256 , :2257 , :2258 , :2259 , :2260 , :2261 , :2262 , :2263 , :2264 , :2265 , :2266 , :2267 , :2268 , :2269 , :2270 , :2271 , :2272 , :2273 , :2274 , :2275 , :2276 , :2277 , :2278 , :2279 , :2280 , :2281 , :2282 , :2283 , :2284 , :2285 , :2286 , :2287 , :2288 , :2289 , :2290 , :2291 , :2292 , :2293 , :2294 , :2295 , :2296 , :2297 , :2298 , :2299 , :2300 , :2301 , :2302 , :2303 , :2304 , :2305 , :2306 , :2307 , :2308 , :2309 , :2310 , :2311 , :2312 , :2313 , :2314 , :2315 , :2316 , :2317 , :2318 , :2319 , :2320 , :2321 , :2322 , :2323 , :2324 , :2325 , :2326 , :2327 , :2328 , :2329 , :2330 , :2331 , :2332 , :2333 , :2334 , :2335 , :2336 , :2337 , :2338 , :2339 , :23 40 , :2341 , :2342 , :2343 , :2344 , :2345 , :2346 , :2347 , :2348 , :2349 , :2350 , :2351 , :2352 , :2353 , :2354 , :2355 , :2356 , :2357 , :2358 , :2359 , :2360 , :2361 , :2362 , :2363 , :2364 , :2365 , :2366 , :2367 , :2368 , :2369 , :2370 , :2371 , :2372 , :2373 , :2374 , :2375 , :2376 , :2377 , :2378 , :2379 , :2380 , :2381 , :2382 , :2383 , :2384 , :2385 , :2386 , :2387 , :2388 , :2389 , :2390 , :2391 , :2392 , :2393 , :2394 , :2395 , :2396 , :2397 , :2398 , :2399 , :2400 , :2401 , :2402 , :2403 , :2404 , :2405 , :2406 , :2407 , :2408 , :2409 , :2410 , :2411 , :2412 , :2413 , :2414 , :2415 , :2416 , :2417 , :2418 , :2419 , :2420 , :2421 , :2422 , :2423 , :2424 , :2425 , :2426 , :2427 , :2428 , :2429 , :2430 , :2431 , :2432 , :2433 , :2434 , :2435 , :2436 , :2437 , :2438 , :2439 , :2440 , :2441 , :2442 , :2443 , :2444 , :2445 , :2446 , :2447 , :2448 , :2449 , :2450 , :245 1 , :2452 , :2453 , :2454 , :2455 , :2456 , :2457 , :2458 , :2459 , :2460 , :2461 , :2462 , :2463 , :2464 , :2465 , :2466 , :2467 , :2468 , :2469 , :2470 , :2471 , :2472 , :2473 , :2474 , :2475 , :2476 , :2477 , :2478 , :2479 , :2480 , :2481 , :2482 , :2483 , :2484 , :2485 , :2486 , :2487 , :2488 , :2489 , :2490 , :2491 , :2492 , :2493 , :2494 , :2495 , :2496 , :2497 , :2498 , :2499 , :2500 , :2501 , :2502 , :2503 , :2504 , :2505 , :2506 , :2507 , :2508 , :2509 , :2510 , :2511 , :2512 , :2513 , :2514 , :2515 , :2516 , :2517 , :2518 , :2519 , :2520 , :2521 , :2522 , :2523 , :2524 , :2525 , :2526 , :2527 , :2528 , :2529 , :2530 , :2531 , :2532 , :2533 , :2534 , :2535 , :2536 , :2537 , :2538 , :2539 , :2540 , :2541 , :2542 , :2543 , :2544 , :2545 , :2546 , :2547 , :2548 , :2549 , :2550 , :2551 , :2552 , :2553 , :2554 , :2555 , :2556 , :2557 , :2558 , :2559 , :2560 , :2561 , :2562 , :2563 , :2564 , :2565 , :2566 , :2567 , :2568 , :2569 , :2570 , :2571 , :2572 , :2573 , :2574 , :2575 , :2576 , :2577 , :2578 , :2579 , :2580 , :2581 , :2582 , :2583 , :2584 , :2585 , :2586 , :2587 , :2588 , :2589 , :2590 , :2591 , :2592 , :2593 , :2594 , :2595 , :2596 , :2597 , :2598 , :2599 , :2600 , :2601 , :2602 , :2603 , :2604 , :2605 , :2606 , :2607 , :2608 , :2609 , :2610 , :2611 , :2612 , :2613 , :2614 , :2615 , :2616 , :2617 , :2618 , :2619 , :2620 , :2621 , :2622 , :2623 , :2624 , :2625 , :2626 , :2627 , :2628 , :2629 , :2630 , :2631 , :2632 , :2633 , :2634 , :2635 , :2636 , :2637 , :2638 , :2639 , :2640 , :2641 , :2642 , :2643 , :2644 , :2645 , :2646 , :2647 , :2648 , :2649 , :2650 , :2651 , :2652 , :2653 , :2654 , :2655 , :2656 , :2657 , :2658 , :2659 , :2660 , :2661 , :2662 , :2663 , :2664 , :2665 , :2666 , :2667 , :2668 , :2669 , :2670 , :2671 , :2672 , :2673 , :2674 , :2675 , :2676 , :2677 , :2678 , :2679 , :2680 , :2681 , :2682 , :2683 , :2684 , :2685 , :2686 , :2687 , :2688 , :2689 , :2690 , :2691 , :2692 , :2693 , :2694 , :2695 , :2696 , :2697 , :2698 , :2699 , :2700 , :2701 , :2702 , :2703 , :2704 , :2705 , :2706 , :2707 , :2708 , :2709 , :2710 , :2711 , :2712 , :2713 , :2714 , :2715 , :2716 , :2717 , :2718 , :2719 , :2720 , :2721 , :2722 , :2723 , :2724 , :2725 , :2726 , :2727 , :2728 , :2729 , :2730 , :2731 , :2732 , :2733 , :2734 , :2735 , :2736 , :2737 , :2738 , :2739 , :2740 , :2741 , :2742 , :2743 , :2744 , :2745 , :2746 , :2747 , :2748 , :2749 , :2750 , :2751 , :2752 , :2753 , :2754 , :2755 , :2756 , :2757 , :2758 , :2759 , :2760 , :2761 , :2762 , :2763 , :2764 , :2765 , :2766 , :2767 , :2768 , :2769 , :2770 , :2771 , :2772 , :2773 , :2774 , :2775 , :2776 , :2777 , :2778 , :2779 , :2780 , :2781 , :2782 , :2783 , :2784 , :2785 , :2786 , :2787 , :2788 , :2789 , :2790 , :2791 , :2792 , :2793 , :2794 , :2795 , :2796 , :2797 , :2798 , :2799 , :2800 , :2801 , :2802 , :2803 , :2804 , :2805 , :2806 , :2807 , :2808 , :2809 , :2810 , :2811 , :2812 , :2813 , :2814 , :2815 , :2816 , :2817 , :2818 , :2819 , :2820 , :2821 , :2822 , :2823 , :2824 , :2825 , :2826 , :2827 , :2828 , :2829 , :2830 , :2831 , :2832 , :2833 , :2834 , :2835 , :2836 , :2837 , :2838 , :2839 , :2840 , :2841 , :2842 , :2843 , :2844 , :2845 , :2846 , :2847 , :2848 , :2849 , :2850 , :2851 , :2852 , :2853 , :2854 , :2855 , :2856 , :2857 , :2858 , :2859 , :2860 , :2861 , :2862 , :2863 , :2864 , :2865 , :2866 , :2867 , :2868 , :2869 , :2870 , :2871 , :2872 , :2873 , :2874 , :2875 , :2876 , :2877 , :2878 , :2879 , :2880 , :2881 , :2882 , :2883 , :2884 , :2885 , :2886 , :2887 , :2888 , :2889 , :2890 , :2891 , :2892 , :2893 , :2894 , :2895 , :2896 , :2897 , :2898 , :2899 , :2900 , :2901 , :2902 , :2903 , :2904 , :2905 , :2906 , :2907 , :2908 , :2909 , :2910 , :2911 , :2912 , :2913 , :2914 , :2915 , :2916 , :2917 , :2918 , :2919 , :2920 , :2921 , :2922 , :2923 , :2924 , :2925 , :2926 , :2927 , :2928 , :2929 , :2930 , :2931 , :2932 , :2933 , :2934 , :2935 , :2936 , :2937 , :2938 , :2939 , :2940 , :2941 , :2942 , :2943 , :2944 , :2945 , :2946 , :2947 , :2948 , :2949 , :2950 , :2951 , :2952 , :2953 , :2954 , :2955 , :2956 , :2957 , :2958 , :2959 , :2960 , :2961 , :2962 , :2963 , :2964 , :2965 , :2966 , :2967 , :2968 , :2969 , :2970 , :2971 , :2972 , :2973 , :2974 , :2975 , :2976 , :2977 , :2978 , :2979 , :2980 , :2981 , :2982 , :2983 , :2984 , :2985 , :2986 , :2987 , :2988 , :2989 , :2990 , :2991 , :2992 , :2993 , :2994 , :2995 , :2996 , :2997 , :2998 , :2999 , :3000 ) or idworderbi0_.id in (:3001 , :3002 , :3003 , :3004 , :3005 , :3006 , :3007 , :3008 , :3009 , :3010 , :3011 , :3012 , :3013 , :3014 , :3015 , :3016 , :3017 , :3018 , :3019 , :3020 , :3021 , :3022 , :3023 , :3024 , :3025 , :3026 , :3027 , :3028 , :3029 , :3030 , :3031 , :3032 , :3033 , :3034 , :3035 , :3036 , :3037 , :3038 , :3039 , :3040 , :3041 , :3042 , :3043 , :3044 , :3045 , :3046 , :3047 , :3048 , :3049 , :3050 , :3051 , :3052 , :3053 , :3054 , :3055 , :3056 , :3057 , :3058 , :3059 , :3060 , :3061 , :3062 , :3063 , :3064 , :3065 , :3066 , :3067 , :3068 , :3069 , :3070 , :3071 , :3072 , :3073 , :3074 , :3075 , :3076 , :3077 , :3078 , :3079 , :3080 , :3081 , :3082 , :3083 , :3084 , :3085 , :3086 , :3087 , :3088 , :3089 , :3090 , :3091 , :3092 , :3093 , :3094 , :3095 , :3096 , :3097 , :3098 , :3099 , :3100 , :3101 , :3102 , :3103 , :3104 , :3105 , :3106 , :3107 , :3108 , :3109 , :3110 , :3111 , :3112 , :3113 , :3114 , :3115 , :3116 , :3117 , :3118 , :3119 , :3120 , :3121 , :3122 , :3123 , :3124 , :3125 , :3126 , :3127 , :3128 , :3129 , :3130 , :3131 , :3132 , :3133 , :3134 , :3135 , :3136 , :3137 , :3138 , :3139 , :3140 , :3141 , :3142 , :3143 , :3144 , :3145 , :3146 , :3147 , :3148 , :3149 , :3150 , :3151 , :3152 , :3153 , :3154 , :3155 , :3156 , :3157 , :3158 , :3159 , :3160 , :3161 , :3162 , :3163 , :3164 , :3165 , :3166 , :3167 , :3168 , :3169 , :3170 , :3171 , :3172 , :3173 , :3174 , :3175 , :3176 , :3177 , :3178 , :3179 , :3180 , :3181 , :3182 , :3183 , :3184 , :3185 , :3186 , :3187 , :3188 , :3189 , :3190 , :3191 , :3192 , :3193 , :3194 , :3195 , :3196 , :3197 , :3198 , :3199 , :3200 , :3201 , :3202 , :3203 , :3204 , :3205 , :3206 , :3207 , :3208 , :3209 , :3210 , :3211 , :3212 , :3213 , :3214 )  
f2xfzfr3pjh3q| select t.* from hisuser.dgby_online_settle_fee_info t where 1=1 and t.jzlsh = :1   
f72rtznv1afds| SELECT COUNT(*) FROM WDP.DPC_STORAGE_DRUG G WHERE G.ITEM_ID = :B1   
f8hq4t3wdkwfp|  select mtinspecta0_.apply_id as apply_id1_34_, mtinspecta0_.address as address2_34_, mtinspecta0_.age as age3_34_, mtinspecta0_.anaesthesia as anaesthesia4_34_, mtinspecta0_.apply_check_state as apply_check_state5_34_, mtinspecta0_.apply_dept_code as apply_dept_code6_34_, mtinspecta0_.apply_dept_id as apply_dept_id7_34_, mtinspecta0_.apply_dept_name as apply_dept_name8_34_, mtinspecta0_.apply_doctor_code as apply_doctor_code9_34_, mtinspecta0_.apply_doctor_id as apply_doctor_id10_34_, mtinspecta0_.apply_doctor_name as apply_doctor_name11_34_, mtinspecta0_.apply_doctor_type as apply_doctor_type12_34_, mtinspecta0_.apply_item_count as apply_item_count13_34_, mtinspecta0_.apply_no as apply_no14_34_, mtinspecta0_.apply_pay_amount as apply_pay_amount15_34_, mtinspecta0_.apply_pay_state as apply_pay_state16_34_, mtinspecta0_.apply_source as apply_source17_34_, mtinspecta0_.apply_time as apply_time18_34_, mtinspecta0_.appt_remark as appt_remark19_34_, mtinspecta0_.appt_stat e as appt_state20_34_, mtinspecta0_.area_id as area_id21_34_, mtinspecta0_.area_name as area_name22_34_, mtinspecta0_.automatic_reservation as automatic_reserva23_34_, mtinspecta0_.bed_no as bed_no24_34_, mtinspecta0_.branch_id as branch_id25_34_, mtinspecta0_.branch_name as branch_name26_34_, mtinspecta0_.date_birth as date_birth27_34_, mtinspecta0_.db_flag as db_flag28_34_, mtinspecta0_.dcheck_rec as dcheck_rec29_34_, mtinspecta0_.dept_code as dept_code30_34_, mtinspecta0_.dept_id as dept_id31_34_, mtinspecta0_.dept_name as dept_name32_34_, mtinspecta0_.diag as diag33_34_, mtinspecta0_.digital_age as digital_age34_34_, mtinspecta0_.dmed_rec as dmed_rec35_34_, mtinspecta0_.dphyexam as dphyexam36_34_, mtinspecta0_.dtell as dtell37_34_, mtinspecta0_.emr_phone as emr_phone38_34_, mtinspecta0_.exampurpose as exampurpose39_34_, mtinspecta0_.examination as examination40_34_, mtinspecta0_.fcalmflag as fcalmflag41_34_, mtinspecta0_.flow_num as flow_num42_34_, mtinspecta 0_.gender as gender43_34_, mtinspecta0_.health_code as health_code44_34_, mtinspecta0_.id_number as id_number45_34_, mtinspecta0_.infecthistory as infecthistory46_34_, mtinspecta0_.inhosp_num as inhosp_num47_34_, mtinspecta0_.insp_type_code as insp_type_code48_34_, mtinspecta0_.insp_type_id as insp_type_id49_34_, mtinspecta0_.insp_type_name as insp_type_name50_34_, mtinspecta0_.internet as internet51_34_, mtinspecta0_.ip_patient_id as ip_patient_id52_34_, mtinspecta0_.isavailable as isavailable53_34_, mtinspecta0_.list_print_date as list_print_date54_34_, mtinspecta0_.list_print_flag as list_print_flag55_34_, mtinspecta0_.logcby as logcby56_34_, mtinspecta0_.logcdate as logcdate57_34_, mtinspecta0_.logluby as logluby58_34_, mtinspecta0_.logludate as logludate59_34_, mtinspecta0_.manual_add_flag as manual_add_flag60_34_, mtinspecta0_.multiresisbact as multiresisbact61_34_, mtinspecta0_.new_ip_patient as new_ip_patient62_34_, mtinspecta0_.op_patient_id as op_patient_i d63_34_, mtinspecta0_.order_num as order_num64_34_, mtinspecta0_.original_area as original_area65_34_, mtinspecta0_.other_remark as other_remark66_34_, mtinspecta0_.pacs_state as pacs_state67_34_, mtinspecta0_.patient_id as patient_id68_34_, mtinspecta0_.patient_name as patient_name69_34_, mtinspecta0_.patient_num as patient_num70_34_, mtinspecta0_.phone as phone71_34_, mtinspecta0_.print_date as print_date72_34_, mtinspecta0_.print_flag as print_flag73_34_, mtinspecta0_.print_times as print_times74_34_, mtinspecta0_.print_user_name as print_user_name75_34_, mtinspecta0_.priority as priority76_34_, mtinspecta0_.relate_apply as relate_apply77_34_, mtinspecta0_.remark as remark78_34_, mtinspecta0_.specialinfection as specialinfection79_34_, mtinspecta0_.special_requirements as special_requireme80_34_, mtinspecta0_.state as state81_34_, mtinspecta0_.sync_remark as sync_remark82_34_, mtinspecta0_.sync_state as sync_state83_34_, mtinspecta0_.transportmode as transportmo de84_34_, mtinspecta0_.valid_end_date as valid_end_date85_34_ from mt_inspect_apply mtinspecta0_ where (mtinspecta0_.patient_num=:1 or mtinspecta0_.patient_name=:2 or mtinspecta0_.op_patient_id=:3 or mtinspecta0_.ip_patient_id=:4 or mtinspecta0_.apply_no=:5 or mtinspecta0_.patient_id=:6 or mtinspecta0_.health_code=:7) and mtinspecta0_.isavailable='Y' and mtinspecta0_.state='ZC' and (mtinspecta0_.apply_check_state=:8 or appt_state in (:9)) and to_char(apply_time, 'yyyy-MM-dd')>=:10  
g1mygga3s3mcz| select pat_index_no, treat_card_no, pat_name, physi_sex_name, date_birth, phone_no, id_number , months_between(trunc(sysdate), trunc(date_birth))/12 ageLimit, fee_type, health_card, age from esb_pa_treat_card_infor where treat_card_no = :1 or health_card=:2   
g2cqspstx3awz|  insert into bab_bed_allocation (accounting_status, admit_method_id, admit_method_name, admit_purpose, admit_status_id, admit_status_name, admit_status_tag, admit_type_id, admit_type_name, admit_way_id, admit_way_name, age, allocation_admit_date, allocation_admit_hour, allocation_bed_code, allocation_bed_descr, allocation_bed_id, allocation_bed_level_name, allocation_bed_name, allocation_bed_time, allocation_bed_type_name, allocation_bed_type_tag, allocation_branch_id, allocation_dept_id, allocation_dept_name, allocation_medical_group_id, allocation_medical_group_name, allocation_sickroom_id, allocation_sickroom_name, allocation_sickroom_sex_tag, allocation_type, allocation_user_id, allocation_user_name, allocation_ward_id, allocation_ward_name, antigen_type, apply_admit_dept_code, apply_admit_dept_name, apply_resource, apply_user_id, apply_user_name, bed_type_id, bed_type_name, birth_addr, birth_city, birth_city_code, birth_district, birth _district_code, birth_postcode, birth_province, birth_province_code, birth_street, birth_street_code, cancel_bed_descr, company_addr, company_phone_no, company_postcode, confirm_apply_time, confirmed_state, contact_addr, contact_city, contact_city_code, contact_credential_type_id, contact_credential_type_name, contact_district, contact_district_code, contact_fail_times, contact_id_number, contact_name, contact_phone_no, contact_postcode, contact_province, contact_province_code, contact_relation_id, contact_relation_name, contact_street, contact_street_code, create_date, create_user, credential_type_id, credential_type_name, cross_dept_type_id, cross_dept_type_name, cross_dept_type_tag, curr_addr, curr_city, curr_city_code, curr_district, curr_district_code, curr_postcode, curr_province, curr_province_code, curr_street, curr_street_code, customer_state, data_source, date_birth, diag_code, diag_name, discharge_date, disease_history, d iseases_class_id, diseases_class_name, diseases_class_tag, emergency_treatment, emr_pre_in_dept_id, emr_pre_in_dept_name, estimate_pros_pay, fever, guardian_credential_type_id, guardian_credential_type_name, guardian_id_number, guardian_name, his_admit_time, his_in_ward_time, hosp_dept_code, hosp_dept_name, household_addr, household_city, household_city_code, household_district, household_district_code, household_postcode, household_province, household_province_code, household_street, household_street_code, id_number, infectious_disease_id, infectious_disease_name, inhosp_id, inhosp_no, inhosp_times, is_accompany, is_allocationd_bed, is_appointment, is_bac_examination, is_fasting, is_icu_bed, is_need_quarantine, is_pat_cross_dept, is_retired_staff, is_window_bed, last_desc, last_state, last_state_tag, last_time, last_user_id, last_user_name, marital_status_id, marital_status_name, medical_cross_dept_descr, medicare_categ_code, medicar e_categ_name, nation_id, nation_name, nationality_id, nationality_name, native_city, native_city_code, native_province, native_province_code, nucleic_acid_date, nucleic_acid_result, occupation_id, occupation_name, other_id, outhosp_no, pat_id, pat_name, pat_phone_no, pat_source_id, pat_source_name, physi_sex_code, physi_sex_name, pre_in_bed_code, pre_in_branch_id, pre_in_dept_id, pre_in_dept_name, pre_in_medical_group_id, pre_in_medical_group_name, pre_in_ward_id, pre_in_ward_name, recept_treat_dr_code, recept_treat_dr_id, recept_treat_dr_name, reserve_admit_date, reserve_apply_date, reserve_descr, reserve_no, revise_reg_msg_num, sickroom_type_id, sickroom_type_name, sync_pre_in_dept_id, sync_pre_in_dept_name, test_results, transfer_out_bed_code, transfer_out_branch_id, transfer_out_dept_id, transfer_out_dept_name, transfer_out_ward_id, transfer_out_ward_name, update_date, update_user, visit_card_no, wait_bed_flag, allocation_no) val ues (:1 , :2 , :3 , :4 , :5 , :6 , :7 , :8 , :9 , :10 , :11 , :12 , :13 , :14 , :15 , :16 , :17 , :18 , :19 , :20 , :21 , :22 , :23 , :24 , :25 , :26 , :27 , :28 , :29 , :30 , :31 , :32 , :33 , :34 , :35 , :36 , :37 , :38 , :39 , :40 , :41 , :42 , :43 , :44 , :45 , :46 , :47 , :48 , :49 , :50 , :51 , :52 , :53 , :54 , :55 , :56 , :57 , :58 , :59 , :60 , :61 , :62 , :63 , :64 , :65 , :66 , :67 , :68 , :69 , :70 , :71 , :72 , :73 , :74 , :75 , :76 , :77 , :78 , :79 , :80 , :81 , :82 , :83 , :84 , :85 , :86 , :87 , :88 , :89 , :90 , :91 , :92 , :93 , :94 , :95 , :96 , :97 , :98 , :99 , :100 , :101 , :102 , :103 , :104 , :105 , :106 , :107 , :108 , :109 , :110 , :111 , :112 , :113 , :114 , :115 , :116 , :117 , :118 , :119 , :120 , :121 , :122 , :123 , :124 , :125 , :126 , :127 , :128 , :129 , :130 , :131 , :132 , :133 , :134 , :135 , :136 , :137 , :138 , :139 , :140 , :141 , :142 , :143 , :144 , :145 , :146 , :147 , :148 , :149 , :150 , :151 , :152 , :153 , :154 , :155 , :156 , :157 , :158 , :159 , :160 , :161 , :162 , :163 , :164 , :165 , :166 , :167 , :168 , :169 , :170 , :171 , :172 , :173 , :174 , :175 , :176 , :177 , :178 , :179 , :180 , :181 , :182 , :183 , :184 , :185 , :186 , :187 , :188 , :189 , :190 , :191 , :192 , :193 , :194 , :195 , :196 , :197 , :198 , :199 , :200 , :201 , :202 , :203 , :204 , :205 , :206 , :207 )  
g56xnb42pv9t4| select A.ID as ROWKEY , A.* from T_PA_PERSON A where a.create_time>sysdate-3   
gdp34xjtzz19w|  \--շѸ֪ select o.org_name, --Ժ i.active_flag, dep.dept_name, -- v.visit_id, --ˮ i.id, --Ʊid i.invoice_no_prefix || i.invoice_no invoice_no, --Ʊ i.card_id, -- v.name, -- sex.item_value gender, --Ա (select pa.item_value from t_sm_paraitem pa where pa.id=i.mi_code and pa.catalog_id like'0405%') mi_code, -- i.total_amount, --Ʊ i.account_debted, --˽ i.individual_payment, --Ը i.cashier_code, --շԱ i.cashier_name, --շԱ nvl((select odw.placer_code from t_odw_orderbilling odw, t_ob_paymentitems ps where rownum=1 and odw.id=ps.order_billing_id and ps.payment_id=i.payment_id and odw.placer_code not in ( select u.user_code from t_sm_userbaseinfo u where u.remark='xn')), '') as dr_code, --ҽ i.charge_datetime, --շʱ to_char((select wm_concat(pa.item_value || ':' ||--ch.amount trim(to_char(nvl(ch.amount, 0), '99999990.99')) ) from t_ob_chargetype ch, t_sm_paraitem pa where ch.invoice_id=i.id and ch.charge_type=pa.id)) zffs, e.BILL_QR_CODE BILLQRC ODE, e.bill_no, h.*, i.ass_win, (case when i.org_id=1 and i.ass_win is not null and i.ass_win<>'ɹ' then '뵽'|| nvl(i.ass_win, 'ҩ') ||'Ŷȡҩ' end) as tips, case when instr(i.remark, '')>0 then substr(i.remark, instr(i.remark, '')) else null end as pre_pay, nvl(i.precharge, 0) as precharge from (select T_OB_FC_AMOUNT.INVOICE_ID, nvl(t_ob_invoice.other_account_debted_total, 0) other_account_debted_total, sum(case when d.id=15989 then AMOUNT else NULL end) AMOUNT_01, --ҩ sum(case when d.id=14987 then AMOUNT else NULL end) AMOUNT_02, --гҩ sum(case when d.id=23006 then AMOUNT else NULL end) AMOUNT_03, --вҩ sum(case when d.id=23509 then AMOUNT else NULL end) AMOUNT_04, -- sum(case when d.id=15992 then AMOUNT else NULL end) AMOUNT_05, -- sum(case when d.id=15993 then AMOUNT else NULL end) AMOUNT_06, -- sum(case when d.id=15994 then AMOUNT else NULL end) AMOUNT_07, --Ʒ sum(case when d.id=15995 then AMOUNT else NULL end) AMOUNT_08, -- sum(case whe n d.id=15996 then AMOUNT else NULL end) AMOUNT_09, --Ѫ sum(case when d.id=15997 then AMOUNT else NULL end) AMOUNT_10, -- sum(case when d.id=15998 then AMOUNT else NULL end) AMOUNT_11, --λ sum(case when d.id=15999 then AMOUNT else NULL end) AMOUNT_12, -- sum(case when d.id=24511 then AMOUNT else NULL end) AMOUNT_15, -- sum(case when d.id=23509 then nvl(AMOUNT, 0)-nvl(T_OB_FC_AMOUNT.NO_DEBTED, 0) else 0 end) refund_zcf from T_OB_FC_AMOUNT, t_fm_reportindex_d d , t_fm_reportindexitem item, t_ob_invoice where d.id = item.rid_id and T_OB_FC_AMOUNT.INVOICE_CLASSIFICATION= item.index_item_id and T_OB_FC_AMOUNT.INVOICE_ID in (:1 /*select i.id from t_ob_invoice i where i.create_datetime>sysdate-10*/) and T_OB_FC_AMOUNT.INVOICE_ID=t_ob_invoice.id group by T_OB_FC_AMOUNT.INVOICE_ID, t_ob_invoice.other_account_debted_total )h, t_ob_invoice i, t_sm_department dep, t_ob_payment p, t_or_account a, t_or_visit v, ( select * from t_ob_electronicbills e where 1=1 and e.status in('- 253905', '-253909') and e.bill_qr_code is not null and DBMS_LOB.GETLENGTH(e.bill_qr_code)>0 )e, (select * from t_sm_paraitem sex where sex.catalog_id ='0215'sex, t_sm_organization o where h.invoice_id=i.id and i.dept_id=dep.id and i.payment_id=p.id and p.account_id=a.account_id and a.visit_id=v.visit_id and i.id = e.invoice_id(+) and v.gender=sex.id and i.org_id=o.id  
ggd2znk56cwt0| DECLARE job BINARY_INTEGER := :job; next_date DATE := :mydate; broken BOOLEAN := FALSE; BEGIN hisuser.PG_HIS_WMD.pf_wmd_drug; :mydate := next_date; IF broken THEN :b := 1; ELSE :b := 0; END IF; END;   
gjm43un5cy843| SELECT SUM(USED), SUM(TOTAL) FROM (SELECT /*+ ORDERED */ SUM(D.BYTES)/(1024*1024)-MAX(S.BYTES) USED, SUM(D.BYTES)/(1024*1024) TOTAL FROM (SELECT TABLESPACE_NAME, SUM(BYTES)/(1024*1024) BYTES FROM (SELECT /*+ ORDERED USE_NL(obj tab) */ DISTINCT TS.NAME FROM SYS.OBJ$ OBJ, SYS.TAB$ TAB, SYS.TS$ TS WHERE OBJ.OWNER# = USERENV('SCHEMAID') AND OBJ.OBJ# = TAB.OBJ# AND TAB.TS# = TS.TS# AND BITAND(TAB.PROPERTY, 1) = 0 AND BITAND(TAB.PROPERTY, 4194400) = 0) TN, DBA_FREE_SPACE SP WHERE SP.TABLESPACE_NAME = TN.NAME GROUP BY SP.TABLESPACE_NAME) S, DBA_DATA_FILES D WHERE D.TABLESPACE_NAME = S.TABLESPACE_NAME GROUP BY D.TABLESPACE_NAME)  
gs22bnjq55v3q| select count(*) as prespSum, count( distinct visit_id) as personSum from VDPB_WAIT_DISPENSE where is_dispense = 'N' and is_cancel_confirm = 'N' and is_checked_in = 'Y' and last_state_id = 'CHECKED_IN' and pharmacy_id = :1 and actual_win_id = :2 and check_in_time >= :3 and check_in_time <= :4   
gsnna7vkctvdp| SELECT P.ID FROM T_SM_PARAITEM P WHERE P.CATALOG_ID = '070111' AND P.ITEM_VALUE = :B1 AND ROWNUM = 1  
gxn6jnu7qx2vw| select t.* from hisuser.add_zyxx_wxy t where 1=1 and t.PATIDCARD = :1 and t.PATNAME = :2 order by t.ADMITDATE  
  
Back to SQL Statistics   
Back to Top

##  Instance Activity Statistics 

  * Key Instance Activity Stats
  * Other Instance Activity Stats
  * Instance Activity Stats - Absolute Values
  * Instance Activity Stats - Thread Activity

Back to Top

### Key Instance Activity Stats

  * Ordered by statistic name

Statistic| Total| per Second| per Trans  
---|---|---|---  
db block changes| 27,318,345| 2,520.90| 56.70  
execute count| 13,595,239| 1,254.55| 28.22  
gc cr block receive time| 39,158| 3.61| 0.08  
gc cr blocks received| 466,253| 43.03| 0.97  
gc current block receive time| 85,728| 7.91| 0.18  
gc current blocks received| 775,877| 71.60| 1.61  
logons cumulative| 9,665| 0.89| 0.02  
opened cursors cumulative| 13,218,222| 1,219.76| 27.44  
parse count (total)| 3,543,284| 326.97| 7.35  
parse time elapsed| 28,654| 2.64| 0.06  
physical reads| 730,576,196| 67,416.55| 1,516.41  
physical writes| 617,276| 56.96| 1.28  
redo size| 5,594,913,372| 516,290.81| 11,613.00  
session cursor cache hits| 3,633,229| 335.27| 7.54  
session logical reads| 3,196,935,601| 295,008.76| 6,635.68  
user calls| 9,707,605| 895.80| 20.15  
user commits| 474,585| 43.79| 0.99  
user rollbacks| 7,195| 0.66| 0.01  
workarea executions - multipass| 0| 0.00| 0.00  
workarea executions - onepass| 0| 0.00| 0.00  
workarea executions - optimal| 3,699,656| 341.40| 7.68  
  
* * *

Back to Instance Activity Statistics   
Back to Top

### Other Instance Activity Stats

  * Ordered by statistic name

Statistic| Total| per Second| per Trans  
---|---|---|---  
Batched IO (bound) vector count| 237,427| 21.91| 0.49  
Batched IO (full) vector count| 1,719| 0.16| 0.00  
Batched IO (space) vector count| 0| 0.00| 0.00  
Batched IO block miss count| 752,223| 69.41| 1.56  
Batched IO buffer defrag count| 382| 0.04| 0.00  
Batched IO double miss count| 2,482| 0.23| 0.01  
Batched IO same unit count| 489,998| 45.22| 1.02  
Batched IO single block count| 230,449| 21.27| 0.48  
Batched IO slow jump count| 116| 0.01| 0.00  
Batched IO vector block count| 33,078| 3.05| 0.07  
Batched IO vector read count| 10,110| 0.93| 0.02  
Block Cleanout Optim referenced| 4| 0.00| 0.00  
CCursor + sql area evicted| 483| 0.04| 0.00  
CPU used by this session| 2,157,091| 199.05| 4.48  
CPU used when call started| 2,057,264| 189.84| 4.27  
CR blocks created| 61,145| 5.64| 0.13  
Cached Commit SCN referenced| 2,538| 0.23| 0.01  
Clusterwide global transactions| 27,357| 2.52| 0.06  
Clusterwide global transactions spanning RAC nodes| 5,837| 0.54| 0.01  
Commit SCN cached| 7,937| 0.73| 0.02  
DBWR checkpoint buffers written| 392,064| 36.18| 0.81  
DBWR checkpoints| 1,108| 0.10| 0.00  
DBWR fusion writes| 82,255| 7.59| 0.17  
DBWR object drop buffers written| 6,140| 0.57| 0.01  
DBWR revisited being-written buffer| 0| 0.00| 0.00  
DBWR tablespace checkpoint buffers written| 3,004| 0.28| 0.01  
DBWR thread checkpoint buffers written| 0| 0.00| 0.00  
DBWR transaction table writes| 1,710| 0.16| 0.00  
DBWR undo block writes| 233,893| 21.58| 0.49  
DFO trees parallelized| 57| 0.01| 0.00  
DX/BB enqueue lock background get time| 1,000| 0.09| 0.00  
DX/BB enqueue lock background gets| 57,286| 5.29| 0.12  
DX/BB enqueue lock foreground requests| 861,052| 79.46| 1.79  
Effective IO time| 571,333| 52.72| 1.19  
GTX processes spawned by autotune| 0| 0.00| 0.00  
GTX processes stopped by autotune| 0| 0.00| 0.00  
HSC Heap Segment Block Changes| 7,034,459| 649.13| 14.60  
Heap Segment Array Inserts| 18,624| 1.72| 0.04  
Heap Segment Array Updates| 0| 0.00| 0.00  
LOB table id lookup cache misses| 0| 0.00| 0.00  
Misses for writing mapping| 0| 0.00| 0.00  
Number of read IOs issued| 5,353,501| 494.01| 11.11  
PX local messages recv'd| 156| 0.01| 0.00  
PX local messages sent| 156| 0.01| 0.00  
PX remote messages recv'd| 235| 0.02| 0.00  
PX remote messages sent| 230| 0.02| 0.00  
Parallel operations not downgraded| 57| 0.01| 0.00  
Requests to/from client| 7,573,784| 698.90| 15.72  
RowCR - row contention| 2,590| 0.24| 0.01  
RowCR attempts| 121,361| 11.20| 0.25  
RowCR hits| 116,609| 10.76| 0.24  
SMON posted for dropping temp segment| 0| 0.00| 0.00  
SMON posted for undo segment recovery| 1| 0.00| 0.00  
SMON posted for undo segment shrink| 4| 0.00| 0.00  
SQL*Net roundtrips to/from client| 7,573,966| 698.92| 15.72  
SQL*Net roundtrips to/from dblink| 59,270| 5.47| 0.12  
TBS Extension: bytes extended| 0| 0.00| 0.00  
TBS Extension: files extended| 0| 0.00| 0.00  
TBS Extension: tasks created| 0| 0.00| 0.00  
TBS Extension: tasks executed| 0| 0.00| 0.00  
active txn count during cleanout| 95,687| 8.83| 0.20  
auto extends on undo tablespace| 0| 0.00| 0.00  
background checkpoints completed| 9| 0.00| 0.00  
background checkpoints started| 10| 0.00| 0.00  
background timeouts| 191,378| 17.66| 0.40  
branch node splits| 33| 0.00| 0.00  
buffer is not pinned count| 1,353,968,032| 124,942.28| 2,810.35  
buffer is pinned count| 7,771,235,354| 717,118.77| 16,130.26  
bytes received via SQL*Net from client| 2,835,387,818| 261,645.64| 5,885.23  
bytes received via SQL*Net from dblink| 160,123,727| 14,775.99| 332.36  
bytes sent via SQL*Net to client| 55,694,015,935| 5,139,366.16| 115,600.51  
bytes sent via SQL*Net to dblink| 14,033,410| 1,294.98| 29.13  
calls to get snapshot scn: kcmgss| 20,254,318| 1,869.04| 42.04  
calls to kcmgas| 1,223,552| 112.91| 2.54  
calls to kcmgcs| 2,641,868| 243.79| 5.48  
cell physical IO interconnect bytes| 6,054,580,335,616| 558,708,233.84| 12,567,106.01  
change write time| 4,947| 0.46| 0.01  
cleanout - number of ktugct calls| 124,522| 11.49| 0.26  
cleanouts and rollbacks - consistent read gets| 32,832| 3.03| 0.07  
cleanouts only - consistent read gets| 8,322| 0.77| 0.02  
cluster key scan block gets| 860,406| 79.40| 1.79  
cluster key scans| 285,721| 26.37| 0.59  
commit batch performed| 681| 0.06| 0.00  
commit batch requested| 681| 0.06| 0.00  
commit batch/immediate performed| 1,653| 0.15| 0.00  
commit batch/immediate requested| 1,653| 0.15| 0.00  
commit cleanout failures: block lost| 1,580| 0.15| 0.00  
commit cleanout failures: buffer being written| 5| 0.00| 0.00  
commit cleanout failures: callback failure| 6,235| 0.58| 0.01  
commit cleanout failures: cannot pin| 242| 0.02| 0.00  
commit cleanouts| 1,289,798| 119.02| 2.68  
commit cleanouts successfully completed| 1,281,736| 118.28| 2.66  
commit immediate performed| 972| 0.09| 0.00  
commit immediate requested| 972| 0.09| 0.00  
commit txn count during cleanout| 179,474| 16.56| 0.37  
consistent changes| 8,119,482| 749.25| 16.85  
consistent gets| 3,167,616,704| 292,303.25| 6,574.82  
consistent gets - examination| 456,185,301| 42,096.14| 946.87  
consistent gets direct| 677,114,768| 62,483.21| 1,405.44  
consistent gets from cache| 2,490,501,934| 229,820.05| 5,169.38  
consistent gets from cache (fastpath)| 1,999,594,865| 184,519.83| 4,150.43  
cursor authentications| 9,977| 0.92| 0.02  
data blocks consistent reads - undo records applied| 4,863,234| 448.77| 10.09  
db block gets| 29,318,604| 2,705.48| 60.85  
db block gets direct| 110,008| 10.15| 0.23  
db block gets from cache| 29,208,596| 2,695.33| 60.63  
db block gets from cache (fastpath)| 3,985,325| 367.76| 8.27  
deferred (CURRENT) block cleanout applications| 612,173| 56.49| 1.27  
dirty buffers inspected| 10,463| 0.97| 0.02  
drop segment calls in space pressure| 0| 0.00| 0.00  
enqueue conversions| 68,704| 6.34| 0.14  
enqueue deadlocks| 0| 0.00| 0.00  
enqueue releases| 4,886,044| 450.88| 10.14  
enqueue requests| 4,889,929| 451.24| 10.15  
enqueue timeouts| 3,828| 0.35| 0.01  
enqueue waits| 19,222| 1.77| 0.04  
exchange deadlocks| 53| 0.00| 0.00  
failed probes on index block reclamation| 19| 0.00| 0.00  
file io service time| 0| 0.00| 0.00  
frame signature mismatch| 0| 0.00| 0.00  
free buffer inspected| 1,864,493| 172.05| 3.87  
free buffer requested| 3,024,253| 279.07| 6.28  
gc blocks compressed| 403,213| 37.21| 0.84  
gc blocks lost| 0| 0.00| 0.00  
gc cr block flush time| 635| 0.06| 0.00  
gc cr blocks served| 380,884| 35.15| 0.79  
gc current block flush time| 133| 0.01| 0.00  
gc current block pin time| 5| 0.00| 0.00  
gc current blocks served| 317,014| 29.25| 0.66  
gc force cr disk read| 12,622| 1.16| 0.03  
gc kbytes saved| 1,324,782| 122.25| 2.75  
gc kbytes sent| 4,258,403| 392.96| 8.84  
gc local grants| 670,618| 61.88| 1.39  
gc read wait failures| 0| 0.00| 0.00  
gc read wait timeouts| 6| 0.00| 0.00  
gc read waits| 2| 0.00| 0.00  
gc remote grants| 189,288| 17.47| 0.39  
gcs messages sent| 2,806,058| 258.94| 5.82  
ges messages sent| 270,934| 25.00| 0.56  
global enqueue get time| 8,242| 0.76| 0.02  
global enqueue gets async| 6,304| 0.58| 0.01  
global enqueue gets sync| 3,088,860| 285.04| 6.41  
global enqueue releases| 2,776,328| 256.20| 5.76  
global undo segment hints helped| 0| 0.00| 0.00  
global undo segment hints were stale| 0| 0.00| 0.00  
heap block compress| 92,333| 8.52| 0.19  
hot buffers moved to head of LRU| 1,217,717| 112.37| 2.53  
immediate (CR) block cleanout applications| 41,189| 3.80| 0.09  
immediate (CURRENT) block cleanout applications| 138,940| 12.82| 0.29  
index crx upgrade (positioned)| 182,104| 16.80| 0.38  
index crx upgrade (prefetch)| 5,372| 0.50| 0.01  
index fast full scans (full)| 3,117| 0.29| 0.01  
index fetch by key| 303,967,946| 28,049.74| 630.93  
index scans kdiixs1| 45,776,170| 4,224.16| 95.01  
leaf node 90-10 splits| 1,505| 0.14| 0.00  
leaf node splits| 11,531| 1.06| 0.02  
lob reads| 1,463,710| 135.07| 3.04  
lob writes| 928,561| 85.69| 1.93  
lob writes unaligned| 909,440| 83.92| 1.89  
local undo segment hints helped| 0| 0.00| 0.00  
logical read bytes from cache| 20,641,468,219,392| 1,904,765,914.96| 42,844,178.30  
max cf enq hold time| 0| 0.00| 0.00  
messages received| 860,070| 79.37| 1.79  
messages sent| 860,070| 79.37| 1.79  
min active SCN optimization applied on CR| 9,121| 0.84| 0.02  
no buffer to keep pinned count| 93| 0.01| 0.00  
no work - consistent read gets| 2,686,423,550| 247,899.42| 5,576.04  
non-idle wait count| 20,150,566| 1,859.47| 41.83  
parse count (describe)| 9| 0.00| 0.00  
parse count (failures)| 56,638| 5.23| 0.12  
parse count (hard)| 99,663| 9.20| 0.21  
parse time cpu| 22,638| 2.09| 0.05  
physical read IO requests| 13,742,520| 1,268.14| 28.52  
physical read bytes| 5,984,880,197,632| 552,276,402.26| 12,422,433.89  
physical read total IO requests| 15,410,410| 1,422.05| 31.99  
physical read total bytes| 6,031,438,488,576| 556,572,736.45| 12,519,071.96  
physical read total multi block requests| 5,328,569| 491.71| 11.06  
physical reads cache| 440,852| 40.68| 0.92  
physical reads cache prefetch| 39,023| 3.60| 0.08  
physical reads direct| 730,135,342| 67,375.87| 1,515.50  
physical reads direct (lob)| 40,674| 3.75| 0.08  
physical reads direct temporary tablespace| 53,028,423| 4,893.39| 110.07  
physical reads prefetch warmup| 0| 0.00| 0.00  
physical write IO requests| 329,476| 30.40| 0.68  
physical write bytes| 5,056,724,992| 466,627.53| 10,495.92  
physical write total IO requests| 1,221,449| 112.71| 2.54  
physical write total bytes| 23,141,847,040| 2,135,497.39| 48,034.06  
physical write total multi block requests| 35,732| 3.30| 0.07  
physical writes direct| 110,777| 10.22| 0.23  
physical writes direct (lob)| 109,826| 10.13| 0.23  
physical writes direct temporary tablespace| 0| 0.00| 0.00  
physical writes from cache| 506,499| 46.74| 1.05  
physical writes non checkpoint| 499,925| 46.13| 1.04  
pinned buffers inspected| 992| 0.09| 0.00  
pinned cursors current| 22| 0.00| 0.00  
prefetch clients - default| 0| 0.00| 0.00  
prefetch warmup blocks aged out before use| 0| 0.00| 0.00  
prefetch warmup blocks flushed out before use| 0| 0.00| 0.00  
prefetched blocks aged out before use| 0| 0.00| 0.00  
process last non-idle time| 10,834| 1.00| 0.02  
queries parallelized| 57| 0.01| 0.00  
recovery blocks read| 2| 0.00| 0.00  
recursive aborts on index block reclamation| 0| 0.00| 0.00  
recursive calls| 17,452,687| 1,610.51| 36.23  
recursive cpu usage| 188,232| 17.37| 0.39  
redo KB read| 25,448,321| 2,348.34| 52.82  
redo KB read (memory)| 5,656,054| 521.93| 11.74  
redo KB read (memory) for transport| 5,656,054| 521.93| 11.74  
redo KB read for transport| 5,657,240| 522.04| 11.74  
redo blocks checksummed by FG (exclusive)| 3,047,247| 281.20| 6.32  
redo blocks written| 11,535,300| 1,064.46| 23.94  
redo buffer allocation retries| 23| 0.00| 0.00  
redo entries| 12,787,809| 1,180.04| 26.54  
redo log space requests| 27| 0.00| 0.00  
redo ordering marks| 409,187| 37.76| 0.85  
redo size for direct writes| 905,205,532| 83,531.10| 1,878.88  
redo subscn max counts| 13,067| 1.21| 0.03  
redo synch long waits| 2,323| 0.21| 0.00  
redo synch poll writes| 0| 0.00| 0.00  
redo synch polls| 0| 0.00| 0.00  
redo synch time| 25,573| 2.36| 0.05  
redo synch time (usec)| 259,405,130| 23,937.54| 538.43  
redo synch time overhead (usec)| 87,001,741| 8,028.40| 180.58  
redo synch time overhead count (<128 msec)| 58| 0.01| 0.00  
redo synch time overhead count (<2 msec)| 224,066| 20.68| 0.47  
redo synch time overhead count (<32 msec)| 121| 0.01| 0.00  
redo synch time overhead count (<8 msec)| 1,195| 0.11| 0.00  
redo synch time overhead count (>=128 msec)| 41| 0.00| 0.00  
redo synch writes| 225,847| 20.84| 0.47  
redo wastage| 120,394,984| 11,109.88| 249.90  
redo write broadcast ack count| 12,124| 1.12| 0.03  
redo write broadcast ack time| 15,083,347| 1,391.87| 31.31  
redo write broadcast lgwr post count| 1| 0.00| 0.00  
redo write info find| 225,488| 20.81| 0.47  
redo write info find fail| 7| 0.00| 0.00  
redo write time| 39,590| 3.65| 0.08  
redo writes| 416,466| 38.43| 0.86  
remote Oradebug requests| 0| 0.00| 0.00  
rollback changes - undo records applied| 2,092| 0.19| 0.00  
rollbacks only - consistent read gets| 31,460| 2.90| 0.07  
root node splits| 0| 0.00| 0.00  
rows fetched via callback| 223,191,415| 20,595.79| 463.26  
session connect time| 0| 0.00| 0.00  
shared hash latch upgrades - no wait| 20,968,302| 1,934.93| 43.52  
shared hash latch upgrades - wait| 2,427| 0.22| 0.01  
sorts (disk)| 0| 0.00| 0.00  
sorts (memory)| 5,272,231| 486.51| 10.94  
sorts (rows)| 5,563,920,483| 513,430.83| 11,548.67  
space was found by tune down| 0| 0.00| 0.00  
sql area evicted| 98,281| 9.07| 0.20  
sql area purged| 56,699| 5.23| 0.12  
steps of tune down ret. in space pressure| 0| 0.00| 0.00  
summed dirty queue length| 44,203| 4.08| 0.09  
switch current to new buffer| 146,064| 13.48| 0.30  
table fetch by rowid| 4,425,017,400| 408,334.44| 9,184.73  
table fetch continued row| 24,465,084| 2,257.60| 50.78  
table scan blocks gotten| 1,720,916,084| 158,803.74| 3,572.00  
table scan rows gotten| 36,211,002,529| 3,341,500.84| 75,160.87  
table scans (direct read)| 1,108| 0.10| 0.00  
table scans (long tables)| 3| 0.00| 0.00  
table scans (rowid ranges)| 0| 0.00| 0.00  
table scans (short tables)| 803,974| 74.19| 1.67  
temp space allocated (bytes)| 11,534,336| 1,064.37| 23.94  
total cf enq hold time| 7,270| 0.67| 0.02  
total number of cf enq holders| 1,363| 0.13| 0.00  
total number of slots| 0| 0.00| 0.00  
total number of times SMON posted| 2,184| 0.20| 0.00  
transaction lock background gets| 0| 0.00| 0.00  
transaction lock foreground requests| 0| 0.00| 0.00  
transaction rollbacks| 1,652| 0.15| 0.00  
transaction tables consistent read rollbacks| 15| 0.00| 0.00  
transaction tables consistent reads - undo records applied| 8,362| 0.77| 0.02  
tune down retentions in space pressure| 0| 0.00| 0.00  
undo change vector size| 1,869,653,872| 172,529.05| 3,880.72  
user logons cumulative| 7,460| 0.69| 0.02  
user logouts cumulative| 7,401| 0.68| 0.02  
write clones created in background| 735| 0.07| 0.00  
write clones created in foreground| 562| 0.05| 0.00  
  
* * *

Back to Instance Activity Statistics   
Back to Top

### Instance Activity Stats - Absolute Values

  * Statistics with absolute values (should not be diffed)

Statistic| Begin Value| End Value  
---|---|---  
logons current| 493| 560  
opened cursors current| 1,012| 1,054  
session cursor cache count| 1,163,959,863| 1,164,111,678  
session pga memory| 51,038,174,639,424| 51,043,227,057,840  
session pga memory max| 279,853,172,623,680| 279,872,391,403,504  
session uga memory| 16,319,134,530,704| 16,320,823,890,176  
session uga memory max| 296,121,469,428,104| 296,179,324,185,792  
workarea memory allocated| 408,072| 445,861  
  
* * *

Back to Instance Activity Statistics   
Back to Top

### Instance Activity Stats - Thread Activity

  * Statistics identified by '(derived)' come from sources other than SYSSTAT

Statistic| Total| per Hour  
---|---|---  
log switches (derived)| 10| 3.32  
  
* * *

Back to Instance Activity Statistics   
Back to Top

##  IO Stats 

  * IOStat by Function summary
  * IOStat by Filetype summary
  * IOStat by Function/Filetype summary
  * Tablespace IO Stats
  * File IO Stats

Back to Top

### IOStat by Function summary

  * 'Data' columns suffixed with M,G,T,P are in multiples of 1024 other columns suffixed with K,M,G,T,P are in multiples of 1000 
  * ordered by (Data Read + Write) desc

Function Name| Reads: Data| Reqs per sec| Data per sec| Writes: Data| Reqs per sec| Data per sec| Waits: Count| Avg Tm(ms)  
---|---|---|---|---|---|---|---|---  
Direct Reads| 5.4T| 1220.47| 526.258| 0M| 0.00| 0M| 13.2M| 0.47  
Others| 44.2G| 163.65| 4.173M| 5.9G| 3.77| .555M| 1781.1K| 0.03  
LGWR| 3M| 0.02| 0M| 11G| 78.94| 1.04M| 416.8K| 0.33  
DBWR| 0M| 0.00| 0M| 3.9G| 20.47| .365M| 0|   
Buffer Cache Reads| 3.4G| 37.83| .318M| 0M| 0.00| 0M| 404.8K| 0.02  
Direct Writes| 0M| 0.00| 0M| 830M| 9.50| .077M| 98.1K| 0.29  
TOTAL:| 5.5T| 1421.97| 530.749| 21.6G| 112.69| 2.036M| 15.9M| 0.40  
  
* * *

Back to IO Stats   
Back to Top

### IOStat by Filetype summary

  * 'Data' columns suffixed with M,G,T,P are in multiples of 1024 other columns suffixed with K,M,G,T,P are in multiples of 1000 
  * Small Read and Large Read are average service times, in milliseconds 
  * Ordered by (Data Read + Write) desc

Filetype Name| Reads: Data| Reqs per sec| Data per sec| Writes: Data| Reqs per sec| Data per sec| Small Read| Large Read  
---|---|---|---|---|---|---|---|---  
Data File| 5T| 541.74| 488.436| 4.7G| 30.40| .445M| 0.01| 1.08  
Temp File| 404.6G| 726.35| 38.228M| 0M| 0.00| 0M| 0.06|   
Log File| 20.5G| 15.83| 1.937M| 11G| 78.93| 1.04M| 0.01| 1.02  
Control File| 22.9G| 138.07| 2.16M| 486M| 2.87| .045M| 0.01| 2.63  
Archive Log| 0M| 0.00| 0M| 5.4G| 0.51| .507M|  |   
TOTAL:| 5.5T| 1421.99| 530.761| 21.6G| 112.71| 2.037M| 0.05| 1.08  
  
* * *

Back to IO Stats   
Back to Top

### IOStat by Function/Filetype summary

  * 'Data' columns suffixed with M,G,T,P are in multiples of 1024 other columns suffixed with K,M,G,T,P are in multiples of 1000 
  * Ordered by (Data Read + Write) desc for each function

Function/File Name| Reads: Data| Reqs per sec| Data per sec| Writes: Data| Reqs per sec| Data per sec| Waits: Count| Avg Tm(ms)  
---|---|---|---|---|---|---|---|---  
Direct Reads | 5.4T| 1220.49| 526.264| 0M| 0.00| 0M| 0|   
Direct Reads (Data File) | 5.4T| 1220.49| 526.264| 0M| 0.00| 0M| 0|   
Others | 44.2G| 163.65| 4.173M| 5.9G| 3.77| .555M| 1651K| 0.01  
Others (Control File) | 22.9G| 138.06| 2.16M| 483M| 2.85| .045M| 1496.1K| 0.01  
Others (Log File) | 20.5G| 15.82| 1.937M| 0M| 0.00| 0M| 49.1K| 0.10  
Others (Archive Log) | 0M| 0.00| 0M| 5.4G| 0.51| .507M| 0|   
Others (Data File) | 827M| 9.77| .076M| 35M| 0.41| .003M| 105.9K| 0.01  
LGWR | 3M| 0.02| 0M| 11G| 78.96| 1.04M| 260| 0.03  
LGWR (Log File) | 0M| 0.00| 0M| 11G| 78.94| 1.04M| 80| 0.09  
LGWR (Control File) | 3M| 0.02| 0M| 3M| 0.02| 0M| 180| 0.01  
DBWR | 0M| 0.00| 0M| 3.9G| 20.47| .365M| 0|   
DBWR (Data File) | 0M| 0.00| 0M| 3.9G| 20.47| .365M| 0|   
Buffer Cache Reads | 3.4G| 37.83| .318M| 0M| 0.00| 0M| 398.8K| 0.01  
Buffer Cache Reads (Data File) | 3.4G| 37.83| .318M| 0M| 0.00| 0M| 398.8K| 0.01  
Direct Writes | 0M| 0.00| 0M| 830M| 9.50| .077M| 0|   
Direct Writes (Data File) | 0M| 0.00| 0M| 830M| 9.50| .077M| 0|   
TOTAL: | 5.5T| 1421.99| 530.755| 21.6G| 112.70| 2.036M| 2050.1K| 0.01  
  
* * *

Back to IO Stats   
Back to Top

### Tablespace IO Stats

  * ordered by IOs (Reads + Writes) desc

Tablespace| Reads| Av Rds/s| Av Rd(ms)| Av Blks/Rd|  1-bk Rds/s| Av 1-bk Rd(ms)| Writes| Writes avg/s| Buffer Waits| Av Buf Wt(ms)  
---|---|---|---|---|---|---|---|---|---|---  
HISSPACE_TEMP | 7,870,583| 726| 0.00| 6.74| 0| 0.05| 0| 0| 0| 0.00  
WOPB | 5,043,222| 465| 0.00| 126.66| 10,898| 2.65| 0| 1| 129| 10.70  
HISSPACE | 478,612| 44| 0.15| 71.36| 249,892| 19.55| 0| 23| 21,540| 1.25  
USERS | 273,354| 25| 0.33| 16.27| 12,880| 22.14| 0| 1| 33| 2.12  
WDPB | 41,359| 4| 0.37| 1.07| 11,737| 3.81| 0| 1| 159| 3.84  
UNDOTBS2 | 6| 0| 0.00| 1.00| 19,038| 0.00| 0| 2| 928| 0.02  
URM_MT_DATA | 14,353| 1| 0.41| 2.92| 4,462| 1.29| 0| 0| 2,044| 1.70  
WPUB | 4,794| 0| 0.11| 1.31| 5,703| 0.39| 0| 1| 20| 0.50  
SYSAUX | 4,516| 0| 0.39| 1.00| 3,111| 0.42| 0| 0| 0| 0.00  
WDP | 460| 0| 0.43| 1.06| 6,024| 0.04| 0| 1| 0| 0.00  
WIP | 229| 0| 0.39| 1.00| 2,321| 0.02| 0| 0| 0| 0.00  
NDNS | 2,404| 0| 0.39| 1.00| 6| 0.22| 0| 0| 0| 0.00  
SYSTEM | 1,567| 0| 0.39| 1.00| 698| 0.14| 0| 0| 270| 0.04  
MZSF | 1,871| 0| 0.42| 1.00| 6| 0.17| 0| 0| 0| 0.00  
HTHIS | 1,589| 0| 0.42| 1.00| 6| 0.15| 0| 0| 0| 0.00  
WMD | 728| 0| 0.27| 1.16| 454| 0.07| 0| 0| 0| 0.00  
URM | 249| 0| 0.44| 1.07| 843| 0.02| 0| 0| 0| 0.00  
WIPB | 196| 0| 0.36| 1.00| 515| 0.02| 0| 0| 0| 0.00  
YP | 470| 0| 0.38| 1.00| 6| 0.04| 0| 0| 0| 0.00  
WOP | 53| 0| 0.00| 1.00| 404| 0.00| 0| 0| 1| 40.00  
BAS | 28| 0| 0.00| 1.00| 169| 0.00| 0| 0| 0| 0.00  
UNDOTBS1 | 44| 0| 0.23| 1.00| 6| 0.00| 0| 0| 313| 0.22  
URM_TAS | 37| 0| 0.00| 1.00| 12| 0.00| 0| 0| 0| 0.00  
WRP | 34| 0| 0.29| 1.00| 12| 0.00| 0| 0| 0| 0.00  
HT | 21| 0| 0.48| 1.00| 6| 0.00| 0| 0| 0| 0.00  
URM_BED | 13| 0| 0.00| 1.00| 12| 0.00| 0| 0| 0| 0.00  
URM_AUTH | 12| 0| 0.00| 1.00| 12| 0.00| 0| 0| 0| 0.00  
URM_SAS | 12| 0| 0.00| 1.00| 12| 0.00| 0| 0| 0| 0.00  
WIPN | 18| 0| 0.00| 1.00| 6| 0.00| 0| 0| 0| 0.00  
OP | 13| 0| 0.00| 1.00| 6| 0.00| 1| 0| 0| 0.00  
LOGIN | 12| 0| 0.00| 1.00| 6| 0.00| 0| 0| 0| 0.00  
OGG | 6| 0| 0.00| 1.00| 6| 0.00| 0| 0| 0| 0.00  
USER_TEMP | 6| 0| 1.67| 1.00| 0| 0.00| 2| 0| 0| 0.00  
  
* * *

Back to IO Stats   
Back to Top

### File IO Stats

  * ordered by Tablespace, File

Tablespace| Filename| Reads| Av Rds/s| Av Rd(ms)| Av Blks/Rd|  1-bk Rds/s| Av 1-bk Rd(ms)| Writes| Writes avg/s| Buffer Waits| Av Buf Wt(ms)  
---|---|---|---|---|---|---|---|---|---|---|---  
BAS| +DGDATA/orcl/datafile/bas01.ddf | 14| 0| 0.00| 1.00| 0| 0.71| 141| 0| 0| 0.00  
BAS| +DGDATA/orcl/datafile/bas02.ddf | 14| 0| 0.00| 1.00| 0| 0.00| 28| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace001 | 67,884| 6| 0.02| 122.96| 0| 0.45| 2,088| 0| 4| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace002 | 72,256| 7| 0.02| 122.17| 0| 0.45| 2,120| 0| 297| 5.15  
HISSPACE| +DGDATA/orcl/datafile/hisspace003 | 68,726| 6| 0.02| 122.60| 0| 0.45| 2,476| 0| 278| 8.63  
HISSPACE| +DGDATA/orcl/datafile/hisspace004 | 67,883| 6| 0.02| 123.04| 0| 0.44| 3,236| 0| 159| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace005 | 10,973| 1| 0.36| 1.00| 1| 0.36| 9,887| 1| 3| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace006 | 10,389| 1| 0.38| 1.00| 1| 0.38| 8,243| 1| 4| 2.50  
HISSPACE| +DGDATA/orcl/datafile/hisspace007 | 5,934| 1| 0.38| 1.00| 1| 0.38| 6,506| 1| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace008 | 8,088| 1| 0.39| 1.00| 1| 0.38| 7,847| 1| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace009 | 12,877| 1| 0.29| 1.00| 1| 0.29| 11,811| 1| 83| 0.60  
HISSPACE| +DGDATA/orcl/datafile/hisspace010 | 25,103| 2| 0.25| 1.00| 2| 0.25| 20,561| 2| 979| 0.56  
HISSPACE| +DGDATA/orcl/datafile/hisspace011 | 22,351| 2| 0.26| 1.00| 2| 0.26| 18,539| 2| 5| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace012 | 4,273| 0| 0.36| 1.00| 0| 0.36| 6,302| 1| 14| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace013 | 1,393| 0| 0.42| 1.00| 0| 0.42| 1,992| 0| 17| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace014 | 4,506| 0| 0.38| 1.00| 0| 0.38| 4,716| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace015 | 1,550| 0| 0.43| 1.00| 0| 0.43| 2,334| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace016 | 6,115| 1| 0.36| 1.00| 1| 0.36| 7,526| 1| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace017 | 9,655| 1| 0.39| 1.00| 1| 0.39| 8,445| 1| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace018 | 6,759| 1| 0.37| 1.00| 1| 0.37| 6,472| 1| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace019 | 9,021| 1| 0.37| 1.00| 1| 0.37| 8,673| 1| 3| 3.33  
HISSPACE| +DGDATA/orcl/datafile/hisspace020 | 5,109| 0| 0.38| 1.00| 0| 0.38| 4,310| 0| 3| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace021 | 830| 0| 0.46| 1.00| 0| 0.46| 1,298| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace022 | 515| 0| 0.47| 1.00| 0| 0.47| 669| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace023 | 633| 0| 0.46| 1.00| 0| 0.46| 940| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace024 | 702| 0| 0.46| 1.00| 0| 0.46| 1,064| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace025 | 1,138| 0| 0.46| 1.00| 0| 0.45| 1,646| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace026 | 706| 0| 0.45| 1.00| 0| 0.45| 1,036| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace027 | 767| 0| 0.46| 1.00| 0| 0.46| 1,046| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace028 | 771| 0| 0.45| 1.00| 0| 0.45| 1,076| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace029 | 720| 0| 0.46| 1.00| 0| 0.46| 1,278| 0| 1| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace030 | 606| 0| 0.45| 1.00| 0| 0.45| 1,090| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace031 | 807| 0| 0.45| 1.00| 0| 0.46| 1,198| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace032 | 630| 0| 0.46| 1.00| 0| 0.46| 1,012| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace033 | 479| 0| 0.46| 1.00| 0| 0.46| 706| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace034 | 572| 0| 0.45| 1.00| 0| 0.45| 699| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace035 | 663| 0| 0.45| 1.00| 0| 0.44| 1,060| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace036 | 919| 0| 0.47| 1.00| 0| 0.47| 1,383| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace037 | 578| 0| 0.45| 1.00| 0| 0.47| 860| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace038 | 701| 0| 0.46| 1.00| 0| 0.46| 1,003| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace039 | 468| 0| 0.45| 1.00| 0| 0.45| 685| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace040 | 273| 0| 0.44| 1.00| 0| 0.44| 419| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace041 | 464| 0| 0.43| 1.00| 0| 0.45| 585| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace042 | 678| 0| 0.47| 1.00| 0| 0.46| 1,102| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace043 | 937| 0| 0.45| 1.00| 0| 0.45| 1,466| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace044 | 587| 0| 0.44| 1.00| 0| 0.43| 889| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace045 | 742| 0| 0.44| 1.00| 0| 0.44| 1,529| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace046 | 18| 0| 0.00| 1.00| 0| 0.00| 12| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace047 | 722| 0| 0.46| 1.00| 0| 0.46| 1,627| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace048 | 722| 0| 0.46| 1.00| 0| 0.44| 1,264| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace049 | 851| 0| 0.45| 1.00| 0| 0.46| 1,022| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace050 | 817| 0| 0.45| 1.00| 0| 0.45| 1,194| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace051 | 388| 0| 0.44| 1.00| 0| 0.44| 494| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace052 | 584| 0| 0.45| 1.00| 0| 0.45| 866| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace053 | 653| 0| 0.43| 1.00| 0| 0.44| 920| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace054 | 386| 0| 0.44| 1.00| 0| 0.44| 794| 0| 54| 59.26  
HISSPACE| +DGDATA/orcl/datafile/hisspace055 | 463| 0| 0.43| 1.00| 0| 0.43| 897| 0| 8| 1.25  
HISSPACE| +DGDATA/orcl/datafile/hisspace056 | 1,064| 0| 0.43| 1.00| 0| 0.43| 1,726| 0| 6| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace057 | 490| 0| 0.45| 1.00| 0| 0.45| 743| 0| 0| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace058 | 671| 0| 0.45| 1.00| 0| 0.45| 1,024| 0| 11| 0.91  
HISSPACE| +DGDATA/orcl/datafile/hisspace059 | 1,182| 0| 0.45| 1.00| 0| 0.45| 2,654| 0| 8| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace060 | 1,042| 0| 0.45| 1.00| 0| 0.45| 2,582| 0| 12| 6.67  
HISSPACE| +DGDATA/orcl/datafile/hisspace061 | 1,327| 0| 0.44| 1.00| 0| 0.44| 3,072| 0| 35| 0.86  
HISSPACE| +DGDATA/orcl/datafile/hisspace062 | 1,938| 0| 0.44| 1.00| 0| 0.44| 4,375| 0| 45| 18.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace063 | 2,947| 0| 0.44| 1.00| 0| 0.44| 6,224| 1| 19,208| 0.65  
HISSPACE| +DGDATA/orcl/datafile/hisspace064 | 1,571| 0| 0.45| 1.00| 0| 0.44| 2,592| 0| 31| 17.74  
HISSPACE| +DGDATA/orcl/datafile/hisspace065 | 2,397| 0| 0.43| 1.00| 0| 0.43| 4,832| 0| 32| 38.75  
HISSPACE| +DGDATA/orcl/datafile/hisspace066 | 2,142| 0| 0.44| 1.00| 0| 0.44| 5,121| 0| 24| 39.58  
HISSPACE| +DGDATA/orcl/datafile/hisspace067 | 7,918| 1| 0.21| 1.00| 1| 0.21| 10,799| 1| 17| 0.00  
HISSPACE| +DGDATA/orcl/datafile/hisspace068 | 10,588| 1| 0.24| 1.00| 1| 0.24| 25,235| 2| 199| 15.58  
HISSPACE_TEMP| +DGDATA/orcl/datafile/hisspace_temp001 | 7,870,583| 726| 0.00| 6.74| 0| 0.02| 0| 0| 0|   
HT| +DGDATA/orcl/datafile/ht.dbf | 21| 0| 0.48| 1.00| 0| 0.48| 6| 0| 0| 0.00  
HTHIS| +DGDATA/orcl/datafile/hthis.dbf | 1,589| 0| 0.42| 1.00| 0| 0.42| 6| 0| 0| 0.00  
LOGIN| +DGDATA/orcl/datafile/login.dbf | 12| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
MZSF| +DGDATA/orcl/datafile/mzsf.dbf | 1,871| 0| 0.42| 1.00| 0| 0.42| 6| 0| 0| 0.00  
NDNS| +DGDATA/orcl/datafile/ndns.dbf | 2,404| 0| 0.39| 1.00| 0| 0.39| 6| 0| 0| 0.00  
OGG| +DGDATA/orcl/datafile/ogg01.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
OP| +DGDATA/orcl/datafile/op.dbf | 13| 0| 0.00| 1.00| 0| 0.77| 6| 0| 0| 0.00  
SYSAUX| +DGDATA/orcl/datafile/sysaux.261.1062251409 | 4,516| 0| 0.39| 1.00| 0| 0.39| 3,111| 0| 0| 0.00  
SYSTEM| +DGDATA/orcl/datafile/system.275.1062251413 | 1,567| 0| 0.39| 1.00| 0| 0.38| 698| 0| 270| 0.04  
UNDOTBS1| +DGDATA/orcl/datafile/undotbs1.268.1062251409 | 44| 0| 0.23| 1.00| 0| 0.23| 6| 0| 313| 0.22  
UNDOTBS2| +DGDATA/orcl/datafile/undotbs2.271.1062251411 | 6| 0| 0.00| 1.00| 0| 0.00| 19,038| 2| 928| 0.02  
URM| +DGDATA/orcl/datafile/urm01.ora | 105| 0| 0.48| 1.04| 0| 0.48| 430| 0| 0| 0.00  
URM| +DGDATA/orcl/datafile/urm02.ora | 144| 0| 0.42| 1.09| 0| 0.42| 413| 0| 0| 0.00  
URM_AUTH| +DGDATA/orcl/datafile/urm_auth01.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_AUTH| +DGDATA/orcl/datafile/urm_auth02.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_BED| +DGDATA/orcl/datafile/urm_bed01.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_BED| +DGDATA/orcl/datafile/urm_bed02.dbf | 7| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_MT_DATA| +DGDATA/orcl/datafile/urm_mt.dbf | 14,353| 1| 0.41| 2.92| 1| 0.37| 4,462| 0| 2,044| 1.70  
URM_SAS| +DGDATA/orcl/datafile/urm_sas01.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_SAS| +DGDATA/orcl/datafile/urm_sas02.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_TAS| +DGDATA/orcl/datafile/urm_tas01.dbf | 19| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
URM_TAS| +DGDATA/orcl/datafile/urm_tas02.dbf | 18| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
USERS| +DGDATA/orcl/datafile/users.276.1062251413 | 28,014| 3| 0.31| 18.79| 2| 0.37| 762| 0| 0| 0.00  
USERS| +DGDATA/orcl/datafile/users02.dbf | 228,415| 21| 0.33| 15.82| 19| 0.38| 8,380| 1| 27| 2.22  
USERS| +DGDATA/orcl/datafile/users03.dbf | 16,925| 2| 0.32| 18.09| 1| 0.37| 3,738| 0| 6| 1.67  
USER_TEMP| +DGDATA/orcl/datafile/user_temp.dbf | 6| 0| 1.67| 1.00| 0| 1.67| 0| 0| 0|   
WDP| +DGDATA/orcl/datafile/wdp01.dbf | 22| 0| 0.45| 1.59| 0| 0.50| 7| 0| 0| 0.00  
WDP| +DGDATA/orcl/datafile/wdp02.dbf | 26| 0| 0.38| 1.42| 0| 0.00| 1,546| 0| 0| 0.00  
WDP| +DGDATA/orcl/datafile/wdp03.dbf | 412| 0| 0.44| 1.01| 0| 0.41| 4,471| 0| 0| 0.00  
WDPB| +DGDATA/orcl/datafile/wdpb01.dbf | 61| 0| 0.33| 1.02| 0| 0.17| 29| 0| 2| 10.00  
WDPB| +DGDATA/orcl/datafile/wdpb02.dbf | 95| 0| 0.21| 1.00| 0| 0.32| 752| 0| 2| 20.00  
WDPB| +DGDATA/orcl/datafile/wdpb03.dbf | 1,386| 0| 0.06| 1.18| 0| 0.04| 2,053| 0| 39| 4.10  
WDPB| +DGDATA/orcl/datafile/wdpb04.dbf | 148| 0| 0.07| 1.00| 0| 0.07| 17| 0| 2| 5.00  
WDPB| +DGDATA/orcl/datafile/wdpb05.dbf | 281| 0| 0.04| 1.00| 0| 0.07| 30| 0| 6| 5.00  
WDPB| +DGDATA/orcl/datafile/wdpb06.dbf | 39,388| 4| 0.38| 1.06| 4| 0.38| 8,856| 1| 108| 3.24  
WIP| +DGDATA/orcl/datafile/wib01.dbf | 79| 0| 0.38| 1.00| 0| 0.38| 1,020| 0| 0| 0.00  
WIP| +DGDATA/orcl/datafile/wib02.dbf | 49| 0| 0.41| 1.00| 0| 0.41| 823| 0| 0| 0.00  
WIP| +DGDATA/orcl/datafile/wib03.dbf | 101| 0| 0.40| 1.00| 0| 0.40| 478| 0| 0| 0.00  
WIPB| +DGDATA/orcl/datafile/wipb01.dbf | 7| 0| 0.00| 1.00| 0| 0.00| 7| 0| 0| 0.00  
WIPB| +DGDATA/orcl/datafile/wipb02.dbf | 6| 0| 0.00| 1.00| 0| 0.00| 13| 0| 0| 0.00  
WIPB| +DGDATA/orcl/datafile/wipb03.dbf | 183| 0| 0.38| 1.00| 0| 0.44| 495| 0| 0| 0.00  
WIPN| +DGDATA/orcl/datafile/wipn01.ora | 18| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
WMD| +DGDATA/orcl/datafile/wmd01.ora | 637| 0| 0.25| 1.18| 0| 0.24| 296| 0| 0| 0.00  
WMD| +DGDATA/orcl/datafile/wmd02.ora | 91| 0| 0.44| 1.04| 0| 0.44| 158| 0| 0| 0.00  
WOP| +DGDATA/orcl/datafile/wop01.dbf | 24| 0| 0.00| 1.00| 0| 0.00| 227| 0| 1| 40.00  
WOP| +DGDATA/orcl/datafile/wop02.dbf | 16| 0| 0.00| 1.00| 0| 0.63| 169| 0| 0| 0.00  
WOP| +DGDATA/orcl/datafile/wop03.dbf | 13| 0| 0.00| 1.00| 0| 0.00| 8| 0| 0| 0.00  
WOPB| +DGDATA/orcl/datafile/wopb01.dbf | 1,499,049| 138| 0.00| 127.07| 0| 0.43| 396| 0| 1| 0.00  
WOPB| +DGDATA/orcl/datafile/wopb02.dbf | 210,530| 19| 0.00| 123.65| 0| 0.29| 99| 0| 0| 0.00  
WOPB| +DGDATA/orcl/datafile/wopb03.dbf | 1,437,339| 133| 0.00| 127.57| 0| 0.41| 306| 0| 1| 0.00  
WOPB| +DGDATA/orcl/datafile/wopb04.dbf | 1,049,563| 97| 0.01| 126.16| 1| 0.40| 5,568| 1| 16| 46.88  
WOPB| +DGDATA/orcl/datafile/wopb05.dbf | 846,741| 78| 0.01| 125.75| 1| 0.40| 4,529| 0| 111| 5.68  
WPUB| +DGDATA/orcl/datafile/wpub01.dbf | 147| 0| 0.41| 1.00| 0| 0.41| 740| 0| 3| 0.00  
WPUB| +DGDATA/orcl/datafile/wpub02.dbf | 155| 0| 0.45| 1.00| 0| 0.39| 1,128| 0| 1| 0.00  
WPUB| +DGDATA/orcl/datafile/wpub03.dbf | 164| 0| 0.18| 1.24| 0| 0.24| 413| 0| 2| 0.00  
WPUB| +DGDATA/orcl/datafile/wpub04.dbf | 4,328| 0| 0.09| 1.34| 0| 0.10| 3,422| 0| 14| 0.71  
WRP| +DGDATA/orcl/datafile/wrp01.ora | 18| 0| 0.56| 1.00| 0| 0.00| 6| 0| 0| 0.00  
WRP| +DGDATA/orcl/datafile/wrp02.ora | 16| 0| 0.00| 1.00| 0| 0.00| 6| 0| 0| 0.00  
YP| +DGDATA/orcl/datafile/yp.dbf | 470| 0| 0.38| 1.00| 0| 0.40| 6| 0| 0| 0.00  
  
* * *

Back to IO Stats   
Back to Top

##  Buffer Pool Statistics 

  * Buffer Pool Statistics
  * Checkpoint Activity

Back to Top

### Buffer Pool Statistics

  * Standard block size Pools D: default, K: keep, R: recycle 
  * Default Pools for other block sizes: 2k, 4k, 8k, 16k, 32k

P| Number of Buffers| Pool Hit%| Buffer Gets| Physical Reads| Physical Writes| Free Buff Wait| Writ Comp Wait| Buffer Busy Waits  
---|---|---|---|---|---|---|---|---  
D| 14,457,590| 100| 2,518,552,117| 440,852| 506,496| 0| 0| 25,442  
  
* * *

Back to Buffer Pool Statistics   
Back to Top

### Checkpoint Activity

  * Total Physical Writes: 617,276

MTTR Writes| Log Size Writes| Log Ckpt Writes| Other Settings Writes| Autotune Ckpt Writes| Thread Ckpt Writes  
---|---|---|---|---|---  
0| 0| 0| 0| 388,740| 0  
  
* * *

Back to Buffer Pool Statistics   
Back to Top

##  Advisory Statistics 

  * Instance Recovery Stats
  * MTTR Advisory
  * Buffer Pool Advisory
  * PGA Aggr Summary
  * PGA Aggr Target Stats
  * PGA Aggr Target Histogram
  * PGA Memory Advisory
  * Shared Pool Advisory
  * SGA Target Advisory
  * Streams Pool Advisory
  * Java Pool Advisory

Back to Top

### Instance Recovery Stats

  * B: Begin Snapshot, E: End Snapshot

| Targt MTTR (s) | Estd MTTR (s)| Recovery Estd IOs| Actual RedoBlks| Target RedoBlks| Log Sz RedoBlks| Log Ckpt Timeout RedoBlks| Log Ckpt Interval RedoBlks| Opt Log Sz(M)| Estd RAC Avail Time  
---|---|---|---|---|---|---|---|---|---|---  
B| 0| 1| 3441| 53865| 255231| 11890800| 255231|  |  | 0  
E| 0| 8| 22287| 576571| 3666414| 11890800| 3666414|  |  | 3  
  
* * *

Back to Advisory Statistics   
Back to Top

### MTTR Advisory

No data exists for this section of the report. 

Back to Advisory Statistics   
Back to Top

### Buffer Pool Advisory

  * Only rows with estimated physical reads >0 are displayed 
  * ordered by Block Size, Buffers For Estimate

P| Size for Est (M)| Size Factor| Buffers (thousands)| Est Phys Read Factor| Estimated Phys Reads (thousands)| Est Phys Read Time| Est %DBtime for Rds  
---|---|---|---|---|---|---|---  
D| 12,288| 0.10| 1,440| 58.48| 633,373,252| 1| 252728434.00  
D| 24,576| 0.20| 2,880| 8.99| 97,318,534| 1| 37769282.00  
D| 36,864| 0.30| 4,319| 4.25| 46,076,406| 1| 17221069.00  
D| 49,152| 0.40| 5,759| 2.93| 31,775,805| 1| 11486496.00  
D| 61,440| 0.50| 7,199| 2.13| 23,056,530| 1| 7990048.00  
D| 73,728| 0.60| 8,639| 1.70| 18,427,852| 1| 6133937.00  
D| 86,016| 0.69| 10,078| 1.44| 15,634,927| 1| 5013967.00  
D| 98,304| 0.79| 11,518| 1.26| 13,696,349| 1| 4236593.00  
D| 110,592| 0.89| 12,958| 1.12| 12,152,311| 1| 3617430.00  
D| 122,880| 0.99| 14,398| 1.01| 10,906,388| 1| 3117812.00  
D| 123,904| 1.00| 14,518| 1.00| 10,829,961| 1| 3087165.00  
D| 135,168| 1.09| 15,837| 0.92| 9,977,925| 1| 2745496.00  
D| 147,456| 1.19| 17,277| 0.86| 9,361,701| 1| 2498389.00  
D| 159,744| 1.29| 18,717| 0.83| 8,977,101| 1| 2344163.00  
D| 172,032| 1.39| 20,157| 0.81| 8,742,860| 1| 2250232.00  
D| 184,320| 1.49| 21,596| 0.79| 8,572,594| 1| 2181955.00  
D| 196,608| 1.59| 23,036| 0.78| 8,459,514| 1| 2136610.00  
D| 208,896| 1.69| 24,476| 0.77| 8,391,301| 1| 2109257.00  
D| 221,184| 1.79| 25,916| 0.76| 8,258,507| 1| 2056006.00  
D| 233,472| 1.88| 27,355| 0.69| 7,460,981| 1| 1736196.00  
D| 245,760| 1.98| 28,795| 0.40| 4,383,178| 1| 501990.00  
  
* * *

Back to Advisory Statistics   
Back to Top

### PGA Aggr Summary

  * PGA cache hit % - percentage of W/A (WorkArea) data processed only in-memory

PGA Cache Hit %| W/A MB Processed| Extra W/A MB Read/Written  
---|---|---  
100.00| 599,119| 0  
  
* * *

Back to Advisory Statistics   
Back to Top

### PGA Aggr Target Stats

  * B: Begin Snap E: End Snap (rows dentified with B or E contain data which is absolute i.e. not diffed over the interval) 
  * Auto PGA Target - actual workarea memory target 
  * W/A PGA Used - amount of memory used for all Workareas (manual + auto) 
  * %PGA W/A Mem - percentage of PGA memory allocated to workareas 
  * %Auto W/A Mem - percentage of workarea memory controlled by Auto Mem Mgmt 
  * %Man W/A Mem - percentage of workarea memory under manual control

| PGA Aggr Target(M)| Auto PGA Target(M)| PGA Mem Alloc(M) | W/A PGA Used(M) | %PGA W/A Mem| %Auto W/A Mem| %Man W/A Mem| Global Mem Bound(K)  
---|---|---|---|---|---|---|---|---  
B| 51,200| 44,401| 3,843.09| 398.04| 10.36| 100.00| 0.00| 1,048,576  
E| 51,200| 44,270| 4,122.70| 434.73| 10.54| 100.00| 0.00| 1,048,576  
  
* * *

Back to Advisory Statistics   
Back to Top

### PGA Aggr Target Histogram

  * Optimal Executions are purely in-memory operations

Low Optimal|  High Optimal| Total Execs| Optimal Execs| 1-Pass Execs| M-Pass Execs  
---|---|---|---|---|---  
2K| 4K| 2,873,700| 2,873,700| 0| 0  
64K| 128K| 5,837| 5,837| 0| 0  
128K| 256K| 489,095| 489,095| 0| 0  
256K| 512K| 235,078| 235,078| 0| 0  
512K| 1024K| 49,225| 49,225| 0| 0  
1M| 2M| 34,907| 34,907| 0| 0  
2M| 4M| 6,044| 6,044| 0| 0  
4M| 8M| 1,455| 1,455| 0| 0  
8M| 16M| 171| 171| 0| 0  
16M| 32M| 52| 52| 0| 0  
32M| 64M| 144| 144| 0| 0  
64M| 128M| 3,680| 3,680| 0| 0  
  
* * *

Back to Advisory Statistics   
Back to Top

### PGA Memory Advisory

  * When using Auto Memory Mgmt, minimally choose a pga_aggregate_target value where Estd PGA Overalloc Count is 0

PGA Target Est (MB)| Size Factr| W/A MB Processed| Estd Extra W/A MB Read/ Written to Disk | Estd PGA Cache Hit %| Estd PGA Overalloc Count| Estd Time  
---|---|---|---|---|---|---  
6,400| 0.13| 3,696,323,741.00| 431,394,113.80| 90.00| 991| 80,414,100,134  
12,800| 0.25| 3,696,323,741.00| 430,640,448.17| 90.00| 739| 80,399,417,603  
25,600| 0.50| 3,696,323,741.00| 430,465,941.97| 90.00| 0| 80,396,017,962  
38,400| 0.75| 3,696,323,741.00| 430,465,941.97| 90.00| 0| 80,396,017,962  
51,200| 1.00| 3,696,323,741.00| 424,942,084.34| 90.00| 0| 80,288,404,977  
61,440| 1.20| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
71,680| 1.40| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
81,920| 1.60| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
92,160| 1.80| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
102,400| 2.00| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
153,600| 3.00| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
204,800| 4.00| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
307,200| 6.00| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
409,600| 8.00| 3,696,323,741.00| 423,782,448.16| 90.00| 0| 80,265,813,535  
  
* * *

Back to Advisory Statistics   
Back to Top

### Shared Pool Advisory

  * SP: Shared Pool Est LC: Estimated Library Cache Factr: Factor 
  * Note there is often a 1:Many correlation between a single logical object in the Library Cache, and the physical number of memory objects associated with it. Therefore comparing the number of Lib Cache objects (e.g. in v$librarycache), with the number of Lib Cache Memory Objects is invalid.

Shared Pool Size(M)| SP Size Factr| Est LC Size (M)| Est LC Mem Obj| Est LC Time Saved (s)| Est LC Time Saved Factr| Est LC Load Time (s)| Est LC Load Time Factr| Est LC Mem Obj Hits (K)  
---|---|---|---|---|---|---|---|---  
19,968| 0.89| 1,265| 54,260| 208,023,400| 1.00| 4,962,133| 1.07| 2,014,500  
20,480| 0.91| 1,777| 67,319| 208,072,183| 1.00| 4,913,350| 1.06| 2,023,799  
20,992| 0.93| 2,289| 80,476| 208,090,053| 1.00| 4,895,480| 1.05| 2,026,663  
21,504| 0.95| 2,801| 93,794| 208,102,893| 1.00| 4,882,640| 1.05| 2,028,724  
22,016| 0.98| 3,313| 107,829| 208,165,728| 1.00| 4,819,805| 1.04| 2,039,232  
22,528| 1.00| 3,825| 120,778| 208,338,479| 1.00| 4,647,054| 1.00| 2,106,903  
23,040| 1.02| 4,336| 133,692| 208,343,840| 1.00| 4,641,693| 1.00| 2,108,536  
23,552| 1.05| 4,848| 146,917| 208,348,215| 1.00| 4,637,318| 1.00| 2,109,919  
24,064| 1.07| 5,360| 160,220| 208,352,304| 1.00| 4,633,229| 1.00| 2,111,178  
24,576| 1.09| 5,872| 173,450| 208,356,130| 1.00| 4,629,403| 1.00| 2,112,335  
25,088| 1.11| 6,384| 186,448| 208,359,621| 1.00| 4,625,912| 1.00| 2,113,375  
25,600| 1.14| 6,896| 199,616| 208,362,718| 1.00| 4,622,815| 0.99| 2,114,327  
26,112| 1.16| 7,408| 212,721| 208,365,581| 1.00| 4,619,952| 0.99| 2,115,224  
26,624| 1.18| 7,920| 226,133| 208,368,308| 1.00| 4,617,225| 0.99| 2,116,073  
27,136| 1.20| 8,432| 239,957| 208,370,904| 1.00| 4,614,629| 0.99| 2,116,889  
27,648| 1.23| 8,944| 253,850| 208,373,358| 1.00| 4,612,175| 0.99| 2,117,661  
30,208| 1.34| 11,504| 322,105| 208,383,344| 1.00| 4,602,189| 0.99| 2,120,720  
32,768| 1.45| 14,064| 386,982| 208,391,205| 1.00| 4,594,328| 0.99| 2,123,109  
35,328| 1.57| 16,624| 454,221| 208,398,649| 1.00| 4,586,884| 0.99| 2,125,293  
37,888| 1.68| 19,184| 519,465| 208,405,092| 1.00| 4,580,441| 0.99| 2,127,085  
40,448| 1.80| 21,744| 585,948| 208,410,671| 1.00| 4,574,862| 0.98| 2,128,634  
43,008| 1.91| 24,304| 652,708| 208,415,724| 1.00| 4,569,809| 0.98| 2,130,026  
45,568| 2.02| 26,864| 719,693| 208,420,069| 1.00| 4,565,464| 0.98| 2,131,228  
  
* * *

Back to Advisory Statistics   
Back to Top

### SGA Target Advisory


SGA Target Size (M)| SGA Size Factor| Est DB Time (s)| Est Physical Reads  
---|---|---|---  
38,400| 0.25| 440,164,500| 687,458,839,983  
48,000| 0.31| 225,062,774| 105,628,940,174  
57,600| 0.38| 224,778,173| 105,628,940,174  
67,200| 0.44| 204,192,006| 50,010,593,222  
76,800| 0.50| 198,462,032| 34,489,093,329  
86,400| 0.56| 194,970,921| 25,025,873,537  
96,000| 0.63| 193,130,499| 20,001,854,698  
105,600| 0.69| 192,257,722| 16,970,548,655  
115,200| 0.75| 191,954,147| 16,970,548,655  
124,800| 0.81| 191,195,211| 14,866,287,262  
134,400| 0.88| 190,569,088| 13,189,809,322  
144,000| 0.94| 190,075,779| 11,754,839,509  
153,600| 1.00| 189,734,256| 10,829,960,852  
163,200| 1.06| 189,696,310| 10,829,960,852  
172,800| 1.13| 189,449,656| 10,160,669,271  
182,400| 1.19| 189,297,868| 9,743,715,779  
192,000| 1.25| 189,203,001| 9,489,211,699  
201,600| 1.31| 189,165,054| 9,305,102,364  
211,200| 1.38| 189,108,134| 9,305,102,364  
220,800| 1.44| 189,070,187| 9,181,640,810  
230,400| 1.50| 189,051,214| 9,181,640,810  
240,000| 1.56| 189,013,267| 8,963,958,597  
249,600| 1.63| 188,690,719| 8,097,561,729  
259,200| 1.69| 187,476,419| 4,757,601,802  
268,800| 1.75| 187,438,472| 4,757,601,802  
278,400| 1.81| 187,400,526| 4,757,601,802  
288,000| 1.88| 187,400,526| 4,757,601,802  
297,600| 1.94| 187,400,526| 4,757,601,802  
307,200| 2.00| 187,400,526| 4,757,601,802  
  
* * *

Back to Advisory Statistics   
Back to Top

### Streams Pool Advisory


Size for Est (MB)| Size Factor| Est Spill Count| Est Spill Time (s)| Est Unspill Count| Est Unspill Time (s)  
---|---|---|---|---|---  
512| 0.50| 0| 0| 0| 0  
1,024| 1.00| 0| 0| 0| 0  
1,536| 1.50| 0| 0| 0| 0  
2,048| 2.00| 0| 0| 0| 0  
2,560| 2.50| 0| 0| 0| 0  
3,072| 3.00| 0| 0| 0| 0  
3,584| 3.50| 0| 0| 0| 0  
4,096| 4.00| 0| 0| 0| 0  
4,608| 4.50| 0| 0| 0| 0  
5,120| 5.00| 0| 0| 0| 0  
5,632| 5.50| 0| 0| 0| 0  
6,144| 6.00| 0| 0| 0| 0  
6,656| 6.50| 0| 0| 0| 0  
7,168| 7.00| 0| 0| 0| 0  
7,680| 7.50| 0| 0| 0| 0  
8,192| 8.00| 0| 0| 0| 0  
8,704| 8.50| 0| 0| 0| 0  
9,216| 9.00| 0| 0| 0| 0  
9,728| 9.50| 0| 0| 0| 0  
10,240| 10.00| 0| 0| 0| 0  
  
* * *

Back to Advisory Statistics   
Back to Top

### Java Pool Advisory


Java Pool Size(M)| JP Size Factr| Est LC Size (M)| Est LC Mem Obj| Est LC Time Saved (s)| Est LC Time Saved Factr| Est LC Load Time (s)| Est LC Load Time Factr| Est LC Mem Obj Hits  
---|---|---|---|---|---|---|---|---  
512| 0.14| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
1,024| 0.29| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
1,536| 0.43| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
2,048| 0.57| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
2,560| 0.71| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
3,072| 0.86| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
3,584| 1.00| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
4,096| 1.14| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
4,608| 1.29| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
5,120| 1.43| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
5,632| 1.57| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
6,144| 1.71| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
6,656| 1.86| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
7,168| 2.00| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
7,680| 2.14| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
8,192| 2.29| 4| 112| 5| 1.00| 4,647,054| 1.00| 81  
  
* * *

Back to Advisory Statistics   
Back to Top

##  Wait Statistics 

  * Buffer Wait Statistics
  * Enqueue Activity

Back to Top

### Buffer Wait Statistics

  * ordered by wait time desc, waits desc

Class| Waits| Total Wait Time (s)| Avg Time (ms)  
---|---|---|---  
data block| 24,186| 33| 1  
undo block| 1,142| 0| 0  
undo header| 99| 0| 0  
1st level bmb| 9| 0| 0  
2nd level bmb| 2| 0| 0  
segment header| 2| 0| 0  
  
* * *

Back to Wait Statistics   
Back to Top

### Enqueue Activity

  * only enqueues with waits are shown 
  * Enqueue stats gathered prior to 10g should not be compared with 10g data 
  * ordered by Wait Time desc, Waits desc

Enqueue Type (Request Reason)| Requests| Succ Gets| Failed Gets| Waits| Wt Time (s)| Av Wt Time(ms)  
---|---|---|---|---|---|---  
TX-Transaction (row lock contention) | 191| 190| 0| 191| 18| 95.55  
TX-Transaction (index contention) | 592| 592| 0| 580| 5| 8.47  
WF-AWR Flush | 126| 126| 0| 114| 5| 40.44  
KO-Multiple Object Checkpoint (fast object checkpoint) | 11,264| 11,264| 0| 2,460| 4| 1.53  
HW-Segment High Water Mark | 89,102| 88,941| 161| 8,249| 3| 0.36  
CF-Controlfile Transaction | 33,237| 33,235| 2| 1,100| 1| 0.69  
CO-KTUCLO Master Slave enq (master slave det) | 3,603| 0| 3,603| 3,603| 1| 0.16  
JQ-Job Queue | 2,004| 1,939| 59| 774| 1| 0.76  
RO-Multiple Object Reuse (fast object reuse) | 2,178| 2,178| 0| 609| 0| 0.76  
TM-DML | 613,789| 613,796| 0| 20| 0| 19.50  
FB-Format Block | 1,278| 1,278| 0| 520| 0| 0.21  
TT-Tablespace | 1,806| 1,806| 0| 447| 0| 0.22  
PS-PX Process Reservation | 402| 402| 0| 160| 0| 0.38  
TA-Instance Undo | 71| 71| 0| 71| 0| 0.42  
US-Undo Segment | 357| 357| 0| 151| 0| 0.13  
JI-Materialized View | 56| 56| 0| 18| 0| 1.11  
MS-Materialized View Refresh Log | 252| 252| 0| 72| 0| 0.14  
SQ-Sequence Cache | 1,916| 1,916| 0| 27| 0| 0.37  
UL-User-defined | 10| 10| 0| 7| 0| 1.43  
WL-Being Written Redo Log | 10| 10| 0| 5| 0| 2.00  
TX-Transaction | 593,690| 593,692| 0| 2| 0| 5.00  
FU-DBFUS | 1| 1| 0| 1| 0| 10.00  
PI-Remote PX Process Spawn Status | 26| 26| 0| 8| 0| 0.00  
MW-MWIN Schedule | 6| 6| 0| 6| 0| 0.00  
PW-Buffer Cache PreWarm (flush prewarm buffers) | 6| 6| 0| 6| 0| 0.00  
WR-LNS archiving log | 10| 10| 0| 5| 0| 0.00  
CR-Reuse Block Range (block range reuse ckpt) | 3,852| 3,852| 0| 4| 0| 0.00  
AF-Advisor Framework (task serialization) | 42| 42| 0| 3| 0| 0.00  
JS-Job Scheduler (job run lock - synchronize) | 6| 6| 0| 3| 0| 0.00  
TX-Transaction (allocate ITL entry) | 3| 3| 0| 3| 0| 0.00  
TD-KTF map table enqueue (KTF dump entries) | 36| 36| 0| 1| 0| 0.00  
  
* * *

Back to Wait Statistics   
Back to Top

##  Undo Statistics 

  * Undo Segment Summary
  * Undo Segment Stats

Back to Top

### Undo Segment Summary

  * Min/Max TR (mins) - Min and Max Tuned Retention (minutes) 
  * STO - Snapshot Too Old count, OOS - Out of Space count 
  * Undo segment block stats: 
  * uS - unexpired Stolen, uR - unexpired Released, uU - unexpired reUsed 
  * eS - expired Stolen, eR - expired Released, eU - expired reUsed

Undo TS#| Num Undo Blocks (K)| Number of Transactions| Max Qry Len (s)| Max Tx Concurcy| Min/Max TR (mins)| STO/ OOS|  uS/uR/uU/ eS/eR/eU  
---|---|---|---|---|---|---|---  
5| 245.70| 591,325| 28,778| 11| 321.1/478.6| 0/0| 0/0/0/0/0/0  
  
* * *

Back to Undo Statistics   
Back to Top

### Undo Segment Stats

  * Most recent 35 Undostat rows, ordered by Time desc

End Time| Num Undo Blocks| Number of Transactions| Max Qry Len (s)| Max Tx Concy| Tun Ret (mins)| STO/ OOS|  uS/uR/uU/ eS/eR/eU  
---|---|---|---|---|---|---|---  
20-Jan 11:00| 28,379| 36,219| 28,778| 10| 479| 0/0| 0/0/0/0/0/0  
20-Jan 10:50| 33,281| 44,970| 28,176| 9| 474| 0/0| 0/0/0/0/0/0  
20-Jan 10:40| 29,628| 45,223| 27,574| 8| 470| 0/0| 0/0/0/0/0/0  
20-Jan 10:30| 30,086| 46,500| 26,972| 8| 461| 0/0| 0/0/0/0/0/0  
20-Jan 10:20| 29,536| 51,147| 26,370| 9| 451| 0/0| 0/0/0/0/0/0  
20-Jan 10:10| 30,054| 46,599| 25,768| 10| 440| 0/0| 0/0/0/0/0/0  
20-Jan 10:00| 30,179| 48,614| 25,167| 10| 430| 0/0| 0/0/0/0/0/0  
20-Jan 09:50| 3,784| 34,097| 24,565| 8| 420| 0/0| 0/0/0/0/0/0  
20-Jan 09:40| 3,893| 30,667| 23,963| 8| 410| 0/0| 0/0/0/0/0/0  
20-Jan 09:30| 3,857| 24,308| 23,361| 9| 400| 0/0| 0/0/0/0/0/0  
20-Jan 09:20| 3,274| 20,214| 22,759| 8| 390| 0/0| 0/0/0/0/0/0  
20-Jan 09:10| 2,802| 18,631| 22,157| 9| 380| 0/0| 0/0/0/0/0/0  
20-Jan 09:00| 2,979| 25,897| 21,556| 9| 370| 0/0| 0/0/0/0/0/0  
20-Jan 08:50| 3,123| 27,478| 20,954| 11| 360| 0/0| 0/0/0/0/0/0  
20-Jan 08:40| 3,593| 30,530| 20,351| 10| 350| 0/0| 0/0/0/0/0/0  
20-Jan 08:30| 2,315| 20,670| 19,750| 11| 340| 0/0| 0/0/0/0/0/0  
20-Jan 08:20| 2,549| 20,705| 19,148| 9| 331| 0/0| 0/0/0/0/0/0  
20-Jan 08:10| 2,387| 18,856| 18,546| 10| 321| 0/0| 0/0/0/0/0/0  
  
* * *

Back to Undo Statistics   
Back to Top

##  Latch Statistics 

  * Latch Activity
  * Latch Sleep Breakdown
  * Latch Miss Sources
  * Mutex Sleep Summary
  * Parent Latch Statistics
  * Child Latch Statistics

Back to Top

### Latch Activity

  * "Get Requests", "Pct Get Miss" and "Avg Slps/Miss" are statistics for willing-to-wait latch get requests 
  * "NoWait Requests", "Pct NoWait Miss" are for no-wait latch get requests 
  * "Pct Misses" for both should be very close to 0.0

Latch Name| Get Requests| Pct Get Miss| Avg Slps /Miss| Wait Time (s)| NoWait Requests| Pct NoWait Miss  
---|---|---|---|---|---|---  
AQ deq hash table latch| 6| 0.00|  | 0| 0|   
ASM Keyed state latch| 15,198| 0.30| 0.00| 0| 0|   
ASM allocation| 91,028| 0.00|  | 0| 0|   
ASM db client latch| 25,977| 0.00|  | 0| 0|   
ASM map headers| 103,305| 0.00|  | 0| 0|   
ASM map load waiting list| 29,495| 0.00|  | 0| 0|   
ASM map operation freelist| 5,278| 0.00|  | 0| 0|   
ASM map operation hash table| 67,309,822| 0.00| 0.00| 0| 0|   
ASM network SGA latch| 30| 0.00|  | 0| 0|   
ASM network background latch| 156,328| 0.00|  | 0| 0|   
ASM network state latch| 32,439| 0.00|  | 0| 0|   
ASM scan context latch| 40| 0.00|  | 0| 0|   
AWR Alerted Metric Element list| 179,753| 0.00|  | 0| 0|   
Change Notification Hash table latch| 3,609| 0.00|  | 0| 0|   
Consistent RBA| 417,929| 0.02| 0.00| 0| 0|   
DML lock allocation| 1,228,004| 0.00| 0.00| 0| 0|   
Event Group Locks| 17,321| 0.00|  | 0| 0|   
FAL Queue| 635| 0.00|  | 0| 0|   
FIB s.o chain latch| 29,496| 0.00|  | 0| 0|   
FOB s.o list latch| 71,462| 0.06| 0.00| 0| 0|   
File State Object Pool Parent Latch| 6| 0.00|  | 0| 0|   
I/O Staticstics latch| 6| 0.00|  | 0| 0|   
IPC other latch| 97| 0.00|  | 0| 0|   
IPC stats buffer allocation latch| 25,973| 0.00|  | 0| 26,205| 0.02  
In memory undo latch| 6| 0.00|  | 0| 0|   
JS Sh mem access| 24| 0.00|  | 0| 0|   
JS broadcast add buf latch| 54,513| 0.00|  | 0| 0|   
JS broadcast drop buf latch| 54,516| 0.00|  | 0| 0|   
JS broadcast load blnc latch| 54,111| 0.00|  | 0| 0|   
JS mem alloc latch| 18| 0.00|  | 0| 0|   
JS queue access latch| 24| 0.00|  | 0| 0|   
JS queue state obj latch| 1,950,792| 0.00|  | 0| 0|   
JS slv state obj latch| 169| 0.00|  | 0| 0|   
KFC FX Hash Latch| 6| 0.00|  | 0| 0|   
KFC Hash Latch| 6| 0.00|  | 0| 0|   
KFCL LE Freelist| 6| 0.00|  | 0| 0|   
KFK SGA Libload latch| 30| 0.00|  | 0| 0|   
KFMD SGA| 48| 0.00|  | 0| 0|   
KGNFS-NFS:SHM structure| 6| 0.00|  | 0| 0|   
KGNFS-NFS:SVR LIST| 6| 0.00|  | 0| 0|   
KJC message pool free list| 316,625| 0.89| 0.02| 0| 62,480| 0.04  
KJCT flow control latch| 4,636,620| 0.03| 0.00| 0| 0|   
KMG MMAN ready and startup request latch| 3,612| 0.00|  | 0| 0|   
KTF sga latch| 1,536| 0.00|  | 0| 3,647| 0.00  
KWQMN job cache list latch| 888| 0.00|  | 0| 0|   
KWQP Prop Status| 12| 0.00|  | 0| 0|   
KWQS pqsubs latch| 18| 0.00|  | 0| 0|   
KWQS pqueue ctx latch| 163| 0.00|  | 0| 0|   
LGWR NS Write| 802,220| 0.00| 0.00| 0| 0|   
Locator state objects pool parent latch| 6| 0.00|  | 0| 0|   
Lsod array latch| 11,219| 0.00|  | 0| 0|   
MQL Tracking Latch| 0|  |  | 0| 216| 0.00  
Memory Management Latch| 6| 0.00|  | 0| 3,612| 0.00  
Memory Queue| 6| 0.00|  | 0| 0|   
Memory Queue Message Subscriber #1| 6| 0.00|  | 0| 0|   
Memory Queue Message Subscriber #2| 6| 0.00|  | 0| 0|   
Memory Queue Message Subscriber #3| 6| 0.00|  | 0| 0|   
Memory Queue Message Subscriber #4| 6| 0.00|  | 0| 0|   
Memory Queue Subscriber| 6| 0.00|  | 0| 0|   
MinActiveScn Latch| 3,783| 0.00|  | 0| 0|   
Mutex| 6| 0.00|  | 0| 0|   
Mutex Stats| 6| 0.00|  | 0| 0|   
OS process| 31,199| 0.00|  | 0| 0|   
OS process allocation| 37,474| 0.17| 0.00| 0| 0|   
OS process: request allocation| 15,198| 0.32| 0.00| 0| 0|   
PL/SQL warning settings| 96,899| 0.03| 0.00| 0| 0|   
PX hash array latch| 6| 0.00|  | 0| 0|   
QMT| 6| 0.00|  | 0| 0|   
Real-time plan statistics latch| 358,402| 0.00| 0.00| 0| 0|   
SGA IO buffer pool latch| 95| 0.00|  | 0| 95| 0.00  
SGA blob parent| 6| 0.00|  | 0| 0|   
SGA bucket locks| 6| 0.00|  | 0| 0|   
SGA heap locks| 6| 0.00|  | 0| 0|   
SGA pool locks| 6| 0.00|  | 0| 0|   
SQL memory manager latch| 6| 0.00|  | 0| 10,796| 0.00  
SQL memory manager workarea list latch| 3,553,332| 0.00| 0.00| 0| 0|   
Shared B-Tree| 764| 0.00|  | 0| 0|   
Streams Generic| 6| 0.00|  | 0| 0|   
Testing| 6| 0.00|  | 0| 0|   
Token Manager| 6| 0.00|  | 0| 0|   
WCR: sync| 6| 0.00|  | 0| 0|   
Write State Object Pool Parent Latch| 6| 0.00|  | 0| 0|   
X$KSFQP| 8| 0.00|  | 0| 0|   
XDB NFS Security Latch| 6| 0.00|  | 0| 0|   
XDB unused session pool| 6| 0.00|  | 0| 0|   
XDB used session pool| 6| 0.00|  | 0| 0|   
active checkpoint queue latch| 371,926| 2.77| 0.00| 0| 0|   
active service list| 709,902| 0.01| 0.01| 0| 20,898| 0.00  
alert log latch| 50| 0.00|  | 0| 0|   
archive control| 975| 0.00|  | 0| 0|   
archive process latch| 1,372| 0.00|  | 0| 0|   
begin backup scn array| 106,592| 0.00|  | 0| 0|   
buffer pool| 6| 0.00|  | 0| 0|   
business card| 120| 0.00|  | 0| 0|   
cache buffer handles| 1,824,192| 0.00| 0.00| 0| 0|   
cache buffers chains| 4,639,396,987| 0.00| 0.00| 0| 10,797,200| 0.00  
cache buffers lru chain| 3,119,050| 0.01| 0.01| 0| 12,515,210| 0.00  
cache table scan latch| 919| 0.00|  | 0| 919| 0.00  
call allocation| 40,842| 0.69| 0.33| 0| 0|   
cas latch| 6| 0.00|  | 0| 0|   
change notification client cache latch| 6| 0.00|  | 0| 0|   
channel handle pool latch| 15,363| 0.30| 0.00| 0| 0|   
channel operations parent latch| 3,041,118| 0.00| 0.00| 0| 0|   
checkpoint queue latch| 34,405,498| 0.00| 0.00| 0| 752,799| 0.00  
client/application info| 64,841| 0.00|  | 0| 0|   
compile environment latch| 9,682| 0.02| 0.00| 0| 0|   
corrupted undo seg latch| 7,928| 0.00|  | 0| 0|   
cp cmon/server latch| 6| 0.00|  | 0| 0|   
cp pool latch| 6| 0.00|  | 0| 0|   
cp server hash latch| 6| 0.00|  | 0| 0|   
cp sga latch| 193| 0.00|  | 0| 0|   
cvmap freelist lock| 6| 0.00|  | 0| 0|   
deferred cleanup latch| 193| 0.00|  | 0| 0|   
dml lock allocation| 193| 0.00|  | 0| 0|   
done queue latch| 6| 0.00|  | 0| 0|   
dummy allocation| 19,303| 0.22| 0.00| 0| 0|   
eighth spare latch - X parent| 6| 0.00|  | 0| 0|   
eleventh spare latch - children| 6| 0.00|  | 0| 0|   
enqueue freelist latch| 6| 0.00|  | 0| 7,347,291| 0.00  
enqueue hash chains| 11,323,593| 0.02| 0.00| 0| 54| 0.00  
enqueues| 9| 0.00|  | 0| 0|   
error message lists| 249| 0.00|  | 0| 0|   
fifteenth spare latch - children| 6| 0.00|  | 0| 0|   
file cache latch| 6,605| 0.00|  | 0| 0|   
first Audit Vault latch| 7,460| 0.25| 0.00| 0| 0|   
flashback copy| 6| 0.00|  | 0| 0|   
fourteenth spare latch - children| 6| 0.00|  | 0| 0|   
fourth Audit Vault latch| 6| 0.00|  | 0| 0|   
gc element| 6,364,078| 0.03| 0.00| 0| 373,338| 0.00  
gc persistent rm| 2| 0.00|  | 0| 0|   
gcs commit scn state| 6| 0.00|  | 0| 0|   
gcs opaque info freelist| 1,027,138| 0.00| 0.00| 0| 0|   
gcs partitioned table hash| 26,673,060| 0.00| 0.00| 0| 1,060,674| 0.00  
gcs pcm hashed value bucket hash| 6| 0.00|  | 0| 0|   
gcs remaster request queue| 236| 0.00|  | 0| 0|   
gcs remastering latch| 2,128| 0.05| 0.00| 0| 51| 0.00  
gcs resource freelist| 88,267| 0.00| 0.00| 0| 0|   
gcs resource hash| 38,672,112| 0.01| 0.00| 0| 5,428| 0.00  
gcs resource scan list| 15,196| 0.00|  | 0| 0|   
gcs resource validate list| 6| 0.00|  | 0| 0|   
gcs shadows freelist| 143,800| 0.00|  | 0| 0|   
ges caches resource lists| 1,554,909| 0.04| 0.01| 0| 433,051| 0.01  
ges deadlock list| 50,860| 0.01| 0.00| 0| 9| 0.00  
ges domain table| 4,578,628| 0.00| 0.00| 0| 0|   
ges enqueue table freelist| 5,909,483| 0.00| 0.00| 0| 0|   
ges group table| 6,261,993| 0.00| 0.00| 0| 0|   
ges process hash list| 204,175| 0.00|  | 0| 0|   
ges process parent latch| 11,982,744| 0.00| 0.00| 0| 0|   
ges process table freelist| 15,198| 0.37| 0.00| 0| 0|   
ges resource hash list| 11,825,603| 0.06| 0.02| 0| 152,804| 0.00  
ges resource scan list| 812| 0.00|  | 0| 0|   
ges resource table freelist| 288,691| 0.00| 0.00| 0| 0|   
ges timeout list| 95,800| 0.01| 0.00| 0| 1,137| 0.00  
ges value block free list| 1,225,471| 0.02| 0.00| 0| 0|   
global KZLD latch for mem in SGA| 7,460| 0.01| 0.00| 0| 0|   
global tx hash mapping| 648,764| 0.00| 0.00| 0| 0|   
granule operation| 6| 0.00|  | 0| 0|   
hash table column usage latch| 2,207| 0.00|  | 0| 24,450,222| 0.01  
hash table modification latch| 795| 0.00|  | 0| 0|   
heartbeat check| 6| 0.00|  | 0| 4,700| 0.00  
heartbeat structure management| 32| 0.00|  | 0| 2,165| 0.00  
internal temp table object number allocation latch| 7| 0.00|  | 0| 0|   
interrupt manipulation| 884| 0.00|  | 0| 0|   
intra txn parallel recovery| 6| 0.00|  | 0| 0|   
io pool granule metadata list| 6| 0.00|  | 0| 0|   
job workq parent latch| 1,959| 0.00|  | 0| 1,954| 3.89  
job_queue_processes free list latch| 3,912| 0.36| 0.00| 0| 0|   
job_queue_processes parameter latch| 56,313| 0.00|  | 0| 0|   
k2q global data latch| 148,881| 0.00|  | 0| 0|   
k2q lock allocation| 1,083,377| 0.00| 0.00| 0| 0|   
kcbtsemkid latch| 10| 0.00|  | 0| 0|   
kdlx hb parent latch| 6| 0.00|  | 0| 0|   
kgb parent| 6| 0.00|  | 0| 0|   
kgnfs mount latch| 6| 0.00|  | 0| 0|   
kokc descriptor allocation latch| 94| 0.00|  | 0| 0|   
krbmrosl| 2| 0.00|  | 0| 0|   
ksfv messages| 6| 0.00|  | 0| 0|   
ksim group membership cache| 512| 0.00|  | 0| 0|   
ksim membership request latch| 0|  |  | 0| 6,077| 0.00  
kss move lock| 116| 0.00|  | 0| 0|   
ksuosstats global area| 1,102| 0.00|  | 0| 0|   
ksv allocation latch| 411| 0.00|  | 0| 0|   
ksv class latch| 290,179| 0.02| 0.14| 0| 0|   
ksv msg queue latch| 36,811| 0.00|  | 0| 36,805| 0.00  
ksxp shared latch| 15,198| 0.24| 0.00| 0| 0|   
ksxp so latch| 15,198| 0.16| 0.00| 0| 0|   
ksz_so allocation latch| 15,198| 0.53| 0.00| 0| 0|   
ktm global data| 4,502| 0.00|  | 0| 0|   
kwqbsn:qsga| 389| 0.00|  | 0| 0|   
lgwr LWN SCN| 521,672| 0.05| 0.00| 0| 0|   
list of block allocation| 25,379| 0.30| 0.00| 0| 0|   
loader state object freelist| 348,826| 0.00| 0.00| 0| 0|   
lob segment dispenser latch| 6| 0.00|  | 0| 0|   
lob segment hash table latch| 42| 0.00|  | 0| 0|   
lob segment query latch| 6| 0.00|  | 0| 0|   
lock DBA buffer during media recovery| 6| 0.00|  | 0| 0|   
logical standby cache| 6| 0.00|  | 0| 0|   
logminer context allocation| 12| 0.00|  | 0| 0|   
logminer local| 6| 0.00|  | 0| 0|   
logminer work area| 6| 0.00|  | 0| 0|   
longop free list parent| 4,262| 0.00|  | 0| 1,062| 0.00  
managed standby latch| 444| 0.00|  | 0| 0|   
mapped buffers lru chain| 6| 0.00|  | 0| 0|   
message pool operations parent latch| 20,931| 0.00|  | 0| 0|   
messages| 3,918,704| 1.37| 0.01| 0| 0|   
mostly latch-free SCN| 534,138| 1.57| 0.00| 0| 0|   
msg queue latch| 6| 0.00|  | 0| 0|   
multiblock read objects| 158,294| 0.00| 0.00| 0| 0|   
name-service memory objects| 107,779| 0.00| 0.00| 0| 0|   
name-service namespace bucket| 110,248| 0.00|  | 0| 0|   
name-service namespace objects| 35| 0.00|  | 0| 0|   
name-service pending queue| 55,754| 0.00|  | 0| 0|   
name-service request| 104| 0.00|  | 0| 0|   
name-service request queue| 175,997| 0.00|  | 0| 0|   
ncodef allocation latch| 193| 0.00|  | 0| 0|   
nineth spare latch - X parent| 6| 0.00|  | 0| 0|   
object queue header heap| 1,000,106| 0.00|  | 0| 981,198| 0.00  
object queue header operation| 20,336,008| 0.01| 0.00| 0| 0|   
object stats modification| 22,665| 0.08| 0.06| 0| 0|   
parallel query alloc buffer| 11,473| 0.00|  | 0| 0|   
parallel query stats| 274| 0.00|  | 0| 0|   
parallel txn reco latch| 20,874| 0.00|  | 0| 0|   
parameter list| 76,189| 0.02| 0.00| 0| 0|   
parameter table management| 101,995| 1.41| 0.00| 0| 0|   
peshm| 6| 0.00|  | 0| 0|   
pesom_free_list| 6| 0.00|  | 0| 0|   
pesom_hash_node| 6| 0.00|  | 0| 0|   
post/wait queue| 1,199,572| 0.00| 0.00| 0| 936,397| 0.00  
process allocation| 67,866| 0.08| 0.11| 0| 7,612| 0.28  
process group creation| 15,198| 0.02| 0.00| 0| 0|   
process queue| 734| 0.00|  | 0| 0|   
process queue reference| 11,334| 0.00|  | 0| 1,066| 0.00  
qmn state object latch| 11| 0.00|  | 0| 0|   
qmn task queue latch| 2,363| 0.00|  | 0| 0|   
query server freelists| 598| 0.00|  | 0| 0|   
query server process| 66| 0.00|  | 0| 17| 0.00  
queued dump request| 36| 0.00|  | 0| 0|   
queuing load statistics| 6| 0.00|  | 0| 0|   
readredo stats and histogram| 463,987| 0.00| 0.00| 0| 0|   
recovery domain hash list| 6| 0.00|  | 0| 0|   
redo allocation| 4,079,339| 0.07| 0.00| 0| 12,784,185| 0.07  
redo copy| 6| 0.00|  | 0| 12,787,684| 0.02  
redo writing| 1,639,113| 0.33| 0.00| 0| 0|   
resmgr group change latch| 9,628| 0.04| 0.00| 0| 0|   
resmgr:active threads| 19,303| 0.00|  | 0| 0|   
resmgr:actses change group| 9,584| 0.00|  | 0| 0|   
resmgr:actses change state| 6| 0.00|  | 0| 0|   
resmgr:free threads list| 19,297| 0.29| 0.00| 0| 0|   
resmgr:plan CPU method| 6| 0.00|  | 0| 0|   
resmgr:resource group CPU method| 6| 0.00|  | 0| 0|   
resmgr:schema config| 486| 0.00|  | 0| 0|   
resmgr:session queuing| 6| 0.00|  | 0| 0|   
rm cas latch| 6| 0.00|  | 0| 0|   
row cache objects| 58,616,559| 0.04| 0.00| 0| 1,132| 0.00  
rules engine rule set statistics| 600| 0.00|  | 0| 0|   
second Audit Vault latch| 6| 0.00|  | 0| 0|   
segmented array pool| 29,496| 0.00|  | 0| 0|   
sequence cache| 118,575| 0.74| 0.00| 0| 0|   
session allocation| 945,332| 0.00|  | 0| 926,238| 0.00  
session idle bit| 20,331,401| 0.00| 0.03| 0| 0|   
session queue latch| 6| 0.00|  | 0| 0|   
session state list latch| 13,302| 0.18| 0.00| 0| 0|   
session switching| 7,748| 0.52| 0.00| 0| 32| 0.00  
session timer| 3,632| 0.00|  | 0| 0|   
seventh spare latch - X parent| 6| 0.00|  | 0| 0|   
shared pool| 6,012,944| 0.02| 0.03| 0| 2,255| 0.00  
shared pool sim alloc| 6| 0.00|  | 0| 0|   
shared pool simulator| 172,243| 0.00|  | 0| 0|   
sim partition latch| 6| 0.00|  | 0| 0|   
simulator hash latch| 179,349,706| 0.00| 0.00| 0| 0|   
simulator lru latch| 6| 0.00|  | 0| 179,337,735| 0.12  
sixth spare latch - X parent| 6| 0.00|  | 0| 0|   
sort extent pool| 9,145| 0.00|  | 0| 0|   
space background state object latch| 17| 0.00|  | 0| 0|   
space background task latch| 843,833| 0.01| 0.62| 0| 7,234| 0.03  
state object free list| 12| 0.00|  | 0| 0|   
statistics aggregation| 4,704| 0.00|  | 0| 0|   
tablespace key chain| 1,147,957| 0.00| 0.00| 0| 0|   
temp lob duration state obj allocation| 99| 0.00|  | 0| 0|   
tenth spare latch - X parent| 6| 0.00|  | 0| 0|   
test excl. parent l0| 6| 0.00|  | 0| 0|   
test excl. parent2 l0| 6| 0.00|  | 0| 0|   
thirteenth spare latch - children| 6| 0.00|  | 0| 0|   
threshold alerts latch| 1,613| 0.00|  | 0| 0|   
transaction allocation| 168,671| 0.00|  | 0| 0|   
transaction branch allocation| 487,375| 0.00| 0.00| 0| 0|   
twelfth spare latch - children| 6| 0.00|  | 0| 0|   
twenty-fifth spare latch - S par| 6| 0.00|  | 0| 0|   
twenty-first spare latch - S par| 6| 0.00|  | 0| 0|   
twenty-fourth spare latch - S par| 6| 0.00|  | 0| 0|   
twenty-second spare latch - S par| 6| 0.00|  | 0| 0|   
twenty-third spare latch - S par| 6| 0.00|  | 0| 0|   
undo global data| 2,453,181| 0.00| 0.00| 0| 0|   
virtual circuit buffers| 6| 0.00|  | 0| 0|   
virtual circuit holder| 6| 0.00|  | 0| 0|   
virtual circuit queues| 6| 0.00|  | 0| 0|   
write info latch| 0|  |  | 0| 428,044| 0.03  
  
* * *

Back to Latch Statistics   
Back to Top

### Latch Sleep Breakdown

  * ordered by misses desc

Latch Name| Get Requests| Misses| Sleeps| Spin Gets  
---|---|---|---|---  
cache buffers chains| 4,639,396,987| 192,545| 122| 192,419  
messages| 3,918,704| 53,630| 394| 53,251  
row cache objects| 58,616,559| 25,026| 23| 25,003  
active checkpoint queue latch| 371,926| 10,291| 32| 10,259  
mostly latch-free SCN| 534,138| 8,403| 11| 8,392  
ges resource hash list| 11,825,603| 7,534| 128| 7,422  
redo writing| 1,639,113| 5,376| 26| 5,350  
redo allocation| 4,079,339| 2,979| 4| 2,975  
KJC message pool free list| 316,625| 2,821| 43| 2,780  
gcs resource hash| 38,672,112| 2,654| 9| 2,645  
enqueue hash chains| 11,323,593| 1,979| 4| 1,975  
gc element| 6,364,078| 1,883| 3| 1,881  
KJCT flow control latch| 4,636,620| 1,449| 1| 1,448  
shared pool| 6,012,944| 1,423| 42| 1,382  
ASM map operation hash table| 67,309,822| 907| 2| 905  
simulator hash latch| 179,349,706| 905| 4| 902  
ges caches resource lists| 1,554,909| 549| 3| 546  
call allocation| 40,842| 281| 92| 189  
checkpoint queue latch| 34,405,498| 278| 1| 277  
cache buffers lru chain| 3,119,050| 220| 2| 218  
space background task latch| 843,833| 115| 71| 44  
active service list| 709,902| 98| 1| 97  
process allocation| 67,866| 54| 6| 48  
ksv class latch| 290,179| 51| 7| 44  
session idle bit| 20,331,401| 30| 1| 29  
object stats modification| 22,665| 18| 1| 17  
  
* * *

Back to Latch Statistics   
Back to Top

### Latch Miss Sources

  * only latches with sleeps are shown 
  * ordered by name, sleeps desc

Latch Name| Where| NoWait Misses|  Sleeps| Waiter Sleeps  
---|---|---|---|---  
ASM map operation hash table| kffmTranslate| 0| 2| 1  
KJC message pool free list| kjcsmpav: allocate a msg buffer| 0| 42| 43  
KJC message pool free list| kjcspfmbq: free vector of msg buffers| 0| 1| 0  
KJCT flow control latch| kjcts_sqenq: queue a message| 0| 1| 1  
PC and Classifier lists for WLM| No latch| 0| 8| 0  
active checkpoint queue latch| kcbbacq: scan active checkpoints| 0| 32| 32  
active service list| kswslogon: session logout| 0| 1| 0  
cache buffers chains| kcbgtcr: fast path (cr pin)| 0| 79| 100  
cache buffers chains| kcbgcur_2| 0| 16| 1  
cache buffers chains| kcbbxsv| 0| 10| 2  
cache buffers chains| kcbgtcr: fast path| 0| 10| 28  
cache buffers chains| kcllkopesc| 0| 8| 0  
cache buffers chains| kcbgtcr: kslbegin shared| 0| 7| 2  
cache buffers chains| kcbzwb| 0| 7| 0  
cache buffers chains| kclwrt| 0| 6| 0  
cache buffers chains| kcbgtcr_2| 0| 5| 0  
cache buffers chains| kcbzibmlt: multi-block read: nowait| 0| 5| 0  
cache buffers chains| kcbrls_2| 0| 4| 0  
cache buffers chains| kclbla| 0| 4| 0  
cache buffers chains| kcbchg1: clear MS bit| 0| 3| 0  
cache buffers chains| kcbchg1: mod cr pin| 0| 3| 0  
cache buffers chains| kcbget: fast exchange| 0| 3| 0  
cache buffers chains| kcbgcur_4| 0| 1| 0  
cache buffers chains| kcbzgb: scan from tail. nowait| 0| 1| 0  
cache buffers chains| kcl_fairness| 0| 1| 0  
cache buffers chains| kclrlstp| 0| 1| 0  
cache buffers lru chain| kcbbic2| 0| 1| 1  
cache buffers lru chain| kcbo_link_q| 0| 1| 0  
call allocation| ksuxds| 0| 91| 61  
call allocation| ksudlp: top call| 0| 1| 30  
checkpoint queue latch| kcbbwdl: thread checkpoint queue| 0| 1| 0  
enqueue hash chains| ksqcmi: if lk mode requested| 0| 3| 0  
enqueue hash chains| ksqcmi: if lk mode not requested| 0| 1| 0  
gc element| kclchkping| 0| 2| 0  
gc element| kclrwrite| 0| 1| 1  
gcs resource hash| kclrwrite| 0| 6| 6  
gcs resource hash| kjbconvert| 0| 2| 2  
gcs resource hash| kjbmpcreatepi| 0| 1| 0  
ges caches resource lists| kjruch: cached obj cleanup| 0| 3| 0  
ges resource hash list| kjrmas1: lookup master node| 0| 113| 14  
ges resource hash list| kjakoca: search for resp by resname| 0| 9| 6  
ges resource hash list| kjlrlr: remove lock from resource queue| 0| 4| 7  
ges resource hash list| kjakcai: search for resp by resname| 0| 2| 6  
ksv class latch| ksvclsl: rdp - recycle| 0| 6| 0  
ksv class latch| ksvclsl: run| 0| 1| 0  
lgwr LWN SCN| kcs023| 0| 7| 0  
messages| ksarcv| 0| 184| 148  
messages| ksaamb: after wakeup| 0| 119| 161  
messages| ksarcv: after wait| 0| 91| 85  
mostly latch-free SCN| kcslcu3| 0| 4| 11  
object stats modification| ksols_rank| 0| 1| 0  
process allocation| ksufap: active procs| 0| 3| 0  
process allocation| ksucrp:1| 0| 2| 0  
process allocation| ksudlp| 0| 1| 2  
redo allocation| kcrfw_redo_gen: redo allocation 1| 0| 4| 0  
redo writing| kcrfwcr| 0| 25| 24  
redo writing| kcrfw_post: rba scn pair| 0| 1| 0  
row cache objects| kqrpre: find obj| 0| 11| 16  
row cache objects| kqreqd: reget| 0| 8| 3  
row cache objects| kqreqd| 0| 4| 3  
session idle bit| ksupuc: clear busy| 0| 1| 0  
shared pool| kghalo| 0| 28| 22  
shared pool| kgh_heap_sizes| 0| 11| 0  
shared pool| kghupr1| 0| 2| 12  
shared pool| kghalp| 0| 1| 1  
simulator hash latch| kcbsacc: insert dba| 0| 2| 0  
simulator hash latch| kcbs_lookup_setid: lookup dba| 0| 1| 0  
simulator hash latch| kcbsacc: lookup dba| 0| 1| 4  
space background task latch| ktsj_grab_task| 0| 63| 71  
  
* * *

Back to Latch Statistics   
Back to Top

### Mutex Sleep Summary

  * ordered by number of sleeps desc

Mutex Type| Location| Sleeps| Wait Time (ms)  
---|---|---|---  
Library Cache| kglhdgn2 106| 8| 0  
Library Cache| kgllkc1 57| 4| 0  
Cursor Pin| kksfbc [KKSCHLFSP2]| 4| 0  
Cursor Pin| kksLockDelete [KKSCHLPIN6]| 3| 0  
Library Cache| kglpnal2 91| 2| 0  
Library Cache| kglhdgn1 62| 1| 0  
Library Cache| kglpnal1 90| 1| 0  
Cursor Pin| kkslce [KKSCHLPIN2]| 1| 0  
  
* * *

Back to Latch Statistics   
Back to Top

### Parent Latch Statistics

No data exists for this section of the report. 

Back to Latch Statistics   
Back to Top

### Child Latch Statistics

No data exists for this section of the report. 

Back to Latch Statistics   
Back to Top

##  Segment Statistics 

  * Segments by Logical Reads
  * Segments by Physical Reads
  * Segments by Physical Read Requests
  * Segments by UnOptimized Reads
  * Segments by Optimized Reads
  * Segments by Direct Physical Reads
  * Segments by Physical Writes
  * Segments by Physical Write Requests
  * Segments by Direct Physical Writes
  * Segments by Table Scans
  * Segments by DB Blocks Changes
  * Segments by Row Lock Waits
  * Segments by ITL Waits
  * Segments by Buffer Busy Waits
  * Segments by Global Cache Buffer Busy
  * Segments by CR Blocks Received
  * Segments by Current Blocks Received

Back to Top

### Segments by Logical Reads

  * Total Logical Reads: 3,196,935,601
  * Captured Segments account for 91.5% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Logical Reads| %Total  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| T_OB_SETTLEACCOUNT|  | TABLE| 505,824,048| 15.82  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 453,761,184| 14.19  
WOPB| WOPB| DPB_OP_DISPENSE_DETAIL|  | TABLE| 300,849,184| 9.41  
URM| USERS| SCHEDULE|  | TABLE| 242,605,824| 7.59  
URM_BED| USERS| BAB_BED_ALLOCATION|  | TABLE| 148,153,792| 4.63  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Physical Reads

  * Total Physical Reads: 730,576,196
  * Captured Segments account for 92.7% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Physical Reads| %Total  
---|---|---|---|---|---|---  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 339,614,853| 46.49  
WOPB| WOPB| DPB_OP_DISPENSE_DETAIL|  | TABLE| 299,147,700| 40.95  
HISUSER| HISSPACE| T_PA_PERSON|  | TABLE| 33,949,266| 4.65  
URM| USERS| SCHEDULE|  | TABLE| 4,441,551| 0.61  
HISUSER| HISSPACE| IDX_NU_MSG_ID|  | INDEX| 28,440| 0.00  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Physical Read Requests

  * Total Physical Read Requests: 13,742,520
  * Captured Segments account for 41.1% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Phys Read Requests| %Total  
---|---|---|---|---|---|---  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 2,693,959| 19.60  
WOPB| WOPB| DPB_OP_DISPENSE_DETAIL|  | TABLE| 2,346,335| 17.07  
URM| USERS| SCHEDULE|  | TABLE| 267,968| 1.95  
HISUSER| HISSPACE| T_PA_PERSON|  | TABLE| 266,810| 1.94  
HISUSER| HISSPACE| IDX_NU_MSG_ID|  | INDEX| 28,440| 0.21  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by UnOptimized Reads

  * Total UnOptimized Read Requests: 13,742,520
  * Captured Segments account for 41.1% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| UnOptimized Reads| %Total  
---|---|---|---|---|---|---  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 2,693,959| 19.60  
WOPB| WOPB| DPB_OP_DISPENSE_DETAIL|  | TABLE| 2,346,335| 17.07  
URM| USERS| SCHEDULE|  | TABLE| 267,968| 1.95  
HISUSER| HISSPACE| T_PA_PERSON|  | TABLE| 266,810| 1.94  
HISUSER| HISSPACE| IDX_NU_MSG_ID|  | INDEX| 28,440| 0.21  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Optimized Reads

No data exists for this section of the report. 

Back to Segment Statistics   
Back to Top

### Segments by Direct Physical Reads

  * Total Direct Physical Reads: 730,135,342
  * Captured Segments account for 92.7% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Direct Reads| %Total  
---|---|---|---|---|---|---  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 339,589,888| 46.51  
WOPB| WOPB| DPB_OP_DISPENSE_DETAIL|  | TABLE| 299,147,001| 40.97  
HISUSER| HISSPACE| T_PA_PERSON|  | TABLE| 33,948,970| 4.65  
URM| USERS| SCHEDULE|  | TABLE| 4,206,264| 0.58  
HISUSER| HISSPACE| SYS_LOB0000093913C00013$$|  | LOB| 26,519| 0.00  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Physical Writes

  * Total Physical Writes: 617,276
  * Captured Segments account for 36.2% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Physical Writes| %Total  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| SYS_LOB0000093913C00014$$|  | LOB| 73,853| 11.96  
HISUSER| HISSPACE| IDX_NU_MSG_ID|  | INDEX| 41,828| 6.78  
HISUSER| HISSPACE| SYS_LOB0000093913C00013$$|  | LOB| 38,204| 6.19  
HISUSER| HISSPACE| T_SM_EXTERNAL_SYS_LOGGER|  | TABLE| 15,377| 2.49  
HISUSER| HISSPACE| IDX_NU_ODW_ORDERBILLING04|  | INDEX| 6,247| 1.01  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Physical Write Requests

  * Total Physical Write Requestss: 329,476
  * Captured Segments account for 65.1% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Phys Write Requests| %Total  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| SYS_LOB0000093913C00014$$|  | LOB| 70,983| 21.54  
HISUSER| HISSPACE| IDX_NU_MSG_ID|  | INDEX| 41,735| 12.67  
HISUSER| HISSPACE| SYS_LOB0000093913C00013$$|  | LOB| 37,558| 11.40  
HISUSER| HISSPACE| T_SM_EXTERNAL_SYS_LOGGER|  | TABLE| 14,681| 4.46  
HISUSER| HISSPACE| IDX_NU_ODW_ORDERBILLING04|  | INDEX| 5,566| 1.69  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Direct Physical Writes

  * Total Direct Physical Writes: 110,777
  * Captured Segments account for 98.8% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Direct Writes| %Total  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| SYS_LOB0000093913C00014$$|  | LOB| 72,399| 65.36  
HISUSER| HISSPACE| SYS_LOB0000093913C00013$$|  | LOB| 36,941| 33.35  
SYS| SYSAUX| WRH$_ACTIVE_SESSION_HISTORY| WRH$_ACTIVE_1539058184_73327| TABLE PARTITION| 121| 0.11  
HISUSER| HISSPACE| SYS_LOB0000315962C00005$$|  | LOB| 28| 0.03  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Table Scans

  * Total Table Scans: 3,120
  * Captured Segments account for 0.2% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Table Scans| %Total  
---|---|---|---|---|---|---  
WPUB| WPUB| PK_P_DRUG|  | INDEX| 2| 0.06  
WOPB| WOPB| DPB_OP_DISPENSE_NOTE|  | TABLE| 1| 0.03  
URM_MT| URM_MT_DATA| IDX_APPLY_NO_3|  | INDEX| 1| 0.03  
URM_MT| URM_MT_DATA| IDX_SEQ_NO_PROUSE|  | INDEX| 1| 0.03  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by DB Blocks Changes

  * % of Capture shows % of DB Block Changes for each top segment compared 
  * with total DB Block Changes for all segments captured by the Snapshot

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| DB Block Changes| % of Capture  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| T_SM_DEPARTMENT|  | TABLE| 2,278,576| 35.66  
HISUSER| HISSPACE| SYS_IL0000093913C00014$$|  | INDEX| 1,424,320| 22.29  
WDP| WDP| DPC_STORAGE_DRUG|  | TABLE| 427,088| 6.68  
HISUSER| HISSPACE| T_SM_MEDICALSERVICESPRICE|  | TABLE| 390,256| 6.11  
HISUSER| HISSPACE| T_SM_EXTERNAL_SYS_LOGGER|  | TABLE| 197,952| 3.10  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Row Lock Waits

  * % of Capture shows % of row lock waits for each top segment compared 
  * with total row lock waits for all segments captured by the Snapshot

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Row Lock Waits| % of Capture  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| IDX_NU_FUNCID|  | INDEX| 203| 28.04  
HISUSER| HISSPACE| T_SM_DBLOCK|  | TABLE| 85| 11.74  
HISUSER| HISSPACE| PK_EXTERNAL_SYSLOGGER|  | INDEX| 65| 8.98  
URM_MT| URM_MT_DATA| MT_SHEDLOCK|  | TABLE| 57| 7.87  
HISUSER| HISSPACE| SYS_IL0000093913C00013$$|  | INDEX| 40| 5.52  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by ITL Waits

  * % of Capture shows % of ITL waits for each top segment compared 
  * with total ITL waits for all segments captured by the Snapshot

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| ITL Waits| % of Capture  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| IDX_NU_T_ODW_ORDER_1|  | INDEX| 1| 33.33  
HISUSER| USERS| IDX_UNQ_OB_ELECTRONICBILLS_01|  | INDEX| 1| 33.33  
HISUSER| HISSPACE| SYS_IL0000093913C00013$$|  | INDEX| 1| 33.33  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Buffer Busy Waits

  * % of Capture shows % of Buffer Busy Waits for each top segment compared 
  * with total Buffer Busy Waits for all segments captured by the Snapshot

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Buffer Busy Waits| % of Capture  
---|---|---|---|---|---|---  
SYS| SYSTEM| JOB$|  | TABLE| 220| 41.28  
HISUSER| HISSPACE| T_SM_DEPARTMENT|  | TABLE| 166| 31.14  
URM_MT| URM_MT_DATA| MT_SHEDLOCK|  | TABLE| 55| 10.32  
SYS| SYSTEM| I_JOB_NEXT|  | INDEX| 49| 9.19  
WDPB| WDPB| PK_PHB_STOCK_VIRTUAL_QUEUE|  | INDEX| 6| 1.13  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Global Cache Buffer Busy

  * % of Capture shows % of GC Buffer Busy for each top segment compared 
  * with GC Buffer Busy for all segments captured by the Snapshot

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| GC Buffer Busy| % of Capture  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| SYS_IL0000093913C00014$$|  | INDEX| 20,306| 86.63  
URM_MT| URM_MT_DATA| IDX_SCHEDULE_DEPTID|  | INDEX| 1,392| 5.94  
HISUSER| HISSPACE| T_SM_CLIENT_SOCKET|  | TABLE| 561| 2.39  
URM_MT| URM_MT_DATA| MT_SHEDLOCK|  | TABLE| 549| 2.34  
WDPB| WDPB| STB_STOCK|  | TABLE| 152| 0.65  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by CR Blocks Received

  * Total CR Blocks Received: 466,253
  * Captured Segments account for 79.7% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| CR Blocks Received| %Total  
---|---|---|---|---|---|---  
HISUSER| HISSPACE| SYS_IL0000093913C00014$$|  | INDEX| 128,488| 27.56  
HISUSER| HISSPACE| T_SM_EXTERNAL_SYS_LOGGER|  | TABLE| 45,057| 9.66  
HISUSER| HISSPACE| PK_EXTERNAL_SYSLOGGER|  | INDEX| 31,633| 6.78  
HISUSER| HISSPACE| T_SM_CLIENT_SOCKET|  | TABLE| 19,511| 4.18  
WDP| WDP| DPC_STORAGE_DRUG|  | TABLE| 17,590| 3.77  
  
* * *

Back to Segment Statistics   
Back to Top

### Segments by Current Blocks Received

  * Total Current Blocks Received: 775,877
  * Captured Segments account for 83.5% of Total

Owner| Tablespace Name| Object Name| Subobject Name| Obj. Type| Current Blocks Received| %Total  
---|---|---|---|---|---|---  
WIPB| WPUB| DPB_DISPENSE_DETAIL|  | TABLE| 144,967| 18.68  
HISUSER| HISSPACE| T_SM_EXTERNAL_SYS_LOGGER|  | TABLE| 55,658| 7.17  
HISUSER| HISSPACE| IDX_NU_OB_INVOICE05|  | INDEX| 51,399| 6.62  
URM_MT| URM_MT_DATA| MT_INSPECT_APPOINTMENT|  | TABLE| 39,468| 5.09  
WDPB| WDPB| STB_STOCK_DETAIL|  | TABLE| 35,450| 4.57  
  
* * *

Back to Segment Statistics   
Back to Top

##  Dictionary Cache Statistics 

  * Dictionary Cache Stats
  * Dictionary Cache Stats (RAC)

Back to Top

### Dictionary Cache Stats

  * "Pct Misses" should be very low (< 2% in most cases) 
  * "Final Usage" is the number of cache entries being used

Cache| Get Requests| Pct Miss| Scan Reqs| Pct Miss| Mod Reqs| Final Usage  
---|---|---|---|---|---|---  
dc_awr_control| 193| 6.22| 0|  | 0| 1  
dc_files| 128| 0.00| 0|  | 0| 128  
dc_global_oids| 8,266| 0.00| 0|  | 0| 44  
dc_histogram_data| 4,306,943| 0.01| 0|  | 0| 9,344  
dc_histogram_defs| 2,271,365| 0.05| 0|  | 0| 9,907  
dc_object_grants| 453| 0.66| 0|  | 0| 431  
dc_objects| 4,481,470| 0.02| 0|  | 167| 4,043  
dc_profiles| 16,873| 0.00| 0|  | 0| 1  
dc_rollback_segments| 104,024| 0.00| 0|  | 1| 297  
dc_segments| 1,047,580| 0.02| 0|  | 147| 2,497  
dc_sequences| 1,924| 17.57| 0|  | 1,924| 15  
dc_table_scns| 25,513| 0.05| 0|  | 113| 69  
dc_tablespaces| 4,653,994| 0.00| 0|  | 0| 49  
dc_users| 5,572,082| 0.00| 0|  | 0| 177  
global database name| 19,252| 0.00| 0|  | 0| 2  
outstanding_alerts| 538| 97.58| 0|  | 0| 0  
sch_lj_oids| 15| 0.00| 0|  | 0| 15  
  
* * *

Back to Dictionary Cache Statistics   
Back to Top

### Dictionary Cache Stats (RAC)


Cache| GES Requests| GES Conflicts| GES Releases  
---|---|---|---  
dc_awr_control| 12| 12| 0  
dc_histogram_defs| 1,175| 0| 4,158  
dc_objects| 846| 80| 457  
dc_rollback_segments| 2| 0| 0  
dc_segments| 542| 60| 328  
dc_sequences| 3,848| 326| 7  
dc_table_scns| 458| 7| 5  
dc_tablespaces| 1| 0| 1  
dc_users| 2| 0| 17  
outstanding_alerts| 1,059| 525| 0  
  
* * *

Back to Dictionary Cache Statistics   
Back to Top

##  Library Cache Statistics 

  * Library Cache Activity
  * Library Cache Activity (RAC)

Back to Top

### Library Cache Activity

  * "Pct Misses" should be very low 

Namespace| Get Requests| Pct Miss| Pin Requests| Pct Miss| Reloads| Invali- dations  
---|---|---|---|---|---|---  
ACCOUNT_STATUS| 22,380| 0.00| 0|  | 0| 0  
BODY| 6,199| 0.02| 198,602| 0.00| 3| 0  
CLUSTER| 57| 1.75| 57| 1.75| 0| 0  
DBLINK| 54,831| 0.01| 0|  | 0| 0  
EDITION| 9,450| 0.00| 18,860| 0.00| 0| 0  
INDEX| 158| 1.27| 158| 10.13| 14| 0  
JAVA DATA| 3| 66.67| 3| 66.67| 0| 0  
JAVA RESOURCE| 3| 66.67| 3| 66.67| 0| 0  
JAVA SOURCE| 3| 66.67| 3| 66.67| 0| 0  
OBJECT ID| 2| 100.00| 0|  | 0| 0  
QUEUE| 90| 0.00| 488| 0.00| 0| 0  
SCHEMA| 9,514| 0.02| 0|  | 0| 0  
SQL AREA| 630,273| 6.23| 14,209,453| 1.68| 59,442| 57,218  
SQL AREA BUILD| 99,614| 41.38| 0|  | 0| 0  
SQL AREA STATS| 99,156| 41.80| 99,156| 41.80| 0| 0  
SUBSCRIPTION| 25| 4.00| 25| 4.00| 0| 0  
SUMMARY| 224| 0.45| 224| 1.79| 1| 3  
TABLE/PROCEDURE| 246,445| 0.05| 967,276| 0.10| 558| 0  
TRIGGER| 718| 0.28| 6,918| 0.06| 2| 0  
  
* * *

Back to Library Cache Statistics   
Back to Top

### Library Cache Activity (RAC)


Namespace| GES Lock Requests| GES Pin Requests| GES Pin Releases| GES Inval Requests| GES Invali- dations  
---|---|---|---|---|---  
ACCOUNT_STATUS| 22,380| 0| 0| 0| 0  
BODY| 0| 196,303| 196,303| 0| 0  
CLUSTER| 57| 57| 57| 0| 0  
DBLINK| 54,831| 0| 0| 0| 0  
EDITION| 9,449| 9,452| 9,452| 0| 0  
INDEX| 158| 158| 158| 0| 0  
JAVA DATA| 3| 3| 3| 0| 0  
JAVA RESOURCE| 3| 3| 3| 0| 0  
JAVA SOURCE| 3| 3| 3| 0| 0  
QUEUE| 18| 488| 488| 0| 0  
SCHEMA| 9,382| 0| 0| 0| 0  
SUBSCRIPTION| 0| 25| 25| 0| 0  
SUMMARY| 224| 224| 224| 3| 3  
TABLE/PROCEDURE| 275,166| 720,985| 720,985| 0| 0  
TRIGGER| 3| 6,918| 6,918| 0| 0  
  
* * *

Back to Library Cache Statistics   
Back to Top

##  Memory Statistics 

  * Memory Dynamic Components
  * Memory Resize Operations Summary
  * Memory Resize Ops
  * Process Memory Summary
  * SGA Memory Summary
  * SGA breakdown difference

Back to Top

### Memory Dynamic Components

  * Min/Max sizes since instance startup 
  * Oper Types/Modes: INItializing,GROw,SHRink,STAtic/IMMediate,DEFerred 
  * ordered by Component 

Component| Begin Snap Size (Mb)| Current Size (Mb)| Min Size (Mb)| Max Size (Mb)| Oper Count| Last Op Typ/Mod  
---|---|---|---|---|---|---  
ASM Buffer Cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT 16K buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT 2K buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT 32K buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT 4K buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT 8K buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
DEFAULT buffer cache| 123,392.00| 123,392.00| 123,392.00| 124,928.00| 0| SHR/IMM  
KEEP buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
PGA Target| 51,200.00| 51,200.00| 51,200.00| 51,200.00| 0| STA/  
RECYCLE buffer cache| 0.00| 0.00| 0.00| 0.00| 0| STA/  
SGA Target| 153,600.00| 153,600.00| 153,600.00| 153,600.00| 0| STA/  
Shared IO Pool| 0.00| 0.00| 0.00| 0.00| 0| STA/  
java pool| 3,584.00| 3,584.00| 3,584.00| 3,584.00| 0| STA/  
large pool| 2,048.00| 2,048.00| 2,048.00| 2,048.00| 0| STA/  
shared pool| 22,528.00| 22,528.00| 22,016.00| 22,528.00| 0| GRO/IMM  
streams pool| 1,024.00| 1,024.00| 0.00| 1,024.00| 0| GRO/IMM  
  
* * *

Back to Memory Statistics   
Back to Top

### Memory Resize Operations Summary

No data exists for this section of the report. 

Back to Memory Statistics   
Back to Top

### Memory Resize Ops

No data exists for this section of the report. 

Back to Memory Statistics   
Back to Top

### Process Memory Summary

  * B: Begin Snap E: End Snap 
  * All rows below contain absolute values (i.e. not diffed over the interval) 
  * Max Alloc is Maximum PGA Allocation size at snapshot time 
  * Hist Max Alloc is the Historical Max Allocation for still-connected processes 
  * ordered by Begin/End snapshot, Alloc (MB) desc

| Category| Alloc (MB)| Used (MB)| Avg Alloc (MB)| Std Dev Alloc (MB)| Max Alloc (MB)| Hist Max Alloc (MB)| Num Proc| Num Alloc  
---|---|---|---|---|---|---|---|---|---  
B| Other| 2,205.52|  | 4.46| 10.02| 91| 162| 495| 495  
B| Freeable| 1,197.13| 0.00| 4.75| 19.02| 131|  | 252| 252  
B| SQL| 438.35| 408.98| 0.99| 16.82| 353| 1,930| 443| 283  
B| PL/SQL| 22.55| 11.84| 0.05| 0.16| 1| 32| 493| 493  
E| Other| 2,401.89|  | 4.27| 9.54| 91| 162| 563| 563  
E| Freeable| 1,231.44| 0.00| 4.28| 17.83| 131|  | 288| 288  
E| SQL| 458.01| 428.26| 0.90| 15.88| 353| 1,930| 509| 288  
E| PL/SQL| 32.35| 12.61| 0.06| 0.18| 1| 32| 561| 560  
  
* * *

Back to Memory Statistics   
Back to Top

### SGA Memory Summary


SGA regions| Begin Size (Bytes)| End Size (Bytes) (if different)  
---|---|---  
Database Buffers| 129,385,889,792|   
Fixed Size| 2,261,848|   
Redo Buffers| 352,444,416|   
Variable Size| 30,601,645,224|   
  
Back to Memory Statistics   
Back to Top

### SGA breakdown difference

  * ordered by Pool, Name 
  * N/A value for Begin MB or End MB indicates the size of that Pool/Name was insignificant, or zero in that snapshot

Pool| Name| Begin MB| End MB| % Diff  
---|---|---|---|---  
java| free memory| 3,574.22| 3,574.22| 0.00  
large| free memory| 2,039.81| 2,039.81| 0.00  
shared| KGLH0| 1,864.79| 1,876.98| 0.65  
shared| KGLHD| 235.42| 238.14| 1.16  
shared| SQLA| 3,281.95| 3,303.57| 0.66  
shared| db_block_hash_buckets| 712.00| 712.00| 0.00  
shared| free memory| 7,676.38| 7,660.83| -0.20  
shared| gc name table| 480.00| 480.00| 0.00  
shared| gcs resources| 3,513.34| 3,513.34| 0.00  
shared| gcs shadows| 2,432.32| 2,432.32| 0.00  
shared| kglsim heap| 255.92| 255.92| 0.00  
shared| kglsim object batch| 435.28| 435.28| 0.00  
streams| free memory| 1,023.99| 1,023.99| 0.00  
| buffer_cache| 123,392.00| 123,392.00| 0.00  
| fixed_sga| 2.16| 2.16| 0.00  
| log_buffer| 336.12| 336.12| 0.00  
  
* * *

Back to Memory Statistics   
Back to Top

##  Streams Statistics 

  * Streams CPU/IO Usage
  * Streams Capture
  * Streams Capture Rate
  * Streams Apply
  * Streams Apply Rate
  * Buffered Queues
  * Buffered Queue Subscribers
  * Rule Set
  * Persistent Queues
  * Persistent Queues Rate
  * Persistent Queue Subscribers

Back to Top

### Streams CPU/IO Usage

  * Streams processes ordered by CPU Time, descending

Session Type| First Logon| CPU time(s)| User IO Wait time(s)| SYS IO Wait time(s)  
---|---|---|---|---  
QMON Coordinator| 0202 02:20:46| 0.42| 0.00| 0.00  
QMON Slaves| 0202 02:20:46| -0.10| 0.00| 0.00  
  
* * *

Back to Streams Statistics   
Back to Top

### Streams Capture

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Streams Capture Rate

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Streams Apply

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Streams Apply Rate

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Buffered Queues

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Buffered Queue Subscribers

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Rule Set

No data exists for this section of the report. 

Back to Streams Statistics   
Back to Top

### Persistent Queues

  * Ordered by Queue Name 
  * * indicates queue (re)started between Begin/End snaps 
  * %Exp Msgs - % of msgs enqueued with expiry 
  * %Delay Msgs - % of msgs enqueued with delay 
  * %Trasf Time - % of Enqueue time spent in transformation 
  * %Eval Time - % of Enqueue time spent in rule evaluation

Queue Name| Enq Msgs| Deq Msgs| %Exp Msgs| %Delay Msgs| Enq Time(s)| Deq Time(s)| %Transf Time| %Eval Time  
---|---|---|---|---|---|---|---|---  
SYS.ALERT_QUE(13069) | 0| 0|  |  | 0.00| 0.00|  |   
SYS.AQ$_ALERT_QT_E(13068) | 0| 0|  |  | 0.00| 0.00|  |   
SYSMAN.MGMT_TASK_Q(87545) | 91| 91| 0.00| 0.00| 0.03| 0.06| 0.00| 0.00  
  
* * *

Back to Streams Statistics   
Back to Top

### Persistent Queues Rate

  * Ordered by Queue Name 
  * * indicates queue (re)started between Begin/End snaps

Queue Name| Enqueue Msgs/sec| Dequeue Msgs/sec| Avg Enqueue sec / msg| Avg Dequeue sec / msg  
---|---|---|---|---  
SYS.ALERT_QUE(13069) | 0.00| 0.00|  |   
SYS.AQ$_ALERT_QT_E(13068) | 0.00| 0.00|  |   
SYSMAN.MGMT_TASK_Q(87545) | 0.01| 0.01| 0.00| 0.00  
  
* * *

Back to Streams Statistics   
Back to Top

### Persistent Queue Subscribers

  * Ordered by Queue Name, Subscriber Name 
  * * indicates Subscriber activity (re)started between Begin/End snaps

Subscriber/Queue| Enqueue Msgs| Dequeue Msgs| Expire Msgs| Enqueue Msgs/sec| Dequeue Msgs/sec| Expire Msgs/sec  
---|---|---|---|---|---|---  
HAE_SUB(1)/SYS.ALERT_QUE | 0| 0| 0|  |  |   
HIS01_3938_ORCL1(41)/SYS.ALERT_QUE | 0| 0| 0| 0.00| 0.00| 0.00  
HIS02_3938_ORCL2(61)/SYS.ALERT_QUE | 0| 0| 0| 0.00| 0.00| 0.00  
  
* * *

Back to Streams Statistics   
Back to Top

### Resource Limit Stats

No data exists for this section of the report. 

  
Back to Top

##  Shared Server Statistics 

  * Shared Servers Activity
  * Shared Servers Rates
  * Shared Servers Utilization
  * Shared Servers Common Queue
  * Shared Servers Dispatchers

Back to Top

### Shared Servers Activity

  * Values represent averages for all samples

Avg Total Connections| Avg Active Connections| Avg Total Shared Srvrs| Avg Active Shared Srvrs| Avg Total Dispatchers| Avg Active Dispatchers  
---|---|---|---|---|---  
0| 0| 1| 0| 1| 0  
  
* * *

Back to Shared Server Statistics   
Back to Top

### Shared Servers Rates


Common Queue Per Sec| Disp Queue Per Sec| Server Msgs/Sec| Server KB/Sec| Common Queue Total| Disp Queue Total| Server Total Msgs| Server Total(KB)  
---|---|---|---|---|---|---|---  
0| 0| 0| 0.00| 0| 0| 0| 0  
  
* * *

Back to Shared Server Statistics   
Back to Top

### Shared Servers Utilization

  * Statistics are combined for all servers 
  * Incoming and Outgoing Net % are included in %Busy

Total Server Time (s)| %Busy| %Idle| Incoming Net %| Outgoing Net %  
---|---|---|---|---  
10,836| 0.00| 100.00| 0.00| 0.00  
  
* * *

Back to Shared Server Statistics   
Back to Top

### Shared Servers Common Queue

No data exists for this section of the report. 

Back to Shared Server Statistics   
Back to Top

### Shared Servers Dispatchers

  * Ordered by %Busy, descending 
  * Total Queued, Total Queue Wait and Avg Queue Wait are for dispatcher queue 
  * Name suffixes: "(N)" \- dispatcher started between begin and end snapshots "(R)" \- dispatcher re-started between begin and end snapshots

Name| Avg Conns| Total Disp Time (s)| %Busy| %Idle| Total Queued| Total Queue Wait (s)| Avg Queue Wait (ms)  
---|---|---|---|---|---|---|---  
D000| 0.00| 10,836| 0.00| 100.00| 0| 0|   
D000| 0.00| 10,836| 0.00| 100.00| 0| 0|   
D000| 0.00| 10,836| 0.00| 100.00| 0| 0|   
D000| 0.00| 10,836| 0.00| 100.00| 0| 0|   
Sum| 0.00|  |  |  | 0| 0|   
Avg| 0.00|  | 0.00| 100.00| 0| 0|   
Std| 0.00|  | 0.00| 0.00| 0| 0|   
  
* * *

Back to Shared Server Statistics   
Back to Top

##  init.ora Parameters 

  * init.ora Parameters
  * init.ora Multi-Valued Parameters

Back to Top

### init.ora Parameters


Parameter Name| Begin value| End value (if different)  
---|---|---  
audit_file_dest| /oracle/app/oracle/admin/orcl/adump|   
audit_trail| NONE|   
cluster_database| TRUE|   
cluster_database_instances| 2|   
compatible| 11.2.0.4.0|   
control_files| +DGDATA/orcl/controlfile/control01.ctl, +DGDATA/orcl/controlfile/control02.ctl|   
db_block_size| 8192|   
db_domain|  |   
db_file_name_convert| /home/oracle/app/oradata/orcl, +dgdata/orcl/datafile|   
db_name| orcl|   
db_recovery_file_dest| +dgdata|   
db_recovery_file_dest_size| 53687091200|   
db_unique_name| orcl|   
diagnostic_dest| /oracle/app/oracle|   
dispatchers| (PROTOCOL=TCP) (SERVICE=orclXDB)|   
enable_goldengate_replication| TRUE|   
instance_name| orcl2|   
instance_number| 2|   
local_listener| (DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=10.24.1.12)(PORT=1521))))|   
log_archive_dest_1| LOCATION=+dgdata/orcl/archivelog|   
log_archive_dest_2| SERVICE=standby LGWR ASYNC VALID_FOR=(ONLINE_LOGFILES, PRIMARY_ROLE) DB_UNIQUE_NAME=orcl|   
log_archive_dest_3|  |   
log_archive_dest_state_2| enable|   
log_archive_dest_state_3| DEFER|   
log_archive_format| %t_%s_%r.dbf|   
log_file_name_convert| /home/oracle/app/oradata/orcl, +dgdata/orcl/onlinelog|   
open_cursors| 300|   
pga_aggregate_target| 53687091200|   
plsql_warnings| DISABLE:ALL|   
processes| 3000|   
remote_listener| hisscan:1521|   
remote_login_passwordfile| EXCLUSIVE|   
resource_limit| TRUE|   
sec_case_sensitive_logon| FALSE|   
service_names| orcl|   
sessions| 4592|   
sga_target| 161061273600|   
spfile| +DGDATA/orcl/spfile/spfile.ora|   
standby_file_management| AUTO|   
thread| 2|   
undo_tablespace| UNDOTBS2|   
  
* * *

Back to init.ora Parameters   
Back to Top

### init.ora Multi-Valued Parameters

  * This section only displays parameters that have more one value 
  * '(NULL)' indicates a missing parameter value 
  * A blank in the End Snapshot indicates the same value as the BeginSnapshot

Parameter Name| Begin value| End value (if different)  
---|---|---  
control_files| +DGDATA/orcl/controlfile/control01.ctl|   
control_files| +DGDATA/orcl/controlfile/control02.ctl|   
db_file_name_convert| +dgdata/orcl/datafile|   
db_file_name_convert| /home/oracle/app/oradata/orcl|   
log_file_name_convert| +dgdata/orcl/onlinelog|   
log_file_name_convert| /home/oracle/app/oradata/orcl|   
  
* * *

Back to init.ora Parameters   
Back to Top

### RAC Statistics

| Begin| End  
---|---|---  
Number of Instances:|  2|  2  
  
Global Cache Load Profile 

| Per Second| Per Transaction  
---|---|---  
Global Cache blocks received:|  114.62|  2.58  
Global Cache blocks served:|  64.40|  1.45  
GCS/GES messages received:|  275.39|  6.19  
GCS/GES messages sent:|  283.94|  6.39  
DBWR Fusion writes:|  7.59|  0.17  
Estd Interconnect traffic (KB)|  1,541.43|   
  
Global Cache Efficiency Percentages (Target local+remote 100%) 

Buffer access - local cache %:|  99.93  
---|---  
Buffer access - remote cache %:|  0.05  
Buffer access - disk %:|  0.02  
  
Global Cache and Enqueue Services - Workload Characteristics 

Avg global enqueue get time (ms):|  0.0  
---|---  
Avg global cache cr block receive time (ms):|  0.8  
Avg global cache current block receive time (ms):|  1.1  
Avg global cache cr block build time (ms):|  0.0  
Avg global cache cr block send time (ms):|  0.0  
Global cache log flushes for cr blocks served %:|  1.4  
Avg global cache cr block flush time (ms):|  1.2  
Avg global cache current block pin time (ms):|  0.0  
Avg global cache current block send time (ms):|  0.0  
Global cache log flushes for current blocks served %:|  0.3  
Avg global cache current block flush time (ms):|  1.3  
  
Global Cache and Enqueue Services - Messaging Statistics 

Avg message sent queue time (ms):|  0.1  
---|---  
Avg message sent queue time on ksxp (ms):|  0.5  
Avg message received queue time (ms):|  0.0  
Avg GCS message process time (ms):|  0.0  
Avg GES message process time (ms):|  0.0  
% of direct sent messages:|  63.56  
% of indirect sent messages:|  35.70  
% of flow controlled messages:|  0.74  
  
* * *

Cluster Interconnect

  * if Public/Source at End snap is different a '*' is displayed

| Begin | End  
---|---|---  
Interface| IP Address| Pub| Source| Pub| Src  
public| 10.24.1.39|  | OS dependent software|  |   
  
##  RAC Statistics 

  * RAC Report Summary
  * Global Messaging Statistics
  * Global CR Served Stats
  * Global CURRENT Served Stats
  * Global Cache Transfer Stats
  * Interconnect Stats
  * Dynamic Remastering Statistics

  
Back to Top

* * *

  
Back to Top

### Global Messaging Statistics


Statistic| Total| per Second| per Trans  
---|---|---|---  
acks for commit broadcast(actual)| 341,133| 31.48| 0.71  
acks for commit broadcast(logical)| 418,071| 38.58| 0.87  
broadcast msgs on commit(actual)| 313,804| 28.96| 0.65  
broadcast msgs on commit(logical)| 313,804| 28.96| 0.65  
broadcast msgs on commit(wasted)| 41,579| 3.84| 0.09  
dynamically allocated gcs resources| 0| 0.00| 0.00  
dynamically allocated gcs shadows| 0| 0.00| 0.00  
flow control messages received| 0| 0.00| 0.00  
flow control messages sent| 0| 0.00| 0.00  
gcs apply delta| 0| 0.00| 0.00  
gcs assume cvt| 1| 0.00| 0.00  
gcs assume no cvt| 105,916| 9.77| 0.22  
gcs ast xid| 17| 0.00| 0.00  
gcs blocked converts| 262,827| 24.25| 0.55  
gcs blocked cr converts| 242,923| 22.42| 0.50  
gcs compatible basts| 4,487| 0.41| 0.01  
gcs compatible cr basts (global)| 61,533| 5.68| 0.13  
gcs compatible cr basts (local)| 291,838| 26.93| 0.61  
gcs cr basts to PIs| 0| 0.00| 0.00  
gcs cr serve without current lock| 0| 0.00| 0.00  
gcs dbwr flush pi msgs| 66,463| 6.13| 0.14  
gcs dbwr write request msgs| 52,344| 4.83| 0.11  
gcs delta msgs sent| 0| 0.00| 0.00  
gcs delta push aborted by cancel| 0| 0.00| 0.00  
gcs delta push aborted by remastering| 0| 0.00| 0.00  
gcs delta push cancelled| 0| 0.00| 0.00  
gcs delta push cancelled at master| 0| 0.00| 0.00  
gcs delta push cancelled by close| 0| 0.00| 0.00  
gcs delta push cancelled by consign| 0| 0.00| 0.00  
gcs delta push cancelled by cvt ping| 0| 0.00| 0.00  
gcs delta push cancelled by dwncvt| 0| 0.00| 0.00  
gcs delta push create pi| 0| 0.00| 0.00  
gcs delta update master msgs sent| 0| 0.00| 0.00  
gcs delta wait aborted by remastering| 0| 0.00| 0.00  
gcs delta wait cancelled| 0| 0.00| 0.00  
gcs error msgs| 0| 0.00| 0.00  
gcs force cr block only| 121| 0.01| 0.00  
gcs force cr grant| 23| 0.00| 0.00  
gcs force cr no current| 0| 0.00| 0.00  
gcs forward cr to pinged instance| 0| 0.00| 0.00  
gcs immediate (compatible) converts| 16,902| 1.56| 0.04  
gcs immediate (null) converts| 141,123| 13.02| 0.29  
gcs immediate cr (compatible) converts| 18,382| 1.70| 0.04  
gcs immediate cr (null) converts| 34,984| 3.23| 0.07  
gcs indirect ast| 201,146| 18.56| 0.42  
gcs indirect bidless ast| 58,067| 5.36| 0.12  
gcs indirect fg ast| 142,887| 13.19| 0.30  
gcs lms flush pi msgs| 0| 0.00| 0.00  
gcs lms write request msgs| 19,325| 1.78| 0.04  
gcs msgs process time(ms)| 55,061| 5.08| 0.11  
gcs msgs received| 2,721,596| 251.15| 5.65  
gcs new served by master| 5,891| 0.54| 0.01  
gcs out-of-order msgs| 17,425| 1.61| 0.04  
gcs pings refused| 1,229| 0.11| 0.00  
gcs pkey conflicts retry| 0| 0.00| 0.00  
gcs push delta| 0| 0.00| 0.00  
gcs queued converts| 91| 0.01| 0.00  
gcs reader bypass N->Xw ping local| 0| 0.00| 0.00  
gcs reader bypass N->Xw ping remote| 0| 0.00| 0.00  
gcs reader bypass grant X on assume| 0| 0.00| 0.00  
gcs reader bypass grant ast| 0| 0.00| 0.00  
gcs reader bypass grant fg ast| 0| 0.00| 0.00  
gcs reader bypass grant immediate| 0| 0.00| 0.00  
gcs recovery claim msgs| 0| 0.00| 0.00  
gcs refuse xid| 11| 0.00| 0.00  
gcs regular cr| 0| 0.00| 0.00  
gcs retry convert request| 67| 0.01| 0.00  
gcs share recovery bast| 0| 0.00| 0.00  
gcs side channel msgs actual| 120,686| 11.14| 0.25  
gcs side channel msgs logical| 1,248,191| 115.18| 2.59  
gcs stale cr| 462,752| 42.70| 0.96  
gcs undo cr| 12,923| 1.19| 0.03  
gcs write notification msgs| 3,347| 0.31| 0.01  
gcs writes refused| 214| 0.02| 0.00  
ges msgs process time(ms)| 2,813| 0.26| 0.01  
ges msgs received| 262,713| 24.24| 0.55  
global posts dropped| 0| 0.00| 0.00  
global posts queue time| 29| 0.00| 0.00  
global posts queued| 91| 0.01| 0.00  
global posts requested| 91| 0.01| 0.00  
global posts sent| 91| 0.01| 0.00  
implicit batch messages received| 55,770| 5.15| 0.12  
implicit batch messages sent| 75,680| 6.98| 0.16  
lmd msg send time(ms)| 560| 0.05| 0.00  
lms(s) msg send time(ms)| 0| 0.00| 0.00  
messages flow controlled| 17,579| 1.62| 0.04  
messages queue sent actual| 737,617| 68.07| 1.53  
messages queue sent logical| 267,681| 24.70| 0.56  
messages received actual| 2,794,105| 257.84| 5.80  
messages received logical| 2,984,309| 275.39| 6.19  
messages sent directly| 1,516,407| 139.93| 3.15  
messages sent indirectly| 851,674| 78.59| 1.77  
messages sent not implicit batched| 121| 0.01| 0.00  
messages sent pbatched| 960,150| 88.60| 1.99  
msgs causing lmd to send msgs| 113,185| 10.44| 0.23  
msgs causing lms(s) to send msgs| 180,855| 16.69| 0.38  
msgs received queue time (ms)| 116,998| 10.80| 0.24  
msgs received queued| 2,984,309| 275.39| 6.19  
msgs sent queue time (ms)| 54,176| 5.00| 0.11  
msgs sent queue time on ksxp (ms)| 1,449,992| 133.80| 3.01  
msgs sent queued| 906,443| 83.65| 1.88  
msgs sent queued on ksxp| 2,671,998| 246.57| 5.55  
number of broadcasted resources| 0| 0.00| 0.00  
number of ges deadlock detected| 0| 0.00| 0.00  
process batch messages received| 551,098| 50.85| 1.14  
process batch messages sent| 724,579| 66.86| 1.50  
  
* * *

  
Back to Top

### Global CR Served Stats


Statistic| Total  
---|---  
CR Block Requests| 350,354  
CURRENT Block Requests| 486,854  
Data Block Requests| 350,355  
Undo Block Requests| 11,754  
TX Block Requests| 12,761  
Current Results| 372,609  
Private results| 662  
Zero Results| 7,553  
Disk Read Results| 456,360  
Fail Results| 3  
Fairness Down Converts| 158,010  
Fairness Clears| 29,388  
Free GC Elements| 0  
Flushes| 5,251  
Flushes Queued| 0  
Flush Queue Full| 0  
Flush Max Time (us)| 0  
Light Works| 4,365  
Errors| 1  
  
* * *

  
Back to Top

### Global CURRENT Served Stats

  * Pins = CURRENT Block Pin Operations 
  * Flushes = Redo Flush before CURRENT Block Served Operations 
  * Writes = CURRENT Block Fusion Write Operations

Statistic| Total| % <1ms| % <10ms| % <100ms| % <1s| % <10s  
---|---|---|---|---|---|---  
Pins| 274| 100.00| 0.00| 0.00| 0.00| 0.00  
Flushes| 1,039| 33.97| 66.03| 0.00| 0.00| 0.00  
Writes| 82,198| 11.15| 85.18| 0.75| 1.60| 1.33  
  
* * *

  
Back to Top

##  Global Cache Transfer Stats 

  * Global Cache Transfer Stats
  * Global Cache Transfer Times (ms)
  * Global Cache Transfer (Immediate)
  * Global Cache Times (Immediate)

Back to Top

### Global Cache Transfer Stats

  * Immediate (Immed) - Block Transfer NOT impacted by Remote Processing Delays 
  * Busy (Busy) - Block Transfer impacted by Remote Contention 
  * Congested (Congst) - Block Transfer impacted by Remote System Load 
  * ordered by CR + Current Blocks Received desc

|  | CR | Current  
---|---|---|---  
Inst No| Block Class | Blocks Received| % Immed| % Busy| % Congst| Blocks Received| % Immed| % Busy| % Congst  
1| data block| 448,308| 74.58| 23.93| 1.49| 731,498| 93.47| 0.13| 6.40  
1| Others| 5,521| 98.90| 0.27| 0.83| 41,530| 98.89| 0.22| 0.89  
1| undo header| 9,174| 97.91| 1.26| 0.83| 2,821| 98.05| 1.24| 0.71  
1| undo block| 2,926| 98.87| 0.68| 0.44| 1| 100.00| 0.00| 0.00  
  
* * *

Back to Global Cache Transfer Stats   
Back to Top

### Global Cache Transfer Times (ms)

  * Avg Time - average time of all blocks (Immed,Busy,Congst) in ms 
  * Immed, Busy, Congst - Average times in ms 
  * ordered by CR + Current Blocks Received desc

|  | CR Avg Time (ms) | Current Avg Time (ms)  
---|---|---|---  
Inst No| Block Class | All| Immed| Busy| Congst| All| Immed| Busy| Congst  
1| data block| 0.87| 0.50| 2.01| 1.50| 1.16| 0.94| 1.52| 4.44  
1| others| 0.37| 0.37| 1.46| 0.34| 0.30| 0.30| 1.32| 0.31  
1| undo header| 0.29| 0.27| 1.32| 0.32| 0.36| 0.35| 1.61| 0.37  
1| undo block| 0.33| 0.32| 1.56| 0.58| 0.29| 0.29|  |   
  
* * *

Back to Global Cache Transfer Stats   
Back to Top

### Global Cache Transfer (Immediate)

  * Immediate (Immed) - Block Transfer NOT impacted by Remote Processing Delays 
  * % of Blocks Received requiring 2 or 3 hops 
  * ordered by CR + Current Blocks Received desc

|  |  | CR | Current  
---|---|---|---|---  
Src Inst#| Block Class | Blocks Lost| Immed Blks Received| % 2hop| % 3hop| Immed Blks Received| % 2hop| % 3hop  
1| data block| 0| 334,368| 100.00| 0.00| 683,754| 100.00| 0.00  
1| others| 0| 5,460| 100.00| 0.00| 41,069| 100.00| 0.00  
1| undo header| 0| 8,982| 100.00| 0.00| 2,766| 100.00| 0.00  
1| undo block| 0| 2,893| 100.00| 0.00| 1| 100.00| 0.00  
  
* * *

Back to Global Cache Transfer Stats   
Back to Top

### Global Cache Times (Immediate)

  * Blocks Lost, 2-hop and 3-hop Average times in (ms) 
  * ordered by CR + Current Blocks Received desc

|  |  | CR Avg Time (ms) | Current Avg Time (ms)  
---|---|---|---|---  
Src Inst#| Block Class | Lost Time| Immed| 2hop| 3hop| Immed| 2hop| 3hop  
1| data block|  | 0.50| 0.50|  | 0.94| 0.94|   
1| others|  | 0.37| 0.37|  | 0.30| 0.30|   
1| undo header|  | 0.27| 0.27|  | 0.35| 0.35|   
1| undo block|  | 0.32| 0.32|  | 0.29| 0.29|   
  
* * *

Back to Global Cache Transfer Stats   
Back to Top

##  Interconnect Stats 

  * Interconnect Latency Stats
  * Interconnect Throughput by Client
  * Interconnect Device Stats

Back to Top

### Interconnect Ping Latency Stats

  * Ping latency of the roundtrip of a message from this instance to 
  * target instances. 
  * The target instance is identified by an instance number. 
  * Average and standard deviation of ping latency is given in miliseconds 
  * for message sizes of 500 bytes and 8K. 
  * Note that latency of a message from the instance to itself is used as 
  * control, since message latency can include wait for CPU

Target Instance| 500B Ping Count| Avg Latency 500B msg| Stddev 500B msg| 8K Ping Count| Avg Latency 8K msg| Stddev 8K msg  
---|---|---|---|---|---|---  
1| 848| 0.31| 0.38| 848| 1.91| 7.87  
2| 848| 0.10| 0.03| 848| 0.09| 0.03  
  
* * *

Back to Interconnect Stats   
Back to Top

### Interconnect Throughput by Client

  * Throughput of interconnect usage by major consumers 
  * All throughput numbers are megabytes per second

Used By| Send Mbytes/sec| Receive Mbytes/sec  
---|---|---  
Global Cache| 0.38| 0.75  
Parallel Query| 0.00| 0.00  
DB Locks| 0.07| 0.07  
DB Streams| 0.00| 0.00  
Other| 0.00| 0.00  
  
* * *

Back to Interconnect Stats   
Back to Top

### Interconnect Device Statistics

  * Throughput and errors of interconnect devices (at OS level) 
  * All throughput numbers are megabytes per second

Device Name| IP Address| Public| Source| Send Mbytes/sec| Send Errors| Send Dropped| Send Buffer Overrun| Send Carrier Lost| Receive Mbytes/sec| Receive Errors| Receive Dropped| Receive Buffer Overrun| Receive Frame Errors  
---|---|---|---|---|---|---|---|---|---|---|---|---|---  
public| 10.24.1.39|  | OS dependent software | 0.00| 0| 0| 0| 0 | 0.00| 0| 0| 0| 0  
  
* * *

Back to Interconnect Stats   
Back to Top

### Dynamic Remastering Stats

  * times are in seconds 
  * Affinity objects - objects mastered due to affinity at begin/end snap

Name| Total| per Remaster Op| Begin Snap| End Snap  
---|---|---|---|---  
remaster ops| 2| 1.00|  |   
remastered objects| 2| 1.00|  |   
replayed locks received| 0| 0.00|  |   
replayed locks sent| 2,410| 1,205.00|  |   
resources cleaned| 0| 0.00|  |   
remaster time (s)| 4.9| 2.47|  |   
quiesce time (s)| 2.8| 1.39|  |   
freeze time (s)| 0.1| 0.03|  |   
cleanup time (s)| 0.5| 0.24|  |   
replay time (s)| 0.0| 0.01|  |   
fixwrite time (s)| 0.8| 0.38|  |   
sync time (s)| 0.9| 0.43|  |   
affinity objects|  |  | 191| 189  
  
* * *

  
Back to Top

End of Report 
