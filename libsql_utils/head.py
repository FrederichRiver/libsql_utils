#!/usr/bin/python3
from dev_global.path import CONF_FILE
from libutils.utils import read_json


IP = read_json("IP", CONF_FILE)
remote = (IP[1], 'stock', 'stock2020', 'stock')
root = ('localhost', 'root', '6414939', 'stock')
local = ('localhost', 'stock', 'stock2020', 'stock')