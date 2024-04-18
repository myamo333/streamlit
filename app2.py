import os
import streamlit as st

def show_folder_structure(folder_path):
    st.sidebar.markdown("### フォルダ構造")

    # フォルダ構造を再帰的に取得する関数
    def list_folders(folder, level=0):
        folders = []
        for item in os.listdir(folder):
            item_path = os.path.join(folder, item)
            if os.path.isdir(item_path):
                folders.append((item, item_path, level))
        return folders

    # フォルダ構造を表示する関数
    def display_folders(folders):
        for folder, _, level in folders:
            st.sidebar.write("    " * level + f"|- {folder}")

    # フォルダ構造を取得して表示
    folders = list_folders(folder_path)
    display_folders(folders)


# 表示するフォルダのパス
folder_path = "/Users/yuhei/Documents"
show_folder_structure(folder_path)
