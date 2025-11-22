# 📰 Real-Time News Sentiment Analysis (Dockerized)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PySpark](https://img.shields.io/badge/Apache%20Spark-PySpark-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)

A real-time data pipeline that fetches live financial news, processes text using **Apache Spark (PySpark)**, and classifies headlines as **Positive** or **Negative** using a Logistic Regression model. The entire application is containerized using Docker to resolve Java/Python dependency conflicts.

---

## 🚀 Features
*   **Live Data Fetching:** Integrates with NewsAPI to get real-time headlines.
*   **Big Data Processing:** Uses PySpark MLlib for Tokenization, Stopword Removal, and TF-IDF hashing.
*   **Machine Learning:** Logistic Regression model trained on the Sarcasm/News Headlines dataset.
*   **Containerization:** Fully Dockerized (Debian Bookworm base) to ensure Java 17 and Python 3.10 compatibility.
*   **Interactive Dashboard:** Built with Streamlit for visualization.

---

## 🐳 Quick Start (Run with Docker)
The easiest way to run this application is using the pre-built Docker image. You do not need to install Python or Java.

**Prerequisite:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) must be installed and running.

1. **Pull the image:**
   ```bash
   docker pull diyagijo/news-project:latest
