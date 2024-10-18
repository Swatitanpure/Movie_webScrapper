from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace YOUR_TMDB_API_KEY with your actual TMDb API key
TMDB_API_KEY = "4169c14863467a03ec24922f3ae9890e"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrap', methods=['POST'])
def scrap_movies():
    content = request.form.get('content')
    search_string = content.replace(" ", "%20")

    # Build the TMDb API URL
    tmdb_url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={search_string}"

    # Make the API request
    response = requests.get(tmdb_url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if any movies were found
        if "results" in data and len(data["results"]) > 0:
            movies = data["results"]
            return render_template('results.html', movies=movies)
        else:
            return render_template('index.html', error="No movies found matching the search term.")
    else:
        return render_template('index.html', error="Something went wrong while fetching movie data.")

if __name__ == "__main__":
    app.run(port=8000,debug=True) # running the app on the local machine on port 8000