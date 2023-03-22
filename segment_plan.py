import cv2
from matplotlib import pyplot as plt
import numpy as np


def segment(filename:str):

    img = cv2.imread(filename)
    img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)