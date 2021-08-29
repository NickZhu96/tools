import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input','--input')
    parser.add_argument('-output','--output')

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
            c = []
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                for word in input_line:
                    if word not in c:
                        c.append(word)
            for word in c:
                output.write(word + '\n')
        output.close()
    input.close()

if __name__ == '__main__':
    main()
