# Testing the Model on New Images

Once your model is trained and validated, you can use it to recognize
faces in entirely new images. This document provides instructions for
running the test command and interpreting its output.

## Selecting Test Images

Test images can contain one or multiple faces and do not need to have
any specific directory structure. Simply provide the path to the file
you wish to analyze. Ensure that:

- The image is reasonably sized (very large images may slow down
  detection).
- Faces are clear and not heavily occluded.
- Faces are of subjects that the model has been trained on, otherwise
  they will be labeled as "Unknown".

## Running the Test Command

To identify faces in a single image, run:

```sh
python main.py --test -f path/to/image.jpg
```

Replace `path/to/image.jpg` with the actual path to your test image.
By default, the script uses the HOG-based face detector. Use `-m cnn`
to select the GPU-accelerated detector if available:

```sh
python main.py --test -f path/to/image.jpg -m cnn
```

The script will:

1. Load the saved encodings from `output/encodings.pkl`.
2. Detect all faces in the given image using the selected model.
3. Compare each detected face’s encoding to your known encodings.
4. Draw a bounding box around each face with the predicted name (or
   "Unknown" if no match is found).
5. Display the annotated image to the user.

If you wish to save the results instead of displaying them, you can
modify the `recognize_faces()` function in `recognition.py` to write the
annotated image to a file with something like:

```python
pillow_image.save("annotated_output.jpg")
```

## Handling Unknown Faces

Faces that do not correspond to any known encoding will be labeled
"Unknown". This is expected behavior when the model encounters
unrecognized subjects. To improve recognition coverage, add more images
of the relevant person to the training set and re-run training.

## Troubleshooting

- **No window appears** – Ensure that your environment supports image
  display (e.g., a local machine with GUI support). When running on a
  headless server, modify the code to save images instead of showing
  them.
- **Incorrect labels** – Review your training data for quality and
  quantity. Consider collecting more diverse images of the mislabeled
  subject.

Happy testing!