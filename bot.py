# -*- coding: utf-8 -*-
import os, json, random, asyncio
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

DATA_FILE = "scores.json"
HISTORY_FILE = "history.json"
QUIZ_TIMEOUT = 30
POINTS = {"Easy":5, "Medium":10, "Hard":15}
CATEGORIES = ["أنمي","Free Fire","Gaming","عامة"]

# --- إدارة النقاط ---
def load_scores():
    if not os.path.exists(DATA_FILE): return {}
    try: return json.load(open(DATA_FILE,"r",encoding="utf-8"))
    except: return {}
def save_scores(scores):
    json.dump(scores, open(DATA_FILE,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
def add_points(uid, pts):
    scores = load_scores()
    scores[str(uid)] = scores.get(str(uid),0) + pts
    save_scores(scores)
def top_scores(n=10):
    items = [(int(uid), pts) for uid, pts in load_scores().items()]
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:n]

# --- إدارة السجل ---
def load_history():
    if not os.path.exists(HISTORY_FILE): return {}
    try: return json.load(open(HISTORY_FILE,"r",encoding="utf-8"))
    except: return {}
def save_history(history):
    json.dump(history, open(HISTORY_FILE,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
def record_answer(user_id, question, answer, correct, category, difficulty):
    history = load_history()
    user_history = history.get(str(user_id), [])
    user_history.append({
        "سؤال": question,
        "إجابة": answer,
        "صح": correct,
        "فئة
