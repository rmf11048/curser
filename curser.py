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
