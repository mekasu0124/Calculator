from typing import Union, List

import json
import time
import os


class Helpers:
    def print_title_bar(self, subtitle: str = None):
        if subtitle:
            txt = [
                "~"*34 + "\n",
                f"   {subtitle} Calculator - v1.0.0\n",
                "~"*34 + "\n"
            ]
        else:
            txt = [
                "~"*25,
                "   Calculator - v1.0.0\n",
                "~"*25
            ]

        self.typewriter(txt)

    def typewriter(self, object: Union[str, List[str]], delay: float = 0.04):
        if isinstance(object, list):
            for line in object:
                for char in line:
                    print(f"{char}\033[0m", end='', flush=True)
                    time.sleep(delay)
        else:
            for char in object:
                print(f"{char}\033[0m", end='', flush=True)
                time.sleep(delay)

    def get_user_history(self):
        curr_dir = os.getcwd()
        src_dir = os.path.join(curr_dir, "src")
        data_dir = os.path.join(src_dir, "data")
        config_file = os.path.join(data_dir, "config.json")

        with open(config_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            history = data["history"]

            return ['\n'.join([hist for hist in history])] if history else "No Previous Calculations Found"
        
    def clear_console(self):
        return print("\033[3J\033[H\033[2J")
    
    def save_entry(self, entry: dict):
        curr_dir = os.getcwd()
        src_dir = os.path.join(curr_dir, "src")
        data_dir = os.path.join(src_dir, "data")
        config_file = os.path.join(data_dir, "config.json")

        with open(config_file, 'r', encoding="utf-8-sig") as f:
            data = json.load(f)

            data["history"].append(entry)

            with open(config_file, 'w+', encoding="utf-8-sig") as new:
                json.dump(data, new, indent=2)

    def wait_user_input(self):
        input("Press Enter To Continue...")
        self.helpers.clear_console()