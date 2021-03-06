#!/usr/bin/env python3
import pyrogue as pr
import rogue.hardware.axi
import pyrogue.utilities.prbs
import AxiPcieDevel.RateTest

class PcieControl(pr.Device):

    def __init__(self,index=0):
        pr.Device.__init__(self,name=f'PcieControl[{index}]')

        self._dataMap = rogue.hardware.axi.AxiMemMap(f'/dev/datagpu_{index}')

        self.add(AxiPcieDevel.RateTest.Fpga(memBase=self._dataMap))

        self._data   = [None] * 4
        self._prbsRx = [None] * 4
        self._prbsTx = [None] * 4

        for i in range(4):
            self._data[i]   = rogue.hardware.axi.AxiStreamDma(f'/dev/datagpu_{index}',i*256,True)
            self._prbsRx[i] = pyrogue.utilities.prbs.PrbsRx(name=f'PrbsRx[{i}]', width=256)
            self.add(self._prbsRx[i])

            pyrogue.streamConnect(self._data[i],self._prbsRx[i])

        for i in range(4):
            self._prbsTx[i] = pyrogue.utilities.prbs.PrbsTx(name=f'PrbsTx[{i}]', width=256)
            self.add(self._prbsTx[i])

            pyrogue.streamConnect(self._prbsTx[i],self._data[i])

