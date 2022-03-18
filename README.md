# ffmpeg_filters_mse

Calculates and visualizes the mean squared error of ffmpeg audio filters in the temporal domain and frequency domain.

## Setup:

### FFMPEG Installation

## Repository Files:

### convert.sh

Small shellscript that converts any audio files in `original_audio` into a .wav file using default ffmpeg conversion

#### Usage

`./convert.sh`

### filters.json

JSON formatted list of ffmpeg audio filters

### config.json

Configuration file for `apply_filters.py` and `stats_calc.py`

| key                 | default         | description                                                                   |
|---------------------|-----------------|-------------------------------------------------------------------------------|
| filters_filename    | filters.json    | filename of filters list in JSON file format                                  |
| segment_len         | 262144          | number of audio samples in each analyzed segment                              |
| sample_skips        | 262144          | number of samples skipped between beginnings of analyzed segments             |
| bit_depth           | 16              | bit depth of analyzed audio                                                   |
| original_audio_dir  | original_audio  | relative path to search for original audio                                    |
| distorted_audio_dir | distorted_audio | relative path to write filtered audio data to                                 |
| output_filename     | output.json     | filename to write temporal and frequency mean squared error to in JSON format |

### config.py

Defines `CONFIG_FILENAME`, `Config` class, and associated JSON loader function (`load_config`).

### apply_filters.py

Loads configuration from `CONFIG_FILENAME`, applies list of ffmpeg audio filters from `filters_filename` to .wav files in `original_audio_dir` and writes resulting audio files to `distorted_audio_dir`.

#### Usage

`python3 apply_filters.py`

### stats_calc.py

Loads configuration from `CONFIG_FILENAME`,

### visualize.py

## Example Figures

### Temporal Domain MSE

<img src="https://github.com/hrichharms/ffmpeg_filters_mse/blob/master/figures/Temporal_Mean_Square_Error_(MSE).png?raw=true" alt="Mean Squared Error in the Temporal Domain" width="400"/>

### Frequency Domain MSE

<img src="https://github.com/hrichharms/ffmpeg_filters_mse/blob/master/figures/Frequency_Mean_Square_Error_(MSE).png?raw=true" alt="Mean Squared Error in the Frequency Domain" width="400"/>

## TODO:
