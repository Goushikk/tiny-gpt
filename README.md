# Simple ChatGPT Interaction Script (Python)

This Python script provides a basic command-line interface for interacting with OpenAI's ChatGPT model (`text-davinci-003`). It allows you to send messages and receive responses until you type 'bye'.

**Warning:** This script requires you to have an OpenAI API key. Ensure you have set up an account and obtained your API key from the OpenAI platform. **Do not share your API key publicly.**

## Prerequisites

* **Python 3.6 or higher:** Ensure you have Python installed on your system.
* **OpenAI Python Library:** Install the OpenAI library using pip:

    ```bash
    pip install openai
    ```

## Setup

1.  **Obtain an OpenAI API Key:**
    * Go to the [OpenAI Platform](https://platform.openai.com/).
    * Sign up or log in to your account.
    * Navigate to the "API keys" section (usually under your profile).
    * Create a new secret key. **Treat this key as confidential.**

2.  **Replace Placeholder in Script:**
    * Open the `your_script_name.py` (or whatever you named the Python file) in a text editor.
    * Locate the line:
        ```python
        openai.api_key = 'YOUR_API_KEY'
        ```
    * Replace `'YOUR_API_KEY'` with your actual OpenAI API key (the one you obtained in the previous step), keeping the single quotes.

## How to Run

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory where you saved the Python script.**
3.  **Run the script using the Python interpreter:**

    ```bash
    python your_script_name.py
    ```

    (Replace `your_script_name.py` with the actual name of your file).

## Usage

Once the script is running, you will see the prompt `User:`.

1.  **Type your message** that you want to send to ChatGPT and press Enter.
2.  The script will send your message to the OpenAI API and display the response from ChatGPT, prefixed with `ChatGPT:`.
3.  Continue typing messages and receiving responses.
4.  To end the conversation, type `bye` (case-insensitive) and press Enter. The script will print `ChatGPT: Goodbye!` and exit.

## Script Details

The Python script performs the following actions:

* **Imports the `openai` library.**
* **Sets your OpenAI API key.**
* **Defines a function `send_message(message)`:**
    * Takes a `message` string as input.
    * Uses `openai.Completion.create()` to send the message to the `text-davinci-003` model.
    * Configures parameters like `max_tokens` (maximum length of the response), `n` (number of responses to generate), `stop` (sequences to stop the generation), and `temperature` (controls the randomness of the output).
    * Returns the stripped text of the first generated choice.
* **Implements a main loop:**
    * Prompts the user for input.
    * If the user types 'bye', it prints a goodbye message and breaks the loop.
    * Otherwise, it calls the `send_message()` function with the user's input.
    * Prints the response received from ChatGPT.

## Support

If you encounter any issues or have questions regarding this script, please consider the following:

* **Check the OpenAI API documentation:** The official OpenAI API documentation ([https://platform.openai.com/docs/api-reference](https://platform.openai.com/docs/api-reference)) is a comprehensive resource for understanding the API and its capabilities.
* **Review the error messages:** If the script encounters an error, the error message might provide clues about the problem (e.g., incorrect API key, network issues).
* **Verify your OpenAI API key:** Double-check that you have correctly entered your API key in the script without any typos or extra spaces.
* **Ensure the OpenAI library is installed:** If you haven't installed the `openai` library, run `pip install openai` in your terminal.
* **Consider your OpenAI account balance:** Using the OpenAI API incurs costs. Ensure you have sufficient credits in your OpenAI account. You can check your usage on the OpenAI platform.
* **For more complex issues or feature requests:** While this is a simple script, for more advanced troubleshooting or feature suggestions related to the OpenAI API itself, you might find help on community forums or by contacting OpenAI support through their platform.

**Please note:** Support for this specific, simple script is provided on a best-effort basis. For issues related to the OpenAI API service itself, please refer to OpenAI's official support channels.

## License

This project is licensed under MIT License. For further visit LICENSE file.

Copyright © [2025] [Goushik Krishna]
