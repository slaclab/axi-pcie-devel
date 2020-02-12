#!/usr/bin/env python3

import pyrogue

pyrogue.addLibraryPath('../../firmware/submodules/axi-pcie-core/python')
pyrogue.addLibraryPath('../../firmware/submodules/surf/python')
pyrogue.addLibraryPath('../../firmware/python')

import pyrogue.pydm
import pyrogue.gui
import rogue
import logging

from AxiPcieDevel.InterCardTest import InterCardRoot

#rogue.Logging.setFilter('pyrogue.memory.block.InterCardRoot.PcieControl[0].Fpga.PrbsTx',rogue.Logging.Debug)
rogue.Logging.setFilter('pyrogue.memory.block',rogue.Logging.Debug)

#rogue.Logging.setLevel(rogue.Logging.Debug)

logger = logging.getLogger('pyrogue.PollQueue')
logger.setLevel(logging.DEBUG)

with InterCardRoot(pollEn=False) as root:

    pyrogue.pydm.runPyDM(root=root)
    #pyrogue.gui.runGui(root=root)
    #pyrogue.waitCntrlC()


