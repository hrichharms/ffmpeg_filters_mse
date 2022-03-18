# ffmpeg_filters_mse

Calculates and visualizes the mean squared error of ffmpeg audio filters in the temporal domain and frequency domain.

## Setup

1. Install [ffmpeg](https://ffmpeg.org/download.html)
2. Install required Python packages ( `pip3 install -r requirements.txt` )
3. Create `original_audio` directory
4. Put original audio in `original_audio` directory

## Usage

1. Run `convert.sh` if audio files are not in .wav format
2. Run `apply_filters.py` to create filtered audio files
3. Run `mse.py` to calculate the mean square error for each filter
4. Run `visualize.py` to visualize the results as bar graphs

## Repository Files

### convert.sh

Converts any audio files in `original_audio` into a .wav file using default ffmpeg conversion and deletes originals.

#### Usage

`./convert.sh`

### filters.json

JSON formatted list of ffmpeg audio filters

### config.json

Configuration file for `apply_filters.py` and `mse.py`

| key                 | default         | description                                                                   |
|---------------------|-----------------|-------------------------------------------------------------------------------|
| filters_filename    | filters.json    | filename of filters list in JSON file format                                  |
| segment_len         | 262144          | number of audio samples in each analyzed segment                              |
| sample_skips        | 262144          | number of samples skipped between beginnings of analyzed segments             |
| bit_depth           | 16              | bit depth of analyzed audio                                                   |
| original_audio_dir  | original_audio  | relative path to search for original audio                                    |
| filtered_audio_dir  | filtered_audio  | relative path to write filtered audio data to                                 |
| output_filename     | output.json     | filename JSON formatted mean square error output                              |

### config.py

Defines `CONFIG_FILENAME`, `Config` class, and associated JSON loader function (`load_config`).

### apply_filters.py

Loads configuration from `CONFIG_FILENAME`, applies list of ffmpeg audio filters from `filters_filename` to .wav files in `original_audio_dir` and writes resulting audio files to `filtered_audio_dir`.

#### Usage

`python3 apply_filters.py`

### mse.py

Loads configuration from `CONFIG_FILENAME` and calculates the average MSE of sequences of length `sequence_len` in the temporal domain and frequency domain ([DCT-II](https://en.wikipedia.org/wiki/Discrete_cosine_transform#DCT-II)) between original audio segments and their filtered counterparts. Resulting MSEs are dumped to `output_filename` in JSON format.

#### Usage

`python3 mse.py`

### visualize.py

Loads configuration from `CONFIG_FILENAME`, read MSE outputs from `output_filename` and plot the results as bar graphs.

## Example Results

The following results were calculated from 3 hours of audio extracted from a Twitch VOD.

| filter      | MSE (temporal domain) | MSE (frequency domain) |
|-------------|-----------------------|------------------------|
| acompressor | 419.5447047722049     | 769325.3616135248      |
| acrusher    | 128.31195087665463    | 788.4744883700115      |
| aecho       | 1973.808181613829     | 11476890.952585308     |
| aphaser     | 2140.157159476164     | 7514830.79328153       |
| alimiter    | 1589.4807644937096    | 33103402.4035865       |

### Temporal Domain MSE

<img src="https://github.com/hrichharms/ffmpeg_filters_mse/blob/master/figures/Temporal_Mean_Square_Error_(MSE).png?raw=true" alt="Mean Squared Error in the Temporal Domain" width="400"/>

### Frequency Domain MSE

<img src="https://github.com/hrichharms/ffmpeg_filters_mse/blob/master/figures/Frequency_Mean_Square_Error_(MSE).png?raw=true" alt="Mean Squared Error in the Frequency Domain" width="400"/>

## TODO
- Add more audio filters
- Add better documentation for example results
