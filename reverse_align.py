with open('/root/work/span_align/alignment/edict.en-ja.align','r') as alignment:
    with open('/root/work/span_align/alignment/edict.ja-en.align','w') as reverse_alignment:
        align_lines = alignment.readlines()
        for align in align_lines:
            a=[]
            if align == []:
                reverse_alignment.write('\n')
                
            align_line = align.split()
            for map in align_line:
                aa = map.split('-')
                a.append([int(aa[1]),int(aa[0])])
            a.sort()
            for _ in a:
                reverse_alignment.write(str(_[0])+'-'+str(_[1])+' ')
            reverse_alignment.write('\n')
    reverse_alignment.close()
alignment.close()
            
