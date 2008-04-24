#----------------------------------------------------------------------
# This file was generated by D:\src\cvl_repository\wxpython\framework\images\make_images.py
#
from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xe6\x01\x19\xfe\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\
\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\
\x08\x08\x08\x08|\x08d\x88\x00\x00\x01\x9dIDAT8\x8d\xa5\x92\xb1k\x14A\x18\
\xc5\x7f\xb3\x1c\x114\x1b\xd0BD\x10\x95$\x8a\x9d\xa0\x8d\x18+\x91T\x82E\xd2j\
\x8a\xfc\x03)\xd2Y\x08V\xb6\xa9\x04\xb5\xb1\xd3F,\x0e\xab\x94)\xaf1\xe0\xa1$\
\x90\x14\x16\x8a$\x81\x80\xd9\xbd\x99\xef{\x16\xbb\xb7\xb7\x01#\t>\x98b\xd8\
\x9d7\xbf\xf7\xe6\x83\xffT\x00x\xbc\xd2[\np\x99\x10f\x80[\xc8\x05!\xe0"\xcb\
\x02Y\x00w\xc7\x92\xf6\xc6:l\\\xbf4q\x1b\x17\xcbs7\x02\x00OVz\xaftB\xbdx\xff\
E\x00\x1d\x00\x05\xee\x01\xbcY\xdbi\xd0\xf4\x0f\xec\xc5\xbb\xe7\xe8o\xef\x95\
\x8d\x01\xc6\x85\xe1\xc7\xe9\xf3\xa7\xaal\xe1\xef\x87\xbf\xfe(\x01(\x8a\xc1\
\xd8\x88@:=\xbc\xf5\xdb\xcf\xf2X\xe5\xc9=\x8c\x08\xdc;C\xb4\xe3\xca\xcdi\x11\
T\xaf1\xffl\x95\xc2\x1d\x17t\x9f?\xe0\xe1\xebY\xf2<\xc7\xdd\x9bef|X\xe8"\xb7\
\x96\x81Wn\xbf\x0e"\xf7o^\xa4\xdb\xfb\x0e@\x9e\x8f35y\x85:&\x92\xf3y\xbd_\
\xedSe\x90U\x06U\xe7\xfb\x85\x11%~\x97\t\x003\'p\xb8\xcddV\xa7N#\x82P\x13\
\x94e\xe4 \x1aV\xc4\xfa\'G\x12 \x90\x90\x84\xd57+\rZ\x11Z\xaf\xae\xd6\x00\
\xa4d\xb8\xac\x89\xe0\x12\xe6\xc3}\x8b\xc0\xa3\x89z\xac?\xadm5\x06\xf9\xf8\
\x1966\xb7\x8912\x88\x11KF\x162\xea\xdeF\x93h\xee[\xc0\xd5\xf5\x97\x8f\x0e\
\xe5};\xf7\x8e\xa3$\xd7nc\x80\xe9\xe3\xfc\xd3\xd5k\x8e\xee\x04\xd7Y\xf7\x04r\
\xe4\x86<\x81\x0c5}\xb8@\xfb\nY\xffH\xf7\x93\xe8\x0f\x11\x00"\x15D}\xb4\xc6\
\x00\x00\x00\x00IEND\xaeB`\x82L[\xd7\x04' )

def getBitmap():
    return BitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return ImageFromStream(stream)
