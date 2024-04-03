# Coding Challenge Discord Bot

## Introduction

The Coding Challenge Discord Bot is designed to offer users a unique and interactive way to practice coding by solving various coding challenges. The bot provides questions of varying difficulties (easy, medium, hard) and checks the answers submitted by users.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Installation

To install and run the Coding Challenge Discord Bot on your server, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone the repository to your local machine or download the bot script.
3. Install the required Python packages by running `pip install -U discord.py`.
4. Create a bot on the Discord Developer Portal and obtain a bot token.
5. Replace the placeholder token in the script with your actual bot token.

## Usage

### Commands

- `!help`: Displays help information about available commands.
- `!newquestion [difficulty]`: Retrieves a new coding challenge. You can specify a difficulty (`easy`, `medium`, `hard`) or leave it blank for a random difficulty.
- `!check <answer>`: Submits your answer for the last question you received. Ensure your answer matches the expected format.

## Features

- Offers coding challenges across three difficulty levels.
- Custom help command that provides users with detailed instructions on using the bot.
- Feedback on submitted answers indicating whether the answer is correct or incorrect.

## Dependencies

- Python 3.6 or higher
- discord.py library

## Documentation

Currently, the bot's documentation consists of the in-built help command which provides users with information on how to use the bot.

## Examples

1. **Getting a new question:**
    ```
    !newquestion medium
    ```
2. **Checking an answer:**
    ```
    !check 42
    ```

## Troubleshooting

- If the bot does not respond, ensure that it has been correctly added to your Discord server and that it is online.
- For command-specific issues, use the `!help` command to verify the syntax.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
