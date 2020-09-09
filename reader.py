
from message import *

class Reader():

    def __init__(self, file_path):
        self.__file_path = file_path

    def read_log(self):
        log_file = open(self.__file_path, "r")
        lines = log_file.readlines()
        log_file.close()
        return lines

    def createMessage(self, mess):
        begin_string = mess['8']
        body_length = int(mess['9'])
        msg_type = mess['35']
        msg_seq_num = mess['34']
        target_comp_id = mess['49']
        sending_time = mess['52']
        h = Header(begin_string, body_length, msg_type, msg_seq_num, target_comp_id, sending_time)
        check_sum = mess['10']
        t = Trailer(check_sum)
        if msg_type == '0' or msg_type == '5':
            #heartbeat / logout
            return Message(h, t)
        elif msg_type == 'A':
            # logon
            heart_beat_int = mess['108']
            return LogOnMessage(h, t, heart_beat_int)
        else:
            #trade
            account = mess['1']
            price = int(mess['31'])
            qty = int(mess['32'])
            side = mess['54']
            code = str(mess['55'])
            print(code)
            time = mess['60']
            exec_type = mess['150']
            order_id = mess['11']
            return TradeMessage(h, t, account, price, qty, side, code, time, exec_type, order_id)


    def read_line(self, line):
        messages = (line.split("|\n")[0]).split("|")
        dict_mess = {}
        for field in messages:
            (key, value) = field.split("=")
            dict_mess[key] = value
        mess = self.createMessage(dict_mess)
        return mess
        
