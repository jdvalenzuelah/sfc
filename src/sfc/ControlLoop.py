from sfc.CommunicationBuffer import CommunicationBuffer
from sfc.FanSpeedCurve import FanSpeedCurve
import time
import logging

"""
The control loop used to modify the given system fan speed using the given optimizer
"""


class ControlLoop:
    def __init__(self, system: CommunicationBuffer, curve: FanSpeedCurve, **kwargs):
        """
        :param system: The communication buffer to get system info and set fan settings
        :param curve: The model used to get the fan speed during a control cycle
        :keyword samplingTime: sample time in seconds, default=1
        :keyword cycleHook: Hook called during each control cycle. Must accept feedback, currentState, newState, time kwargs
        """

        self.system = system
        self.curve = curve

        self.samplingTime = int(kwargs['samplingTime']) if 'samplingTime' in kwargs else 1
        self.cycleHook = None
        if 'cycleHook' in kwargs:
            self.setCycleHook(kwargs['cycleHook'])

        self.running = False
        self.lastCycle = None

    def setCycleHook(self, hook: callable):
        if not callable(hook):
            # TODO raise exception
            return

        # TODO: Check hook signature
        self.cycleHook = hook

    def __control(self):
        """
        Control cycle, gets the system state and feedback and sets the new state based on the value returned by the
        optimizer
        """
        now = time.time()
        if self.lastCycle and self.samplingTime > (now - self.lastCycle):
            return

        logging.info('starting control cycle')

        self.lastCycle = now
        feedback = self.system.getSystemTemperature()
        currentState = self.system.getFanSpeed()

        newState = self.curve.getFanSpeed(feedback, currentState)

        logging.info(f'setting new state {newState} from feedback={feedback} currentState={currentState}')
        self.system.setFanSpeed(newState)

        if self.cycleHook:
            logging.debug('executing cycle hook')
            self.cycleHook(feedback=feedback, currentState=currentState, newState=newState, time=now)

    def start(self):
        """
        Start the control loop
        :return: None
        """
        self.running = True

        logging.info('Starting control loop')
        while self.running:
            self.__control()

    def stop(self):
        """
        Stop the control loop
        :return:
        """
        logging.warning('Stopping control loop')
        self.running = False
