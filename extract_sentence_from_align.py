import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_ja','--input_ja')
    parser.add_argument('-input_en','--input_en')
    parser.add_argument('-alignment','--alignment')
    parser.add_argument('-output_ord_en','--output_en')
    parser.add_argument('-output_preord_ja','--output_ja')
    parser.add_argument('-output_ord_ja','--output_ordja')

    args = parser.parse_args()

    return args

def get_len():

    args = parse_args()

    with open(args.alignment,'r') as align:
        l = align.readlines()
    align.close()

    return len(l)


def extract_sentence_to_ord():

    args = parse_args()
    l = get_len()

    with open(args.input_ja,'r') as ja:
        with open(args.alignment,'r') as align:
            with open(args.output_ordja,'w') as ord_ja:
    
                for i in range(l):
                    c = []
                    
                    ja_line =ja.readline()
                    align_line = align.readline()
                    
                    ja_line = ja_line.split()
                    a = align_line.split()
                    
                    for k in range(len(a)):
                        b = a[k].split("-")
                        c.append(int(b[1]))
                    
                    c.sort()
                    
                    for num in c:
                        ord_ja.write(ja_line[int(num)] + ' ')
                    ord_ja.write('\n')
            
            ord_ja.close()
        align.close()
    ja.close()
    

def main():

    args = parse_args()
    l = get_len()
    
    with open(args.input_ja,'r') as ja:
        with open(args.alignment,'r') as align:
            with open(args.input_en,'r') as en:
                with open(args.output_ja,'w') as pre:
                    with open(args.output_en,'w') as ord:
                        
                        for i in range(l):
                            ja_line = ja.readline()
                            align_line = align.readline()
                            en_line = en.readline()
                            
                            ja_line =ja_line.split()
                            en_line =en_line.split()
                            a= align_line.split()
                            
                            for k in range(len(a)):
                                b = a[k].split("-")
#                            print(b)
                                pre.write(ja_line[int(b[1])] + ' ')
                                ord.write(en_line[int(b[0])] + ' ')
                            
                            pre.write('\n')
                            ord.write('\n')
                
                    ord.close()
                pre.close()
            en.close()
        align.close()
    ja.close()
    
if __name__ == '__main__':
    main()
    extract_sentence_to_ord()
