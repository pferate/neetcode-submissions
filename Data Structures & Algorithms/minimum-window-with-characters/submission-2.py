from collections import Counter, defaultdict
import logging

logging.basicConfig(level=logging.INFO)

def find_all_needle_indexes(needles, haystack) -> defaultdict[int]:
    output = defaultdict(list)
    for needle in set(needles):
        output[needle] = [index for index, letter  in enumerate(haystack) if letter  == needle]
    return output


def haystackContains(needles, haystack) -> bool:
    hay_cntr = Counter(haystack)
    hay_cntr.subtract(needles)
    # Ensure that none of the needles are negative after subtracting
    for needle in set(needles):
        if hay_cntr[needle] < 0:
            return False
    return True

class BookshelfTracker:
    def __init__(self):
        self.books = []
        self.start = None
        self.end = None
    
    @property
    def bookend_distance(self):
        if self.start is None or self.end is None:
            return None
        return self.end - self.start

    
    def find_best_spot(self, potential_spots):
        logging.info(f"Finding best spot for: {potential_spots}, current: [{self.start}, {self.end}]")
        if len(potential_spots) == 0:
            return None
        # If there's only one potential spot, we have to use it
        if len(potential_spots) == 1:
            return potential_spots[0]
        if self.start is None and self.end is None:
            # We have multiple choices, but nothing on the shelf, it's ambiguous at this point
            raise ValueError("Unable to find best spot")
        best_so_far = None, 99999  # (index, scalar distance)
        for spot in potential_spots:
            # If the spot is already taken, go to the next
            if spot in self.books:
                continue
            if spot < self.start:
                dist = self.start - spot
            elif self.start < spot < self.end:
                # If within the bookends, we can immediately use it
                best_so_far = (spot, 0)
                break
            elif self.end < spot:
                dist = spot - self.end
            if dist < best_so_far[1]:
                best_so_far = (spot, dist)
        if best_so_far is None:
            raise ValueError("Unable to find best spot")
        logging.info(f"\tBest spot: Index: {best_so_far[0]}, External Distance: {best_so_far[1]}")
        return best_so_far[0]
    
    def add(self, index):
        # If there's no books, the first one is both the start and the end
        if self.start is None and self.end is None:
            self.books.append(index)
            self.start = self.end = index
        # If the book is within the current range, just make note
        if self.end < index:
            self.books.append(index)
            self.end = index
        # If the book is before the start, that's the new start
        if index < self.start:
            self.books.append(index)
            self.start = index
    
    def add_to_best_spot(self, potential_spots):
        best_spot = self.find_best_spot(potential_spots)
        self.add(best_spot)

def generate_bookshelf(s: str, t: str, starting_index: int|None = None) -> BookshelfTracker:
    logging.debug(f"s: {s}, t: {t}, starting_index: {starting_index}")
    all_needle_indexes = find_all_needle_indexes(t, s)
    needle_cntr = Counter(t)
    bookshelf = BookshelfTracker()
    if starting_index is not None:
        bookshelf.add(starting_index)
        needle_cntr.subtract(s[starting_index])
    while needle_cntr.total() > 0:
        letters_to_retry = []
        # Note for Counter: +counter  # remove zero and negative counts
        for letter in list(+needle_cntr):
            try:
                bookshelf.add_to_best_spot(all_needle_indexes[letter])
            except ValueError:
                letters_to_retry.append(letter)
            needle_cntr.subtract(letter)
        # Retry any letters that we weren't able to add initially
        # This should be needed if for letters with multiple choices before finding one with a single possibility
        # We could potentially have a case where no letter has a single possibility, then we need to try multiple variations
        logging.info(f"Retrying letters: {letters_to_retry}")
        for letter in letters_to_retry:
            try:
                bookshelf.add_to_best_spot(all_needle_indexes[letter])
            except ValueError:
                letters_to_retry.append(letter)
            needle_cntr.subtract(letter)
    return bookshelf

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        # Exit fast if the haystack doesn't contain everything needed
        if not haystackContains(t, s):
            return ""
        all_needle_indexes = find_all_needle_indexes(t, s)
        # If all letters have more than one potential spot, then try each combination of one letter
        best_bookshelf = None
        logging.debug(f"all_needle_indexes: {all_needle_indexes}")
        logging.debug(f"Looping through key: {t[0]}")
        for i in all_needle_indexes[t[0]]:
            bookshelf = generate_bookshelf(s, t, i)
            logging.debug(f"bookshelf.books: {bookshelf.books}")
            if best_bookshelf is None or bookshelf.bookend_distance < best_bookshelf.bookend_distance:
                best_bookshelf = bookshelf
        logging.debug(f"best_bookshelf.books: {best_bookshelf.books}")
        return s[best_bookshelf.start:best_bookshelf.end + 1]
