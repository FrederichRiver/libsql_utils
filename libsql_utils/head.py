#!/usr/bin/python3
from dev_global.path import CONF_FILE
from libutils.utils import read_json


IP = read_json("IP", CONF_FILE)
remote = ('stock', 'stock2020', 'stock', IP[1])
root = ('root', '6414939', 'stock')
local = ('stock', 'stock2020', 'stock')