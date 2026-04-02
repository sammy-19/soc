import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import BlogPost

@receiver(post_save, sender=BlogPost)
def post_to_facebook(sender, instance, created, **kwargs):
    """
    Automatically post to Facebook when a blog post is published.
    """
    if instance.is_published and settings.FACEBOOK_PAGE_ACCESS_TOKEN:
        try:
            # Build the message
            message = f"{instance.title}\n\n{instance.excerpt or instance.content[:200]}..."
            
            # Get the full URL to the blog post
            post_url = f"https://www.soczambia.org{instance.get_absolute_url()}"
            
            # Prepare the data for Facebook API
            data = {
                'message': message,
                'link': post_url,
                'access_token': settings.FACEBOOK_PAGE_ACCESS_TOKEN
            }
            
            # If there's an image, include it
            if instance.image:
                data['picture'] = instance.image.url
            
            # Post to Facebook
            response = requests.post(
                f"https://graph.facebook.com/{settings.FACEBOOK_PAGE_ID}/feed",
                data=data
            )
            
            if response.status_code == 200:
                print(f"Successfully posted to Facebook: {instance.title}")
            else:
                print(f"Failed to post to Facebook: {response.text}")
                
        except Exception as e:
            print(f"Error posting to Facebook: {str(e)}")