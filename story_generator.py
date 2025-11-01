import os 
from dotenv import load_dotenv
from google import genai
from gtts import gTTS
from io import BytesIO

load_dotenv()

google_api = os.getenv("GOOGLE_API_KEY")
if not google_api:
    raise ValueError("Api key not found")

client = genai.Client(api_key=google_api)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = "what is a car expain in 400 words ?"
)

def create_advanced_prompt(style):

    base_prompt = f"""
    **Your Persona:** You are a friendly and engaging storyteller. Your goal is to tell a story that is fun and easy to read.
    **Your main goal:** Write a story in simple, clear, and modern English.
    **Your Task:** Create one single story that connects all the provided images in order.
    **Style Requirement:** The story must fit the '{style}' genre.
    **Core Instructions:**
    1. **Tell One Single Story:** Connect all images into a narrative with beginning, middle, and end.
    2. **Use Every Image:** Include a key detail from each image.
    3. **Creative Interpretation:** Infer the relationships between the images.
    4. **Nationality:** Use ONly Indian Names, Chracters, Places, Persona Etc.
    **Output Format:**
    -   **Title:** Start with a simple and clear title.
    -   **Length:** The story must be between 4 and 5 paragraphs.
"""
    
    style_instruction = ""
    if style == "Morale":
        style_instruction = "\n**Special Section:** After the story, you MUST add a section starting with the exact tag `[MORAL]:` followed by the single-sentence moral of the story."
    elif style == "Mystery":
        style_instruction = "\n**Special Section:** After the story, that reveals the culprit and the key clue."
    elif style == "Thriller":
        style_instruction = "\n**Special Section:** After the story, that reveals a final, shocking twist."

    return base_prompt + style_instruction

# function -> images -> style -> story
def generate_story_from_images(images,style):
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents = [images, create_advanced_prompt(style)]
    )

    return response.text

def narrate_story(story_text):
    try: 
        tts = gTTS(text=story_text,lang='en',slow = False)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)  
        return audio_fp
    except Exception as e:
        return f"An unexpected error occured during the API call"