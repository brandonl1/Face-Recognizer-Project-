# Validating the Face Recognition Model

Validation allows you to estimate how well your trained model performs
on unseen data. This file explains how to organize your validation
dataset and run the validation process.

## Preparing Validation Data

Place images that depict people from your training dataset into the
`validation/` directory. Unlike the training set, you **do not** need
subdirectories here. Each file should contain a single known face. The
names of the files are not used for labeling, so feel free to choose
descriptive filenames.

Example structure:

```
validation/
├── ben_affleck1.jpg
├── ben_affleck2.png
├── michael_jordan1.jpg
└── ...
```

Make sure these images are distinct from those used in training; they
should not be duplicate photos but should depict the same subjects.

## Running Validation

Execute the following command to validate your model:

```sh
python main.py --validate
```

This command loads the encodings from `output/encodings.pkl` and
processes each image in `validation/`, attempting to recognize the
faces. For each image, a window will appear showing the image with
bounding boxes around detected faces and labels for recognized faces.

Validation serves two purposes:

1. **Quality Check** – If the model labels faces correctly on your
   validation images, it’s likely to perform well on similar data.
2. **Debugging** – If certain subjects are misidentified or labeled
   "Unknown," consider adding more images to the training set or
   improving image quality.

## Extending Validation

The provided validation function displays images and labels but does not
compute quantitative metrics. To perform a more rigorous evaluation,
consider extending `validate()` to:

- Compare predicted names against actual names and compute accuracy.
- Generate a confusion matrix or other performance metrics (e.g., recall,
  precision).
- Save annotated validation images to disk instead of displaying them.

Such extensions are straightforward thanks to the modular design of
`face_recognizer`. See `validate.py` for the current implementation.