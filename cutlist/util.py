#!/usr/bin/python

import os


def make_relative_path_absolute(relative_path):
    return os.path.join(os.getcwd(), relative_path)
