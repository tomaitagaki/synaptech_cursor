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

    interface: View = PyGameView()
    interface.initialize(pygame_view.DEFAULT_SETUP)
    
    # Problem with this implementation:
    # the window will only close after an entire trial has finished.
    # Closing it earlier requires a keyboard interrupt.
    while interface.update():
        # TODO: code to run trial
        # This is a short demonstration of the different states of the interface
        
        for move in range(num_moves):
            features = brain_data.get_features()
            # TODO: features -> movement (model.py)
            # movement -> absolute cursor position
            interface.move(260, 260) # new cursor position
            time.sleep(input_speed / 1000) # time later
        interface.clear()
        # update decoder (parameter: resulting cursor position, index of target)
        time.sleep(2) # time in between trials
        interface.restart()

if __name__ == "__main__":
    main()
