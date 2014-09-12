##
# The MIT License (MIT)
#
# Copyright (c) 2014 Stefan Wendler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
##

__author__ = 'Stefan Wendler, sw@kaltpost.de'

"""
Very simple example showing how to use the SmartPlug API to set the schedule of one week.

"""

# import plug API
from ediplug.smartplug import SmartPlug

# create plug object for plug with IP 172.16.100.75, login admin and password 1234
p = SmartPlug("172.16.100.75", ('admin', '1234'))

# write schedule for one week
p.schedule = [
        {'state': u'ON', 'sched': [[[1, 0], [1, 30]]], 'day': 0},
        {'state': u'ON', 'sched': [[[2, 0], [2, 30]]], 'day': 1},
        {'state': u'ON', 'sched': [[[3, 0], [3, 30]]], 'day': 2},
        {'state': u'ON', 'sched': [[[4, 0], [4, 30]]], 'day': 3},
        {'state': u'ON', 'sched': [[[5, 0], [5, 30]]], 'day': 4},
        {'state': u'ON', 'sched': [[[6, 0], [6, 30]]], 'day': 5},
        {'state': u'ON', 'sched': [[[7, 0], [7, 30]]], 'day': 6},
    ]