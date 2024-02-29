from tiktoken.Tokenizer import Tokenizer
import sys

tokenizer = Tokenizer()

# Ensure that the script receives the expected command-line arguments
if len(sys.argv) != 2:
    print("Usage: python script_name.py <code>")
    sys.exit(1)

code = sys.argv[1]
token_count = len(list(tokenizer.tokenize(code)))

print(token_count)
