import pyautogui
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
import PIL
import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
import pathlib
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential #.models
import tensorflow_datasets as tfds
import random
import object_detection
from urllib.request import urlopen
from zipfile import ZipFile
import wget
import shutil
import glob
import pandas as pd
import io
import xml.etree.ElementTree as ET
import argparse
from object_detection.utils import dataset_util, label_map_util
from collections import namedtuple

CUSTOM_MODEL_NAME = "wheat"
PRETRAINED_MODEL_NAME = "ssd_mobilnet_v2_fpnlite_320x320_coco17_tpu-8"
PRETRAINED_MODEL_URL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8"
TF_RECORD_SCRIPT_NAME = "generate_tfrecord.py"
LABEL_MAP_NAME = "label_map.pbtxt"

def isWheat():
    wheatLocation = pyautogui.locateOnScreen('./assets/wheat.png', confidence=0.4)
    print(wheatLocation)
    if wheatLocation != None:
        x = wheatLocation[0]/2+wheatLocation[2]/2
        y = wheatLocation[1]/2+wheatLocation[3]/2
        pyautogui.click(x,y)
    return True

def tensWheat():
    print("lets begin")
    # data_dir = pathlib.Path('./assets/wheat')
    # image_count = len(list(data_dir.glob('*/*.png')))
    # print(image_count)
    # wheat = list(data_dir.glob('*'))
    # i = random.randrange(0, len(wheat))
    # im = PIL.Image.open(str(wheat[i]))
    # im.show()
    
    # shutil.move(PRETRAINED_MODEL_NAME+'tar.gz', '../') 
    # tar -zxvf {PRETRAINED_MODEL_NAME+'tar.gz'}
    #config = config_util.get_configs_from_pipeline_file(files['PIPELINE_CONFIG'])
    # print(builder.info)  # num examples, labels... are automatically calculated
    # ds = builder.as_dataset(split='wheat', shuffle_files=True)
    # tfds.show_examples(ds, builder.info)
    # return True