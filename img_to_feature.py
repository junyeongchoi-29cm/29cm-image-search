from pathlib import Path

import numpy as np
from PIL import UnidentifiedImageError
from tensorflow.keras.preprocessing.image import load_img

from feature_extractor import FeatureExtractor
from PIL.Image import open

if __name__ == '__main__':
    fe = FeatureExtractor()

    for img_path in sorted(Path("./static/img").glob("*.jpg")):
        try:
            feature_path = Path("./static/feature") / (img_path.stem + ".npy")  # e.g., ./static/feature2/xxx.npy
            if feature_path.exists():
                continue
            print(img_path)  # e.g., ./static/img/xxx.jpg
            feature = fe.extract(load_img(img_path, color_mode='rgb'))
            np.save(feature_path, feature)
        except UnidentifiedImageError as e:
            print("Wrong Image" + str(e))
