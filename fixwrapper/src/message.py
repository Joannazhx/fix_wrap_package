import re

class Header():

    def __init__(self, begin_string, body_length, msg_type, msg_seq_num, target_comp_id, sending_time):
        self.__begin_string = begin_string# = mess['8']
        self.__body_length = body_length # = mess['9']
        self.__msg_type = msg_type # = mess['35']
        self.__msg_seq_num = msg_seq_num # = mess['34']
        self.__target_comp_id = target_comp_id # = mess['56']
        self.__sending_time = sending_time # = mess['52']

    def setBeginString(self, begin_string):
        self.__begin_string = begin_string

    def setBodyLength(self, body_length):
        self.__body_length = body_length

    def setMsgType(self, msg_type):
        self.__msg_type = msg_type

    def setMsgSeqNum(self, msg_seq_num):
        self.__msg_seq_num = msg_seq_num
    
    def setTargetCompId(self, target_comp_id):
        self.__target_comp_id = target_comp_id

    def setSendingTime(self, sending_time):
        self.__sending_time = sending_time

    def getBeginString(self):
        return self.__begin_string 

    def getBodyLength(self):
        return self.__body_length

    def getMsgType(self):
        return self.__msg_type

    def getMsgSeqNum(self):
        return self.__msg_seq_num
    
    def getTargetCompId(self):
        return self.__target_comp_id

    def getSendingTime(self):
        return self.__sending_time

class Trailer():
    def __init__(self, check_sum):
        self.__check_sum = check_sum # mess['10']

    def setCheckSum(self, check_sum):
        self.__check_sum = check_sum
    
    def getCheckSum(self):
        return self.__check_sum


class Message():

    def __init__(self,header,trailer):
        self.__header = header
        self.__trailer = trailer
    
    def getHeader(self):
        return self.__header

    def getTrailer(self):
        return self.__trailer
    

class LogOnMessage(Message):

    def __init__(self, header, trailer, heart_beat_int, reset_seq_num_flag=True):
        super().__init__(header, trailer)
        self.__heart_beat_int = heart_beat_int
        self.__reset_seq_num_flag = reset_seq_num_flag

    def setHeartBeatInt(self, heart_beat_int):
        self.__heart_beat_int = heart_beat_int

    def setResetSeqNumFlag(self, reset_seq_num_flag):
        self.__reset_seq_num_flag = reset_seq_num_flag

    def getHeartBeatInt(self):
        return self.__heart_beat_int

    def getResetSeqNumFlag(self):
        return self.__reset_seq_num_flag 

class TradeMessage(Message):

    def __init__(self, header, trailer, account, price, quantity, side, code, 
                    time, exec_type, order_id, aver_price, left_qty, sum_qty):
        super().__init__(header, trailer)
        self.__account = account
        self.__price = price
        self.__quantity = quantity
        if side == '1':
            self.__side = "buy"
        elif side == '2':
            self.__side = "sell"
        else:
            self.__side = side
        self.__code = re.sub('^', r"\t", code) # save start '0' in csv file
        self.__time = time
        self.__exec_type = exec_type
        self.__order_id = order_id
        self.__aver_price = aver_price
        self.__left_qty = left_qty
        self.__sum_qty = sum_qty

    def getAverPrice(self):
        return self.__aver_price

    def setAverPrice(self, aver_price):
        self.__aver_price = aver_price

    def getLeftQty(self):
        return self.__left_qty

    def setLeftQty(self, left_qty):
        self.__left_qty = left_qty

    def getSumQty(self):
        return self.__sum_qty

    def setSumQty(self, sum_qty):
        self.__sum_qty = sum_qty

    def getOrderId(self):
        return self.__order_id

    def setOrderId(self, order_id):
        self.__order_id = order_id

    def setExecType(self, exec_type):
        self.__exec_type = exec_type
    
    def getExecType(self):
        return self.__exec_type

    def setAccount(self, account):
        self.__account = account
    
    def setPrice(self, price):
        self.__price = price

    def setQuantity(self, quantity):
        self.__quantity = quantity
    
    def setSide(self, side):
        if side == '1':
            self.__side = "buy"
        elif side == '2':
            self.__side = "sell"
        else:
            self.__side = side
    
    def setCode(self, code):
        self.__code = code
    
    def setTime(self, time):
        self.__time = time

    def getAccount(self):
        return self.__account
    
    def getPrice(self):
        return self.__price 

    def getQuantity(self):
        return self.__quantity
    
    def getSide(self):
        return self.__side
    
    def getCode(self):
        return self.__code 
    
    def getTime(self):
        return self.__time

    def execMessageFormat(self):
        return [str(self.getCode()), self.getQuantity(), self.getPrice(), 
                self.getSide(), self.getAccount(), self.getOrderId(), self.getTime()]

    def orderMessageFormat(self):
        return [str(self.getCode()), self.getAccount(), self.getLeftQty(), 
                self.getSide(), self.getOrderId(), self.getTime()]