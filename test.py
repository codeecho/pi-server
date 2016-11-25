#!/usr/bin/env python

import PiServer

def handleEvent(event):
    print event

PiServer.handleEvent = handleEvent
PiServer.run()