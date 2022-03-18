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
    fig1 = pyplot.figure(f"Temporal Mean Square Error (LEFT)")
    ax1 = fig1.add_subplot(111)
    ax1.set_xlabel("Filter")
    ax1.set_ylabel("MSE")
    ax1.bar(temporal_mse.keys(), [val[0] for val in temporal_mse.values()])

    fig2 = pyplot.figure(f"Temporal Mean Square Error (RIGHT)")
    ax2 = fig2.add_subplot(111)
    ax2.set_xlabel("Filter")
    ax2.set_ylabel("MSE")
    ax2.bar(temporal_mse.keys(), [val[1] for val in temporal_mse.values()])

    fig3 = pyplot.figure(f"Temporal Mean Square Error (MONO)")
    ax3 = fig3.add_subplot(111)
    ax3.set_xlabel("Filter")
    ax3.set_ylabel("MSE")
    ax3.bar(temporal_mse.keys(), [(val[0] + val[1]) / 2 for val in temporal_mse.values()])


    frequency_mse = output["frequency"]
    fig4 = pyplot.figure(f"Frequency Mean Square Error (LEFT)")
    ax4 = fig4.add_subplot(111)
    ax4.set_xlabel("Filter")
    ax4.set_ylabel("MSE")
    ax4.bar(frequency_mse.keys(), [val[0] for val in frequency_mse.values()])

    fig5 = pyplot.figure(f"Frequency Mean Square Error (RIGHT)")
    ax5 = fig5.add_subplot(111)
    ax5.set_xlabel("Filter")
    ax5.set_ylabel("MSE")
    ax5.bar(frequency_mse.keys(), [val[1] for val in frequency_mse.values()])

    fig6 = pyplot.figure(f"Frequency Mean Square Error (MONO)")
    ax6 = fig6.add_subplot(111)
    ax6.set_xlabel("Filter")
    ax6.set_ylabel("MSE")
    ax6.bar(frequency_mse.keys(), [(val[0] + val[1]) / 2 for val in frequency_mse.values()])

    pyplot.show()
