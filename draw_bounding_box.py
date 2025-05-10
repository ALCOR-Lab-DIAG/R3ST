import cv2 as cv
import numpy as np
import os
import argparse


def main(frames_path, labels_path, frame_number):
  image_path = os.path.join(frames_path, f"frame_{frame_number}.jpeg")
  print(f"Processing image: {image_path}")

  image = cv.imread(image_path)
  h, w, _ = image.shape

  labels = os.path.join(labels_path, os.path.basename(image_path).replace(".jpeg", ".txt").split("_")[1])

  with open(labels, "r") as f:
    lines = f.readlines()
    for line in lines:
      class_id, cx, cy, bw, bh = map(float, line.split())
      cx, cy, bw, bh = int(cx * w), int(cy * h), int(bw * w), int(bh * h)
      x1, y1, x2, y2 = cx - bw // 2, cy - bh // 2, cx + bw // 2, cy + bh // 2
      cv.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

  cv.imshow("Image", image)
  #cv.imwrite("/output_directory", image)
  cv.waitKey(0)

  return 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames", type=str, required=True, help="Path to frames directory")
    parser.add_argument("--labels", type=str, required=True, help="Path to labels directory")
    parser.add_argument("--frame_number", type=str, required=True, help="Frame number to process")
    args = parser.parse_args()

    main(args.frames, args.labels, args.frame_number)