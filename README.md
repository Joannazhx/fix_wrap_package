# FIX log file constructor
> Given the FIX log file extracted from integration testing, reconstruct the log file.

This is an efficient python implementation of reconstructing a standard FIX (Financial Information Exchange) log data messages from the platform build for a brokerage client.
<https://www.onixs.biz/fix-dictionary/4.4/index.html>
For a short definition of trading and positions to understand the log data <https://www.quora.com/What-is-the-difference-between-Orders-Trades-and-Positions-in-Forex-trading#:~:text=A%20position%20is%20exposure%20to,now%20you%20sell%20to%20close.>
 The program outputs 3 csv files containing the orders made by customer, executed trade transactions and the related account position of the relative orders.
```
FIX_wrapper
│
└─── src
│     │
│     └─── wrapper.py     (process log file)
│     │
│     └─── reader.py      (process data line by line)
│     │
│     └─── order.py       (order)
│     │
│     └─── order_pool.py  (order pool)
│     │
│     └─── message.py     (message)
│     │
│     └─── const.py       (const variables)
│     │
│     └─── main.py        (parser / entrance)
│
└─── unit_test
│   	 │
│   	 └─── order_test.py           (Order unit test cases)
│   	 │
│   	 └─── order_pool_test.py      (OrderPool unit test cases)
│   	 │
│   	 └─── message_test.py         (Message unit test cases)
│   	 │
│   	 └─── reader_test.py          (Reader unit test cases)
│   	 │
│   	 └─── test_wrap.py            (unit test execution-automatic loading)
│   	 │
│   	 └─── logs_test.py            (log files test cases)
│   	 │
│   	 └─── test_logs
│   	 		  │
│   	 		  └─── test1.txt / test2.txt   (input log files for test)
│   	 		  │
│   	 		  └─── output_1 / output_2     (expected results)
│   	 		  		  │
│   	 		  		  └─── account_position.csv
│   	 		  		  │
│   	 		  		  └─── orders.csv
│   	 		  		  │
│   	 		  		  └─── execu.csv
│
└─── input
│      │
│      └─── FIX.09-Jan-2018.log   (input log file)
│
└─── output   (output files)
│   	│
│   	└─── account_position.csv  	(account position)
│   	│
│   	└─── orders.csv		    	(customer order)
│   	│
│       └─── execu.csv			     (executed transactions)
│   	│
│       └─── test_report.txt	   	(unit test report)
│
└─── Design (UML design)
```
#Description
This program aims to analysis log file from integration testing, the test platform using standard FIX (Financial Information Exchange) protocol to instruct the client’s system to send orders and return the execution results. This platform receives orders from customer and make transcations.This program is able to reconstruct the log file and analysis orders and trade.
##The input data format
Every type include header and trailer
###Header
```
		+   -HEADER
    	|   8 @begin_string      = FIX.4.4
    	|   9 @body_length       = 178
    	|   35 @msg_type         = Logon (A)
    						   	   Logout (5)
                                   Heart beat (0)
                                   Execution Report (8)
    	|   34 @msg_seq_num      = 1
    	|   49 @sender_comp_id   = testusr4109
    	|   52 @sending_time     = 20101124-20:27:25.000
    	|   56 @target_comp_id   = WIKIPEDIA
```
###Trailer
```
    	|   10  @check_sum         = 133
```

### 1. Heart Beat / Log Out
```
        @header
        @trailer
```
Heart beat
8=FIX.4.4	|	9=55	|	35=0	|	34=9	|	49=FIXSIM|52=20180109-00:03:33.438	|	56=QFSAMPLE	|	10=067	|

LogOut
8=FIX.4.4	|	9=55	|	35=5	|	34=1	|	49=FIXSIM	|	52=20180109-04:56:33.624	|	56=QFSAMPLE	|	10=073	|

### 2. Log On
```
		@header
        +   BODY
        |  108 @heart_beat_int       = 300
        |  141 @reset_seq_num_flag   = Y
        @trailer
```
LogOn
8=FIX.4.4	|	9=73	|	35=A	|	34=1	|	49=FIXSIM	|	52=20180109-00:00:03.618	|	56=QFSAMPLE	|	98=0	|	108=30	|	141=Y	|	10=140	|

###3. Trade / New Order
```
		@header
        +   BODY
        |   1    @account        = TEST1234
        |   31   @price          = 25
        |   32   @quantity       = 3
        |   54   @side           = 1 (Buy)
        						   2 (Sell)
        |   55   @code           = 0700
        |   60   @time           = 20180109-07:01:07
        |   150  @exec_type      = 0 (New)
        						   F (Trade partial fill / fill)
        |   11   @order_id       = 30636510780671786000
        |   6    @aver_price     = 25
        |   151  @left_qty       = 50
        |   14   @sum_qty        = 50
        @trailer
```
New Order
8=FIX.4.4	|	9=232	|	35=8	|	34=242	|	49=FIXSIM|52=20180109-07:01:01.905	|	56=QFSAMPLE	|	1=TEST1234	|	6=0	|	11=QO37NA54U3C8NTYKHDT15N4_0	|	14=0	|	17=2636510780617342000	|	31=0	|	32=0	|	37=2636510780617342000	|	38=100	|	39=0	|	54=1	|	55=0700	|	60=20180109-07:01:01	|	150=0	|	151=100	|	207=HKE	|	10=226	|
Trade
8=FIX.4.4	|	9=235	|	35=8	|	34=249	|	49=FIXSIM|52=20180109-07:01:04.214	|	56=QFSAMPLE	|	1=TEST1234	|	6=25	|	11=QO37NA54U3C8NTYKHDT15N4_0	|	14=50	|	17=9636510780641834000	|	31=25	|	32=50	|	37=9636510780641834000	|	38=100	|	39=1	|	54=1	|	55=0700	|	60=20180109-07:01:04	|	150=F	|	151=50	|	207=HKE	|	10=194	|
