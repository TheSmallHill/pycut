#!/usr/bin/python

import argparse
from cutlist.core import controller
from cutlist.input_manager import config
import logging

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some cut-list inputs')
    parser.add_argument('--config', type=str, nargs='+')
    parser.add_argument('--log-file', type=str, default='log.txt')
    parser.add_argument('--log-level', type=str, default='WARNING')

    # parse arguments
    args = parser.parse_args()

    # Setup the logger object that this tool will output to. We convert the string version of the level into an integer for
    # use with the configuration method.
    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % args.log_level)

    logging.basicConfig(filename=args.log_file, level=numeric_level)

    logging.info('Initialized logger')

    tool_config_data = config.ToolConfig(args.config)

    # Start the tool
    tool_controller = controller.Controller(tool_config_data)
