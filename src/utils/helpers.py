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
                "\n   Calculator - v1.0.0\n",
                "~"*25
            ]

        for line in txt:
            for char in line:
                print(f"{char}\033[0m", end='', flush=True)
                time.sleep(0.04)

    def print_menu(self, menu: list):
        for line in menu:
            for char in line:
                print(f"{char}\033[0m", end='', flush=True)
                time.sleep(0.04)

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
