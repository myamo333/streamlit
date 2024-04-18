import yaml

def load_checks_from_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            checks = yaml.safe_load(file)
        print("YAMLファイルを読み込みました。")
        return checks
    except FileNotFoundError:
        print("指定されたファイルが見つかりません。")
        return {}
    except yaml.YAMLError as e:
        print(f"YAMLファイルの読み込みエラー: {e}")
        return {}

# 確認する内容を指定するYAMLファイルのパスを指定してください
yaml_file_path = "checks.yaml"

# YAMLファイルを読み込む
checks = load_checks_from_yaml(yaml_file_path)

# 読み込んだ内容を表示する
print(checks)
