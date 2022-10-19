#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:16:40 2022

@author: ray
"""

mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"email@domain\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml