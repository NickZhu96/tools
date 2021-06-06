DATA_FILE=../ALT_corpus/ALT_dataset_token/train.concat
MODEL_NAME_OR_PATH=../../m-bert
OUTPUT_FILE=./out
input1=../ALT_corpus/ALT_dataset_token/train.zh
input2=../ALT_corpus/ALT_dataset_token/train.en
output1=./extract_zh
output2=./extract_en

wc -l ../ALT_corpus/ALT_dataset_token/train.zh | awk '{print $1}' > num
paste $input1 $input2 | awk -F '\t' '{print $1 " ||| " $2}' > $DATA_FILE

CUDA_VISIBLE_DEVICES=0,1 awesome-align \
    --output_file=$OUTPUT_FILE \
    --model_name_or_path=$MODEL_NAME_OR_PATH \
    --data_file=$DATA_FILE \
    --extraction 'softmax' \
    --batch_size 32

python ../../extract_alignment_to_dic.py \
    --input1 $input1 \
    --input2 $input2 \
    --output1 $output1 \
    --output2 $output2 \
    --alignment ./out 

paste $output1 $output2 > dic_

sort dic_ > dic__

cat dic__ | uniq > dic

rm dic_ dic__
