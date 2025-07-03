import tweepy
import schedule
import time
from datetime import datetime
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class TwitterPoster:
    def __init__(self):
        # Initialize Twitter API credentials
        self.consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        
        # Authenticate with Twitter
        self.client = tweepy.Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )
        
        # Optional: For media uploads
        self.auth = tweepy.OAuth1UserHandler(
            self.consumer_key, self.consumer_secret,
            self.access_token, self.access_token_secret
        )
        self.api = tweepy.API(self.auth)
        
        # Post content options
        self.post_options = [
            "Today is a great day to learn something new! #Motivation #DailyThought",
            "Did you know? Continuous learning is the key to success. #Knowledge #Growth",
            "The secret of getting ahead is getting started. - Mark Twain #QuoteOfTheDay",
            "What small step towards your goals will you take today? #Productivity #Goals",
            "Technology is best when it brings people together. #Tech #Innovation"
        ]
    
    def generate_post(self):
        """Generate a post - can be customized with your own logic"""
        # Simple random selection for demonstration
        # You could replace this with AI-generated content, RSS feeds, etc.
        post = random.choice(self.post_options)
        
        # Add date for variety
        today = datetime.now().strftime("%A, %B %d")
        return f"{today}: {post}"
    
    def post_to_twitter(self, text=None, image_path=None):
        """Post text and optionally an image to Twitter"""
        try:
            if not text:
                text = self.generate_post()
            
            if image_path:
                # Upload image
                media = self.api.media_upload(image_path)
                # Post with media
                response = self.client.create_tweet(text=text, media_ids=[media.media_id])
            else:
                # Post text only
                response = self.client.create_tweet(text=text)
            
            print(f"Posted successfully at {datetime.now()}")
            return response
        except Exception as e:
            print(f"Error posting to Twitter: {e}")
            return None
    
    def schedule_daily_post(self, post_time="09:00", image_path=None):
        """Schedule daily posts at a specific time"""
        print(f"Scheduling daily posts at {post_time}...")
        
        def job():
            self.post_to_twitter(image_path=image_path)
        
        schedule.every().day.at(post_time).do(job)
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    poster = TwitterPoster()
    
    # Test posting immediately
    poster.post_to_twitter()
    
    # Uncomment to run the scheduler
    # poster.schedule_daily_post(post_time="09:00")  # 9 AM daily