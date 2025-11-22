import streamlit as st
import pandas as pd
import requests
from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

# 1. Start Spark (This uses the Docker Java 17)
spark = SparkSession.builder.appName("NewsSentimentApp").getOrCreate()

# 2. Load Data
try:
    df_large = spark.read.json("Sarcasm_Headlines_Dataset.json")
    df_large = df_large.selectExpr("headline as text", "is_sarcastic as label")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# 3. Train Model
train, test = df_large.randomSplit([0.8, 0.2], seed=42)
tokenizer = Tokenizer(inputCol="text", outputCol="words")
remover = StopWordsRemover(inputCol="words", outputCol="filtered")
hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures", numFeatures=5000)
idf = IDF(inputCol="rawFeatures", outputCol="features")
lr = LogisticRegression(featuresCol="features", labelCol="label")

pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf, lr])
model = pipeline.fit(train)

# 4. Fetch News
API_KEY = "6309ce02cac045199be2c849359f2d62" 

def fetch_live_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    try:
        response = requests.get(url).json()
        if response.get("status") != "ok":
            return []
        return [a["title"] for a in response.get("articles", []) if a.get("title")]
    except:
        return []

# 5. Dashboard
st.title("News Sentiment Dashboard")

headlines = fetch_live_news()
if headlines:
    df_live = spark.createDataFrame([(t, 0) for t in headlines], ["text", "label"])
    preds = model.transform(df_live).select("text", "prediction").toPandas()
    preds["Sentiment"] = preds["prediction"].apply(lambda x: "Positive" if x == 1 else "Negative")
    
    st.write(f"Fetched {len(preds)} headlines")
    st.table(preds[["text", "Sentiment"]])
    st.bar_chart(preds["Sentiment"].value_counts())
else:
    st.warning("No news fetched. Check API Key.")