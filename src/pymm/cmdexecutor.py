#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from os.path import abspath
import subprocess

__author__ = "Srikanth Mujjiga"
__copyright__ = "Srikanth Mujjiga"
__license__ = "mit"

class MetamapCommand:
    def __init__(self, metamap_path, input_file, output_file, debug):
        self.metamap_path = abspath(metamap_path)
        self.input_file = input_file
        self.output_file = output_file
        self.debug = debug
        self.command = self._get_command()
        if self.debug:
            print (self.command)

    def _get_command(self):
        cmd = [self.metamap_path, "-c", "-Q", "4", "-y", "-K", "--sldi", "-I", "--XMLf1", "--negex"]
        if self.debug:
            cmd += ["--silent"]
        cmd += [self.input_file, self.output_file]
        return cmd

    def execute(self, timeout=10):
        proc = subprocess.Popen(self.command , stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            outs, errs = proc.communicate(timeout=timeout)
        finally:
            proc.kill()
