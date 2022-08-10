import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# Images
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
img = "c.jpg"
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
results.save()  # or .show(), .save(), .crop(), .pandas(), etc.
results.crop()  # or .show(), .save(), .crop(), .pandas(), etc.
results.pandas()  # or .show(), .save(), .crop(), .pandas(), etc.
