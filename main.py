import argparse
from image_processor import ImageProcessor

def main():
    parser = argparse.ArgumentParser(description='GTPNutriCount Image Analyzer')
    parser.add_argument('folder', type=str, help='Path to the folder containing Item directories')
    args = parser.parse_args()

    processor = ImageProcessor(args.folder)
    processor.process_images()

if __name__ == '__main__':
    main()