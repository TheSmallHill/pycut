#!/usr/bin/python

from ..input_manager import config as _config


class Controller:

    __config = None

    def __init__(self, config):
        self.__config = config

