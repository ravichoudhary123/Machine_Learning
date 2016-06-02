Problem 1: Predict the portion of time (%) that the cpu is run in user mode (as opposed to system mode, waiting for IO, or idle) from various system activity measures collected from a Sun Sparc station 20/712 with 128 Mbytes of memory running in a multi-user university department.

Feature Information:

lread - Reads (transfers per second ) between system memory and user memory
lwrite - writes (transfers per second) between system memory and user memory
scall - Number of system calls of all types per second
sread - Number of system read calls per second .
swrite - Number of system write calls per second .
fork - Number of system fork calls per second.
exec - Number of system exec calls per second.
rchar - Number of characters transferred per second by system read calls
wchar - Number of characters transferred per second by system write calls
pgout - Number of page out requests per second
ppgout - Number of pages, paged out per second
pgfree - Number of pages per second placed on the free list.
pgscan - Number of pages checked if they can be freed per second
atch - Number of page attaches (satisfying a page fault by reclaiming a page in memory) per second
pgin - Number of page-in requests per second
ppgin - Number of pages paged in per second
pflt - Number of page faults caused by protection errors (copy-on-writes).
vflt - Number of page faults caused by address translation .
runqsz - Process run queue size
freemem - Number of memory pages available to user processes
freeswap - Number of disk blocks available for page swapping.

============================================================================================================================

Problem 2: Predict a community’s median house value in California from various census statistics.

Feature Information:

longitude: continuous.
latitude: continuous.
housingMedianAge: continuous. 
totalRooms: continuous. 
totalBedrooms: continuous. 
population: continuous. 
households: continuous. 
medianIncome: continuous. 
