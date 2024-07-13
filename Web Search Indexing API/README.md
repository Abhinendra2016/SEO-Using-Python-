# Web Search Indexing API Using Python
The Indexing API allows site owners to notify Google when they add or remove pages from their site, or update content at a previously-submitted URL. This can help Google schedule pages for a fresh crawl, which can lead to higher quality user traffic and improved search visibility.

## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework for building the application.
- **Google OAuth2 and Auth Libraries**: For authenticating API requests.
- **Requests Library**: For making HTTP requests to the Google Indexing API.
- **JSON**: For data storage and handling.
- **HTML/CSS/JavaScript**: For frontend development and user interaction.
- **Jinja2**: For rendering HTML templates with dynamic data.
- **Google Indexing API**: External API for URL indexing.
- **Datetime Module**: For date handling.
- **os Module**: For environment variable access and file handling.

## Prerequisites

- Python 3.7+
- A Google Cloud project with the Indexing API enabled
- A service account key file (JSON format)
- Flask
- Requests
- google-auth

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/Abhinendra2016/SEO-Using-Python-/tree/7b60bc34425f1eb988667b742c6e9d2933c14897/Web%20Search%20Indexing%20API
    cd web-search-indexing-api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file and add your Flask secret key:
    
    ```plaintext
    FLASK_SECRET_KEY=your_secret_key
    ```

5. **Place your service account JSON key file:**

    Place your service account key file (e.g., `smooth-pen.json`) in the project directory.

6. **Run the application:**

    ```sh
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open the application in your web browser.
2. Enter URLs (one per line) in the textarea and submit.
3. The results will be displayed on the results page.
4. You can view the history of submitted URLs on the main page.

## Project Structure

- `app.py`: Main application file containing the Flask routes and core functionality.
- `history.json`: JSON file for storing the history of submitted URLs.
- `templates/`: Folder containing HTML templates.
  - `index.html`: Main page template.
  - `result.html`: Results page template.
- `static/`: Folder containing static files like CSS and images.
  - `css/styles.css`: Stylesheet for the application.
  - `images/logo.png`: Company logo.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Google Indexing API](https://developers.google.com/search/apis/indexing-api/v3/)

