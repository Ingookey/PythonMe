
import os
import struct
import logging

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', \
                    filename='D:\logger.log', filemode='w', \
                    level=logging.DEBUG)

class WithHex:
    def __init__(self, binFile):
        if os.path.exists(binFile):
            self.binFile = binFile
            logging.debug("file {} exists and have done init".format(self.binFile))
        else:
            logging.debug("file not exists, init fail")
        pass

    def readHex(self):
        try:
            binData = open(self.binFile, 'rb')
            size = os.path.getsize(self.binFile)
            logging.info("The {} size: {}".format(self.binFile, size))

            for i in range(size):
                data1Byte = binData.read(1)
                dataTuple = struct.unpack('B', data1Byte)
                logging.debug("The {} is: {} and {}".format(i, data1Byte, dataTuple[0]))
        finally:
            binData.close()
        pass

    def getHex(self, posStart = 0, posOffset = 0, howMuch = 0):
        logging.debug("posStart: {}, posOffset: {}".format(posStart, posOffset))
        if posStart not in range(3):
            logging.info("wrong input, check again.")
            exit(1)

        try:
            binData = open(self.binFile, 'rb')
            size = os.path.getsize(self.binFile)
            logging.info("The {} size: {}, curPos: {}".format(self.binFile, size, binData.tell()))

            import math
            if math.fabs(posOffset) + math.fabs(howMuch) > size:
                logging.info("offset over size, chck again.")
                exit(1)

            binData.seek(posOffset, posStart)
            logging.info("The {} size: {}, curPos: {}".format(self.binFile, size, binData.tell()))
            dataByte = binData.read(howMuch)
        finally:
            binData.close()

        if dataByte:
            return None
        else:
            return dataByte


    def writeHex(self, newData, offset = 0):
        content = str.encode(newData)
        filepath = "d:\Temp.Files\dataNew.jpg" # todo remove
        try:
            binfile = open(filepath, 'rb+')
            logging.debug("The position: {}".format(binfile.tell()))
            binPre = binfile.read(offset)
            logging.debug("binPre: {}".format(binPre))

            binfile.seek(offset, 0)
            logging.debug("The position: {}".format(binfile.tell()))
            binPost = binfile.read()
            logging.debug("binPost: {}".format(binPost))

            binfile.seek(0, 0)
            binfile.write(binPre)
            binfile.write(content)
            binfile.write(binPost)
        finally:
            binfile.close()

        try:
            binfile = open(filepath, 'rb')
            logging.debug("check binfile: {}".format(binfile.read()))
        finally:
            binfile.close()
        pass


filepath = "d:\Temp.Files\data.jpg"

def main():
    logging.info("main")
    rh = WithHex(filepath)
    #rh.readHex()
    #logging.debug("the byte data: {}".format(rh.getHex(0, 40880, 3)))
    rh.writeHex("oo", 2)

    del rh # destroy rh instance
    pass

if __name__ == "__main__":
    main()
    pass