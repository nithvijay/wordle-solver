# Basic Wordle Solver

This repo contains a basic solver for the daily word game at [https://www.powerlanguage.co.uk/wordle/](https://www.powerlanguage.co.uk/wordle/).

[See an example here!](https://www.loom.com/share/e059386060604ef18ac5b6a9db980511)

## Usage

1. Clone the repository
```console
$ git clone https://github.com/nithvijay/wordle-solver
$ cd wordle-solver
```
2. Install the dependencies with [Poetry](https://python-poetry.org/)
```
$ poetry install
```

3. Run the Command Line App
```
$ poetry run python wordle_solver/main.py
```

> If you want to fetch today's solution, Chrome webdriver (`chromedriver`) is required. On MacOS, this can be installed with homebrew. The cask is located [here](https://formulae.brew.sh/cask/chromedriver).

## Solver

The word list is taken directly from the website. This algorithm filters out invalid words based on the user's feedback of the result of each letter. Then, from the remaining valid words, the frequency of characters is counted and each word is given a score based on how common its characters are where words with more common characters are given higher scores, The words with the 20  greatest scores are then output to the user.

In the future, I hope to modify the scoring algorithm by changing how the weights are assigned and by incorporating the location of the letters.
