# 🌍 Multi-Agent SEO Blog Generator 🚀

### 📖 About the Project
The **Multi-Agent SEO Blog Generator** is a Python-based system that **automates blog creation** by researching, planning, generating, and optimizing content using AI-driven agents. It collects **real-world data** from the web and produces **high-quality, SEO-optimized blog posts** on trending HR-related topics.

---

## 🏗️ System Architecture
The system follows a **multi-agent workflow**, where each agent has a defined role:

🔍 **Research Agent** – Gathers trending HR topics and fetches relevant data from **Google Search (via SerpAPI) and Wikipedia**.

📝 **Content Planning Agent** – Creates a **structured blog outline** based on research findings.

✍️ **Content Generation Agent** – Writes **detailed blog sections** using the structured outline and research data.

📈 **SEO Optimization Agent** – Enhances content using **SEO best practices** such as **keyword optimization, readability improvement, and meta descriptions**.

✅ **Review Agent** – Proofreads and ensures **clarity, correctness, and coherence** in the final blog.

📂 **File Generator** – Saves the blog in multiple formats: **Markdown, TXT, HTML, and PDF**.

---

## 🔄 How It Works
1️⃣ **Research Agent** collects **data** from Google and Wikipedia.

2️⃣ **Content Planning Agent** structures the information into an **outline**.

3️⃣ **Content Generation Agent** writes **detailed** and **engaging** blog sections.

4️⃣ **SEO Optimization Agent** ensures **search engine-friendly** formatting and keyword density.

5️⃣ **Review Agent** proofreads and finalizes the blog for **clarity and coherence**.

6️⃣ The final blog post is **saved in multiple formats**.

---

## 🛠️ Technologies Used
🚀 **Python** – Core programming language

🔎 **SerpAPI, Wikipedia API** – Fetching research data from online sources

🛠 **Requests & BeautifulSoup** – Web scraping & content extraction

📜 **Markdown, HTML, TXT, PDF (FPDF/ReportLab)** – Generating multiple output formats

🧠 **Natural Language Processing (NLP)** – Enhancing content quality

📊 **Git & GitHub** – Version control and repository management

---

## 📂 Project Structure
```plaintext
blog_generator/
│-- main.py                  # Main execution script
│-- README.md                # Project documentation
│-- agents/
│   │-- research_agent.py    # Fetches research data
│   │-- content_planning_agent.py  # Creates blog outlines
│   │-- content_generation_agent.py  # Writes content
│   │-- seo_optimization_agent.py  # Enhances SEO
│   │-- review_agent.py      # Proofreads and refines content
│-- blog_posts/              # Folder for generated blogs
```

---

## 🔧 Installation & Setup
### 1️⃣ Install Dependencies
```sh
pip install requests beautifulsoup4 markdown fpdf reportlab
```

### 2️⃣ Get a **SerpAPI Key**
- Sign up at [SerpAPI](https://serpapi.com/) to get an **API key**.
- Replace `YOUR_SERPAPI_KEY` in `research_agent.py`:
  ```python
  self.api_key = "YOUR_SERPAPI_KEY"
  ```

### 3️⃣ Run the Blog Generator
```sh
python main.py
```
✅ The script will **fetch data, generate a structured blog, optimize for SEO, and save it in `blog_posts/`.**

---

## 📂 Output Example
A blog post is generated and saved as:
```plaintext
blog_posts/
│-- remote_work_strategies_2025.md
│-- remote_work_strategies_2025.txt
│-- remote_work_strategies_2025.html
│-- remote_work_strategies_2025.pdf
```

---

## ✨ Features
✔ **Fetches real-world research from Google Search & Wikipedia** 🔍
✔ **Creates structured blog outlines** 📝
✔ **Generates detailed blog content dynamically** ✍️
✔ **Optimizes content for SEO (keywords, readability, meta tags, etc.)** 📈
✔ **Proofreads & improves readability** ✅
✔ **Saves blog in multiple formats (Markdown, TXT, HTML, PDF)** 📂

---

## 🔗 Contributing
Feel free to **fork this repository** and contribute! Open issues, suggest improvements, or add new features. 🚀
