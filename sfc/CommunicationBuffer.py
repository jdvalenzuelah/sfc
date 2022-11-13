from abc import ABCMeta, abstractmethod

"""
The communication layer used by teh control loop to interact between the system and the optmization model
"""


class CommunicationBuffer(metaclass=ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        pass

    @abstractmethod
    def getSystemTemperature(self) -> float:
        """
        Get the current temperature of the system

        :return: the temperature of the system in degree Celsius
        """
        raise NotImplementedError

    @abstractmethod
    def getFanSpeed(self) -> int:
        """
        Get the current fan speed of the system
        :return: the fan speed PWM percentage, between 0-100
        """
        raise NotImplementedError

    @abstractmethod
    def setFanSpeed(self, speed: int):
        """
        Set the fan speed in the system
        :param speed:  PWM percentage of the fan speed must be between 0-100
        :return:
        """
        raise NotImplementedError

