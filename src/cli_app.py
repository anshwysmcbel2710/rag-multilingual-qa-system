import argparse
from src.generator import answer_question
from src.utils import detect_language

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", required=True, help="Enter your question")
    parser.add_argument("--lang", default="", help="en or ar (optional)")
    args = parser.parse_args()

    lang = args.lang if args.lang else detect_language(args.q)
    print(answer_question(args.q, lang))
