import time

total_iterations = 10

for i in range(total_iterations):
    # 何らかの処理
    time.sleep(1)
    # 進捗情報を出力
    progress = (i + 1) / total_iterations * 100
    print(f"進捗: {progress}% 完了")
