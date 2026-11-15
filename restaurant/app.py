from flask import Flask, render_template

app = Flask(__name__)


MENU = [
    {"id": 1, "name": "Margherita Pizza", "price_cents": 1200},
    {"id": 2, "name": "Chicken Burger", "price_cents": 950},
    {"id": 3, "name": "Garden Salad", "price_cents": 700},
]


@app.get("/")
def show_menu():
    return render_template("menu.html", menu=MENU)
