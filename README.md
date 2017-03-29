# GSOC-aerospaceresearch 
>This idea will be about a scheduler. Managing the different tasks. For
example:
tuning to another band at different times based on a scheduler list.
if no scheduled tasks are there, follow a "scanning" routine for example
listening to one band like the ADSB (planes) band on 1090mhz. Or you can
decide what else can be tuned on.  

The program is a very crude form of scheduler that schedules tasks as mentioned above on the basis of time.  
Their are many issues to be worked out such as using POSIX time, etc. Currently i'm looking into sched library of python to better the code.  
The time will be feeded in the string format as mentioned and the code has been written as the above example.  
