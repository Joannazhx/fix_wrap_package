from wrapper import *
import argparse

def parse(options):
    file_path = os.path.abspath(options.file)
    if not os.path.isfile(file_path):
        print("Can't find file, please try again")
        sys.exit()
    out_dir = os.path.abspath(options.out_dir)
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    
    w = Wrapper(file_path, out_dir)
    w.start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="drag log file here/input file path") #action="store_true")
    parser.add_argument("-o", "--out_dir", default="../output",
                        help="drag log file here/input file path") #action="store_true")
    options = parser.parse_args()
    parse(options)
    