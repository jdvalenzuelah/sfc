from abc import ABCMeta, abstractmethod

"""
The optimization model to use to get the fan speed

Model behavior exposed is the same regardless of the settings of each implementation thus set points and other settings
must be set up in each implementation. 
"""


class FanSpeedCurve(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return hasattr(subclass, 'getFanSpeed') and callable(subclass.getFanSpeed)

    @abstractmethod
    def getFanSpeed(self, feedback: float, currentSpeed: int) -> int:
        """
        Get the fan speed based on the system feedback temperatura and current fan speed

        :param feedback: System feedback temperature in degree Celsius
        :param currentSpeed: Current system speed in PWM percentage (must be between 0-100)
        :return: new fan speed PWM percentage (between 0-100)
        """
        raise NotImplementedError
