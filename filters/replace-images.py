#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Planet Venus filter script.
Replaces images with hyperlinks to image source and text: "[img]".
(Like Jogger's main page.)
"""
import sys
from xml.dom import minidom
# minidom for namespace awareness and to avoid external dependencies


def create_img_placeholder(img_src):
    document = minidom.Document()
    
    placeholder = document.createElement('a')
    placeholder.attributes['href'] = img_src
    placeholder.appendChild(feed.createTextNode('[img]'))

    return placeholder


feed = minidom.parse(sys.stdin)
img_nodes = feed.getElementsByTagName('img')

for img_node in img_nodes:
    img_src = img_node.attributes['src'].value
    img_placeholder = create_img_placeholder(img_src)

    img_node.parentNode.replaceChild(img_placeholder, img_node)

sys.stdout.write(feed.toxml(encoding='utf-8'))


