import os,csv

Stocks = {}

#read log line by line
def read_log(filepath):
    log_file = open(filepath, "r")
    lines = log_file.readlines()
    log_file.close()
    return lines

def process_log(lines):
    rows = []
    for line in lines:
        if line[0] == '#':
            continue
        mess = decode_line(line)
        #ignore heartbeat
        if mess['35'] == '8' and mess['150'] == 'F':
            rows.append(trans_wrap(mess))
    return rows



# decode each line to a string[](split)
def decode_line(line):
    messages = (line.split("|\n")[0]).split("|")
    dict_mess = {}
    for field in messages:
        (key, value) = field.split("=")
        dict_mess[key] = value
    # print(dict_mess['35'])
    return dict_mess

def trans_wrap(mess):

    side = ''
    if mess['54'] == 1:
        side = "Buy"
    else:
        side = 'Sell'

    return [mess['55'], mess['32'], mess['31'], side, mess['1'], mess['17'], mess['60']]




#output as requested to csv file
def csv_wrap(rows):
    with open("test.csv","w") as csvfile: 
        writer = csv.writer(csvfile)

        #先写入columns_name
        writer.writerow(["Stock Code","Transaction Quantity","Transaction Price", "Transaction Side", "Account", "Transaction Reference ID", "Transaction Time"])
        #写入多行用writerows
        writer.writerows(rows)

#check each message 10 legnth*256 = checksum
def checkSum():
    pass




# time format transfer
def time_format():
    pass

# add unit test cases
def Unit_test():
    pass


#advance
class Message(object):
    pass

class Unit_test(object):
    pass

if __name__ == "__main__":
    dir_path = os.path.abspath(os.path.dirname(__file__))
    # file_p = os.path.abspath(os.path.join(dir_path, "FIX.09-Jan-2018.log"))
    # print("file path : {}".join(file_p))
    # file_path = input("file :")
    file_path = "/Users/joanna/Desktop/jobs/OnGoing/quantifeed/FIX.09-Jan-2018.log"
    lines = read_log(file_path)
    #line = lines[0]
    rows = process_log(lines)
    csv_wrap(rows)
    pass
# GUI