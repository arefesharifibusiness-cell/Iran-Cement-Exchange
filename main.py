import os
import sys
import json
from datetime import datetime

import requests
from dotenv import load_dotenv

import cement_core as core



load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

DEFAULT_INPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input", "simupdate.xlsx")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

STATE_PATH = os.getenv("SIMAN_STATE_PATH") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "sent_dates.json"
)


def send_telegram_message(text: str, parse_mode: str = "HTML"):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        raise RuntimeError("TELEGRAM_BOT_TOKEN یا TELEGRAM_CHAT_ID تنظیم نشده (فایل .env رو چک کن)")
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    resp = requests.post(url, data={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": parse_mode,
    })
    resp.raise_for_status()


def send_telegram_photo(file_path: str, caption: str = ""):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    with open(file_path, "rb") as f:
        resp = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "caption": caption,
            "parse_mode": "HTML",
        }, files={"photo": f})
    resp.raise_for_status()


def send_telegram_document(file_path: str, caption: str = ""):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as f:
        resp = requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "caption": caption,
        }, files={"document": f})
    resp.raise_for_status()


def load_sent_dates() -> set:
    if not os.path.exists(STATE_PATH):
        return set()
    with open(STATE_PATH, "r", encoding="utf-8") as f:
        return set(json.load(f))


def save_sent_dates(dates: set):
    tmp_path = STATE_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(sorted(dates), f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, STATE_PATH)


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT_PATH
    print(f"در حال خواندن: {input_path}")
    print(f"📍 مسیر فایل حافظه‌ی تاریخ‌های فرستاده‌شده: {STATE_PATH}")

    raw = core.load_data(input_path)
    df = core.clean_data(raw)

    all_dates = sorted(
        d for d in df['تاریخ معامله'].dropna().unique()
        if d and d not in ('0', 'nan', 'None')
    )

    sent_dates = load_sent_dates()
    print(f"تاریخ‌هایی که قبلاً ثبت شدن ({len(sent_dates)} مورد): {sorted(sent_dates)}")

    new_dates = [d for d in all_dates if d not in sent_dates]

    if not all_dates:
        print("⚠️ هیچ تاریخ معتبری تو فایل پیدا نشد؛ کاری برای ارسال نیست.")
        return
    if not new_dates:
        print("همه‌ی تاریخ‌های این فایل قبلاً گزارش شدن؛ چیز جدیدی برای ارسال نیست.")
        return

    print(f"تاریخ‌های جدید برای ارسال: {new_dates}")

    actually_sent = []
    for d in new_dates:
        day_df = df[df['تاریخ معامله'] == d]

       
        summary_html = core.build_summary_html(day_df, date_label=d)
        send_telegram_message(summary_html, parse_mode="HTML")


        try:
            chart_path = os.path.join(OUTPUT_DIR, f"chart_{d.replace('/', '-')}.png")
            core.plot_top_producers(day_df, chart_path, n=10,
                                     title=f"تولیدکننده‌های برتر — {d}")
            send_telegram_photo(chart_path, caption=f"📈 تولیدکننده‌های برتر — {d}")
        except Exception as e:
            print(f"⚠️ ساخت/ارسال عکس نمودار برای {d} با خطا مواجه شد: {e}")

        print(f"✅ گزارش {d} فرستاده شد.")
        actually_sent.append(d)
        sent_dates.add(d)
        save_sent_dates(sent_dates) 

    
    try:
        trend_path = os.path.join(OUTPUT_DIR, "chart_price_trend.png")
        core.plot_price_trend(df, trend_path)
        send_telegram_photo(trend_path, caption="📈 روند قیمت میانگین موزون (کل بازه)")
    except Exception as e:
        print(f"⚠️ ساخت/ارسال نمودار روند قیمت با خطا مواجه شد: {e}")

    dashboard_html = core.create_cement_dashboard_custom(df)
    today_str = datetime.now().strftime("%Y-%m-%d")
    out_path = os.path.join(OUTPUT_DIR, f"dashboard_{today_str}.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(dashboard_html)
    print(f"داشبورد ذخیره شد: {out_path}")

    date_range_label = actually_sent[0] if len(actually_sent) == 1 else f"{actually_sent[0]} تا {actually_sent[-1]}"
    send_telegram_document(out_path, caption=f"📊 داشبورد کامل و تعاملی — {date_range_label}")

    print("با موفقیت به تلگرام ارسال شد ✅")


if __name__ == "__main__":
    main()
