# FIX_wrapper
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
│   	 		  		  └─── account_position.csv  (account position)
│   	 		  		  │
│   	 		  		  └─── orders.csv		    (customer order)
│   	 		  		  │
│   	 		  		  └─── execu.csv			 (executed transactions)
│
└─── input
│      │
│      └─── FIX.09-Jan-2018.log          (input log file)
│
└─── output   (output files)
│   	│
│   	└─── account_position.csv  (account position)
│   	│
│   	└─── orders.csv		    (customer order)
│   	│
│       └─── execu.csv			 (executed transactions)
│   	│
│       └─── test_report.txt	   (unit test report)
│
└─── Design (UML design)
```