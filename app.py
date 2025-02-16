from flask import Flask, render_template

app = Flask(__name__)

# Data
LOGO_URL = "https://i.ibb.co/kdztGbj/photo-2025-02-16-16-39-58.jpg"
MENU_ITEMS = [
    ("☕️ Espresso", "$2.50"),
    ("☕️ Cappuccino", "$3.00"),
    ("☕️ Latte", "$3.50"),
    ("☕️ Mocha", "$4.00"),
    ("🍰 Chocolate Cake", "$4.50"),
    ("🍰 Cheesecake", "$4.00"),
    ("🍰 Red Velvet", "$4.75"),
    ("🍰 Carrot Cake", "$4.25"),
]
MENU_IMAGES = [
    "https://i.ibb.co/KcV2G3BQ/photo-2025-02-16-16-16-18.jpg",
    "https://i.ibb.co/jZG5yWgJ/photo-2025-02-16-16-26-41.jpg"
]
BOOKS = [
    ("Little Women", "https://i.ibb.co/N2LXhD9X/photo-2025-02-16-13-54-38.jpg"),
    ("Ikigai", "https://i.ibb.co/1f6jyT5t/photo-2025-02-16-14-23-33.jpg"),
    ("1984", "https://i.ibb.co/MDRfZhfC/photo-2025-02-16-09-29-15.jpg"),
    ("Pride and Prejudice", "https://i.ibb.co/4ZfRBCyb/photo-2025-02-16-14-03-52.jpg"),
    ("Days Gone By", "https://i.ibb.co/ZCqkr5H/photo-2025-02-16-14-11-46.jpg"),
    ("The Kite Runner", "https://i.ibb.co/k2DK1Pm3/photo-2025-02-16-14-08-43.jpg"),
    ("The Old Man and The Sea", "https://i.ibb.co/Tx723tQY/photo-2025-02-16-14-07-22.jpg"),
    ("Crime and Punishment", "https://i.ibb.co/RTR2GnNt/photo-2025-02-16-14-01-40.jpg"),
    ("The Alchemist", "https://i.ibb.co/pjYjtJvj/photo-2025-02-16-14-05-01.jpg"),
    ("The Orient Express", "https://i.ibb.co/HfDkBX3H/photo-2025-02-16-13-58-33.jpg"),
]
CONTACT_INFO = {
    "Email": "bookcafe@example.com",
    "Phone 1": "+998 90 123 45 67",
    "Phone 2": "+998 91 234 56 78",
    "Location": "Tashkent, Uzbekistan",
}

@app.route('/')
def home():
    return render_template("index.html", logo=LOGO_URL)

@app.route('/menu')
def menu():
    return render_template("menu.html", menu=MENU_ITEMS, images=MENU_IMAGES)

@app.route('/books')
def books():
    return render_template("books.html", books=BOOKS)

@app.route('/contact')
def contact():
    return render_template("contact.html", contact=CONTACT_INFO)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
