import base64
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input','-i', help = 'input a file with base64 encoded')
parser.add_argument('--output','-o', help = 'output a file with raw text')

args = parser.parse_args()

f1 = open( '{}'.format(args.input), 'r' )
f2 = open('{}'.format(args.output), 'wb+')



file = f1.readlines()

file = ''.join(file)

str = base64.b64decode(file)

print(str)

f2.write(str)


f1.close()
f2.close()


