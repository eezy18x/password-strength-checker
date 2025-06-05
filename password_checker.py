import re
import math
import requests

# Check for character variety
def character_checks(password):
    checks = {
        "Length >= 8": len(password) >= 8,
        "Has uppercase": bool(re.search(r"[A-Z]", password)),
        "Has lowercase": bool(re.search(r"[a-z]", password)),
        "Has digit": bool(re.search(r"\d", password)),
        "Has special char": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }
    return checks

# Detect keyboard patterns and repetition
def detect_patterns(password):
    lower = password.lower()
    keyboard_patterns = ["qwerty", "asdf", "zxcv", "1234", "password", "admin"]
    for pattern in keyboard_patterns:
        if pattern in lower:
            return f"Detected common pattern: {pattern}"
    if re.search(r"(.)\1{2,}", password):  # e.g., aaa or 111
        return "Detected repeated characters"
    return "No suspicious patterns"

# Estimate crack time (offline brute force)
def estimate_crack_time(password):
    charset_size = 0
    if re.search(r"[a-z]", password): charset_size += 26
    if re.search(r"[A-Z]", password): charset_size += 26
    if re.search(r"\d", password): charset_size += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): charset_size += 32

    entropy = math.log2(charset_size ** len(password))
    crack_time_seconds = 2 ** entropy / 1e9  # Assume 1 billion guesses/sec

    if crack_time_seconds < 60:
        crack_time = f"{int(crack_time_seconds)} seconds"
    elif crack_time_seconds < 3600:
        crack_time = f"{int(crack_time_seconds / 60)} minutes"
    elif crack_time_seconds < 86400:
        crack_time = f"{int(crack_time_seconds / 3600)} hours"
    else:
        crack_time = f"{int(crack_time_seconds / 86400)} days"
    
    return crack_time

# Check if password is pwned (HaveIBeenPwned)
def check_pwned(password):
    import hashlib
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    if suffix in res.text:
        return True
    return False

# Final score based on features
def evaluate_password(password):
    print("\n🔍 Password Evaluation Report:")
    
    # Character checks
    checks = character_checks(password)
    for desc, result in checks.items():
        print(f"{'✅' if result else '❌'} {desc}")
    
    # Pattern detection
    pattern_result = detect_patterns(password)
    print(f"🔎 Pattern Check: {pattern_result}")

    # Crack time
    crack_time = estimate_crack_time(password)
    print(f"⏱️ Estimated Crack Time (offline): {crack_time}")

    # Breach check
    try:
        pwned = check_pwned(password)
        print(f"{'❌' if pwned else '✅'} Pwned Check: {'Found in breaches' if pwned else 'Not found'}")
    except:
        print("⚠️ Could not check for breaches (offline or network error)")

    # Final rating
    score = sum(checks.values())
    if pattern_result != "No suspicious patterns":
        score -= 1
    if pwned:
        score -= 2

    if score >= 5:
        print("✅ Final Strength: STRONG")
    elif score >= 3:
        print("⚠️ Final Strength: MEDIUM")
    else:
        print("❌ Final Strength: WEAK")


# ==== RUN APP ====
if __name__ == "__main__":
    pwd = input("🔐 Enter your password: ")
    evaluate_password(pwd)
