#!/usr/bin/python

import logging
import os
from ..types.unit import Unit
import yaml as pkg_yaml


class ToolConfig:
    # Some default values that are just kept internally
    __input_directory_name = 'inputs'
    __output_directory_name = 'outputs'

    # The base input directory that should be searched for child configuration data and other input files
    base_input_directory_absolute = os.path.join(os.getcwd(), __input_directory_name)

    # The base output directory, must be absolute
    base_output_directory_absolute = os.path.join(os.getcwd(), __output_directory_name)

    # Unit that dimensions are given in
    dimension_unit = Unit.INCHES

    solver_configs = []

    __config_files = []
    __current_config = None

    def __init__(self, config_files):
        for config_file in config_files:
            if not os.path.isabs(config_file):
                msg = 'Top level configuration file path must be given as an absolute path: %s' % config_file

                logging.error(msg)
                raise RuntimeError(msg)

        self.append_config(config_files)

    def process_configs(self):
        # @todo Do processing here to set class members
        pass

    def append_config(self, config_files):
        self.__config_files.append(config_files)

        # reload
        for config_file in config_files:
            with open(config_file) as cf:
                partial_config_data = pkg_yaml.safe_load(cf)

            self.__current_config.update(partial_config_data)

        # reprocess
        self.process_config()


class SolverConfig:
    # Directory that any output files should be placed in.
    output_directory_relative = None
    output_directory_absolute = None

    # How should the outputs be represented?
    output_file_types = []

    # Array of available stock to use for cutting
    input_stock = []

    # Kerf of the blade being used to make the cuts. Provided in the configured units for the tool
    kerf = 0.125

    # The sizes of the outputs that the cuts and layout are being optimized to create
    input_cut_dimensions = []

    # What the cuts should be optimized for (reduced waste, area of waste, speed of calculation, etc.)
    # Use of this is TBD and I just think it could be a nice thing to be able to specify, may end up just going away...
    optimize_for = None

    # The currently loaded configuration data, straight from YAML. Processed configuration data is placed in the member
    # variables and this is kept as the original data.
    __current_config = None

    def __init__(self, config_file):
        # @todo
        pass

    def append_config_file(self, config_file):
        pass
