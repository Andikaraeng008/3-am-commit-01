import os

TEXT = "fix: rolled back the 3am deploy; it passed all tests, including the three I invented"


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not whitespace-only.
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry fails the 1-200 char gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
