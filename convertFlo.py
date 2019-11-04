from os.path import join

import flowiz as fz
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm
import sys

dataset='Mushroom'
datatype=['', 'orig', 'tip', 'inter', 'gdci', ]

typeindex=int(sys.argv[1]) # 把数字作为参数传进来
filepathFlo='./dataset/flo/inference/run.epoch-0-flow-field/'
filepathPng='./dataset/VideoR/'+dataset+'/png/'+datatype[typeindex]+'/'
files = sorted(glob.glob(join(filepathFlo + '*.flo')))
with tqdm(total=len(files), ncols=60) as pbar:
    for fi in range(len(files)):
        pbar.update(1)
        img = fz.convert_from_file(files[fi])
        # plt.savefig(img)
        plt.imsave(join(filepathPng + ('%05d' % (fi+1)) + '.png'), img)
