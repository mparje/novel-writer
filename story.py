import openai
import re
import random

def generate_lists(prompt):
    # Generate a set of characters for the story
    character_prompt = f"Generate a set of characters for a story about {prompt}"
    characters = openai.Completion.create(engine="text-davinci-002", prompt=character_prompt, max_tokens=1024, n=1, stop=None, temperature=0.5).choices[0].text

    # Print the generated characters
    print("Generated characters for your story:")
    print(characters)

    # Generate bullet points for the story outline (scenes/chapters)
    outline_prompt = f"Generate bullet points for the outline of a story about {prompt} with the following characters: {characters}, where each bullet point is a scene or chapter in the story"
    outline = openai.Completion.create(engine="text-davinci-002", prompt=outline_prompt, max_tokens=1024, n=1, stop=None, temperature=0.5).choices[0].text

    # Print the generated outline
    print("Generated outline for your story:")
    print(outline)

    # Extract the list of characters
    character_list = characters.strip().split("\n")

    # Extract the list of chapters
    chapter_list = outline.strip().split("\n")
    return character_list, chapter_list

# replace YOUR_API_KEY with your actual API key for the ChatGPT service
openai.api_key = "YOUR_API_KEY"
with open("key.txt", "r") as key_file:
    api_key = key_file.read().strip()
openai.api_key = api_key

# Get the user's story prompt
user_prompt = input("Please provide a simple prompt for your story (e.g. 'a story about a prince'): ")
prompt = user_prompt if user_prompt else "a story about a prince"

character_list, chapter_list = generate_lists(prompt)

# Initialize a dictionary to store the character appearances
character_appearances = {}

# Iterate through the chapters/scenes and update the character appearances
for character in character_list:
    first_appearance = random.randint(1, len(chapter_list))
    last_appearance = random.randint(first_appearance, len(chapter_list))
    # move last apparents
    for i, chapter in enumerate(chapter_list):
        if re.search(character.lstrip("-"), chapter):
            first_appearance = min(first_appearance, i + 1)
            last_appearance = max(last_appearance, i + 1)
    character_appearances[character] = {"first_appearance": first_appearance, "last_appearance": last_appearance}

def print_summary():
    print("SUMMARY:")
    summary = {}
    for i, chapter in enumerate(chapter_list):
        summary[i+1] = {"name": chapter, "characters_first_appear": [], "characters_last_appear": []}
    for character, appearances in character_appearances.items():
        if appearances["first_appearance"] in summary:
            summary[appearances["first_appearance"]]["characters_first_appear"].append(character)
        if appearances["last_appearance"] in summary:
            summary[appearances["last_appearance"]]["characters_last_appear"].append(character)
 
    for chapter_num, chapter_data in summary.items():
        print(f"{chapter_num}. {chapter_data['name']}")
        if chapter_data["characters_first_appear"]:
            for character in chapter_data["characters_first_appear"]:
                print(f"  a. first appearance of {character}")
        if chapter_data["characters_last_appear"]:
            for character in chapter_data["characters_last_appear"]:
                print(f"  b. last appearance of {character}")

print_summary()
