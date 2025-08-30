try:

   from main import StoryGenerator

   generator = StoryGenerator()

   result = generator.generate_story("test prompt")

   print("Test passed:", result)

except Exception as e:

   print("Test failed:", str(e))
