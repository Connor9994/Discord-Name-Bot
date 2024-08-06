# Discord Name Bot

## Overview
The **Discord Name Bot** is a Python script designed to automate changing your Discord username periodically. It randomly selects from a predefined list of humorous names, allowing you to showcase your wit or entertain your friends. The script utilizes the `nodriver` library to control a browser instance, ensuring that the name changes happen seamlessly.

![1](https://github.com/user-attachments/assets/34c7b501-e08b-4161-a7bc-3db42720df84)


## Features
- Randomly selects a name from a predefined list.
- Periodically changes username at a customizable interval.
- User-friendly interface with options to interact directly with Discord.

### **NoDriver Instead of Selenium**
Official successor of the Undetected-Chromedriver python package that does NOT use WebDriver 
https://github.com/ultrafunkamsterdam/nodriver

## Prerequisites
Before using the Discord Name Bot, make sure you have the following installed:
- Python 3.x
- `nodriver` library

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Connor9994/Discord-Name-Bot.git
   cd Discord-Name-Bot
   ```

2. **Install the Dependency:**
   ```bash
   pip install nodriver
   ```

3. **Set Up Browser Environment:**
   - Download the Chrome browser and place it at the path specified in the script (or modify the script to point to your Chrome executable).
   - Prepare a folder structure for user data `.\Users`. This folder will hold your Discord session cookies.

4. **Modify the Script:**
   - Update the `names` list with your desired funny names.
   - Change the `DiscordChannelUrl` variable to the URL of your Discord channel.
   - Adjust the `IntervalTimer` to set how often (in seconds) you want the username to change.
   - Set `LoggedIn` to `1` once you have successfully logged in to Discord with your cookies saved.

5. **Run the Script:**
   To start the bot, simply run:
   ```bash
   python your_script.py
   ```

## Usage
- If you are logged in and have cookies set up correctly, the bot will automatically change your username every few seconds as specified.
- If you are not logged in, the script will take you to the Discord login page to enter your credentials.

## Important Notes
- Make sure to comply with Discord's Terms of Service when using the bot. Automating user interactions can lead to your account being flagged or banned.
- Use this bot for entertainment purposes only, and ensure that other members of your Discord community find it amusing.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features!
