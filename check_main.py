import yaml
import csv
import json
import os
from checkers import whitespace_checker
#, forbidden_characters_checker, syntax_checker, specific_syntax_checker

def load_rules(rule_file_path):
    with open(rule_file_path, "r") as file:
        rules = yaml.safe_load(file)
    return rules

def load_csv_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row[0])  # 各行の最初の要素を追加
    return data

def load_json_data(folder_path):
    json_data_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as json_file:
                data = json.load(json_file)
                json_data_list.append(data)
    return json_data_list



def main():
    datas = load_csv_data("target_folder.csv")
    # チェックルールをロードする
    for data in datas:
        rules = load_rules(f"./rules/rules_{data}.yaml")
        # JSONデータ (仮の例)
        json_data = {"key": " "}
        # フォルダ内のすべてのJSONファイルを読み込む
        json_data_list = load_json_data(f"./Requirement/{data}")
        for json_data in json_data_list:
            # チェック関数とルールの対応
            check_functions = {
                "check_whitespace": whitespace_checker.check,
                #"check_forbidden_characters": forbidden_characters_checker.check,
                #"check_syntax": syntax_checker.check,
                #"check_specific_syntax": specific_syntax_checker.check,
            }

            # 各チェック機能をルールに基づいて実行する
            for rule, check_function in check_functions.items():
                if rules.get(rule):
                    print(check_function(json_data, rules.get(rule)))

if __name__ == "__main__":
    main()
