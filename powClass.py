from cryptotools.ECDSA.secp256k1 import PrivateKey
from random import randrange

class PoWClass:

    def __init__(self):
        self.data = []

    def splitRangeForWork(self, startRange, endRange, rangeParts):
        intStart = int(startRange)
        intEnd = int(endRange)
        partsize = intEnd / rangeParts
        partList = []
        start = intStart
        for x in range(rangeParts):
            listString = ('{}{}{}').format(hex(int(start)), ':', hex(int(start + partsize)))
            partList.append(listString)
            start += partsize
        return partList

    def createPoWAddress(self, startRange, endRange):
        randPoWKeyRange = int(randrange(startRange, endRange))
        randPoWKey = '{:064x}'.format(randPoWKeyRange)
        private = PrivateKey.from_hex(randPoWKey)
        public = private.to_public()
        address = public.to_address('P2PKH', True)
        addrList = [private.hex(), address]
        return addrList


