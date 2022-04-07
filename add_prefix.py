import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input','--input_dic')
    parser.add_argument('-output','--output_dic')
    parser.add_argument('-prefix','--prefix')
    parser.add_argument('-input_ord','--input_ord')
    parser.add_argument('-output_ord','--output_ord')
    parser.add_argument('-input_pre','--input_pre')
    parser.add_argument('-output_pre','--output_pre')
    args = parser.parse_args()

    return args

def get_len():

    args = parse_args()

    with open(args.input_ord,'r') as input:
        l = input.readlines()
    input.close()

    return len(l)

def main():
    args = parse_args()
    l = get_len()
    with open(args.input_dic,'r') as input:
        with open(args.output_dic,'w') as output:
            c = [args.prefix + '\n']
            input_lines = input.readlines()
            for line in input_lines:
                c.append(line)
            for word in c:
                output.write(word)
        output.close()
    input.close()
    
    with open(args.input_ord,'r') as input:
        with open(args.output_ord,'w') as output:
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                input_line.insert(0,args.prefix)

                for word in input_line:
                    output.write(word + ' ')
                output.write('\n')

        output.close()
    input.close()

    with open(args.input_pre,'r') as input:
        with open(args.output_pre,'w') as output:
            for i in range(l):
                input_line = input.readline()
                input_line = input_line.split()
                input_line.append(args.prefix)

                for word in input_line:
                    output.write(word + ' ')
                output.write('\n')

        output.close()
    input.close()


if __name__ == '__main__':
    main()

