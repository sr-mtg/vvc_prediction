#!/bin/bash
mkdir all_of_result
list_video="/home/ubuntu/Crawl_result/list_of_video.txt"
url_video="/home/ubuntu/Crawl_result/link_of_video.txt"
line_number=1
max_line=$(wc -l < "$url_video")
#max_line=1
while [ "$line_number" -le "$max_line" ]; do
    url=$(sed -n "${line_number}p" "$url_video")
    name=$(sed -n "${line_number}p" "$list_video")
    mkdir vidoe
    cd vidoe
    mkdir result 
    wget $url
    ffmpeg -i $name -pix_fmt yuv420p output.yuv > $name.yuv.txt 2>&1
    #not use yuv beacuse  Error reading FRAME tag
    ffmpeg -i $name -f yuv4mpegpipe - | ~/VCA/build/source/apps/vca/vca --y4m --input stdin --complexity-csv $name.csv > $name.vca.txt 2>&1
    #you can set QP with -x265-params "qp=<QP_VALUE>" or -x264-params "qp=<QP_VALUE>" 
    ffmpeg -s:v 3840x2160 -r 1199/50 -i output.yuv -c:v libx264 -preset medium output_h264.264 > $name.264.txt 2>&1
    ffmpeg -s:v 3840x2160 -r 1199/50 -i output.yuv -c:v libx265 -preset medium output_h265.265 > $name.265.txt 2>&1
    cp *.txt result/
    cp *.csv result/
    cp result/* ../all_of_result/
    cd ..
    rm -rf vidoe
    ((line_number++))  #
done
