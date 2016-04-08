#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Planet Venus filter script.
Removes all images.
"""
import sys
from xml.dom import minidom
# minidom for namespace awareness and to avoid external dependencies

feed = minidom.parse(sys.stdin)
img_nodes = feed.getElementsByTagName('img')

for img_node in img_nodes:
    img_node.parentNode.removeChild(img_node)

sys.stdout.write(feed.toxml(encoding='utf-8'))


