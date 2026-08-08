# 🏭 SimanKala — Cement Market Intelligence

**SimanKala** is an automated data pipeline and reporting system for monitoring the **cement market**.

The system automatically collects and updates market data, processes and analyzes the data, generates interactive reports and visualizations, and sends the latest market insights directly to **Telegram**.

🤖 **Telegram Bot:** `https://t.me/SimanKala_Bot`

---

## 🚀 Features

* 🔄 **Automatic data collection & update** from the market data source
* 📊 Daily cement market analysis
* 📈 Price trend visualization
* 🏭 Top producers analysis
* 📋 Automated daily market summaries
* 🌐 Interactive HTML dashboard
* 📱 Automatic Telegram reporting
* 🖼️ Send charts directly to Telegram
* 📁 Send interactive HTML dashboards to Telegram
* 🧠 Prevent duplicate reports
* 💾 Track previously reported dates
* ⚙️ Supports scheduled daily execution

---

## 🔄 How It Works

```text
        🌐 Data Source
             │
             ▼
      🔄 Update Market Data
             │
             ▼
        📊 Excel Dataset
             │
             ▼
       🧹 Data Processing
             │
             ▼
        📈 Data Analysis
             │
       ┌─────┴─────┐
       ▼           ▼
   📋 Daily      🌐 Interactive
    Report         Dashboard
       │           │
       └─────┬─────┘
             ▼
       🤖 Telegram Bot
          SimanKala
```

---

## 📊 Generated Outputs

### 📋 Daily Market Report

For every new trading date, the system generates a summary report and sends it to Telegram.

### 🏭 Top Producers

A daily chart showing the top cement producers is generated automatically and sent to Telegram.

### 📈 Price Trend

The system generates a price trend chart based on the available market data.

### 🌐 Interactive Dashboard

A complete HTML dashboard is generated with the processed market data and sent to Telegram as a file.

---

## 🔄 Automatic Data Update

The project is designed to keep the dataset up to date automatically.

Instead of manually entering new market data every day:

```text
🌐 Market Website
       ↓
📥 Fetch New Data
       ↓
📊 Update Excel
       ↓
🧹 Clean & Process
       ↓
📈 Analyze
       ↓
🤖 Send Report to Telegram
```

This makes the entire daily reporting workflow automated.

---

## 🧠 Duplicate Report Prevention

SimanKala keeps track of dates that have already been reported.

```text
New Data
   ↓
Check Reported Dates
   ↓
┌───────────────────┐
│ Already reported? │
└─────────┬─────────┘
          │
     ┌────┴────┐
     │         │
    YES       NO
     │         │
   Skip      Report
```

Previously processed dates are stored in:

```text
sent_dates.json
```

This prevents the same daily report from being sent multiple times.

---

## 📱 Telegram Integration

The system uses the Telegram Bot API to automatically send:

* 💬 Daily market summaries
* 📈 Market charts
* 🌐 Interactive HTML dashboards

### Bot

**SimanKala**

---

## 📁 Project Structure

```text
SimanKala/
│
├── main.py
├── cement_core.py
├── requirements.txt
├── .env
├── sent_dates.json
│
├── input/
│   └── simupdate.xlsx
│
└── output/
    ├── chart_*.png
    ├── chart_price_trend.png
    └── dashboard_*.html
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd SimanKala
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

⚠️ **Never commit your `.env` file or Telegram bot token to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
sent_dates.json
output/
__pycache__/
```

---

## ▶️ Run

If the Excel file is located in the default input directory:

```bash
python main.py
```

Or provide a custom Excel path:

```bash
python main.py path/to/simupdate.xlsx
```

---

## ⏰ Automation

The script is designed to run once, process the latest data, generate the reports, send them to Telegram, and exit.

It can therefore be scheduled using:

* Windows Task Scheduler
* Linux Cron
* VPS
* Cloud Server
* GitHub Actions

Example:

```text
Scheduled Task
      ↓
   main.py
      ↓
Update Data
      ↓
Process & Analyze
      ↓
Generate Dashboard
      ↓
Send to Telegram
```

---

## 🛠️ Tech Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| 🐍 Python             | Core application          |
| 📊 Excel              | Market data storage       |
| 🧹 Data Processing    | Cleaning & transformation |
| 📈 Data Visualization | Charts & trends           |
| 🌐 HTML               | Interactive dashboard     |
| 🤖 Telegram Bot API   | Automated reporting       |
| 🔐 python-dotenv      | Environment configuration |

---

## 🎯 Project Goal

SimanKala aims to automate the complete **cement market intelligence workflow**:

```text
Data Collection
      ↓
Data Update
      ↓
Data Processing
      ↓
Data Analysis
      ↓
Visualization
      ↓
Automated Reporting
      ↓
Telegram
```

The goal is to turn raw daily market data into **actionable and easily accessible market insights**.

---

## 🚀 Future Improvements

* 🔎 Search market data by date through Telegram
* 📅 Request historical reports
* 📊 Producer comparison
* 🔔 Automated market alerts
* 📈 Advanced price analysis
* 🤖 AI-powered market insights
* 💬 Natural-language questions over market data
* ☁️ Full VPS deployment
* 📊 Advanced market KPIs



## 👤 Project

