#利用BERT生成cls位置embedding的脚本
#输入是row文本
#输出是对应文本的768维度向量



from transformers import BertTokenizer, BertModel
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input','-i',help = 'input file')
parser.add_argument('--output','-o',help = 'output file')

args = parser.parse_args()



with open('{}'.format(args.input),'r') as f1:
    lines = f1.readlines()
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertModel.from_pretrained("bert-base-uncased")
    a = []
    count = 0
    for line in lines:
        
        encoded_input = tokenizer(line, return_tensors='pt')
        output = model(**encoded_input)
        a.append(output[0][0][0].tolist())
        print(line)
        print(np.array(a[count]))
        count = count + 1
    np.savetxt('{}'.format(args.output),np.array(a))
f1.close()
