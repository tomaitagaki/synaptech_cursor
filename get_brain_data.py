from band_config import Band
from hardware_interface import HeadSet

from brainflow.board_shim import BoardShim, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, WindowFunctions, DetrendOperations

# C3 (left motor) index 2 (channel 3)
# C4 (right motor) index 3 (channel 4)

class BrainData:
    def __init__(self, input_source, bands, channels, window_ms=400):
        self.input_source = input_source
        self.sampling_rate = BoardShim.get_sampling_rate(self.input_source.board_id)
        self.sampling_power_two = DataFilter.get_nearest_power_of_two(self.sampling_rate)
        self.bands = bands
        self.channels = channels

        self.window = int(window_ms / 1000 * self.sampling_rate)

    def __get_recent_data(self):
        # Get data from brainflow
        data = self.input_source.board.get_current_board_data(self.window)

    def __clean_data(self, data):
        # what is ch_data --> do we want to pass this in or have this done automatically
        DataFilter.detrend(data, DetrendOperations.LINEAR.value)
        DataFilter.perform_bandpass(data, self.sampling_rate, 51.0, 100.0, 2, FilterTypes.BUTTERWORTH.value, 0)
        DataFilter.perform_bandstop(data, self.sampling_rate, 50.0, 4.0, 2, FilterTypes.BUTTERWORTH.value, 0)
        DataFilter.perform_bandstop(data, self.sampling_rate, 60.0, 4.0, 2, FilterTypes.BUTTERWORTH.value, 0)

    def get_features(self):

        features = []
        data = self.__get_recent_data()

        for ch in self.channels:
            band_powers = []
            ch_data = data[ch]
            self.__clean_data(ch_data)
            psd = DataFilter.get_psd_welch(ch_data, self.sampling_power_two,
                self.sampling_power_two // 2, self.sampling_rate, WindowFunctions.BLACKMAN_HARRIS.value)

            for band in self.bands:
                band_powers.append(DataFilter.get_band_power(psd, band.value.freq_start, band.value.freq_stop))
            features.append(band_powers)
        
        return band_powers # [[3-mu, 3-beta], [4-mu, 4-beta]]
