#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

import collections
from xml.dom.minidom import parse as parse_xml

__author__ = "Srikanth Mujjiga"
__copyright__ = "Srikanth Mujjiga"
__license__ = "mit"


candidate_mapping = { "score" : "CandidateScore", "cui": "CandidateCUI", "semtypes": "SemType", 'ismapping': None, 'matched' : 'CandidateMatched', 'isnegated': 'Negated', 'matchedstart': None, 'matchedend' : None }

class Concept(collections.namedtuple("Concept", list(candidate_mapping.keys()))):
    @classmethod
    def from_xml(cls, candidate, is_mapping=False):
        def get_data(candidate, tagName):
            return candidate.getElementsByTagName(tagName)[0].childNodes[0].data

        return cls(
                cui=get_data(candidate, candidate_mapping['cui']),
                score=get_data(candidate, candidate_mapping['score']),
                matched=get_data(candidate, candidate_mapping['matched']),
                semtypes = [semtype.childNodes[0].data for semtype in candidate.getElementsByTagName(candidate_mapping['semtypes'])],
                ismapping = is_mapping,
                isnegated = get_data(candidate, candidate_mapping['isnegated']),
                matchedstart = [int(m.childNodes[0].data) for m in candidate.getElementsByTagName("TextMatchStart")],
                matchedend = [int(m.childNodes[0].data) for m in candidate.getElementsByTagName("TextMatchEnd")]
                )
        
    def __str__(self):
        #@todo: print MMI format
        return "{0}, {1}, {2}, {3}, {4}, [{5}:{6}]".format(self.score, self.cui, self.semtypes, self.matched, self.isnegated, self.matchedstart, self.matchedend)

class MMOS():
    def __init__(self, mmos):
        self.mmos = mmos
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = MMO(self.mmos[self.index])
        except IndexError:
            raise StopIteration
        self.index += 1
        return result


class MMO():
    def __init__(self, mmo):
        self.mmo = mmo
        self.index = 0
        self.concept = None
    
    def __iter__(self):
        for idx, tag in enumerate(["Candidates", "MappingCandidates"]):
            for candidates in self.mmo.getElementsByTagName(tag):
                candidates = candidates.getElementsByTagName("Candidate")
                #print ("Found {0} {1}".format(len(candidates), tag))
                for concept in candidates:
                    yield Concept.from_xml(concept,is_mapping=idx) 

def parse(xmlf1_file):
    document = parse_xml(xmlf1_file).documentElement
    return MMOS(document.getElementsByTagName("MMO"))
