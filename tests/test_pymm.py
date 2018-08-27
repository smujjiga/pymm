#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from pymm import Metamap
from os.path import exists

__author__ = "Srikanth Mujjiga"
__copyright__ = "Srikanth Mujjiga"
__license__ = "mit"

# Point the path pointing to metamap
METAMAP_PATH = "/home/smujjiga/smujjiga/public_mm/bin/metamap16"

def test_alive():
    mm = Metamap(METAMAP_PATH, debug=True)
    assert mm.is_alive()

def test_parse():
    mm = Metamap(METAMAP_PATH)
    assert mm != None
    mmos = mm.parse(['heart attack', 'mayocardia infarction'])
    cuis = list()
    for idx, mmo in enumerate(mmos):
        for jdx, concept in enumerate(mmo):
            cuis.append(concept.cui)

    assert idx == 1
    assert len(cuis) == 10

    expected = {'C0027051', 'C0018787', 'C0277793', 'C1261512', 'C1281570', 'C1304680', 'C0027051', 'C0021308', 'C0333541', 'C0021308'}

    assert set(cuis).intersection(expected) == expected

def test_cleanup():
    mm = Metamap(METAMAP_PATH)
    assert exists(mm.input_file)
    assert exists(mm.output_file)
    mm.close()
    assert not exists(mm.input_file)
    assert not exists(mm.output_file)

if __name__ == "__main__":
    test_alive()
    test_parse()
    test_cleanup()
