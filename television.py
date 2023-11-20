from typing import Union
from television import Television

class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Function is meant to hold all the constants.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        This is meant to turn the TV on and off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        This function is meant to mute and unmute the TV when the TV is on.
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        This function is used to increase the channel, and if the channel is at the highest then it has to loop around back to the minimum channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        This function is used to decrease TV channel, and if the channel is at the lowest it should loop around and set TV channel to the highest.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        This function is used to increase the volume, and if it is already at max volume it should stay there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        """
        This function is used to decrease TV volume when TV is on, and remain that same if volume is already at its lowest.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        """
        This function is used to send the values of the TV object in a specific format.
        :return: TV status 
        """
        muted_str = " (Muted)" if self.__muted else ""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}{muted_str}"

