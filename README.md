# 🔄 ETL Pipeline — Python | Docker | Railway

An end-to-end ETL (Extract, Transform, Load) pipeline built in Python that processes Indian retail sales and product returns data, with CLI control, incremental loading, automated scheduling, Docker containerization, and cloud deployment via Railway.

---

## 📌 Project Overview

| Detail | Value |
|--------|-------|
| Language | Python 3.11 |
| Database | SQLite |
| Scheduler | APScheduler |
| Container | Docker |
| Deployment | Railway |
| Data Sources | Sales CSV, Product Returns CSV |

---

## 📁 Project Structure

```
etl_project/
│
├── data/
│   ├── superstore.csv          ← Raw sales data (50 rows)
│   └── product_returns.csv     ← Product returns data (20 rows)
│
├── output/
│   ├── etl.db                  ← SQLite database
│   ├── sales_output.csv        ← Processed sales data
│   └── returns_output.csv      ← Processed returns data
│
├── logs/
│   └── etl.log                 ← Timestamped pipeline logs
│
├── etl_pipeline.py             ← Main ETL script
├── scheduler.py                ← Automated scheduler
├── requirements.txt            ← Python dependencies
├── Dockerfile                  ← Docker configuration
└── .gitignore
```

---

## ⚙️ Features

- **Extract** — Reads sales and product returns data from CSV files
- **Transform** — Cleans column names, derives new fields (revenue, month, year), removes duplicates
- **Load** — Saves processed data to SQLite database and CSV files
- **CLI Arguments** — Control source and mode directly from terminal
- **Incremental Loading** — Only processes new records since the last pipeline run
- **Logging** — Timestamped logs written to `logs/etl.log`
- **Scheduling** — APScheduler runs the pipeline automatically every 2 minutes
- **Docker** — Fully containerized for consistent runs anywhere
- **Cloud Deployment** — Deployed and running on Railway

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- Anaconda or Miniconda
- Docker (for containerized runs)

### 1. Clone the Repository

```bash
git clone https://github.com/Lakshmipathyakash/etl-pipeline.git
cd etl-pipeline
```

### 2. Create and Activate Conda Environment

```bash
conda create -n etl_env python=3.11
conda activate etl_env
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Pipeline

```bash
# Full load — all sources
python3 etl_pipeline.py --source all --mode full

# Only sales data
python3 etl_pipeline.py --source sales --mode full

# Only returns data
python3 etl_pipeline.py --source returns --mode full

# Incremental — only new records since last run
python3 etl_pipeline.py --source all --mode incremental
```

### 5. Run the Scheduler

```bash
python3 scheduler.py
```

Pipeline triggers automatically every 2 minutes. Press `Ctrl+C` to stop.

---

## 🐳 Docker Usage

### Build the Image

```bash
docker build -t etl-pipeline .
```

### Run the Container

```bash
docker run --name etl-run etl-pipeline
```

### Verify the Run

```bash
docker ps -a
# STATUS: Exited (0) → Success
```

---

## 📊 Data Sources

### Sales Data (`superstore.csv`)

| Column | Description |
|--------|-------------|
| Order ID | Unique order identifier |
| Order Date | Date the order was placed |
| Ship Mode | Shipping method |
| Customer Name | Customer name |
| Region | North / South / East / West |
| Category | Technology / Clothing / Kitchen |
| Product Name | Name of the product |
| Sales | Revenue from the sale (₹) |
| Quantity | Units sold |
| Discount | Discount applied |
| Profit | Profit from the sale (₹) |

### Product Returns (`product_returns.csv`)

| Column | Description |
|--------|-------------|
| return_id | Unique return identifier |
| order_id | Original order reference |
| product | Product name |
| category | Product category |
| return_date | Date of return |
| reason | Defective / Wrong Size / Damaged / etc. |
| refund_amount | Amount refunded (₹) |
| region | Region of return |

---

## 📋 Pipeline Output

After a successful run:

```
🚀 Starting ETL | source=all | mode=full

✅ ETL complete! Check output/ and logs/
```

Sample log (`logs/etl.log`):

```
2026-04-19 17:36:58 | INFO | Pipeline started | source=all | mode=full
2026-04-19 17:36:58 | INFO | Extracting | source=all | mode=full
2026-04-19 17:36:58 | INFO | Sales transformed: 50 rows
2026-04-19 17:36:58 | INFO | Returns transformed: 20 rows
2026-04-19 17:36:58 | INFO | Loaded 50 sales rows to DB + CSV
2026-04-19 17:36:58 | INFO | Loaded 20 returns rows to DB + CSV
2026-04-19 17:36:58 | INFO | Pipeline completed successfully
```

---

## 🧰 Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.11 | Core language |
| Pandas | Latest | Data extraction and transformation |
| SQLite3 | Built-in | Database storage |
| APScheduler | 3.11.2 | Automated scheduling |
| Docker | 29.1.3 | Containerization |
| Railway | — | Cloud deployment |
| GitHub | — | Version control |

---

## ☁️ Deployment

This pipeline is deployed on **Railway** via GitHub integration.

- Railway auto-detects the `Dockerfile`
- Builds and runs the container on every push to `main`
- Status: ✅ Completed

---

## 👤 Author

**Lakshmipathy R**
- GitHub: [@Lakshmipathyakash](https://github.com/Lakshmipathyakash)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
