from .book import BOOK_SEARCH_FIELDS
from .utils import generate_query_argument_description

DESCRIPTIONS = {"books": generate_query_argument_description(BOOK_SEARCH_FIELDS)}
