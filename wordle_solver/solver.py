import pandas as pd


def filter_combined(perfect, misplaced, incorrect, words):
    filtered = words
    if perfect:
        filtered = [word for word in filtered if check_perfect(perfect, word)]
    if misplaced:
        filtered = [word for word in filtered if check_misplaced(misplaced, word)]
    if incorrect:
        filtered = [word for word in filtered if check_incorrect(incorrect, word)]
    return filtered


def check_perfect(perfect, word):
    for perfect_dict in perfect:
        if word[perfect_dict["index"]] != perfect_dict["character"]:
            return False
    return True


def check_misplaced(misplaced, word):
    word_set = set(word)
    for misplaced_dict in misplaced:
        if word[misplaced_dict["index"]] == misplaced_dict["character"]:
            return False
        elif misplaced_dict["character"] not in word_set:
            return False
    return True


def check_incorrect(incorrect, word):
    word_set = set(word)
    for incorrect_letter in incorrect:
        if incorrect_letter in word_set:
            return False
    return True


def get_best_words(perfect, misplaced, incorrect, words, n=50):
    new_valid_words = filter_combined(perfect, misplaced, incorrect, words)
    # removes duplicate letters within words, e.g. apple -> aple
    deduped = ["".join(list(set(word))) for word in new_valid_words]
    if not deduped:
        return "No words found"
    string_series = pd.Series(deduped)
    split_strings = string_series.str.split("", expand=True)
    letter_frequencies = split_strings.melt()['value'].value_counts()
    letter_frequencies[""] = 0
    best_indices = split_strings.apply(lambda col: col.map(letter_frequencies)).sum(axis=1).nlargest(n).index
    return pd.Series(new_valid_words)[best_indices]
