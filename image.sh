#!/bin/bash

#simple oneliner to solve lemur xor challenge (xors two images together)
#will implement something more programmatic in python

convert flag_7ae18c704272532658c10b5faad06d74.png lemur_ed66878c338e662d3473f0d98eedbd0d.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" C.png