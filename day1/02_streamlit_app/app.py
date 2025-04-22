# app.py
import streamlit as st
import ui                   # UIモジュール
import llm                  # LLMモジュール
import database             # データベースモジュール
import metrics              # 評価指標モジュール
import data                 # データモジュール
import torch
from transformers import pipeline
from config import MODEL_NAME
from huggingface_hub import HfFolder

# --- アプリケーション設定 ---
st.set_page_config(page_title="Phi-2 Chatbot", layout="wide")

# --- 初期化処理 ---
# NLTKデータのダウンロード（初回起動時など）
metrics.initialize_nltk()

# データベースの初期化（テーブルが存在しない場合、作成）
database.init_db()

# データベースが空ならサンプルデータを投入
data.ensure_initial_data()

# LLMモデルのロード（キャッシュを利用）
# モデルをキャッシュして再利用
@st.cache_resource
def load_model():
    """LLMモデルをロードする"""
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        st.info(f"Using device: {device}") # 使用デバイスを表示
        pipe = pipeline(
            "text-generation",
            model=MODEL_NAME,
            model_kwargs={"torch_dtype": torch.float16 if device == "cuda" else torch.float32},
            device=device
        )
        st.success(f"モデル '{MODEL_NAME}' の読み込みに成功しました。")
        return pipe
    except Exception as e:
        st.error(f"モデル '{MODEL_NAME}' の読み込みに失敗しました: {e}")
        st.error("GPUメモリ不足の可能性があります。不要なプロセスを終了するか、より小さいモデルの使用を検討してください。")
        return None
pipe = llm.load_model()

# --- Streamlit アプリケーション ---
st.title("🤖 Phi-2 Chatbot with Feedback")
st.write("Phi-2モデルを使用したチャットボットです。回答に対してフィードバックを行えます。")
st.markdown("---")

# --- サイドバー ---
st.sidebar.title("ナビゲーション")
# セッション状態を使用して選択ページを保持
if 'page' not in st.session_state:
    st.session_state.page = "チャット" # デフォルトページ

page = st.sidebar.radio(
    "ページ選択",
    ["チャット", "履歴閲覧", "サンプルデータ管理"],
    key="page_selector",
    index=["チャット", "履歴閲覧", "サンプルデータ管理"].index(st.session_state.page), # 現在のページを選択状態にする
    on_change=lambda: setattr(st.session_state, 'page', st.session_state.page_selector) # 選択変更時に状態を更新
)


# --- メインコンテンツ ---
if st.session_state.page == "チャット":
    if pipe:
        ui.display_chat_page(pipe)
    else:
        st.error("チャット機能を利用できません。モデルの読み込みに失敗しました。")
elif st.session_state.page == "履歴閲覧":
    ui.display_history_page()
elif st.session_state.page == "サンプルデータ管理":
    ui.display_data_page()

# --- フッターなど（任意） ---
st.sidebar.markdown("---")

# 開発者名の管理
if 'developer_name' not in st.session_state:
    st.session_state.developer_name = ""
    st.session_state.edit_mode = True
elif 'edit_mode' not in st.session_state:
    st.session_state.edit_mode = not bool(st.session_state.developer_name)

# 編集モードの切り替え関数
def toggle_edit_mode():
    st.session_state.edit_mode = not st.session_state.edit_mode

# 名前保存関数
def save_name():
    if st.session_state.dev_name_input:
        st.session_state.developer_name = st.session_state.dev_name_input
        st.session_state.edit_mode = False

# 編集モードの場合は入力フィールドを表示
if st.session_state.edit_mode:
    with st.sidebar.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.text_input(
                "開発者名:",
                value=st.session_state.developer_name,
                key="dev_name_input",
                on_change=save_name
            )
        with col2:
            st.button("保存", on_click=save_name, use_container_width=True)
    
    if not st.session_state.developer_name:
        st.sidebar.info("👆 開発者名を入力してください")
# 表示モードの場合は名前を表示
else:
    with st.sidebar.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.info(f"👨‍💻 開発者: {st.session_state.developer_name}")
        with col2:
            st.button("編集", on_click=toggle_edit_mode, use_container_width=True)
