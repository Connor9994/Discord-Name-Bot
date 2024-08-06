from random import *

import nodriver as uc
from nodriver import *

names = [
    "Funny Name 1",
    "Funny Name 2",
    "Connor (Funny Name 3)"
]

DiscordChannelUrl = "https://discord.com/channels/1113511191788491111/1113570111188411151"

async def main():
    while True:
        driver = await uc.start(
            headless = False,
            user_data_dir=r'C:\Users\Administrator\Desktop\Discord-Name-Bot\Users\1',
            browser_executable_path=r'C:\Users\Administrator\Desktop\Discord-Name-Bot\Chrome SxS\Application\chrome.exe',
        )
        tab = await driver.get(DiscordChannelUrl)

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