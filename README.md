# Daily Quote Email Scheduler

A simple automation that sends a **random quote in Polish or English once per day (Monday–Friday)** via email.

The project uses an external **quotes API** to retrieve a random quote and **GitHub Actions** to run the scheduler automatically. Email credentials and configuration values are stored securely using **GitHub Secrets**.

## How it Works

1. **GitHub Actions** runs on a weekday schedule.
2. The workflow calls the script.
3. The script fetches a **random quote (EN or PL)** from an API.
4. The quote is sent to the configured email address.

## Configuration

Sensitive values such as:

* SMTP credentials
* API keys
* recipient email address

are stored in **GitHub Secrets**.
