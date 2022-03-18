from json import load

from dataclasses import dataclass


CONFIG_FILENAME = "config.json"


@dataclass
class Config:
    filters_filename: str
    segment_len: int
    sample_skips: int
    bit_depth: int
    original_audio_dir: str
    filtered_audio_dir: str
    output_filename: str


def load_config(filename: str) -> Config:
    with open(filename) as config_file:
        config_data = load(config_file)
    return Config(
        config_data["filters_filename"],
        config_data["segment_len"],
        config_data["sample_skips"],
        config_data["bit_depth"],
        config_data["original_audio_dir"],
        config_data["filtered_audio_dir"],
        config_data["output_filename"]
    )
