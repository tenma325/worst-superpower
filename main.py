"""Worst Superpower - a gift that arrives exactly one second too late.

Written for the make.fun bounty 'Worst Superpower' (u-suroto): one
line, at most 140 characters, inventing the most useless superpower
imaginable - a power so pointless that naming it is the whole joke.

Perfect microwave-beep prediction would be a fine power. Arriving
one second after the beep makes it a pure liability: you still hear
every beep, and now you also know your gift is real and worthless.
Precision without timing is just documentation of your own failure.
"""

from pathlib import Path

ENTRY = (
    "The power to always know exactly when the microwave will beep, "
    "one second after it beeps."
)


def useless_power_check(line: str) -> bool:
    """The power must sound impressive and deliver nothing.

    One second late is the exact gap between a gift and a curse.
    """
    return len(line) <= 140 and "after it beeps" in line


def main() -> None:
    assert useless_power_check(ENTRY), "the power must stay useless"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
