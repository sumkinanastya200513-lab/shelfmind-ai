import cv2
import pandas as pd

from detector import detect_price_tags
from ocr_module import extract_text
from qr_module import read_qr
from utils import parse_fields


def process_video(video_path):

    cap = cv2.VideoCapture(video_path)

    results = []

    frame_id = 0

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        # берем каждый 5 кадр
        if frame_id % 5 != 0:
            frame_id += 1
            continue

        detections = detect_price_tags(frame)

        for det in detections:

            x1, y1, x2, y2 = det

            crop = frame[y1:y2, x1:x2]

            text = extract_text(crop)

            qr_data = read_qr(crop)

            fields = parse_fields(text)

            fields.update(qr_data)

            fields["x_min"] = x1
            fields["y_min"] = y1
            fields["x_max"] = x2
            fields["y_max"] = y2

            results.append(fields)

        frame_id += 1

    cap.release()

    return pd.DataFrame(results)