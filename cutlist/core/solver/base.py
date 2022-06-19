#!/usr/bin/python

from ...input_manager import config as config_type


class Base:
    __config = None

    def __init__(self, config=None):
        # Handle some errors around the (hopefully) passed configuration object
        if config is None:
            raise RuntimeError("Missing configuration data for solver")
        elif not isinstance(config, config_type.Config):
            raise TypeError("Incorrect configuration structure for solver")

    def configure(self, config):
        # @todo configure the solver (ins, outs, etc.)
        pass

    def solve(self):
        #
        pass

    # Private copies of methods
    __configure = configure
    __solve = solve
