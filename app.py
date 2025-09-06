from flask import Flask
from flask import render_template
import requests # type: ignore

app = Flask(__name__)


@app.route('/')
def index():
    dog_pic = get_dog()
    return render_template("index.html", dog_pic=dog_pic)


def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url, timeout=5).json()
        return response["message"] 
    except Exception as e:
        print("API error", e)
        return "https://via.placeholder.com/300?text=No+Meme", "unknown"
   

if __name__ == "__main__":
    app.run(debug=True)