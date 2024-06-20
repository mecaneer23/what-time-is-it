#!/usr/bin/env python3

from datetime import datetime


def main() -> None:
    print(datetime.now().strftime("%I:%M:%S%p  %b %d, %Y"))


if __name__ == "__main__":
    main()
