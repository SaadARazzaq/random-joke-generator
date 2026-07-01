import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """
    A random joke generator that fetches jokes from external APIs.
    Supports multiple joke APIs for variety and reliability.
    """
    
    # Primary API: Official Joke API
    JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"
    
    # Backup API: JokeAPI
    JOKEAPI_URL = "https://v2.jokeapi.dev/joke/Any"
    
    def __init__(self, timeout: int = 5):
        """
        Initialize the JokeGenerator.
        
        Args:
            timeout: Request timeout in seconds (default: 5)
        """
        self.timeout = timeout
        self.session = requests.Session()
    
    def get_random_joke(self, use_api: str = "official") -> Optional[Dict]:
        """
        Fetch a random joke from the specified API.
        
        Args:
            use_api: Which API to use - "official", "jokeapi", or "random"
            
        Returns:
            Dictionary containing the joke data, or None if the request fails
        """
        try:
            if use_api == "jokeapi":
                return self._get_jokeapi_joke()
            else:
                return self._get_official_joke()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def _get_official_joke(self) -> Optional[Dict]:
        """
        Fetch a joke from Official Joke API.
        Returns: {'type': 'general', 'setup': '...', 'punchline': '...', 'id': 123}
        """
        try:
            response = self.session.get(self.JOKE_API_URL, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Official Joke API error: {e}")
            return None
    
    def _get_jokeapi_joke(self) -> Optional[Dict]:
        """
        Fetch a joke from JokeAPI.
        Returns: {'setup': '...', 'delivery': '...', ...} or {'joke': '...'}
        """
        try:
            response = self.session.get(self.JOKEAPI_URL, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"JokeAPI error: {e}")
            return None
    
    def format_joke(self, joke_data: Dict) -> str:
        """
        Format joke data from different APIs into a readable string.
        
        Args:
            joke_data: Dictionary containing joke information
            
        Returns:
            Formatted joke string
        """
        if not joke_data:
            return "Could not fetch a joke. Try again later!"
        
        # Handle Official Joke API format
        if "setup" in joke_data and "punchline" in joke_data:
            return f"Q: {joke_data['setup']}\nA: {joke_data['punchline']}"
        
        # Handle JokeAPI single-line format
        if "joke" in joke_data:
            return joke_data["joke"]
        
        # Handle JokeAPI two-part format
        if "delivery" in joke_data:
            return f"Q: {joke_data.get('setup', '')}\nA: {joke_data['delivery']}"
        
        return "Could not format the joke."
    
    def tell_joke(self, use_api: str = "official") -> str:
        """
        Tell a complete joke by fetching and formatting it.
        
        Args:
            use_api: Which API to use
            
        Returns:
            Formatted joke string
        """
        joke_data = self.get_random_joke(use_api)
        return self.format_joke(joke_data)
    
    def get_multiple_jokes(self, count: int = 5) -> list:
        """
        Get multiple random jokes.
        
        Args:
            count: Number of jokes to fetch
            
        Returns:
            List of formatted jokes
        """
        jokes = []
        for i in range(count):
            joke = self.tell_joke()
            jokes.append(joke)
            print(f"Fetched joke {i+1}/{count}...")
        return jokes
    
    def close(self):
        """Close the session."""
        self.session.close()


def main():
    """Main function to demonstrate the JokeGenerator."""
    print("🎭 Random Joke Generator 🎭\n")
    print("=" * 50)
    
    generator = JokeGenerator()
    
    try:
        # Get a single joke
        print("\n📝 Single Random Joke:\n")
        joke = generator.tell_joke()
        print(joke)
        
        # Get another joke from a different API
        print("\n" + "=" * 50)
        print("\n📝 Joke from JokeAPI:\n")
        joke2 = generator.tell_joke(use_api="jokeapi")
        print(joke2)
        
        # Get multiple jokes
        print("\n" + "=" * 50)
        print("\n📝 Three More Random Jokes:\n")
        multiple_jokes = generator.get_multiple_jokes(3)
        for i, joke in enumerate(multiple_jokes, 1):
            print(f"\nJoke {i}:")
            print(joke)
        
    finally:
        generator.close()
        print("\n" + "=" * 50)
        print("✨ Thanks for using the Joke Generator!")


if __name__ == "__main__":
    main()
