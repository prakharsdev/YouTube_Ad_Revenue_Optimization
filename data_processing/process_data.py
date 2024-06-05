from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("YouTubeDataProcessing") \
    .getOrCreate()

# Read data from S3
df = spark.read.json("s3a://youtube-data-bucket/raw/youtube_data.json")

# Process data (e.g., cleaning, aggregations)
processed_df = df.selectExpr('items[0].statistics.viewCount as views', 'items[0].statistics.likeCount as likes')

# Save processed data back to S3
processed_df.write.parquet("s3a://youtube-data-bucket/processed/processed_data.parquet")
