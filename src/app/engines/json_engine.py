from pathlib import Path

import json
import os


class JsonEngine:
    def ensure_exists(self) -> Path:
        curr_dir = os.getcwd()
        src_dir = os.path.join(curr_dir, "src")
        data_dir = os.path.join(src_dir, "data")

        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        json_file = os.path.join(data_dir, "config.json")

        if not os.path.isfile(json_file):
            with open(json_file, 'w+', encoding="utf-8-sig") as new:
                json.dump({"history": []}, new, indent=2)
            
            return json_file

        return json_file
    
    def get_setup_value(self) -> bool:
        json_file = self.ensure_exists()

        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

        return data["setup"]
    
    def update_setup_value(self) -> None:
        json_file = self.ensure_exists()

        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["setup"] = not data["setup"]

    def get_history(self) -> list:
        print("Getting History")
        json_file = self.ensure_exists()

        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            if not data["history"]:
                print("No History Found")
            else:
                print(data["history"])
    
    def save_to_history(self, new_data: dict) -> dict:
        json_file = self.ensure_exists()

        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["history"].append(new_data)

            with open(json_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)
            
    def remove_from_history(self, id: int) -> list:
        json_file = self.ensure_exists()

        with open(json_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            del data["history"][id]

            with open(json_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=4)

                return data
