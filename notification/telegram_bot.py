import telegram
from datetime import datetime
import os

# Load environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')

# Initialize the bot
bot = telegram.Bot(token=bot_token)

def send_message(message):
    bot.send_message(chat_id=chat_id, text=message)

def notify_pipeline_start():
    message = f"Pipeline started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    send_message(message)

def notify_pipeline_success():
    message = f"Pipeline completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    send_message(message)

def notify_pipeline_failure(error):
    message = f"Pipeline failed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\nError: {error}"
    send_message(message)

def notify_model_training_completion():
    message = "Model training completed successfully."
    send_message(message)

def notify_model_performance(metrics):
    message = f"Model performance metrics:\n{metrics}"
    send_message(message)

def notify_ad_revenue_prediction(prediction):
    message = f"Predicted Ad Revenue: ${prediction}"
    send_message(message)
