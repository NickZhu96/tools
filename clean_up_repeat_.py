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
            count = 0
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                for time in range(int(args.t)):
                    for j in range(1,4):
                        for k in range(l-j-j):
                            if input_line[k:k+j] == input_line[k+j:k+j+j]:
                                input_line[k+j:k+j+j] = ''
                print(count+1)
                count = count+1
                for word in input_line:
                    output.write(word + ' ')
                output.write('\n')
                       
        output.close()
    input.close()

if __name__ == '__main__':
    main()
