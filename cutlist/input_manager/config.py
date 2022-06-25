#!/usr/bin/python

import logging
from ..types.unit import Unit
from ..types.stock import Stock
from ..util import *
import yaml as pkg_yaml


class ToolConfig:
    # Some default values that are just kept internally
    __input_directory_name = 'inputs'
    __output_directory_name = 'outputs'

    available_stock = []
    kerf = 0.125
    cuts = []

    # The base input directory that should be searched for child configuration data and other input files
    base_input_directory_absolute = os.path.join(os.getcwd(), __input_directory_name)

    # The base output directory, must be absolute
    base_output_directory_absolute = os.path.join(os.getcwd(), __output_directory_name)

    # Unit that dimensions are given in
    dimension_unit = Unit.INCHES

    solver_configs = {}

    __config_files = []
    __current_config = None

    def __init__(self, config_files):
        for config_file in config_files:
            if not os.path.isabs(config_file):
                msg = 'Top level configuration file path must be given as an absolute path: %s' % config_file

                logging.error(msg)
                raise RuntimeError(msg)

        self.append_config(config_files)

    def process_config(self):
        if self.__current_config['unit'] is not None:
            # @todo convert the specified unit into the enumeration
            pass

        if self.__current_config['input-directory'] is not None:
            self.__input_directory_name = self.__current_config['input-directory']
            self.base_input_directory_absolute = make_relative_path_absolute(self.__input_directory_name)

        if self.__current_config['output-directory'] is not None:
            self.__output_directory_name = self.__current_config['output-directory']
            self.base_output_directory_absolute = make_relative_path_absolute(self.__output_directory_name)

        if self.__current_config['kerf'] is not None:
            self.kerf = self.__current_config['kerf']

        for solver in self.__current_config['solver']:
            new_solver = SolverConfig(solver)

            self.solver_configs[new_solver.name] = new_solver

        for stock in self.__current_config['stock']:
            has_all_nominal = stock['nominal-width'] is not None and stock['nominal-length'] is not None and \
                stock['nominal-thickness'] is not None
            has_all_actual = stock['actual-width'] is not None and stock['actual-length'] is not None and \
                stock['name'] is not None

            if not has_all_nominal or not has_all_actual:
                raise ValueError("Missing required data for available stock element")

            new_stock = Stock(stock['nominal-width'], stock['nominal-length'], stock['nominal-thickness'], \
                              stock['actual-width'], stock['actual-length'], stock['actual-thickness'], stock['name'])

        for cut in self.__current_config['cuts']:
            # @todo get each sub item and use it to create a cut object
            pass

    def append_config(self, config_files):
        self.__config_files.append(config_files)

        # reload
        for config_file in config_files:
            with open(config_file) as cf:
                partial_config_data = pkg_yaml.safe_load(cf)

                if self.__current_config is None:
                    self.__current_config = partial_config_data
                else:
                    self.__current_config.update(partial_config_data)

        # reprocess
        self.process_config()


class SolverConfig:
    name = "Default"

    # What the cuts should be optimized for (reduced waste, area of waste, speed of calculation, etc.)
    # Use of this is TBD and I just think it could be a nice thing to be able to specify, may end up just going away...
    optimize_for = None

    # The currently loaded configuration data, straight from YAML. Processed configuration data is placed in the member
    # variables and this is kept as the original data.
    __current_config = None

    def __init__(self, config):
        if config['name'] is not None:
            self.__current_config = config

            self.process_config(self.__current_config)
        else:
            raise ValueError("A solver configuration must include a name")

    def append_config_file(self, config):
        self.__current_config.update(config)

    def process_config(self, config):
        self.name = self.__current_config['name']
