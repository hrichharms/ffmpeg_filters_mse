from os import mkdir, system, listdir
from os.path import isdir, join
from json import load

from config import (
    CONFIG_FILENAME,
    load_config
)


if __name__ == "__main__":

    config = load_config(CONFIG_FILENAME)

    if not isdir(config.distorted_audio_dir):
        mkdir(config.distorted_audio_dir)

    with open(config.filters_filename) as filters_file:
        filters = load(filters_file)

    for filter_name in filters:
        for filename in listdir(config.original_audio_dir):
            system(f"ffmpeg -i {join(config.original_audio_dir, filename)} \
-af {filter_name} distorted_audio/{filter_name}_{filename}")
