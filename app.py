from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_artist_country(artist_name):

    url = (
        f"https://musicbrainz.org/ws/2/artist/"
        f"?query={artist_name}&fmt=json"
    )

    headers = {
        "User-Agent": "ZikiDiscover/1.0"
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    artists = data.get("artists", [])

    if artists:
        return artists[0].get("country", "Unknown")

    return "Unknown"

def get_trending_songs():

    artists = [
        "Asake",
        "Andy  Bumuntu",
        "Tyla",
        "Ayra Starr",
        "Diamond Platnumz",
        "Joshua Baraka",
        "Mike Kayihura"
    ]

    songs = []

    for artist in artists:

        url = f"https://api.deezer.com/search?q={artist}"

        response = requests.get(url)

        data = response.json()

        if data.get("data"):
            songs.extend(data["data"][:2])

    return songs


@app.route("/")
def home():

    trending = get_trending_songs()

    return render_template(
        "index.html",
        trending=trending
    )


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/search")
def search():

    query = request.args.get("query")

    if not query:
        return render_template(
            "search.html",
            artists=[]
        )

    url = f"https://api.deezer.com/search?q={query}"

    response = requests.get(url)

    data = response.json()

    artists = data.get("data", [])

    return render_template(
         "search.html",
         artists=artists,
         query=query
)

@app.route("/artist/<artist_id>")
def artist(artist_id):

    url = f"https://api.deezer.com/artist/{artist_id}"

    response = requests.get(url)

    artist = response.json()

    country = get_artist_country(artist["name"])

    return render_template(
        "artist.html",
        artist=artist,
        country=country
    )


if __name__ == "__main__":
    app.run(debug=True)