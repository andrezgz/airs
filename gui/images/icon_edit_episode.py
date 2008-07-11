#----------------------------------------------------------------------
# This file was generated by D:\src\airs\gui\images\make_images.py
#
from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xe6\x02\x19\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\
\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\
\x08\x08\x08\x08|\x08d\x88\x00\x00\x02\x9dIDAT8\x8d\xa5\x93[HTQ\x14\x86\xbf\
\xbd\xcf93\xe3\xa4\x8ea\x8e\x19\x9a\xb7\xc4\xca\xc4\xecBF\xfa\x18IE\xf4P\x0f\
\x95DAT\x04\x11\xbeFPDF$\xf6\x12Q\x90\x11\xd1K\xf5T\x90\x90\x84v\xa1\x12\xba\
\x90\xa5\xa2Iw\xf1\x8e\x97\xf1\x823g\xce\xd9\xbb\x87\xf1\n\xbe\xf5\xc3\x82\
\xbd\x16\x9b\x7f\x7f\x9b\xb5\x16\xfc\xa7\x04\xc0\xc1\xb3\x8fj\\G\x1c\x1a\x99\
r|\x13\x91En\xb9\x0bS\x9f\x0f\x12}\xdc}\\s\xa0\xd2\x04p5\x15\x97NlHI\r\x06\
\x85\x10&\x1a\xd0\x80\x9a~Ck\xd0z&\xd7\xb8\x8e\xcd\xd1\x8b\xcf\x8e\x001\x83\
\x91\t\xd7\x1bL\t\x8aS\xd7\xee\xb3"#\t\xaf\xa1p\xb5\x17d\x00)\x88\x85\x14\
\x18R\xf0\xb7\xa3\x85\xaa\xca\x938\xae\x14\x00&\xc0d\x04\xa44\xc9\xcb\xcdb]I\
)\x864\xd0\xda\x05a\x82\x10H!\x10B"\xa5\xc42$J\xcd}\xc7\x9c9(\xc0\xeb\xf5\
\xe1\x8b\x8b\x8f\xf1.\xa2\x84\x91F\xf6\xdaw\x18\x7f\xddD\xf5\xfaW\x01n\x14\
\x1c^`\x10\xb5\xc3D\xc3S \x04Z+\x94vQJ"\x80\xe4\xf1:\xf2B\x9f\x89+\xac \x90]\
\xcc\xe8\xaf|\xda\xebk\xaf\xce\x1ah\r\x83\xa1\x1e\x86\x06BD\x95\x83\xd2.c\
\x91~l7\x9dl\xf5\x82u\xe9?H\xcc\xdb\xc6\xf0\x8fv<\xc2&!q9\xf1\xc9+\x03\x0b\
\x0c\xfa\xfa\xfdX]\xe1\xb9\x82N!\xd3|\xc3\xce\xd5\x9d$\xe5\xec \xd2\xfb\x00\
\x8f_\xf0\xa7\xb9\x83\xd1\t\xad\xa53\\$\x99n\x99\xd6 \r\x0f\xd2\xf0\xc6\xc2\
\xf4\x91\xe9i\xa6"\xff\x0bI\xb9;\t\xf7\xdcFX#X\xf1\t\xc4\xa9!n}\xdf4\xb9\xe5\
\xf4\xe3N9\x9f`\xbe\x82c\xcf\xd9\x9f\xf1\x9e\xc0\xaa=\x84\xbbo"\xad(\xf6X\
\x16]\x8d\x9f0J\xce\xd3c/s\x01b\x04\xaeB\x00\x03\xbf\xdb\xe8jkB\xb6\xdd\xa4|\
y+\xc1\x82]\xd8}\xb5\x18\x1eMd,\x93\xee\x97\x1f\xb9\xd0R\x8cL\xce\xc7U\xf3\
\xda(\xa6\'\xec\xc6\xe5s\xf4\x7f~D\x8aV8\xa4\xd3\xdbr\x9d\xa5A\x0f\xe1\xe1\
\x0c\x86>t \xca\xefpq_\x1a`\xcf\x92J\x80\xc48\x19RN\x984\xbf\xcd\xc0\xd7Z\
\xd6\x96\x1e\xc7\xdb\xf5\x86\xce\'oi\xae\x1f\xe6[C3\x81\xedU\xa4\x06\x93I\
\xf5G\xb1\xa4\x8d\xd7B\xcf\x12,\xf1\x19\x0f\x8fU5l\x9drtaYx `\xb7=%\xbb\xa8\
\x8c\xd0\xe0\x10\xdf?~\xd3u\xfe3\x93}\xd5\xad.\xb4\xc6\x96\xc9\x04\xbf\xc5\
\xbd9\xfay\xdaW\x9a4\xb517\xd5\xdc\xbc&\x07mE\xdeE\x06\x07\x8f\xee\xbe\xd2\
\xf2s\xd1\xd1\x04\xfe\x01}\xb6\r\x17\x1bK\xa9J\x00\x00\x00\x00IEND\xaeB`\x82\
7rVC' )

def getBitmap():
    return BitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return ImageFromStream(stream)

