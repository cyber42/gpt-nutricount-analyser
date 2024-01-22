import os
import json
from typing import List

class FileUtils:
    @staticmethod
    def json_file_exists(folder: str) -> bool:
        return 'NutriCountItem.json' in os.listdir(folder)

    @staticmethod
    def get_image_files(folder: str) -> List[str]:
        supported_formats = ('.jpg', '.jpeg', '.png', '.gif')
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(supported_formats)]

    @staticmethod
    def write_json_file(folder: str, data: dict):
        with open(os.path.join(folder, 'NutriCountItem.json'), 'w') as json_file:
            json.dump(data, json_file, indent=4)