import os
import json
from typing import List

class FileUtils:
    supported_formats = ('.jpg', '.jpeg', '.png', '.gif')

    @staticmethod
    def json_file_exists(item_path: str) -> bool:
        file_name = os.path.basename(item_path)
        json_file_name = f'NutriCountEstimate__{file_name}.json'
        json_file_path = os.path.join(os.path.dirname(item_path), json_file_name)
        return os.path.exists(json_file_path)

    @staticmethod
    def is_supported_format(file_name: str) -> bool:
        return file_name.lower().endswith(FileUtils.supported_formats)
    
    @staticmethod
    def get_image_files(folder: str) -> List[str]:
        return [os.path.join(folder, f) for f in os.listdir(folder) if FileUtils.is_supported_format(f)]

    @staticmethod
    def write_json_file(item_path: str, data: dict):
        file_name = os.path.basename(item_path)
        json_file_name = f'NutriCountEstimate__{file_name}.json'
        json_file_path = os.path.join(os.path.dirname(item_path), json_file_name)
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
