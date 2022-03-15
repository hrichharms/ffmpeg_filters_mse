#! /bin/bash

for f in original_audio/*; do
    ffmpeg -i $f  ${f%.*}.wav
    rm $f
done