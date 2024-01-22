import os
from file_utils import FileUtils
from openai_client import OpenAIClient

class ImageProcessor:
    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.openai_client = OpenAIClient()

    def process_images(self):
        for dirpath, dirnames, filenames in os.walk(self.root_folder):
            for dirname in dirnames:
                if dirname.startswith('Item'):
                    item_folder = os.path.join(dirpath, dirname)
                    if not FileUtils.json_file_exists(item_folder):
                        image_files = FileUtils.get_image_files(item_folder)
                        if image_files:
                            nutritional_info = self.openai_client.get_nutritional_info(image_files)
                            FileUtils.write_json_file(item_folder, nutritional_info)