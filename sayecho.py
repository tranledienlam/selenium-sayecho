
from pathlib import Path
from browser_automation import BrowserManager

from selenium.webdriver.common.by import By

from browser_automation import Node

class Demo:
    def __init__(self, node: Node, profile: dict) -> None:
        self.driver = node._driver
        self.node = node
        self.profile_name = profile.get('profile_name')

    def _run_logic(self):
        self.node.go_to('https://www.sayecho.xyz/')
        if not self.node.find(By.TAG_NAME, 'video'):
            self.node.snapshot('[sayecho] Không tìm thấy button check-in')
            return False
        
        script = """
            (function() {
                'use strict';
                const videos = document.querySelectorAll('video');
                if (videos.length > 0) {
                    videos[0].click();
                    setTimeout(() => {
                        videos[0].click();
                    }, 100);  // Delay 100ms (0.1s)
                    return "✅ Đã tìm thấy video và click 2 lần!";
                } else {
                    return "⚠️ Không tìm thấy video nào.";
                }
            })();
        """
        self.driver.execute_script(script)
        self.node.log('Click check-in')

class Main:
    def __init__(self, node, profile) -> None:
        self.node = node
        self.profile = profile
        
    def _run(self):
        Demo(self.node, self.profile)._run_logic()


if __name__ == '__main__':
    DATA_DIR = Path(__file__).parent/'data.txt'

    if not DATA_DIR.exists():
        print(f"File {DATA_DIR} không tồn tại. Dừng mã.")
        exit()

    PROFILES = []
    num_parts = 1

    with open(DATA_DIR, 'r') as file:
        data = file.readlines()

    for line in data:
        parts = line.strip().split('|')
        if len(parts) < num_parts:
            print(f"Warning: Dữ liệu không hợp lệ - {line}")
            continue

        profile_name, *_ = (parts + [None] * num_parts)[:num_parts]

        PROFILES.append({
            'profile_name': profile_name,
            # 'username': username,
            # 'email': email,
            # 'password': password
        })

    manager = BrowserManager(Main)
    manager.run_terminal(
        profiles=PROFILES,
        auto=False,
        max_concurrent_profiles=4
    )
