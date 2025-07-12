# 🤬 Curser

**Curser** is a stupid clipboard utility that cycles through curse words every second. That’s it. That’s the app.

Whenever your clipboard is empty — or still contains the last curse word Curser shoved in — it replaces it with a new one from its rotating profanity list. Then you can just paste a random curse word wherever you like. For reasons known only to you.

---

## ❓ Why

No idea. Maybe you’re mad. Maybe you're a performance artist. Maybe you're just tired of typing "fuck" manually.

This app won’t stop you from copying other stuff — it knows when to back off. But when the clipboard’s empty, Curser steps in with some bad words like an uninvited bouncer at your text box.

---

## 🧃 Features

- Rotates a list of curse words every 1 second  
- Only updates the clipboard if:  
  - The clipboard is **empty**, or  
  - It still contains a curse word previously set by **Curser**  
- Ignores your normal copy-paste behavior  
- Quietly runs in the background ruining your day, one clipboard at a time

---

## 🛠️ Setup

You need Python 3.7 or higher.

### Install dependencies:
```bash
pip install pyperclip
```

## 🐍 The Code

Just copy this into a file called `curser.py`:

```python
import time
import pyperclip
import hashlib

# List of curse words (customize as desired)
curse_words = [
    "damn", "hell", "crap", "bloody", "bastard", "shit",
    "fuck", "asshole", "dickhead", "bollocks", "wanker"
]

def hash_text(text):
    return hashlib.md5(text.encode()).hexdigest()

def curser_loop():
    idx = 0
    last_app_clipboard_hash = None

    while True:
        time.sleep(1)  # rotate every 1 second
        current_clip = pyperclip.paste()
        current_hash = hash_text(current_clip)

        # If clipboard is empty or still contains what Curser set earlier
        if not current_clip.strip() or current_hash == last_app_clipboard_hash:
            curse_word = curse_words[idx % len(curse_words)]
            pyperclip.copy(curse_word)
            last_app_clipboard_hash = hash_text(curse_word)
            print(f"[Curser] Clipboard set to: {curse_word}")
            idx += 1
        else:
            # User copied something else — leave clipboard alone
            print(f"[Curser] Clipboard owned by user: {current_clip[:20]}...")

if __name__ == "__main__":
    try:
        curser_loop()
    except KeyboardInterrupt:
        print("\n[Curser] Exiting.")
```

---

## 🧠 How It Works

1. You run it.  
2. It waits.  
3. If clipboard is empty or contains its own filth, it replaces it with a new curse word.  
4. You paste it somewhere.  
5. You question your life choices.  
6. Repeat.

---

## 🤡 Curse List

Edit the `curse_words` array in `curser.py` to suit your temperament:

```python
curse_words = [
    "damn", "hell", "crap", "bloody", "bastard",
    "shit", "fuck", "asshole", "dickhead", "bollocks", "wanker"
]
```

---

## 🧪 Example Use Case

- Open a text box.  
- Do nothing.  
- Hit Ctrl+V.  
- Paste "shit".  
- Wait 1 second.  
- Hit Ctrl+V again.  
- Paste "wanker".  
- Laugh, maybe. Cry, probably.

---

## 🔚 Stopping the Madness

Hit `Ctrl+C` in the terminal. Or yank the power cord. Whichever feels more satisfying.

---

## 🧱 Packaging (Optional)

Turn it into a standalone app if you want to trick friends:

```bash
pip install pyinstaller
pyinstaller --onefile curser.py
```

---

## ⚠️ Warning

This app is dumb. Don’t use it at work. Don’t use it in school. Honestly, don’t use it at all.

---

## 🏁 License

MIT — because we don’t want to be sued if someone pastes “bollocks” into a company email.

---

## 🙃 Made for No Good Reason
