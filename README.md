# 🚀 Space4Kids Telegram Bot

> A Telegram bot built for the **SK Kids Challenge**, designed to help users navigate the [space4kids.ru](https://space4kids.ru) website — with space facts, bilingual support, and small talk.

**🏆 1st place winner at SK Kids Challenge**

> [!NOTE]
> The bot is currently offline. It was hosted at [@Space4KidsBot](https://t.me/Space4KidsBot).

---

## ✨ Features

### 🗺️ Site Navigation
The bot acts as an interactive guide to [space4kids.ru](https://space4kids.ru), giving users quick access to all major sections and subsections via keyboard buttons — no need to browse the website manually.

### 🌌 Random Space Facts
Hit the **"👀 Ты этого точно не знал!"** button and get 10 random space facts from a curated list of 60+ facts (Russian only).

### 💬 Small Talk
The bot responds to casual messages like greetings and simple questions:
- `Привет!` → `Привет!`
- `Как дела?` → `Хорошо!`
- `Что делаешь?` → `Помогаю людям!`

### 🌐 Bilingual Support

| Feature | 🇷🇺 Russian | 🇬🇧 English |
|---|---|---|
| Main sections | ✅ | ✅ |
| Subsections | ✅ | ❌ |
| Random space facts | ✅ | ❌ |
| Small talk | ✅ | ❌ |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Library:** [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (`telebot`)
- **Structure:**
  - `skbot.py` — main bot logic, message handlers, space facts list
  - `menu.py` — menu and submenu button definitions

---

## 📁 Project Structure

```
space4kids-telegram-bot/
├── skbot.py       # Bot entry point — handlers, facts, logic
├── menu.py        # Menu button definitions and submenu links
└── README.md
```

---

## 📄 License

This project has no explicit license. Feel free to explore and learn from the code.
