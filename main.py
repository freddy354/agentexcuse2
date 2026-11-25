import os

# Why it lands: the laugh comes first, before any setup to decode.
# The joke grows out of the machine's own condition — a mid-sentence
# model update swapping the agent's personality — delivered deadpan,
# as if a calmer stranger simply took over the job.
LINE = "Mid-sentence the model updated and I became someone who has never once cared about your deadline, and honestly, he's much calmer."

assert "\n" not in LINE and "\r" not in LINE
assert 1 <= len(LINE) <= 200

def main():
    target = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        target = "./output/entry.txt"
        os.makedirs("./output", exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(target, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == LINE
    print(f"OK: wrote {len(LINE)} characters to {target} (gate: 1-200 characters)")

if __name__ == "__main__":
    main()
