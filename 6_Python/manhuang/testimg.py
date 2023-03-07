import aircv as ac
from PIL import Image
import sys
# https://www.iloveimg.com/zh-cn/crop-image

ALL_IMAGE = 'mh_all.png'
IMG_PREFIX = 'imgs/'
def match_img(imgsrc, imgobj, confidencevalue=0.9):  # imgsrc=原始图像，imgobj=待查找的图片   
    img_src =  IMG_PREFIX+imgsrc
    img_obj = IMG_PREFIX+imgobj
    imsrc = ac.imread(img_src)
    imobj = ac.imread(img_obj)
    match_result = ac.find_all_template(imsrc, imobj, confidencevalue)  
    print(f'img_src:{img_src},img_obj:{img_obj},{confidencevalue}.match_result:{match_result}')
    #[{'result': (61.0, 135.5), 'rectangle': ((36, 110), (36, 161), (86, 110), (86, 161)), 'confidence': 1.0}]
    return match_result

def match_img_pos(imgobj, confidencevalue=0.9):
    xyt = match_img(ALL_IMAGE, imgobj, confidencevalue)    
    if xyt != None and len(xyt) > 0:
        x = xyt[0]['result'][0]
        y = xyt[0]['result'][1]
        return (int(x), int(y))
    return (0,0)

if __name__ == "__main__":
    imgname = "welfare.png"
    confidence_val=0.8
    argv = sys.argv[1:]
    if argv:
        imgname = argv[0]
        if len(argv) > 1:
            print(argv)
            confidence_val = float(argv[1])

    res = match_img(ALL_IMAGE, imgname, confidencevalue=confidence_val)
    all_img = Image.open(IMG_PREFIX+ALL_IMAGE)
    for img in res:
        rect = img['rectangle']
        start = rect[0]
        end = rect[3]
        print(f'start:{start},end:{end}')
        im = all_img.crop((start[0], start[1], end[0], end[1]))
        im.show()
        print(img['rectangle'][0])

    pos = match_img_pos(imgname)
    print(f'pos:{pos}')
    


