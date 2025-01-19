import os
from openai import OpenAI
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.getenv('API_KEY'),
)

# Function to generate image
def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024"  # You can use "256x256", "512x512", or "1024x1024"
    )

    # Get the image URL from the response
    image_url = response.data[0].url

    return image_url

# Function to save the image
def save_image(image_url, save_path):
    # Send GET request to download the image
    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        # Save the image to the specified path
        with open(save_path, 'wb') as f:
            f.write(image_response.content)
        print(f"Image saved to {save_path}")
    else:
        print("Failed to download image.")

# Main function
def main():
    # Your prompt
    prompt = "A futuristic city skyline at sunset"

    # Generate image based on the prompt
    image_url = generate_image(prompt)

    # Get the current timestamp
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")

    # Set the save path
    save_path = os.path.join(os.getcwd(), "generated", f"image-{timestamp}.png")

    # Save the image to your computer
    save_image(image_url, save_path)

if __name__ == "__main__":
    main()