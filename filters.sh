#! /bin/bash

# define list of filters
FILTERS=(acompressor acontrast acrusher)

# if distorted_audio doesn't exist, create it
if [ ! -d distorted_audio ]; then
    mkdir distorted_audio
fi

# apply filters and write outputs to distorted_audio
for filter in ${FILTERS[*]}; do
    for filename in original_audio/*.wav; do
        dirs_removed=${filename##*/}
        ext_removed=${dirs_removed%.*}
        ffmpeg -i $filename -af $filter distorted_audio/${ext_removed}_${filter}.wav
    done
done
