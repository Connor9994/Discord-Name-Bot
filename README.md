# Discord Name Bot

## Overview
The **Discord Name Bot** is a Python script designed to automate changing your Discord username periodically. It randomly selects from a predefined list of humorous names, allowing you to showcase your wit or entertain your friends. The script utilizes the `nodriver` library to control a browser instance, ensuring that the name changes happen seamlessly.

## Features
- Randomly selects a name from a predefined list.
- Periodically changes username at a customizable interval.
- User-friendly interface with options to interact directly with Discord.

## Prerequisites
Before using the Discord Name Bot, make sure you have the following installed:
- Python 3.x
- `nodriver` library (install it using `pip install nodriver`)

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
   - Prepare a folder structure for user data at `C:\Users\Administrator\Desktop\Discord-Name-Bot\Users\1`. This folder will hold your Discord session cookies.

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
- If you are not logged in, the script will take you to the Discord login page to enter your credentials. After that, the bot will switch to username changing mode.

## Important Notes
- Make sure to comply with Discord's Terms of Service when using the bot. Automating user interactions can lead to your account being flagged or banned.
- Use this bot for entertainment purposes only, and ensure that other members of your Discord community find it amusing.

## Troubleshooting
- If the bot fails to find the text box or save button, check your internet connection and the current state of the Discord interface.
- Ensure that you have the correct paths set for the browser executable and user data directory.

## Contributing
Feel free to fork the repository and submit pull requests for improvements or new features!

## License
This project is open-source and available under the MIT License.

## Acknowledgements
Special thanks to the creators of the `nodriver` library for making browser automation easy and accessible.

--- 

Feel free to customize any section based on your preferences!
