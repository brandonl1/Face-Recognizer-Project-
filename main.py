#!/usr/bin/env python3
"""Command-line interface for the face recognizer project.

This script provides a convenient entry point for interacting with the
face recognition project from the terminal. It exposes commands to train
the model, validate it on a set of images, and test it on an unknown
image. Under the hood, it dispatches to functions defined in the
``face_recognizer`` package.

Usage examples::

    # Train the model on images located in the `training/` directory
    python main.py --train -m hog

    # Validate the trained model on images in the `validation/` directory
    python main.py --validate

    # Test the model on a single image
    python main.py --test -f path/to/image.jpg

Run ``python main.py --help`` to see all available options.
"""

import argparse
from pathlib import Path
from face_recognizer import encode_known_faces, recognize_faces, validate

def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments using argparse.

    Returns:
        argparse.Namespace: Parsed arguments with attributes corresponding to
            each CLI option.
    """
    parser = argparse.ArgumentParser(description="Recognize faces in an image")
    parser.add_argument(
        "--train", action="store_true", help="Train on input data in the training directory"
    )
    parser.add_argument(
        "--validate", action="store_true", help="Validate the trained model on the validation directory"
    )
    parser.add_argument(
        "--test", action="store_true", help="Test the model with an unknown image"
    )
    parser.add_argument(
        "-m",
        action="store",
        default="hog",
        choices=["hog", "cnn"],
        help="Which model to use for face detection: hog (CPU) or cnn (GPU)",
    )
    parser.add_argument(
        "-f", action="store", help="Path to an image with an unknown face for testing"
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for command-line execution.

    Determines which action(s) to perform based on parsed arguments and calls
    the corresponding functions from the ``face_recognizer`` package.
    """
    args = parse_arguments()
    if args.train:
        encode_known_faces(model=args.m)
    if args.validate:
        validate(model=args.m)
    if args.test:
        if not args.f:
            raise ValueError("You must provide an image path with -f when testing.")
        recognize_faces(image_location=args.f, model=args.m)


if __name__ == "__main__":
    main()