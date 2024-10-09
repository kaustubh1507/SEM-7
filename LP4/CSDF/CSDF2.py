from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os


# Function to generate random characters for the CAPTCHA
def generate_random_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# Function to generate CAPTCHA image
def generate_captcha(text):
    width, height = 160, 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # Try to load arial font, fallback to default if not found
    try:
        font = ImageFont.truetype('arial.ttf', 40)  # Specify path to font
    except OSError:
        font = ImageFont.load_default()  # Use default font if the specified font is unavailable

    draw = ImageDraw.Draw(image)

    # Drawing text on image
    for i, char in enumerate(text):
        x = 10 + i * 24  # Adjust positioning
        y = random.randint(10, 20)
        draw.text((x, y), char, font=font,
                  fill=(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)))

    # Applying some distortions for extra security
    image = image.filter(ImageFilter.GaussianBlur(1))

    # Adding noise
    for _ in range(100):
        draw.point((random.randint(0, width), random.randint(0, height)),
                   fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # Save the image
    image.save('captcha_image.png')
    return text


# Function to verify user input
def verify_captcha(user_input, actual_captcha):
    return user_input.upper() == actual_captcha


# Main program
if __name__ == "__main__":
    # Generate CAPTCHA
    captcha_text = generate_random_text()
    print(f"Generated CAPTCHA: {captcha_text}")
    generate_captcha(captcha_text)

    # Show CAPTCHA image to the user
    captcha_image = Image.open('captcha_image.png')
    captcha_image.show()

    # Ask user for input
    user_input = input("Enter the CAPTCHA text: ")

    # Verify if the input matches the CAPTCHA
    if verify_captcha(user_input, captcha_text):
        print("CAPTCHA Verified successfully!")
    else:
        print("CAPTCHA Verification failed.")
