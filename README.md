# 📬 Daily Quote Email Scheduler

A lightweight automation that emails a **random inspirational quote - in Polish or English - once every weekday morning (Monday-Friday)**.

It fetches a random quote from an external **quotes API**, then sends it to one or more recipients over SMTP. The whole thing runs for free on **GitHub Actions** - no server required - and all credentials are kept safe in **GitHub Secrets**.

---

## ✨ Features

- 🎲 Random quote in **Polish or English** on each run
- 👤 Includes the author's name and, when available, a short bio
- 📅 Runs automatically on a **weekday schedule** via GitHub Actions
- 👥 Supports **multiple recipients** (comma-separated)
- 🔒 Credentials stored in **GitHub Secrets** - nothing sensitive in the code
- 🕵️ Recipient addresses are **masked in the logs** (e.g. `kt*******@g****.com`)

---

## ⚙️ How It Works

1. **GitHub Actions** triggers the workflow on a weekday schedule (or manually).
2. The workflow installs dependencies and runs `daily_quote_email.py`.
3. The script fetches a **random quote (EN or PL)** from the [Quotes API on RapidAPI](https://rapidapi.com/martin.svoboda/api/quotes15).
4. The quote is emailed to every configured recipient via Gmail SMTP.

---

## 🚀 Setup

### 1. Fork or clone the repository

```bash
git clone https://github.com/Ssilith/Email-Scheduler.git
cd Email-Scheduler
```

### 2. Add the required GitHub Secrets

Go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret | Description |
|--------|-------------|
| `EMAIL_ADDRESS` | The Gmail address used to **send** the email |
| `EMAIL_PASSWORD` | A Gmail **[App Password](https://support.google.com/accounts/answer/185833)** (not your normal password) |
| `RECIPIENT_EMAILS` | Recipient address(es), **comma-separated** for multiple |
| `RAPIDAPI_KEY` | Your API key from [RapidAPI](https://rapidapi.com/martin.svoboda/api/quotes15) |

> 💡 Gmail requires 2-Step Verification enabled and an **App Password** for SMTP login.

### 3. Done!

The workflow runs on its schedule automatically. You can also trigger it manually from the **Actions** tab → *Send Daily Quote Email* → **Run workflow**.

---

## 💻 Running Locally

```bash
pip install -r requirements.txt

# Set environment variables
$env:EMAIL_ADDRESS    = "you@gmail.com"
$env:EMAIL_PASSWORD   = "your-app-password"
$env:RECIPIENT_EMAILS = "friend@example.com,colleague@example.com"
$env:RAPIDAPI_KEY     = "your-rapidapi-key"

python daily_quote_email.py
```

---

## 🕒 Schedule

The schedule is defined by the cron expression in [`.github/workflows/send_daily_quote.yml`](.github/workflows/send_daily_quote.yml):

```yaml
schedule:
  - cron: '0 6 * * 1-5'   # 06:00 UTC, Monday–Friday
```

> ⏰ GitHub Actions cron runs in **UTC**. Adjust the hour if you want a specific local time (e.g. CET is UTC+1 in winter, UTC+2 in summer).

---

## 📦 Tech Stack

- **Python 3** + [`requests`](https://pypi.org/project/requests/)
- **Gmail SMTP** (`smtplib`) for delivery
- **GitHub Actions** for scheduling
- **Quotes15 API** (via RapidAPI) for the quotes

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
