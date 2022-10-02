#!/bin/bash

find ~dance/.itgmania/Songs -type f -name '*.ssc' -o -name '*.sm' | python songs.py
