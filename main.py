import feedparser

# DEV
import pickle
from pathlib import Path

def main():
    # DEV
    p = Path("./feed.pickle")
    if p.exists():
        feed = pickle.loads(p.read_bytes())
    else:
        feed = feedparser.parse("http://rss.cnn.com/rss/edition_world.rss")
        p.write_bytes(pickle.dumps(feed))

    print(len(feed["entries"]))


if __name__ == "__main__":
    main()
