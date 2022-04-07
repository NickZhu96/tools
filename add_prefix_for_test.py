import argparse
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input','--input')
    parser.add_argument('-output','--output')
    parser.add_argument('-prefix','--prefix')
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
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                input_line.insert(0,args.prefix)
                for word in input_line:
                    output.write(word + ' ')
                output.write('\n')

        output.close()
    input.close()


if __name__ == '__main__':
    main()
