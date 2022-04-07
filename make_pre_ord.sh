source=th
target=ja

DIR=/root/work/nmt/alignment/th_ja_awesome
language1=/root/work/nmt/alignment/tools/train.$target
language2=/root/work/nmt/alignment/tools/train.$source
Alignment=/root/work/awesome-align/alignment/alt_jath_align


ord_language1=/root/work/nmt/alignment/th_ja_awesome/ord.$target
ord_language2=/root/work/nmt/alignment/th_ja_awesome/ord.$source
pre_language2=/root/work/nmt/alignment/th_ja_awesome/pre.$source


cd /root/work/ja_thai_alt
cat train.*.truecase.$source valid.*.truecase.$source test.*.truecase.$source > $source

cd -




DIC=/root/work/ja_thai_alt/th

test1=/root/work/ja_thai_alt/test.detok.truecase.$source



mkdir -p $DIR
mkdir $DIR/test

echo 'doing the preordering...'

python preord.py -i1 $language1 -i2 $language2 -align $Alignment -ord $ord_language1 -pre $pre_language2

echo 'cleaning...'

python clean_up_repeat.py -input $pre_language2 -output _ -clean_time 5
python clean_up_repeat.py -input _ -output __ -clean_time 5
python clean_up_repeat.py -input __ -output ___ -clean_time 5
python clean_up_repeat.py -input ___  -output ____ -clean_time 5
python clean_up_repeat.py -input ____ -output _____ -clean_time 5

rm _ __ ___ ____
mv _____ $DIR/pre.$source.clean

echo 'extracting normal order sentence...'

python normal_ord.py -i2 $language2 -align $Alignment -ord $ord_language2

echo 'cleaning...'

python clean_up_repeat.py -input $ord_language2 -output _ -clean_time 5
python clean_up_repeat.py -input _ -output __ -clean_time 5
python clean_up_repeat.py -input __ -output ___ -clean_time 5 
python clean_up_repeat.py -input ___  -output ____ -clean_time 5
python clean_up_repeat.py -input ____ -output _____ -clean_time 5

rm _ __ ___ ____
mv _____ $DIR/ord.$source.clean

echo 'make dic...'

python build_dic.py -input $DIC -output $DIR/dic

echo 'cut_length'
cp $DIR/ord.$source.clean $DIR/_.ord
cp $DIR/pre.$source.clean $DIR/_.pre

perl /root/work/mosesdecoder/scripts/training/clean-corpus-n.perl -ratio 2  $DIR/_ ord pre $DIR/$source 1 120

rm  $DIR/_.ord  $DIR/_.pre
echo 'turn tokens into index'

python from_word_to_num.py -d $DIR/dic -pre $DIR/$source.pre -ord $DIR/$source.ord -ord_num $DIR/$source.ord.num -pre_num $DIR/$source.pre.num
python lookup_dic.py -d $DIR/dic -t $test1 -o $DIR/test.$source.num
