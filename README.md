
# Lululemon Inventory Tracker

A Python-based automation tool that monitors specific Lululemon product pages for restocks and sends real-time notifications via Telegram.

## Features

* **Headless Monitoring**: Runs silently in the background without interrupting your work.
* **Smart Detection**: Uses Explicit Waits to handle dynamic page loading and avoid "element not found" errors.
* **Mobile Alerts**: Instant Telegram notifications when the "Add to Bag" button becomes active.
* **Anti-Detection**: Includes custom User-Agents and window sizing to blend in with organic traffic.

## Setup & Installation

1. **Install Dependencies**:
```bash
pip install selenium webdriver-manager requests python-dotenv

```


2. **Secrets Management**:
Create a `.env` file in the root directory to store your credentials (do not commit this file to GitHub):
```text
TELEGRAM_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id

```



## Telegram Configuration

To get your bot credentials:

1. **Bot Token**: Search for **@BotFather** on Telegram. Use the `/newbot` command, follow the prompts, and copy the API Token provided. **Important**: Open a chat with your new bot and press **Start**.
2. **Chat ID**: Search for **@userinfobot** on Telegram. Send it any message, and it will reply with your unique numerical ID.

## Tracking Different Products

To track a different item or size, you must provide the "Direct Size URL."

1. Go to [Lululemon's website](https://shop.lululemon.com) on your computer.
2. Navigate to the product you want.
3. **Crucial Step**: Click on the specific **Color** and the specific **Size** you want to track.
4. Look at your browser's address bar. The URL should change to include parameters like `?color=XXXXX&sz=XX`.
5. Copy this **full URL** and paste it into the `url` variable in `main.py`.

> **Note**: If the size is sold out, the URL will still contain the size information. Ensure the page specifically shows your desired size as selected before copying.

## Running the Project

To run the script locally:

```bash
python3 main.py

```

