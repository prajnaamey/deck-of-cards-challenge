# Deck of Cards Challenge

A Python script that interacts with the [Deck of Cards API](https://www.deckofcardsapi.com/) to draw and sort a hand of five cards.

## Description

This project contains a Python script, `commure_coding_challenge.py`, that performs the following actions:
1.  Sends a request to the Deck of Cards API to shuffle a new deck of cards.
2.  Draws five cards from the shuffled deck.
3.  Displays the names and suits of the drawn cards to the console in ascending order of their value (Ace through King).

## Requirements

- Python 3
- `requests` library

## How to Run

1.  **Install dependencies:**
    ```bash
    pip install requests
    ```

2.  **Run the script:**
    ```bash
    python commure_coding_challenge.py
    ```

### Sample Output
```
7 of HEARTS
8 of DIAMONDS
10 of CLUBS
JACK of DIAMONDS
JACK of SPADES
```