from flask import Flask, render_template, Response
import cv2
import numpy as np
import torch
import requests
from utils.datasets import letterbox
from utils.general import non_max_suppression, scale_coords
from utils.plots import Annotator
import pygame

MODEL_PATH = 'runs/train/exp4/weights/best.pt'
URL = "http://172.30.1.2"

img_size = 640
conf_thres = 0.5
iou_thres = 0.45
max_det = 1000
classes = None
agnostic_nms = False

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

ckpt = torch.load(MODEL_PATH, map_location=device)
model = ckpt['ema' if ckpt.get('ema') else 'model'].float().fuse().eval()
class_names = ['횡단보도', '빨간불', '초록불']
stride = int(model.stride.max())
colors = ((50, 50, 50), (0, 0, 255), (0, 255, 0))

def set_resolution(url: str, index: int=1, verbose: bool=False):
    try:
        if verbose:
            resolutions = "10: UXGA(1600x1200)\n9: SXGA(1280x1024)\n8: XGA(1024x768)\n7: SVGA(800x600)\n6: VGA(640x480)\n5: CIF(400x296)\n4: QVGA(320x240)\n3: HQVGA(240x176)\n0: QQVGA(160x120)"
            print("available resolutions\n{}".format(resolutions))

        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_quality(url: str, value: int=1, verbose: bool=False):
    try:
        if value >= 10 and value <=63:
            requests.get(url + "/control?var=quality&val={}".format(value))
    except:
        print("SET_QUALITY: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
    except:
        print("SET_QUALITY: something went wrong")
    return awb

app = Flask(__name__)

# pygame 초기화
pygame.init()

# 초록불 및 빨간불에 대한 사운드 로딩
green_light_sound = pygame.mixer.Sound("static/green_light_sound.wav")
red_light_sound = pygame.mixer.Sound("static/red_light_sound.wav")

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    cap = cv2.VideoCapture(URL + ":81/stream")
    set_resolution(URL, index=10)
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            break

        img_input = letterbox(img, img_size, stride=stride)[0]
        img_input = img_input.transpose((2, 0, 1))[::-1]
        img_input = np.ascontiguousarray(img_input)
        img_input = torch.from_numpy(img_input).to(device)
        img_input = img_input.float()
        img_input /= 255.
        img_input = img_input.unsqueeze(0)

        pred = model(img_input, augment=False, visualize=False)[0]

        pred = non_max_suppression(pred, conf_thres, iou_thres, classes, agnostic_nms, max_det=max_det)[0]

        pred = pred.cpu().numpy()

        pred[:, :4] = scale_coords(img_input.shape[2:], pred[:, :4], img.shape).round()

        annotator = Annotator(img.copy(), line_width=3, example=str(class_names), font='data/malgun.ttf')

        for p in pred:
            class_name = class_names[int(p[5])]

            x1, y1, x2, y2 = p[:4]

            if class_name == '초록불':
                annotator.box_label([x1, y1, x2, y2], '%s %d' % (class_name, float(p[4]) * 100), color=colors[int(p[5])])
                green_light_sound.play()
            elif class_name == '빨간불':
                annotator.box_label([x1, y1, x2, y2], '%s %d' % (class_name, float(p[4]) * 100), color=colors[int(p[5])])
                red_light_sound.play()
            else:
                annotator.box_label([x1, y1, x2, y2], '%s %d' % (class_name, float(p[4]) * 100), color=colors[int(p[5])])

        result_img = annotator.result()

        ret, buffer = cv2.imencode('.jpg', result_img)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True) 