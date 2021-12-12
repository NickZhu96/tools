import argparse
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input_ja','--input_ja')
    parser.add_argument('-alignment','--alignment')
    parser.add_argument('-output_preord_ja','--output_ja')

    args = parser.parse_args()

    return args

def get_len():

    args = parse_args()

    with open(args.alignment,'r') as align:
        l = align.readlines()
    align.close()

    return len(l)

def takeSecond(elem):
    return elem[1]

def main():

    args = parse_args()
    l = get_len()
    
    with open(args.input_ja,'r') as ja:
        with open(args.alignment,'r') as align:
            with open(args.output_ja,'w') as pre:
                        
                for i in range(l):
                    pp=[]
                    ja_line = ja.readline()
                    align_line = align.readline()
                            
                    ja_line =ja_line.split()
                    a= align_line.split()
                    del(ja_line[0])
                    del(a[0])
                    try:
                        for k in a:
                            ak = k.split('-')
                            pp.append([int(ak[0]),int(ak[1])])
                        #pp =np.array(pp)
                        #pp=pp[np.argsort(pp[:,1]),:]
                        #sorted(pp, key=lambda x: x[1])
                        pp.sort(key=takeSecond)
                        for kk in pp:
                            pre.write(ja_line[int(kk[0])] + ' ')
                    except:
                        pre.write(' ')
                    pre.write('\n')
#                            print(b)
#                            for kk in range(len(pp)):
#                                pre.write(ja_line[int(pp[1])] + ' ')
#                                ord.write(en_line[int(pp[0])] + ' ')
                            
#                            pre.write('\n')
#                            ord.write('\n')
                
            pre.close()
        align.close()
    ja.close()
    
if __name__ == '__main__':
    main()
