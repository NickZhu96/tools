with open('/root/work/span_align/alignment/jazh.align','r') as align:
    with open('/root/work/nmt/alignment/zh_ja_prefix/zh.pre.noclear.index','w') as pre:
        with open('/root/work/nmt/alignment/zh_ja/train.zh','r') as zh:
            with open('/root/work/nmt/alignment/zh_ja_prefix/zh.pre.noclear','w') as noclear:
                zh_lines = zh.readlines()
                align_lines = align.readlines()
                for i in range(18088):
                    zh_line = zh_lines[i]
                    align_line = align_lines[i]

                    zh_line = zh_line.split()
                    align_line = align_line.split()
                
                    for j in range(len(align_line)):
                        a = align_line[j].split('-')
                        noclear.write(zh_line[int(a[1])] + ' ')
                        pre.write(str(int(a[1])+1) +' ')
                    pre.write('0')
                    noclear.write('\n')
                    pre.write('\n')

