from flask import Flask, request
from flask import render_template
import requests # type: ignore

app = Flask(__name__)


@app.route('/')
def index():
    dog_pic, dog_breed = get_dog()
    cat_pic, cat_breed = get_cat()

    return render_template("index.html", 
                           cat_pic=cat_pic, 
                           dog_pic=dog_pic,
                           dog_result = None,
                           cat_result = None,
                           dog_breed=dog_breed,
                           cat_breed=cat_breed)



@app.route('/guess_dog', methods=['POST'])
def guess_dog():
    user_guess = request.form.get('dog_guess', '').lower()
    dog_pic, dog_breed = get_dog()
    result = "correct!" if user_guess == dog_breed.lower() else f"Wrong it was {dog_breed}"
    return render_template("index.html", dog_pic=dog_pic,dog_breed=dog_breed, dog_result=result, cat_pic=None)

@app.route('/guess_cat', methods=['POST'])
def guess_cat():
    user_guess = request.form.get('cat_guess', '').lower()
    cat_pic, cat_breed = get_cat()
    result = "correct!" if user_guess == cat_breed.lower() else f"Wrong this is {cat_breed}"
    return render_template("index.html", cat_pic=cat_pic, cat_breed=cat_breed, cat_result=result, dog_pic=None)


def get_dog():
    url = "https://dog.ceo/api/breeds/image/random"
    try:
        response = requests.get(url).json()
        breed = response["message"].split("/")[4]
        return response["message"], breed
    except Exception as e:
        print("API error", e)
        return "https://via.placeholder.com/300?text=No+Meme", "unknown"
    
def get_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    try:
        response = requests.get(url).json()
        print("cat API response:", response)
        breed = response[0].get("breeds", [{"name": "unknown"}])[0]["name"]
        return response[0]["url"],breed
    except Exception as e:
        print("API Error", e)
        return "https://via.placeholder.com/300?text=No+Meme", "unknown"
   

if __name__ == "__main__":
    app.run(debug=True)