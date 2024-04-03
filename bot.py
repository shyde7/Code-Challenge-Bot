from discord.ext import commands    
import discord
import random

class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Coding Challenge Bot Help",
            description="Hello! I am the Coding Challenge Bot! I offer coding challenges to solve.",
            color=discord.Color.blue()
        )
        embed.add_field(
            name="Commands",
            value=(
                "`!newquestion [difficulty]`: Get a new coding question. "
                "Specify the difficulty (`easy`, `medium`, `hard`) or leave blank for a random question.\n\n"
                "`!check <answer>`: Check your answer for the last question."
            ),
            inline=False
        )
        embed.add_field(
            name="Examples",
            value=(
                "`!newquestion easy`: You'll get an easy coding question!\n\n"
                "`!check Hello World`: Checks if 'Hello World' is the correct answer."
            ),
            inline=False
        )
        embed.set_footer(text="Good luck, and happy coding!")

        channel = self.get_destination()
        await channel.send(embed=embed)

# Initialize the bot with the custom help command
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=CustomHelpCommand())
BOT_TOKEN = "MTIyNDczNDA0NjUyNjExMTgzNA.GxXhiZ.fmkglcBeWwMCteP0t8SCZoo445YYInv5xYoTmI"

# Dictionaries to store current answers by channel
current_answers = {}

# Questions
easy_questions = [
    {"question" : "What is the output of the following code?: ```python\nprint('Hello World')```", "answer" : "Hello World"},
    {"question": "What is the output of the following code?\n```python\na = True\nb = False\nc = False\n\nif a or b and c: \n    print(\"apples\") \nelse: \n    print(\"oranges\")\n```", "answer": "apples"},
    {"question": "What is the output of the following code? \n```python\nx=5\ny=3\nprint(x+y)\n```", "answer": "8"},
    {"question": "What is the output of the following code? WRITE THE ENTIRE STRING:\n```python\na=10\nb=20\nprint(\"The sum is:\", a + b)\n```", "answer": "The sum is: 30"},
    {"question" : "What is the output of the following code?\n```python\nfruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[1])\n```", "answer" : "banana"},
    {"question" : "What is the output of the following code?\n```python\nx = \"Hello, World!\"\nprint(x[2:5])\n```", "answer" : "llo"},
]

medium_questions = [
    {"question" : "What is the output of the following code?: ```python\na = 5\nb = 5\nprint(a is b)```", "answer" : "True"},
    {"question": "What is the output of the following code?\n```python\na = 5\nb = 5\nprint(a is not b)\n```", "answer": "False"},
    {"question": "What is the output of the following code?\n```python\nx = [1, 2, 3]\nx.pop()\nprint(x)\n```", "answer": "[1, 2]"},
    {"question": "What is the output of the following code?\n```python\nx = [1, 2, 3]\nprint(x[1:])\n```", "answer": "[2, 3]"},
    {"question": "What is the output of the following code?\n```python\nx = 10\ny = 3\nprint(divmod(x, y))\n```", "answer": "(3, 1)"},
    {"question": "What is the output of the following code?\n```python\nx = 10\ny = 3\nz = x / y\nprint(round(z, 2))\n```", "answer": "3.33"},
    {"question": "What is the output of the following code?\n```python\nx = 10\ny = 3\nprint(divmod(x, y))\n```", "answer": "(3, 1)"},
]

hard_questions = [
    {"question": "What is the output of the following code? Give your answer in this format: [x₁, x₂, ..., xₙ]\n```python\nx = [1, 2, 3]\ny = x.copy()\nx.append(4)\nprint(y)\n```", "answer": "[1, 2, 3]"},
    {"question": "What is the output of the following code?\n```python\nclass MyClass:\n    def __init__(self, x):\n        self.x = x\n\n    def __repr__(self):\n        return str(self.x)\n\nobj = MyClass(5)\nprint(obj)\n```", "answer": "5"},
    {"question": "What is the output of the following code?\n```python\ndef outer():\n    x = 10\n\n    def inner():\n        nonlocal x\n        x = 20\n        return x\n\n    return inner()\n\nprint(outer())\n```", "answer": "20"},
]

@bot.event 
async def on_ready():
    print("Bot is ready")
    channel = bot.get_channel(1224838735405777016)  # Example channel ID
    embed = discord.Embed(
        title="Coding Challenge Bot is ready!",
        description="I am ready to offer coding challenges. Use `!newquestion` to get started or `!help` if you're confused!",
        color=discord.Color.blurple()
    )

    await channel.send(embed=embed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(brief="Get a new coding question", description="Get a new coding question to solve. You can specify the difficulty of the question by using !newquestion easy, !newquestion medium, or !newquestion hard. If you don't specify a difficulty, I will give you a random question.")
async def newquestion(ctx, difficulty: str= None):
    global current_answers

    if difficulty == "easy":
        question = random.choice(easy_questions)
    elif difficulty == "medium":
        question = random.choice(medium_questions)
    elif difficulty == "hard":
        question = random.choice(hard_questions)
    else:
        all_questions = easy_questions + medium_questions + hard_questions
        question = random.choice(all_questions)
        difficulty = "random"
    
    current_answers[ctx.channel.id] = question["answer"]  # Store answer by channel ID
    embed = discord.Embed(
        title=f"Here is a {difficulty} difficulty coding question for you to solve:",
        description= "Use `!check <answer>` to check your answer.\n\n" + question["question"],
        color=discord.Color.gold()
    )
    await ctx.send(embed=embed)

@bot.command()
async def check(ctx, *, user_answer: str):  # '*' to consume entire message as 'user_answer'
    global current_answers

    correct_answer = current_answers.get(ctx.channel.id, "").strip().lower()

    if not correct_answer:
        await ctx.send("There is no question to check. Use !newquestion to get a new question.")
        return
    
    if user_answer.strip().lower() == correct_answer:
        embed = discord.Embed(
            title="Coding Challenge Check",
            description=f"Your answer: {user_answer}\nCorrect answer: {correct_answer}",
            color=discord.Color.green()
        )
        embed.set_footer(text="Congratulations! Your answer is correct.")
    else:
        embed = discord.Embed(
            title="Coding Challenge Check",
            description=f"Your answer: {user_answer}\nCorrect answer: {correct_answer}",
            color=discord.Color.red()
        )
        embed.set_footer(text="Sorry! Your answer is incorrect.")

    await ctx.send(embed=embed)

# Replace "YOUR_BOT_TOKEN_HERE" with your actual bot token
bot.run(BOT_TOKEN)
