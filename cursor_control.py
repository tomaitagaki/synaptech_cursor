"""
Integrates the interface with the processed EEG data and manages
timing of trials.
"""
import time
import pygame_view
from view import View
from pygame_view import PyGameView
from get_brain_data import BrainData
from hardware_interface import HeadSet
from band_config import Band
import numpy as np


def main():
    input_speed = 50 # ms
    timeout_seconds = 10 # s
    num_moves = (timeout_seconds * 1000) // input_speed

    # initialize headset instance
    # input_source = HeadSet('/dev/cu.usbserial-DM0258JS')
    input_source = HeadSet('/dev/cu.usbserial-DM03GSKK')

    # start session
    input_source.init_board()
    input_source.start_session() # can also end_session()

    brain_data = BrainData(input_source, [Band.MU, Band.BETA], [3, 4])

    time.sleep(4)

    # interface: View = PyGameView()
    # interface.initialize(pygame_view.DEFAULT_SETUP)
    
    # Problem with this implementation:
    # the window will only close after an entire trial has finished.
    # Closing it earlier requires a keyboard interrupt.
    # while interface.update():
    # while True:
    #     # TODO: code to run trial
    #     # This is a short demonstration of the different states of the interface
        
    #     for move in range(num_moves):
    #         features = brain_data.get_features()
    #         print(features)
    #         # TODO: features -> movement (model.py)
    #         # movement -> absolute cursor position
    #         # interface.move(260, 260) # new cursor position
    #         time.sleep(input_speed / 1000) # time later
    #     # interface.clear()
    #     # update decoder (parameter: resulting cursor position, index of target)
    #     time.sleep(2) # time in between trials
        # interface.restart()

    # keep track for b-value
    past_mu_3 = []
    past_mu_4 = []
    past_beta_3 = []
    past_beta_4 = []

    counter = 0
    print('mu_r', 'be_r', 'mu_l', 'be_l') # r refers to right electrode
    while counter < 200:
        counter += 1
        features = brain_data.get_features()
        past_mu_3.append(features[0][0])
        past_mu_4.append(features[0][1])
        past_beta_3.append(features[1][0])
        past_beta_4.append(features[1][1])
        print(features[0][0], features[0][1], features[1][0], features[1][1])
        time.sleep(0.05)

# use to average "past voltages" for b values in decoder
def get_b_values(mu_3, mu_4, beta_3, beta_4):
    b_mu = np.mean([np.mean(mu_3), np.mean(mu_4)])
    b_beta = np.mean([np.mean(beta_3), np.mean(beta_4)])
    return b_mu, b_beta

if __name__ == "__main__":
    main()

# TODO:
# neutral, right up, left up, right down, left down