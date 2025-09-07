from flask import Flask, request
from flask import render_template
import requests # type: ignore

app = Flask(__name__)


@app.route('/')
def index():
    dog_pic = get_dog()
    cat_pic = get_cat()
    dog_result = None
    cat_result = None
    return render_template("index.html", 
                           cat_pic=cat_pic, 
                           dog_pic=dog_pic,
                           dog_result=dog_result,
                           cat_result=cat_result)


def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url, timeout=5).json()
        return response["message"] 
    except Exception as e:
        print("API error", e)
        return "https://via.placeholder.com/300?text=No+Meme", "unknown"
    
def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url, timeout=5).json()
        print("cat API response:", response)
        return response[0]["url"]
    except Exception as e:
        print("API Error", e)
        return "https://via.placeholder.com/300?text=No+Meme", "unknown"
   

if __name__ == "__main__":
    app.run(debug=True)