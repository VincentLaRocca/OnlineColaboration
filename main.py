class StoryGenerator:

   def __init__(self):

       self.prompt = ""  # Store the story prompt



   def generate_story(self, prompt):

       self.prompt = prompt

       return f"Once upon a time, {self.prompt}..."



if __name__ == "__main__":

   generator = StoryGenerator()
