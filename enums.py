#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:16:11 2018

@author: Faïcel Chamroukhi & Bartcus Marius
"""

from enum import Enum
class variance_types(Enum):
    free = 1
    common = 2 # according to wether all the segments with a cluster share the same noise variance or no