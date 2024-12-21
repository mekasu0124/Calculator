import json
import os


class Config:
    """
    A custom Config class used for creating app-needed
    files on launch. This process is in place to protect
    
    """

    def __init__(self):
        pass

    def start_setup(self):
        curr_dir = os.getcwd()
        src_dir = os.path.join(curr_dir, "src")
        
        data_dir = os.path.join(src_dir, "data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        config_file = os.path.join(data_dir, "config.json")

        if not os.path.isfile(config_file):
            default_dict = {
                "setup": False,
                "history": []
            }

            with open(config_file, 'w+', encoding="utf-8-sig") as f:
                json.dump(default_dict, f, indent=2)