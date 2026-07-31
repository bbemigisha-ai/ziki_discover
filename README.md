ZIKI DISCOVER

Discover the Rhythm of Africa

Deployed Application

The application is deployed and can be accessed through the load balancer at:

**https://34.203.202.192**

Demo Video

**https://youtu.be/-F3j0VkldTM**

Project Overview(Description)

The word Ziki is a slang word used in my Ugandan Highschool from the Bantu word "Muziki" which means "Music". Ziki Discover is a Flask web application that helps users explore African music and discover african artists by searching for artists, songs, and albums from across the continent. The application integrates the Deezer API to retrieve music information and song previews, and the MusicBrainz API to provide additional artist information such as their country of origin.
The idea behind this project was to create a simple and interactive platform that celebrates African music while giving me practical experience working with APIs, Flask, and web deployment.

 Features

- Search for your choice of artists, songs and albums
- Listen to 30-second song previews
- View artist information and country of origin
- Browse artists by country
- Browse music by genre
- View trending African songs
- Responsive black and gold themed interface


 Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Gunicorn
- Nginx
- HAProxy
- Git & GitHub


 APIs Used

1.Deezer API(my main API)
- Search for songs, artists and albums
- Retrieve album artwork
- Play 30-second song previews
Documentation:
https://developers.deezer.com/api

2.MusicBrainz API
- Retrieve artist information
- Display artist country of origin ,used in the artist.html page
Documentation:
https://musicbrainz.org/doc/MusicBrainz_API


My Project Structure

```
ziki_discover/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── search.html
│   ├── artist.html
│   └── about.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

 Installation

Clone the repository:

     git clone https://github.com/bbemigisha-ai/ziki_discover.git
     cd ziki_discover

Create and activate a virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Install the required packages:

    pip install -r requirements.txt


Run the application:

     python app.py


Open your browser and visit:

    http://127.0.0.1:5000


Deployment

After testing the application locally, I deployed it to my web servers using Gunicorn, Nginx and HAProxy.

Steps followed

1. Clone the repository onto the web server.
2. Create and activate a Python virtual environment.
3. Install the required dependencies using:

     pip install -r requirements.txt


4. Run the application with Gunicorn.
5. Configure Nginx to proxy requests to the Gunicorn server.
6. Configure HAProxy to distribute traffic between the backend web servers.
7. Restart the services and verify that the application is accessible through the load balancer.

 Challenges faced throughout this project

The most challenging part of this project was deployment. Honestly, its's not for the weak. After successfully playing around with APIs, lol, I had to configure Gunicorn, Nginx and HAProxy correctly and troubleshoot issues where different backend servers were serving different versions of the project(mainly work from the intranet projects). Debugging these deployment problems helped me better understand how Flask applications are hosted in a production environment.


Future Improvements

Some features I would like to add in the future include:

- User accounts for authentication 
- Favourite artists and playlists
- Better search filters
- Music recommendations
- More African artists and genres


CREATOR

Bertha Mbonimpa Bemigisha
Software Engineering, Cohort 2, Web Infrastructure

Acknowledgements

This project was developed as part of my Web Infrastructure Summative, "Playing Around With APIs". I would like to acknowledge the Deezer API and MusicBrainz API for providing the music data used in this application.