"""
Yolov5 Image Classification Model Inferencing Execution
And generate the report using the sweetviz
Auther: Shailesh S Sarda
"""

import torch
from PIL import Image
import torch.nn.functional as F
from torchvision import transforms as T
from PIL import Image, ImageDraw, ImageFont
import pathlib
import cv2
import os
from pathlib import Path
import sys
from utils.general import increment_path
from io import StringIO
import pandas as pd
import sweetviz


FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


## Pathlib to solve the windows errors
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


IMAGENET_MEAN = 0.485, 0.456, 0.406
IMAGENET_STD = 0.229, 0.224, 0.225


def classify_transforms(size=224):
    return T.Compose([T.ToTensor(), T.Resize(size), T.CenterCrop(size), T.Normalize(IMAGENET_MEAN, IMAGENET_STD)])

## For image
def predict(imgz,name='exp'):
    ## Initialization on torch model hub
    model = torch.hub.load("ultralytics/yolov5", "custom",
                           "runs/best.pt")

    ## Load Image, Apply transformation and convert to tensor results
    imgs = imgz
    image = Image.open(imgs)
    transformations = classify_transforms()
    convert_tensor = transformations(image)
    convert_tensor = convert_tensor.unsqueeze(0)

    results = model(convert_tensor)
    pred = F.softmax(results, dim=1)

    ## Extract the predicted text from the model
    for i, prob in enumerate(pred):
        prob = prob * 100
        top5i = prob.argsort(0, descending=True)[:5].tolist()
        text = '\n'.join(f'{prob[j]:.2f}% {model.names[j]}' for j in top5i)

    save_dir = increment_path(Path('runs/predict-cls') / name, exist_ok=False)  # increment run
    (save_dir).mkdir(parents=True, exist_ok=True)  # make dir


    p = Path(imgs)  # to Path
    save_path = str(save_dir / p.name)

    save_img = imgs
    ## print result and save result
    if save_img:  # Add text to image
        infer_image = Image.open(imgs)
        # print(infer_image.filename) # Get the Image file path
        draw = ImageDraw.Draw(infer_image)
        font = ImageFont.truetype("fonts/16020_FUTURAM.ttf", 
                                    size=20)
        draw.text((5, 5), text=text,
                  fill=(0, 0, 0),
                  font=font)
        infer_image.show()
        infer_image.save(save_path,'JPEG')
        print("[INFO] Image saved Successfully.")
        cols = ['Probability','Emotion_Sign']
        df = pd.read_csv(StringIO(text),  dtype=str, sep=' ',names=cols)
        # my_report = sweetviz.analyze(df, target_feat='Emotion_Sign')
        my_report = sweetviz.analyze(df)
        my_report.show_html('FinalReport.html')



if __name__=="__main__":
    predict('val_data/mohit.png')
