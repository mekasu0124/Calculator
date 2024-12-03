import json
import os


class JsonEngine:
    def __init__(self):
        pass

    def create_if_not_exists(self, path):
        curr_dir = os.getcwd()
        src_dir = os.path.join(curr_dir, "src")
        data_dir = os.path.join(src_dir, "data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        json_file_path = os.path.join(data_dir, path)

        if not os.path.isfile(json_file_path):
            default_dict = {
                "setup": False,
                "user_agree": False,
            }

        return json_file_path
    
    def update_setup(self):
        json_path = self.create_if_not_exists("setup.json")

        with open(json_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["setup"] = True

            with open(json_path, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=4)

    def update_user_agree(self):
        json_path = self.create_if_not_exists("setup.json")

        with open(json_path, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["user_agree"] = True

            with open(json_path, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=4)
