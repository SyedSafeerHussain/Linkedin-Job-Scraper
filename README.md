**LinkedIn Job Scraper Bot**

---

### 🚀 What is This Project?

A fully functional, real-browser LinkedIn job scraper that uses **Playwright in stealth mode** with **session cookies** to extract job postings without being detected. Built in Python with modular design.

---

### 🏢 Key Features

| Feature                      | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| ✔️ Stealth Browsing          | Uses real session cookies to mimic a logged-in user      |
| ✔️ Job Data Extraction       | Scrapes job titles, companies, locations, and links      |
| ✔️ CSV Output                | Saves extracted jobs in a clean CSV format               |
| ✔️ Modular Code Structure    | Easy-to-read code organized into `scraper/` and `utils/` |
| ✔️ Bypass Anti-bot Detection | Avoids LinkedIn's detection using session injection      |

---

### 🗂️ Folder Structure

```bash
linkedin_scraper/
├── scraper/
│   ├── job_extractor.py       # Scrapes job data from LinkedIn
│   ├── playwright_setup.py    # Sets up Playwright browser & context
│
├── utils/
│   ├── csv_writer.py          # Writes output to CSV
│   ├── session_manager.py     # Loads session cookies from file
│
├── main.py                    # Orchestrates scraping workflow
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Ignores cookies.json and sensitive files
```

---

### ⚙️ How to Use

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

#### 2. Add Your Session Cookies

Paste your LinkedIn cookies into `cookies.json` inside the project (this file is gitignored).

#### 3. Run the Scraper

```bash
python main.py
```

---

### 📄 Output Format (CSV)

Each row contains:

* Job Title
* Company
* Location
* Job Link

---

### 🚫 Disclaimer

This project is for educational purposes only. Scraping LinkedIn may violate their Terms of Service. Use responsibly.

---

### ✨ Author

Built by **Safeer Hussain**
Python developer | Automation enthusiast
