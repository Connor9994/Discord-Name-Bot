import asyncio
import random
import string
import logging
import os
from random import *
import time

logging.basicConfig(level=30)

import nodriver as uc
from nodriver import *

from selenium.webdriver.common.keys import Keys

names = [
    "BTC Wastes Electricity",
    "Reuters Is My Bible",
    "If You Buy a Lib a Book",
    "Zuberi",
    "OPEC Lies",
    "🇺🇸🎤👀🔥💥🍻",
    "Y'all-Qaeda Member",
    "YeeHawdist",
    "I am a 🐈",
    "Sell Now, Ask Questions Later",
    "Well, Bloomberg Said It",
    "Back to $20 Fast",
    "I Ain't Readin' All Of That",
    "DFV's Alt",
    "What's An Exit Strategy?",
    "Lauer Is A Good Guy",
    "GG Hates Retail",
    "Finest Investor Of Our Gen",
    "BRICS Slut",
    "Except As A Punishment For Crime",
    "I Love The 1%",
    "🍑🍌",
    "I Forgot How To Read",
    "WTF Is A Book",
    "Scratch a Lib? Fascist Bleeds.",
    "Narcissistic Math Teacher",
    "Peak-Redditor Energy",
    "You Failed The Vibe Check",
    "BTC to 15k",
    "BTC to 500k",
    "Definitely Not A Fed",
    "I Did Not Sell My Socials",
    "Please Buy My Substack",
    "Average Joe",
    "Algos Are Math",
    "Multi-Discipline Area Of Tech",
    "Crypto Start-Ups Slap",
    "6-Year Blockchain Pro",
    "Centralization Is Awesome",
    "90% Of Global Production",
    "70% Of Lithium Production",
    "Waste Of Time And Energy",
    "Proficient Grasp Of Calculus",
    "SHA-2 Is Super Safe",
    "Dunk On The Bitcoiners Forever",
    "Send Me Tinfoil Links",
    "High-Transaction Fees Are Dope",
    "Have You Read Blocksize Wars?",
    "Who Killed BTC?",
    "Actually? I see in 3D.",
    "51% Attack",
    "3D Tetrahedron Neural Network",
    "Over 10K $0.01 Transactions",
    "Russian Bot",
    "Please Continue The Culture War",
    "🍄🧻👐",
    "China Will Crash Soon - 1949",
    "Nuke the DPRK",
    "Crypto-Class Student",
    "Harmonics Of Universal Math",
    "2D Tetrahedron",
    "I Use Moscow Standard Time",
    "MAGA Hat Gaming Conventions",
    "Gaming is a liberal demographic",
    "Chickenshit Bitch-Ass",
    "Dif Opinions =/= Shit Stirring",
    "Toxic Gaming Culture",
    "Dorky Liberal Idiot",
    "Lovey-Dovey Libs",
    "Zero Moral Compass",
    "Quite A Bit More Educated",
    "No Science Background"
]

async def main():
    while True:
        driver = await uc.start(
            headless = False,
            user_data_dir=r'C:\Users\Administrator\Desktop\DiscordBot\Users\1',
            browser_executable_path=r'C:\Users\Administrator\Desktop\DiscordBot\Chrome SxS\Application\chrome.exe',
        )
        tab = await driver.get("https://discord.com/channels/1113570191788494948/1113570191788494951")

        shuffle(names)
        for name in names:
            try:
                textBox = await tab.select(".inputDefault_f8bc55",timeout=3)
                while textBox.attrs['value'] == name:
                    continue
                await tab.sleep(t=1)
                await textBox.clear_input()
                await textBox.send_keys(name)
                SaveButton = await tab.find("Save Changes", best_match=True,return_enclosing_element=True,timeout=5)
                await SaveButton.click()
                await tab.sleep(t=60)
            except:
                try:
                    topLeft = await tab.select(".headerContent_fd6364.primaryInfo_fd6364",timeout=3)
                    await topLeft.click()
                    topTab = await tab.select(".labelWrapper_c61a51",timeout=3)
                    await topTab.click()
                    await tab.sleep(t=3)
                except:
                    print("")
                

    input("Press Enter to continue...")

if __name__ == "__main__":
    uc.loop().run_until_complete(main())