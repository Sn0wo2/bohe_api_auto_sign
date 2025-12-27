import json
import os
from typing import Dict, Optional

TOKEN_FILE = "./data/token.json"


def load_tokens() -> Dict[str, str]:
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    initial_tokens = {
        "bohe_sign_token": "",
        "linux_do_connect_token": "",
        "linux_do_token": ""
    }
    try:
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_tokens, f, indent=4, ensure_ascii=False)
        return initial_tokens
    except Exception:
        pass
    return {}


def save_tokens(bohe_token: Optional[str] = None,
                linux_do_connect_token: Optional[str] = None,
                linux_do_token: Optional[str] = None) -> None:
    tokens = load_tokens()
    
    if bohe_token:
        tokens["bohe_sign_token"] = bohe_token
    if linux_do_connect_token:
        tokens["linux_do_connect_token"] = linux_do_connect_token
    if linux_do_token:
        tokens["linux_do_token"] = linux_do_token

    try:
        with open(TOKEN_FILE, "w", encoding="utf-8") as f:
            json.dump(tokens, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving tokens: {e}")

def get_token(key: str) -> Optional[str]:
    tokens = load_tokens()
    return tokens.get(key)