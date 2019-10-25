from PIL import Image
import sys, os
source_file = ''
filename_template = ''
try:
    if len(sys.argv) == 3:
        source_file = sys.argv[1]
        filename_template = sys.argv[2]
        if os.path.isfile(source_file):
            for size in [1024,512,256,128,152,180,120,80,87,58,60,40,167,36,48,72,96,144,192]:
                imgname = filename_template%size
                im = Image.open(source_file)
                im = im.resize((size, size), Image.ANTIALIAS)
                im = im.convert("RGB")
                im.save(imgname, 'PNG')
                print(imgname)
        else:
            raise BaseException("Source image not found")
    else:
        raise BaseException('usage: python3 '+sys.argv[0]+' "sourceimagefile.png" "icon%d.png"')
except BaseException as e:  # 에러 종류
    print(str(e))
