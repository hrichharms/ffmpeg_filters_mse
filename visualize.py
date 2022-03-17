from json import load

from matplotlib import pyplot

from config import CONFIG_FILENAME, load_config


if __name__ == "__main__":

    config = load_config(CONFIG_FILENAME)

    with open(config.filters_filename) as filters_file:
        filters = load(filters_file)

    with open(config.output_filename) as output_file:
        output = load(output_file)

    temporal_mse = output["temporal"]
    fig1 = pyplot.figure(f"Temporal Mean Square Error (MSE)")
    ax1 = fig1.add_subplot(111)
    ax1.set_xlabel("Filter")
    ax1.set_ylabel("MSE")
    ax1.bar(temporal_mse.keys(), temporal_mse.values())

    spectral_mse = output["spectral"]
    print(spectral_mse)
    fig2 = pyplot.figure(f"Spectral Mean Square Error (MSE)")
    ax2 = fig2.add_subplot(111)
    ax2.set_xlabel("Filter")
    ax2.set_ylabel("MSE")
    ax2.bar(spectral_mse.keys(), spectral_mse.values())

    pyplot.show()
