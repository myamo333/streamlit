import const
import streamlit as st

import subprocess
import os
st.set_page_config(**const.SET_PAGE_CONFIG)
st.markdown(const.HIDE_ST_STYLE, unsafe_allow_html=True)


st.title('UI検討')

# フォルダ内のHTMLファイルのリストを取得する関数
def get_html_files(folder_path):
    html_files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path) and item.endswith(".html"):
            html_files.append(item)
    return html_files

# ファイルアップロードのUIを作成
uploaded_file = st.file_uploader("ファイルをアップロードしてください", type=['xlsx'])

# サイドバーに説明を追加
st.sidebar.title('ウェブアプリの説明')
st.sidebar.write("""
このウェブアプリは、err.logファイルの内容を表示するものです。
""")



# test.pyスクリプトを実行する
st.write("test.pyスクリプトの実行結果:")
output_text = ""

try:
    process = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    
    for stdout_line in iter(process.stdout.readline, ""):
        # test.pyからの出力を連結
        output_text += stdout_line.strip() + "\n"
    # 連結された出力を一つのコードブロックとして表示
    st.code(output_text.strip(), language='text')

except subprocess.CalledProcessError as e:
    st.error(f"エラーが発生しました: {e.output}")
except subprocess.TimeoutExpired:
    st.error("タイムアウトしました。")


# err.logファイルのパス
err_log_path = "err.log"

# err.logファイルの内容を読み取り、表示する
with open(err_log_path, "r") as f:
    err_log_content = f.read()

st.write("err.logファイルの内容:")
st.code(err_log_content, language='text')

st.write("下記が要件")

# デフォルトのフォルダパスを指定
default_folder_path = "/Users/yuhei/Documents/streamlit/"  # 現在のディレクトリ 
folder_path = default_folder_path
# フォルダの存在を確認してHTMLファイルの一覧を表示
if os.path.exists(folder_path):
    html_files = get_html_files(folder_path)
    if len(html_files) > 0:
        st.sidebar.write("HTMLファイルの一覧:")
        for html_file in html_files:
            if st.sidebar.button(html_file):
                html_content = open(os.path.join(folder_path, html_file)).read()
                st.markdown(html_content, unsafe_allow_html=True)
    else:
        st.sidebar.write("フォルダ内にHTMLファイルが見つかりません。")
else:
    st.sidebar.write("指定されたパスにフォルダが見つかりません。")