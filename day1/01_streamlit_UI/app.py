import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Streamlit デモ",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for modern look
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f8f9fa;
        padding: 20px;
    }
    
    /* Card styling */
    .stCard {
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
        background-color: white;
    }
    
    /* Header styling */
    h1 {
        color: #1E88E5;
        font-weight: 700;
    }
    
    h2 {
        color: #333;
        font-weight: 600;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 10px;
    }
    
    h3 {
        color: #555;
        font-weight: 500;
    }
    
    /* Button styling */
    .stButton>button {
        border-radius: 6px;
        font-weight: 500;
    }
    
    /* Highlight text */
    .highlight {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 5px;
        border-left: 3px solid #1E88E5;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 30px;
        padding-top: 20px;
        border-top: 1px solid #eee;
        font-size: 14px;
        color: #777;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# サイドバー 
# ============================================
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    st.title("Streamlit デモ")
    st.info("このデモでは、Streamlitの様々な機能を体験できます。")
    
    
    # Navigation
    st.subheader("ナビゲーション")
    page = st.radio(
        "セクションを選択",
        ["基本的なUI要素", "レイアウト", "データ表示", "グラフ表示", "インタラクティブ機能", "カスタマイズ"]
    )
    
    # Show current time
    st.subheader("現在時刻")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.write(current_time)

# ============================================
# ヘッダー
# ============================================
st.title("✨ Streamlit デモ")
st.markdown("### Streamlitの機能を体験しましょう")

# Show different sections based on sidebar selection
if page == "基本的なUI要素":
    # ============================================
    # 基本的なUI要素
    # ============================================
    st.header("基本的なUI要素")
    
    with st.container():
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        
        # テキスト入力
        st.subheader("テキスト入力")
        name = st.text_input("あなたの名前", "ゲスト")
        st.write(f"こんにちは、{name}さん！")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        # ボタン
        st.subheader("ボタン")
        if st.button("クリックしてください", key="basic_button"):
            st.success("ボタンがクリックされました！")
        
        # チェックボックス
        st.subheader("チェックボックス")
        if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
            st.info("これは隠れたコンテンツです！")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        # スライダー
        st.subheader("スライダー")
        age = st.slider("年齢", 0, 100, 25, key="age_slider")
        st.write(f"あなたの年齢: {st.session_state.age_slider}")
        
        # セレクトボックス
        st.subheader("セレクトボックス")
        option = st.selectbox(
            "好きなプログラミング言語は?",
            ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
        )
        st.write(f"あなたは{option}を選びました")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "レイアウト":
    # ============================================
    # レイアウト
    # ============================================
    st.header("レイアウト")
    
    # カラム
    st.subheader("カラムレイアウト")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("これは左カラムです")
        st.number_input("数値を入力", value=10)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("これは右カラムです")
        st.metric("メトリクス", "42", "2%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # タブ
    st.subheader("タブ")
    tab1, tab2, tab3 = st.tabs(["第1タブ", "第2タブ", "第3タブ"])
    with tab1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("これは第1タブの内容です")
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=200)
        st.markdown('</div>', unsafe_allow_html=True)
    with tab2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("これは第2タブの内容です")
        st.code("print('Hello, Streamlit！')")
        st.markdown('</div>', unsafe_allow_html=True)
    with tab3:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.write("これは第3タブの内容です")
        st.info("タブを使うと情報を整理できます")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # エクスパンダー
    st.subheader("エクスパンダー")
    with st.expander("詳細を表示"):
        st.markdown('<div class="highlight">', unsafe_allow_html=True)
        st.write("これはエクスパンダー内の隠れたコンテンツです")
        st.code("print('Hello, Streamlit！')")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "データ表示":
    # ============================================
    # データ表示
    # ============================================
    st.header("データの表示")
    
    # サンプルデータフレームを作成
    df = pd.DataFrame({
        '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
        '年齢': [25, 30, 22, 28, 33],
        '都市': ['東京', '大阪', '福岡', '札幌', '名古屋'],
        '給料': [350000, 420000, 280000, 390000, 450000]
    })
    
    # データフレーム表示
    st.subheader("データフレーム")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # テーブル表示
    st.subheader("テーブル")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.table(df)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # メトリクス表示
    st.subheader("メトリクス")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.metric("温度", "23°C", "1.5°C")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.metric("湿度", "45%", "-5%")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.metric("気圧", "1013hPa", "0.1hPa")
        st.markdown('</div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.metric("風速", "5m/s", "-2m/s")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "グラフ表示":
    # ============================================
    # グラフ表示
    # ============================================
    st.header("グラフの表示")
    
    # ラインチャート
    st.subheader("ラインチャート")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C'])
    st.line_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # バーチャート
    st.subheader("バーチャート")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    chart_data = pd.DataFrame({
        'カテゴリ': ['A', 'B', 'C', 'D', 'E'],
        '値': [10, 25, 15, 30, 20]
    }).set_index('カテゴリ')
    st.bar_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # エリアチャート
    st.subheader("エリアチャート")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    chart_data = pd.DataFrame(
        np.random.randn(20, 3).cumsum(axis=0),
        columns=['X', 'Y', 'Z'])
    st.area_chart(chart_data)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 散布図
    st.subheader("散布図")
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    scatter_data = pd.DataFrame(
        np.random.randn(50, 2),
        columns=['x', 'y'])
    st.scatter_chart(scatter_data)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "インタラクティブ機能":
    # ============================================
    # インタラクティブ機能
    # ============================================
    st.header("インタラクティブ機能")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # プログレスバー
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("プログレスバー")
        progress = st.progress(0)
        if st.button("進捗をシミュレート"):
            for i in range(101):
                time.sleep(0.01)
                progress.progress(i / 100)
            st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # ファイルアップロード
        st.markdown('<div class="stCard">', unsafe_allow_html=True)
        st.subheader("ファイルアップロード")
        uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
        if uploaded_file is not None:
            # ファイルのデータを表示
            bytes_data = uploaded_file.getvalue()
            st.write(f"ファイルサイズ: {len(bytes_data)} bytes")
            
            # CSVの場合はデータフレームとして読み込む
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                st.write("CSVデータのプレビュー:")
                st.dataframe(df.head())
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 日付選択
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("日付選択")
    col1, col2 = st.columns(2)
    with col1:
        d = st.date_input("日付を選択", datetime.now())
        st.write(f"選択された日付: {d}")
    with col2:
        t = st.time_input("時間を選択", datetime.now().time())
        st.write(f"選択された時間: {t}")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # スライダーの高度な使用法
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("範囲スライダー")
    values = st.slider(
        "範囲を選択",
        0.0, 100.0, (25.0, 75.0))
    st.write(f"選択された範囲: {values[0]} から {values[1]}")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "カスタマイズ":
    # ============================================
    # カスタマイズ
    # ============================================
    st.header("スタイルのカスタマイズ")
    
    # カスタムCSS
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("カスタムCSS")
    st.markdown("""
    カスタムCSSを使用すると、アプリの見た目を自由にカスタマイズできます。
    """)
    
    st.markdown("""
    <div style="
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin: 10px 0;
    ">
        <h4 style="color: #1E88E5; margin-top: 0;">カスタムスタイルの例</h4>
        <p>これはカスタムCSSでスタイリングされたテキストです！</p>
        <button style="
            background-color: #1E88E5;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
        ">スタイル付きボタン</button>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # アニメーション
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("アニメーションとインタラクション")
    
    if st.button("エフェクトを表示"):
        st.balloons()
        st.snow()
        st.success("🎉 おめでとうございます！特別なエフェクトが表示されました！")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # テーマ
    st.markdown('<div class="stCard">', unsafe_allow_html=True)
    st.subheader("カラーテーマ")
    theme = st.selectbox(
        "テーマを選択",
        ["ブルー", "グリーン", "レッド", "パープル", "オレンジ"]
    )
    
    theme_colors = {
        "ブルー": "#1E88E5",
        "グリーン": "#4CAF50",
        "レッド": "#F44336",
        "パープル": "#9C27B0",
        "オレンジ": "#FF9800"
    }
    
    st.markdown(f"""
    <div style="
        background-color: {theme_colors[theme]}22;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {theme_colors[theme]};
        margin: 10px 0;
    ">
        <h4 style="color: {theme_colors[theme]}; margin-top: 0;">{theme}テーマのサンプル</h4>
        <p>このテキストは選択されたテーマカラーに合わせてスタイリングされています。</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# フッター
# ============================================
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("© 2025 Streamlit デモ | 作成者: AI Engineering講座")
st.markdown('</div>', unsafe_allow_html=True)
