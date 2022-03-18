from os import listdir
from os.path import join
from json import load, dump

from numpy import ndarray, zeros, float64
from scipy.io.wavfile import read
from scipy.fft import dct

from config import (
    CONFIG_FILENAME,
    load_config
)


def max_dct_coefficient(n_samples: int, bit_depth: int) -> int:
    return 2 * n_samples * (2 ** bit_depth)


def mse(a: ndarray, b: ndarray) -> float:
    return ((a - b) ** 2).mean()


if __name__ == "__main__":

    config = load_config(CONFIG_FILENAME)

    with open(config.filters_filename) as filters_file:
        filters = load(filters_file)

    filter_temporal_mse = {
        filter_name: [0, 0]
        for filter_name in filters
    }
    filter_frequency_mse = {
        filter_name: [0, 0]
        for filter_name in filters
    }
    segment_count = 0
    for original_filename in listdir(config.original_audio_dir):
        print(original_filename)

        _osr, o_data = read(join(config.original_audio_dir, original_filename))

        d_data = {}

        for filter_name in filters:
            print(f"{filter_name}_{original_filename}")
            _dsr, d_data[filter_name] = read(
                join(
                    config.filtered_audio_dir,
                    f"{filter_name}_{original_filename}"
                ))

        for k in range(
            0, o_data.shape[0] - config.segment_len,
            config.sample_skips
        ):
            print(f"{k / (o_data.shape[0] - config.segment_len) * 100:.2f} %", end="\n")
            o_segment = o_data[k: k + config.segment_len]
            o_segment_l, o_segment_r = o_segment[:, 0], o_segment[:, 1]
            for filter_name in filters:
                filter_temporal_mse[filter_name][0] += mse(
                    o_segment_l,
                    d_data[filter_name][k: k + config.segment_len, 0]
                )
                filter_temporal_mse[filter_name][1] += mse(
                    o_segment_r,
                    d_data[filter_name][k: k + config.segment_len, 1]
                )

                filter_frequency_mse[filter_name][0] += mse(
                    dct(o_segment_l),
                    dct(d_data[filter_name][k: k + config.segment_len, 0])
                )
                filter_frequency_mse[filter_name][1] += mse(
                    dct(o_segment_r),
                    dct(d_data[filter_name][k: k + config.segment_len, 1])
                )

            segment_count += 1

    filter_temporal_mse = {
        key: [l_val / segment_count, r_val / segment_count] 
        for key, (l_val, r_val) in filter_temporal_mse.items()
    }
    filter_frequency_mse = {
        key: [l_val / segment_count, r_val / segment_count]
        for key, (l_val, r_val) in filter_frequency_mse.items()
    }

    print("\n".join(
        f"{key}: {val[0]}, {val[1]}"
        for key, val in filter_temporal_mse.items()
    ), end="\n\n")
    print("\n".join(
        f"{key}: {val[0]}, {val[1]}"
        for key, val in filter_frequency_mse.items()
    ))

    with open(config.output_filename, "w") as output_file:
        dump(
            {
                "temporal": filter_temporal_mse,
                "frequency": filter_frequency_mse
            },
            output_file
        )
