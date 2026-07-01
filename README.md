# 🎭 Random Joke Generator

A lightweight Python application that fetches random jokes from multiple external APIs with intelligent error handling, fallback mechanisms, and support for different joke formats.

## ✨ Features

- 🤖 **Multiple API Support** - Integrates with Official Joke API and JokeAPI
- 🔄 **Fallback Handling** - Automatically switches between APIs on failure
- 📝 **Format Detection** - Intelligently handles different API response formats
- 🎯 **Batch Fetching** - Get single or multiple jokes at once
- 🚀 **Session Management** - Efficient HTTP session reuse
- ⏱️ **Timeout Protection** - Configurable request timeouts
- 💪 **Robust Error Handling** - Graceful error handling with informative messages

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- `requests` library

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/SaadARazzaq/random-joke-generator.git
cd random-joke-generator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Usage

#### Run the Demo
```bash
python joke_generator.py
```

#### Use as a Module
```python
from joke_generator import JokeGenerator

# Initialize generator
generator = JokeGenerator()

# Get a single joke
joke = generator.tell_joke()
print(joke)

# Get a joke from specific API
joke = generator.tell_joke(use_api="jokeapi")
print(joke)

# Get multiple jokes
jokes = generator.get_multiple_jokes(5)
for joke in jokes:
    print(joke)

# Clean up
generator.close()
```

## 📚 API Documentation

### `JokeGenerator` Class

#### `__init__(timeout: int = 5)`
Initialize the JokeGenerator with optional timeout configuration.

**Parameters:**
- `timeout` (int): Request timeout in seconds. Default: 5

**Example:**
```python
generator = JokeGenerator(timeout=10)
```

---

#### `tell_joke(use_api: str = "official") -> str`
Fetch and format a complete joke.

**Parameters:**
- `use_api` (str): Which API to use - `"official"` or `"jokeapi"`. Default: `"official"`

**Returns:**
- `str`: Formatted joke string

**Example:**
```python
joke = generator.tell_joke(use_api="official")
print(joke)
# Output:
# Q: Why did the scarecrow win an award?
# A: Because he was outstanding in his field!
```

---

#### `get_random_joke(use_api: str = "official") -> Optional[Dict]`
Fetch raw joke data from the API without formatting.

**Parameters:**
- `use_api` (str): Which API to use

**Returns:**
- `Dict`: Raw API response, or `None` on failure

**Example:**
```python
joke_data = generator.get_random_joke()
print(joke_data)
```

---

#### `get_multiple_jokes(count: int = 5) -> list`
Fetch multiple random jokes.

**Parameters:**
- `count` (int): Number of jokes to fetch. Default: 5

**Returns:**
- `list`: List of formatted joke strings

**Example:**
```python
jokes = generator.get_multiple_jokes(3)
for i, joke in enumerate(jokes, 1):
    print(f"Joke {i}: {joke}\n")
```

---

#### `format_joke(joke_data: Dict) -> str`
Format raw joke data into a readable string.

**Parameters:**
- `joke_data` (Dict): Raw joke dictionary from API

**Returns:**
- `str`: Formatted joke string

**Supports:**
- Two-part jokes (setup/punchline)
- Two-part jokes (setup/delivery)
- Single-line jokes

---

#### `close()`
Close the HTTP session (recommended for cleanup).

**Example:**
```python
generator.close()
```

## 🔌 Supported APIs

| API | Endpoint | Format | Status |
|-----|----------|--------|--------|
| **Official Joke API** | `https://official-joke-api.appspot.com/random_joke` | Setup/Punchline | ✅ Active |
| **JokeAPI** | `https://v2.jokeapi.dev/joke/Any` | Setup/Delivery or Single-line | ✅ Active |

### API Response Examples

**Official Joke API:**
```json
{
  "type": "general",
  "setup": "Why did the scarecrow win an award?",
  "punchline": "Because he was outstanding in his field!",
  "id": 1
}
```

**JokeAPI (Two-Part):**
```json
{
  "category": "Programming",
  "type": "twopart",
  "setup": "How many programmers does it take to change a light bulb?",
  "delivery": "None, that's a hardware problem",
  "id": 2,
  "safe": true,
  "lang": "en"
}
```

**JokeAPI (Single-Line):**
```json
{
  "category": "Misc",
  "type": "single",
  "joke": "Why did the programmer quit his job? Because he didn't get arrays.",
  "id": 3,
  "safe": true,
  "lang": "en"
}
```

## 💡 Examples

### Example 1: Simple Joke Fetcher
```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
print(generator.tell_joke())
generator.close()
```

### Example 2: Batch Download
```python
from joke_generator import JokeGenerator

generator = JokeGenerator()
jokes = generator.get_multiple_jokes(10)

with open('jokes.txt', 'w') as f:
    for i, joke in enumerate(jokes, 1):
        f.write(f"Joke {i}:\n{joke}\n\n")

generator.close()
```

### Example 3: API Comparison
```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

print("Official Joke API:")
print(generator.tell_joke(use_api="official"))

print("\nJokeAPI:")
print(generator.tell_joke(use_api="jokeapi"))

generator.close()
```

### Example 4: Error Handling
```python
from joke_generator import JokeGenerator

generator = JokeGenerator(timeout=2)

joke_data = generator.get_random_joke()
if joke_data:
    joke = generator.format_joke(joke_data)
    print(joke)
else:
    print("Failed to fetch joke")

generator.close()
```

## 🧪 Testing

Run the included demo:
```bash
python joke_generator.py
```

Expected output:
```
🎭 Random Joke Generator 🎭

==================================================

📝 Single Random Joke:

Q: Why did the scarecrow win an award?
A: Because he was outstanding in his field!

==================================================

📝 Joke from JokeAPI:

Q: How many programmers does it take to change a light bulb?
A: None, that's a hardware problem

==================================================

📝 Three More Random Jokes:

Joke 1:
Q: Why don't scientists trust atoms?
A: Because they make up everything!

Joke 2:
Q: What do you call a fake noodle?
A: An impasta!

Joke 3:
Q: Why did the coffee file a police report?
A: It got mugged!

==================================================
✨ Thanks for using the Joke Generator!
```

## ⚠️ Limitations & Considerations

- **API Rate Limits:** Both APIs have rate limits. Respect them by not making excessive requests.
- **Internet Required:** This application requires an active internet connection to fetch jokes.
- **API Availability:** If both APIs are down, the generator will fail gracefully.
- **Timeout Handling:** Default timeout is 5 seconds. Adjust if you have slow internet.
- **No Caching:** Each call fetches fresh data. Consider implementing caching for production use.

## 🔧 Advanced Configuration

### Custom Timeout
```python
# Set a longer timeout for slower connections
generator = JokeGenerator(timeout=15)
```

### Error Resilience
```python
# Implement retry logic
max_retries = 3
for attempt in range(max_retries):
    joke = generator.tell_joke()
    if joke and "Could not" not in joke:
        print(joke)
        break
```

## 📦 Dependencies

- **requests** (2.31.0+) - HTTP library for making API calls

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add support for more joke APIs
- Improve documentation
- Optimize performance

## 🔗 Resources

- [Official Joke API](https://official-joke-api.appspot.com/)
- [JokeAPI Documentation](https://v2.jokeapi.dev/)
- [Python Requests Library](https://requests.readthedocs.io/)

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Made with ❤️ by SaadARazzaq**

⭐ If you found this helpful, please consider giving it a star!
