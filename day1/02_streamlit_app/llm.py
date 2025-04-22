# llm.py
import os
import torch
from transformers import pipeline
import streamlit as st
import time
from config import MODEL_NAME
from huggingface_hub import login

# モデルをキャッシュして再利用
@st.cache_resource
def load_model():
    """LLMモデルをロードする"""
    try:
        # アクセストークンを保存
        hf_token = st.secrets["huggingface"]["token"]
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        st.info(f"Using device: {device}") # 使用デバイスを表示
        
        # Phi-2モデル用の設定
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

def generate_response(pipe, user_question):
    """LLMを使用して質問に対する回答を生成する"""
    if pipe is None:
        return "モデルがロードされていないため、回答を生成できません。", 0

    try:
        start_time = time.time()
        
        # Phi-2モデル用のプロンプト形式
        prompt = f"User: {user_question}\nAssistant:"
        
        # 応答生成
        outputs = pipe(
            prompt, 
            max_new_tokens=512, 
            do_sample=True, 
            temperature=0.7, 
            top_p=0.9,
            return_full_text=False  # プロンプト部分を除外
        )

        # Phi-2の出力から応答を抽出
        assistant_response = ""
        if outputs and isinstance(outputs, list) and len(outputs) > 0:
            # 生成されたテキストを取得
            generated_text = outputs[0].get("generated_text", "").strip()
            assistant_response = generated_text
            
            # 不要なプレフィックスがある場合は削除
            if assistant_response.startswith("Assistant:"):
                assistant_response = assistant_response[len("Assistant:"):].strip()
        
        if not assistant_response:
            # 上記で見つからない場合のフォールバックやデバッグ
            print("Warning: Could not extract assistant response. Full output:", outputs)
            assistant_response = "回答の抽出に失敗しました。"


        end_time = time.time()
        response_time = end_time - start_time
        print(f"Generated response in {response_time:.2f}s") # デバッグ用
        return assistant_response, response_time

    except Exception as e:
        st.error(f"回答生成中にエラーが発生しました: {e}")
        # エラーの詳細をログに出力
        import traceback
        traceback.print_exc()
        return f"エラーが発生しました: {str(e)}", 0
