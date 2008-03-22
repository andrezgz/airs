#----------------------------------------------------------------------
# This file was generated by D:\src\cvl_repository\wxpython\framework\images\make_images.py
#
from wx import ImageFromStream, BitmapFromImage, EmptyIcon
import cStringIO, zlib


def getData():
    return zlib.decompress(
'x\xda\x01\xd8\x02\'\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x02\x8fIDAT8\x8d\xa5\x93KH\x94a\x14\x86\x9f\
\xf9\xc7[e\xd2\xc5R\xc7\xec\xe2d\x16\x95!\xdd\xb3\x92 \x82\x10"\xb0\x8dRA\
\x10DA\xd0\x80\x9bhWD\xd0.\xa4E\xb5\xca\xa4E\x90\x9b$4S\xba\x87P\x94\x15\x95\
\xa1\rZ\xe3\x0c\x939\xce\x8c3\xfa\xff\xdfw\xbe\xbfU\xd3\x8d\xdat\x96\x07\xde\
s\x1e\xce\xfb\x1e\xf8\xcf\xf2\xfc\xde8\xdf\xdd\xe47Z7*-\x07\xc5\xe8be\x04\
\xa5uD\x1biQ\xda\xbd\xde\xdc\xd02\xf8\xd7\x01\xe7\xbb\x02\xf5"4\x97\xcd\xf7\
\x97T\x16\xafaZv>\x8eq\x88N\x8c\xf0t\xa0\x87\xe8h4\xac\x1du\xfc\xca\xa1\xb6\
\x9b\xdf5\xde\x9f\xc5Z\x9b\xab\xeb+j\xe7T\x97\xd5\x10\x99\n38\xd1Ox\xf23\xde\
,/U\x0b6\x92\xd4c3#_\xbf\xd4\xad\xae[\xda\xff\xaa\xfd\xc3\xbb\x0c\xc1\xb9\
\xae\x13\xe5\xae\xe6a\xb5\x7f\x8b\xaf\xa2\xa8\x8a\xfb\xe1;\xa4Si\x94\xab\xc9\
\xcb\xcb\xc5\xc5\xc566+\nV\xf1\xa4\xff.\xef\x83\x83#b\xd4\xb6\xb6c\xdd\x1f-\
\x00\xc4\xdd?{\xd6<\xdf\xe2\xc2\xe5<\x8at3\xa9\xa6H\xabI\x02kOqte\x13\xe3v\
\x8c\xb1x\x84\xa7\xe1{lZ\xb6\x03+G|\x8e\x92\xfd\x00\x16\x80\xd6\xe6\xc0\xa2\
\xf9\x95\xbc\x8f\xbfa41J"\x9d`<\x15\xcb\xdc&\x14\x1cF\xd9)R\xc9\xaf|N\x04\
\xa9\xa9\xacA\x89>\x00\x90\x05\xa0\x8c*\xcd\xcb\x9e\xceP2\x88clNn8\xfb\x8b3\
\x17\xeb[\x01\x08t6\x12\x1a\xff\xc8\xaa\xb9\xebPZ\x95\xfe \x10MJ%I:\t\x94W\
\xfd\xd3wW\x0c\x1e\\\x94h2\x04\x8e\xe8P(6\xb44?7\x9f\xf1\xc91\x02\x0f\x0e\
\x93\x8a&\xb8\xbc\xefFf3\x80\xe5\xb1\xf0\x15,d8\x1aD\x8b\x0ee\x08\x94\x91k/\
\x83\xbd,\x9c\xbe\x04W\xd9xD3g\xf6\x8c_6\x1bq\xb1\x8c\x87\xb2\x82%\xdc\xee\
\xebF\x89\\\xfbA\xa0\xa4\xd5\x88u\xa4w\xe0\x9eos\xf9N\x1e\x0fu\xa0\x8d&\xd0\
\xd9\x88+\x00.9\x96\x97\xda\xf2\xddt\xbcl\'\x9e\x9c\x18\xb1\x8d\xdd\x9a\t\
\xd2\xb3\xb6\xd7\xb15{*\x86\xc6b\xf1\xba\xb8\x1d\xcd\xd9\xee\xdfE\x96\x95\
\x8d\xed\xa4\xc9\xb1\xb2\xf1\x17.\xa7\xaax=\x1d}\xb7\xe8}\xfb*%Z\x1f\xe9;\
\xfd\xe1\xc9\x1fQn\xb8\xb4\xbb\xde\xd1\xaaY\xb2\xa4\xa4v\xc5V\x8a\nJ\xc0\x85\
O\xb1a:_\xf4\x90H\xa6\xc3"\xea\xf8\x8b3\xfd\x99(\xff\xf1L{/\xec\xf0\xdb\xa2\
\x1b\x1d\x91\x83bT\xe6\x99DL\x0bj\xea\xfa\xf3\xb3\x03\x83\xbfk\xfe\xab\xbe\
\x01\xb3ubo\xce}P\x14\x00\x00\x00\x00IEND\xaeB`\x82\x1d\xe8[\xf9' )

def getBitmap():
    return BitmapFromImage(getImage())

def getImage():
    stream = cStringIO.StringIO(getData())
    return ImageFromStream(stream)

