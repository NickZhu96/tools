DATA_FILE=./ja_en/train_concat
MODEL_NAME_OR_PATH=../../m-bert
OUTPUT_FILE=./ja_en/align_output
input1=./ja_en/_en
input2=./ja_en/_ja
output1=./ja_en/extract_en
output2=./ja_en/extract_ja

#wc -l $input1 | awk '{print $1}' > num
#paste $input1 $input2 | awk -F '\t' '{print $1 " ||| " $2}' > $DATA_FILE

#CUDA_VISIBLE_DEVICES=0,1 awesome-align \
#    --output_file=$OUTPUT_FILE \
#    --model_name_or_path=$MODEL_NAME_OR_PATH \
#    --data_file=$DATA_FILE \
#    --extraction 'softmax' \
#    --batch_size 32

python ../../extract_alignment_to_dic.py \
    --input1 $input1 \
    --input2 $input2 \
    --output1 $output1 \
    --output2 $output2 \
    --alignment $OUTPUT_FILE

cd ./ja_en

paste extract_ja extract_en > dic_ 
sed -i -e '/%q/d' dic_
sed -i -e '/%a/d' dic_
sort dic_ > dic__ 
uniq -c dic__ > dic___ 
sort -n -r dic___ > dic

rm dic_ dic__ dic___ ../num
#cat dic__ | uniq > dic

#rm dic_ dic__ num
