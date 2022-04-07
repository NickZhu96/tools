source=zh
target=ja

DIR=/root/work/nmt/alignment/zh_ja_prefix
language1=/root/work/nmt/alignment/zh_ja/train.$target
language2=/root/work/nmt/alignment/zh_ja/train.$source
Alignment=/root/work/span_align/alignment/jazh.align

ord_language1=/root/work/nmt/alignment/zh_ja_prefix/ord.$target
ord_language2=/root/work/nmt/alignment/zh_ja_prefix/ord.$source
pre_language2=/root/work/nmt/alignment/zh_ja_prefix/pre.$source

prefix='<zh>'

#cd /root/work/alignment/zh_ja
#cat train.*.truecase.$source valid.*.truecase.$source test.*.truecase.$source > $source
cd /root/work/nmt/alignment/zh_ja
cat train.zh test.zh > $source

cd -




DIC=/root/work/nmt/alignment/zh_ja/$source


test1=/root/work/nmt/alignment/zh_ja/test.$source



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


echo 'make dic...'

python build_dic.py -input $DIC -output $DIR/dic

echo 'cut_length'
cp $language2 $DIR/_.ord
cp $DIR/pre.$source.clean $DIR/_.pre

perl /root/work/mosesdecoder/scripts/training/clean-corpus-n.perl -ratio 2  $DIR/_ ord pre $DIR/$source 1 120

rm  $DIR/_.ord  $DIR/_.pre

python add_prefix.py --input_dic $DIR/dic --output_dic $DIR/dic_prefix -prefix $prefix -input_ord $DIR/$source.ord -output_ord $DIR/$source.ord.prefix -input_pre $DIR/$source.pre -output_pre $DIR/$source.pre.prefix

echo 'turn tokens into index'

python from_word_to_num.py -d $DIR/dic_prefix -pre $DIR/$source.pre.prefix -ord $DIR/$source.ord.prefix -ord_num $DIR/$source.ord.prefix.num -pre_num $DIR/$source.pre.prefix.num

python add_prefix_for_test.py --input $test1 --output $DIR/test.$source.prefix --prefix $prefix

python lookup_dic.py -d $DIR/dic_prefix -t $DIR/test.$source.prefix -o $DIR/test.$source.prefix.num
