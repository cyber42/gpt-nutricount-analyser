# GTPNutriCount Image Analyzer

[gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) generated project, case study, fully operational. `gpt-engineer` prompts used are in `prompt00` and `prompt01` files. `prompt01` was executed using the `--improve` flag to `gpt-engineer`.

## Description
GTPNutriCount Image Analyzer is a command-line tool that estimates the nutritional values of food items based on photos.  Given an input folder as an argument, it recursively iterates through sub-folders searching for single image files and groupped image files in folders named Item... There are single photos of food items in the input folder and groupped photos of food items in the Item folders. Groupped photos depict the same item in different orientations. Supported photo formats include .jpg, .jpeg, .png, .gif, etc. 

## Usage
To use the tool, run the following command in your terminal:

    export OPENAI_API_KEY={your key}
    python -m main <path_to_folder>

Replace `<path_to_folder>` with the path to the folder containing the Item directories.

## Output
The tool creates a `NutriCountEstimate__....json` files with the estimated nutritional values.

## Requirements
- Python 3.11
- Install the required packages using:

    pip install -r requirements.txt