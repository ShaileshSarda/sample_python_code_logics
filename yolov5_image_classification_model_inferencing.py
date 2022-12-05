import torch
from PIL import Image
import torch.nn.functional as F
from torchvision import transforms as T
from PIL import Image, ImageDraw, ImageFont
import pathlib
import cv2

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


IMAGENET_MEAN = 0.485, 0.456, 0.406
IMAGENET_STD = 0.229, 0.224, 0.225

model = torch.hub.load("ultralytics/yolov5", "custom",
                       "runs/best.pt")

def classify_transforms(size=224):
    return T.Compose([T.ToTensor(), T.Resize(size), T.CenterCrop(size), T.Normalize(IMAGENET_MEAN, IMAGENET_STD)])

imgs = "val_data/fear.jpg"
image = Image.open(imgs)
transformations = classify_transforms()
convert_tensor = transformations(image)
convert_tensor = convert_tensor.unsqueeze(0)

results = model(convert_tensor)
print(results)
pred = F.softmax(results, dim=1)

save_img = imgs

for i, prob in enumerate(pred):
    top5i = prob.argsort(0, descending=True)[:5].tolist()
    text = '\n'.join(f'{prob[j]:.2f} {model.names[j]}' for j in top5i)
    print(text)

if save_img:  # Add bbox to image
    infer_image = Image.open(imgs)
    draw = ImageDraw.Draw(infer_image)
    font = ImageFont.truetype("fonts/16020_FUTURAM.ttf", size=14)
    draw.text((10,10), text = text, 
                fill=(0, 0, 0), 
                font=font)
    infer_image.show()

if save_img:
    cv2.imwrite('new.jpg', infer_image)
    print("[INFO] Image saved Successfully.")