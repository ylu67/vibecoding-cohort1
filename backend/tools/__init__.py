from backend.tools.count_words import TOOL_DEFINITION as _COUNT_WORDS_DEF
from backend.tools.count_words import count_words

TOOL_DEFINITIONS = [
    _COUNT_WORDS_DEF,
]

TOOL_FUNCTIONS = {
    "count_words": lambda args: count_words(args["metin"]),
}
