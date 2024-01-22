# GTPNutriCount Image Analyzer

[gpt-engineer](https://github.com/gpt-engineer-org/gpt-engineer) generated project, case study, fully operational.

## Description
GTPNutriCount Image Analyzer is a command-line tool that estimates the nutritional values of food items based on photos. It processes images in folders named Item001, Item002, ..., Item999 and generates a JSON file with estimated nutritional information.

## Usage
To use the tool, run the following command in your terminal:

    python -m main <path_to_folder>

Replace `<path_to_folder>` with the path to the folder containing the Item directories.

## Output
The tool creates a `NutriCountItem.json` file in each Item folder with the estimated nutritional values.

## Requirements
- Python 3.11
- Install the required packages using:

    pip install -r requirements.txt