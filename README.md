# Face Recognizer Project

This repository contains a modular implementation of a simple face
recognition tool based on the [Real Python tutorial on face
recognition]. The goal
of this project is to provide a clean, maintainable code base that you can
customize for your own datasets and extend for new features. 

## Project Structure

```
face_recognizer/       # Python package with core functionality
├── __init__.py        # Package exports
├── encodings.py       # Functions to generate and save face encodings
├── recognition.py     # Functions to recognize faces and draw results
├── validate.py        # Functions to validate the model on known images
output/                # Directory where generated encodings will be stored
training/              # Directory containing subfolders of training images
validation/            # Directory containing validation images
main.py                # Command-line interface for training/validation/testing
requirements.txt       # Pinned project dependencies
README.md              # Top-level documentation (this file)
README_train.md        # Documentation specific to the training process
README_validate.md     # Documentation specific to validation
README_test.md         # Documentation specific to testing
```

### Data Directories

The project expects a specific directory layout for training and validation
data:

- **`training/`** – Contains one subdirectory per person. Each subdirectory
  must be named after the person it contains and hold images of that
  person. For example, `training/ben_affleck/img_1.jpg` and
  `training/ben_affleck/img_2.png` would be valid.
- **`validation/`** – Contains images of known people used to evaluate the
  model’s performance. These images should *not* be part of the training
  set but must depict the same subjects for meaningful validation.
- **`output/`** – Used by the program to store the pickled encodings file
  (`encodings.pkl`). This file is automatically created after training.

Feel free to modify or extend this directory structure. The paths used in
the modules are configurable via function arguments if you wish to store
your data elsewhere.

## Installation

1. **Clone the repository** (or copy these files into your own
   repository).

2. **Create a virtual environment** (recommended) and install
   dependencies:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Prepare your dataset**. Populate the `training/` directory with
   folders named after each subject and the `validation/` directory with
   standalone images of known faces.

> **Note:** This project was originally built on Python 3.9 and tested on
> 3.10. Newer Python versions may require minor adjustments due to changes
> in third-party libraries.

## Usage

All interactions with the project are performed through the `main.py` script.
Run `python main.py --help` to see the available options. The high-level
workflow is summarized below. See the branch-specific README files for
more detailed instructions.

### Train the Model

Generate encodings from your training data. This must be done at least
once before validation or testing:

```sh
python main.py --train
```

You can choose the detection model (HOG for CPU or CNN for GPU) using
`-m`:

```sh
python main.py --train -m cnn
```

### Validate the Model

Run the model on all images in `validation/` to verify its performance:

```sh
python main.py --validate
```

This will display each validation image with bounding boxes and labels
drawn around the detected faces.

### Test on Unknown Images

Provide any image containing unknown faces and get the model’s predictions:

```sh
python main.py --test -f path/to/unknown_image.jpg
```

This command loads the image, detects faces, compares them against known
encodings, and displays the result.

## Customization

- **Data** – Feel free to swap in your own training and validation
  datasets. The directory names within `training/` define the labels used
  during recognition.
- **Extensions** – The modular structure makes it straightforward to add
  features. For example, you can implement video-based recognition by
  iterating over frames and calling the functions in `recognition.py`.
- **Performance** – For better performance on large datasets, consider
  caching intermediate results, using GPU acceleration with the `cnn`
  model, or implementing batch processing.

## Branch-Specific Documentation

This repository includes three supplementary README files:

| File              | Purpose                                           |
|-------------------|---------------------------------------------------|
| **README_train.md**   | Detailed guidance on preparing your environment and training the model |
| **README_validate.md** | Best practices for validating your trained model |
| **README_test.md**     | Instructions for testing the model on new images |

You can use these files as templates for branch-specific documentation in
your own Git branches. For example, you might maintain a `train` branch
dedicated to improving the training process. In that branch, ensure the
root `README.md` points to `README_train.md` for accurate instructions.

## License

This project is provided for educational purposes and is distributed
under the MIT License. See `LICENSE` (if provided) for details.