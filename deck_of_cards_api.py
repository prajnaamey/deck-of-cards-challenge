import requests

class DeckOfCards:
    """
    A class to interact with the Deck of Cards API to draw and display cards.
    """
    def __init__(self, card_count=5):
        """
        Initializes the DeckOfCards class.

        Args:
            card_count (int): The number of cards to draw.
        """
        self.base_url = "https://www.deckofcardsapi.com/"
        self.card_count = card_count
        self.deck_id = None

    def _shuffle_cards(self):
        """
        Shuffles a new deck of cards and stores the deck_id.

        Returns:
            dict: The response from the API, or None if an error occurs.
        """
        try:
            response = requests.get(f"{self.base_url}/api/deck/new/shuffle/?deck_count=1")
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            data = response.json()
            self.deck_id = data.get('deck_id')
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error shuffling cards: {e}")
            return None

    def _draw_cards(self):
        """
        Draws a specified number of cards from the shuffled deck.

        Returns:
            list: A list of cards drawn from the deck, or None if an error occurs.
        """
        if not self.deck_id:
            print("Error: Deck ID not found. Please shuffle the cards first.")
            return None

        try:
            response = requests.get(f"{self.base_url}/api/deck/{self.deck_id}/draw/?count={self.card_count}")
            response.raise_for_status()
            cards_data = response.json()
            return cards_data.get("cards")
        except requests.exceptions.RequestException as e:
            print(f"Error drawing cards: {e}")
            return None

    def display_sorted_cards(self, list_of_cards):
        """
        Displays the drawn cards in ascending order of value.

        Args:
            list_of_cards (list): A list of card dictionaries.
        """
        if not list_of_cards:
            print('No cards to display.')
            return

        value_map = {
            'ACE': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'JACK': 11, 'QUEEN': 12, 'KING': 13
        }

        cards_with_values = []
        for card in list_of_cards:
            value = card.get("value")
            suit = card.get("suit")
            sort_value = value_map.get(value)
            if sort_value is not None:
                cards_with_values.append((sort_value, value, suit))

        cards_with_values.sort()

        for _, value, suit in cards_with_values:
            print(f"{value} of {suit}")

    def draw_and_display_cards(self):
        """
        Orchestrates shuffling, drawing, and displaying the cards.
        """
        if self._shuffle_cards():
            cards = self._draw_cards()
            if cards:
                self.display_sorted_cards(cards)

if __name__ == "__main__":
    deck = DeckOfCards(card_count=5)
    deck.draw_and_display_cards()