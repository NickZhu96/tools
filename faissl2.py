#faiss工具
#python faissl2.py -db DATABASE() -q QUERY
#两个以上vector适用，不论database还是query
#输出的数字为query对应的database里面的行数
#dim = 维度

import numpy as np
import faiss
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--database','-db', help = 'input a database')
parser.add_argument('--query','-q',help = 'input a query vector')
parser.add_argument('--dim','-d',help = 'dim of the vectors')
parser.add_argument('--numbern','-num',help = 'find the Nbest of the vector')
args = parser.parse_args()

v_db = np.loadtxt("{}".format(args.database))
q_v = np.loadtxt("{}".format(args.query))



v_db = np.float32(v_db)
q_v = np.float32(q_v)



cpu_index = faiss.IndexFlatL2(int(args.dim))   # build the index
gpu_index = faiss.index_cpu_to_all_gpus(cpu_index)
gpu_index.add(v_db)                  # add vectors to the     index
k = 4                # we want to see 4 nearest     neighbors
D,I = gpu_index.search(q_v, k)     # actual search
print(I)      # neighbors of the 5 first queries          
for id in I:
    print(id[int(args.numbern)-1] + 1)
