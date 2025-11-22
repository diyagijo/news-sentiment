# 1. Use the "Bookworm" version (Stable Linux with Java 17 support)
FROM python:3.10-slim-bookworm

# 2. Install Java 17 (Now this will work guaranteed)
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    apt-get clean;

# 3. Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# 4. Set working directory
WORKDIR /app

# 5. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy code and data
COPY app.py .
COPY Sarcasm_Headlines_Dataset.json .

# 7. Expose port
EXPOSE 8501

# 8. Run app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]