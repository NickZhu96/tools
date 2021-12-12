import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input','--input')
    parser.add_argument('-output','--output')
    parser.add_argument('-clean_time','--t')

    args = parser.parse_args()

    return args
def get_len():

    args = parse_args()

    with open(args.input,'r') as input:
        l = input.readlines()
    input.close()

    return len(l)


def main():
    args = parse_args()
    l = get_len()
    with open(args.input,'r') as input:
        with open(args.output,'w') as output:
            all = []
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                for time in range(int(args.t)):
                    for k in range(len(input_line)-1):
                        if input_line[k] == input_line[k+1]:
                            input_line[k+1] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-3):
                        if input_line[k] == input_line[k+2] and input_line[k+1] == input_line[k+3]:
                            input_line[k+2] = ''
                            input_line[k+3] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-5):
                        if input_line[k] == input_line[k+3] and input_line[k+1] == input_line[k+4] and input_line[k+2] == input_line[k+5]:
                            input_line[k+3] = ''
                            input_line[k+4] = ''
                            input_line[k+5] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-7):
                        if input_line[k] == input_line[k+4] and input_line[k+1] == input_line[k+5] and input_line[k+2] == input_line[k+6] and input_line[k+3] == input_line[k+7]:
                            input_line[k+4] = ''
                            input_line[k+5] = ''
                            input_line[k+6] = ''
                            input_line[k+7] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-9):
                        if input_line[k] == input_line[k+5] and input_line[k+1] == input_line[k+6] and input_line[k+2] == input_line[k+7] and input_line[k+3] == input_line[k+8] and input_line[k+4] == input_line[k+9]:
                            input_line[k+5] = ''
                            input_line[k+6] = ''
                            input_line[k+7] = ''
                            input_line[k+8] = ''
                            input_line[k+9] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-11):
                        if input_line[k] == input_line[k+6] and input_line[k+1] == input_line[k+7] and input_line[k+2] == input_line[k+8] and input_line[k+3] == input_line[k+9] and input_line[k+4] == input_line[k+10] and input_line[k+5] == input_line[k+11]:
                            input_line[k+6] = ''
                            input_line[k+7] = ''
                            input_line[k+8] = ''
                            input_line[k+9] = ''
                            input_line[k+10] = ''
                            input_line[k+11] = ''
                for time in range(int(args.t)):
                    for k in range(len(input_line)-13):
                        if input_line[k] == input_line[k+7] and input_line[k+1] == input_line[k+8] and input_line[k+2] == input_line[k+9] and input_line[k+3] == input_line[k+10] and input_line[k+4] == input_line[k+11] and input_line[k+5] == input_line[k+12] and input_line[k+6] == input_line[k+13]:
                            input_line[k+7] = ''
                            input_line[k+8] = ''
                            input_line[k+9] = ''
                            input_line[k+10] = ''
                            input_line[k+11] = ''
                            input_line[k+12] = ''
                            input_line[k+13] = ''



                for word in input_line:
                    output.write(word + ' ')
                output.write('\n')
            
        output.close()
    input.close()

if __name__ == '__main__':
    main()
