# Training the Face Recognition Model

This guide explains how to prepare your environment and data for training
the face recognition model, then walks through the training process.

## Environment Setup

Before you can train the model, ensure the following:

1. **Install Dependencies** – Install the Python packages listed in
   `requirements.txt`. Using a virtual environment is highly recommended.
   See the top-level `README.md` for instructions.

2. **C++ Build Tools** – The `dlib` library depends on a C++ compiler and
   CMake. On macOS, install them via Homebrew: `brew install cmake gcc`.
   On Ubuntu, use: `sudo apt-get install build-essential cmake`.
   Windows users may install MinGW through Chocolatey: `choco install mingw`.

3. **Python Version** – The code targets Python 3.9+. Versions earlier
   than 3.8 may not be compatible with the pinned package versions.

## Preparing Training Data

The training set lives in the `training/` directory. Organize your
images as follows:

```
training/
├── person1/
│   ├── img1.jpg
│   ├── img2.png
│   └── ...
├── person2/
│   ├── img1.jpg
│   └── img2.png
└── ...
```

Each subdirectory name (e.g., `person1`) will become a label during
recognition. You can include as many images per person as you like.

Tips:

- Use clear, well-lit photos for best results.
- Include multiple images per person with varying angles and expressions.
- Avoid mixing different people in one subdirectory.

## Running the Training Process

To generate face encodings, run the following command from the project
root:

```sh
python main.py --train
```

By default, this uses the HOG model for face detection. If you have a
GPU and want to leverage a convolutional neural network, specify `cnn`:

```sh
python main.py --train -m cnn
```

Depending on your dataset size and hardware, training may take some
time. Once complete, a file named `encodings.pkl` will appear in the
`output/` directory. This file contains all the learned encodings and
must exist before you can validate or test the model.

## Troubleshooting

- **No faces found** – Ensure the images contain frontal faces with
  minimal occlusion. The detection model may struggle with side
  profiles.
- **Performance** – Training can be slow on large datasets. Consider
  pruning duplicate images or using a smaller dataset during development.
- **Path errors** – Use absolute paths or ensure you run commands from
  the project root so that relative paths resolve correctly.

Once training is complete, proceed to validation (see
`README_validate.md`) to evaluate your model’s accuracy.