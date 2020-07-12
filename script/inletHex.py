import os
import struct
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename=r'D:\logger.log',
                    filemode='w', level=logging.DEBUG)


class WithHex:
    def __init__(self, bin_file):
        if os.path.exists(bin_file):
            self.bin_file = bin_file
            logging.debug("file {} exists and have done init".format(self.bin_file))
        else:
            logging.debug("file not exists, init fail")
        pass

    def readHex(self):
        try:
            bin_data = open(self.bin_file, 'rb')
            size = os.path.getsize(self.bin_file)
            logging.info("The {} size: {}".format(self.bin_file, size))

            for i in range(size):
                data1Byte = bin_data.read(1)
                dataTuple = struct.unpack('B', data1Byte)
                logging.debug("The {} is: {} and {}".format(i, data1Byte, dataTuple[0]))
        finally:
            bin_data.close()
        pass

    def getHex(self, posStart=0, posOffset=0, howMuch=0):
        logging.debug("posStart: {}, posOffset: {}".format(posStart, posOffset))
        if posStart not in range(3):
            logging.info("wrong input, check again.")
            exit(1)

        try:
            bin_data = open(self.bin_file, 'rb')
            size = os.path.getsize(self.bin_file)
            logging.info("The {} size: {}, curPos: {}".format(self.bin_file, size, bin_data.tell()))

            import math
            if math.fabs(posOffset) + math.fabs(howMuch) > size:
                logging.info("offset over size, chck again.")
                exit(1)

            bin_data.seek(posOffset, posStart)
            logging.info("The {} size: {}, curPos: {}".format(self.bin_file, size, bin_data.tell()))
            data_byte = bin_data.read(howMuch)
        finally:
            bin_data.close()

        if data_byte:
            return None
        else:
            return data_byte

    def writeHex(self, new_data, offset=0):
        content = str.encode(new_data)
        file_path = r"d:\Temp.Files\dataNew.jpg"
        try:
            bin_file = open(file_path, 'rb+')
            logging.debug("The position: {}".format(bin_file.tell()))
            bin_pre = bin_file.read(offset)
            logging.debug("bin_pre: {}".format(bin_pre))

            bin_file.seek(offset, 0)
            logging.debug("The position: {}".format(bin_file.tell()))
            bin_post = bin_file.read()
            logging.debug("bin_post: {}".format(bin_post))

            bin_file.seek(0, 0)
            bin_file.write(bin_pre)
            bin_file.write(content)
            bin_file.write(bin_post)
        finally:
            bin_file.close()

        try:
            bin_file = open(file_path, 'rb')
            logging.debug("check bin_file: {}".format(bin_file.read()))
        finally:
            bin_file.close()
        pass


def main():
    file_path = r"d:\Temp.Files\data.jpg"
    rh = WithHex(file_path)
    # rh.readHex()
    # logging.debug("the byte data: {}".format(rh.getHex(0, 40880, 3)))
    rh.writeHex("oo", 2)

    del rh  # destroy rh instance
    pass


if __name__ == "__main__":
    main()
    pass
