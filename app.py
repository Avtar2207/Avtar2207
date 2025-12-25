from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Yeh aapka product data hai (Aap isme 1000 items bhi daal sakte hain)
products = [
    {"name": "Rice (Basmati) 5 kg", "price": 190, "unit": "5 kg", "img": "rice.jpg"},
    {"name": "Atta (Ashirwad) 5 kg", "price": 190, "unit": "5 kg", "img": "atta.jpg"},
    {"name": "Tea (Tata) 250g", "price": 60, "unit": "250g", "img": "tea.jpg"},
    {"name": "Sugar 1 kg", "price": 45, "unit": "1 kg", "img": "sugar.jpg"},
    {"name": "Milk 500ml", "price": 30, "unit": "500ml", "img": "milk.jpg"},
    {"name": "Rifine (tel) 1 pkt", "price": 130, "unit": "1 pkt", "img": "rifine.jpg"},
    {"name": "sarf 1 pkt", "price": 70, "unit": "1 pkt", "img": "sarf.jpg"},
    {"name": "lifeboy 1 pic", "price": 27, "unit": "1 pic", "img": "lifeboy.jpg"},
    {"name": "shampoo 1 pic", "price": 2, "unit": "1 pic", "img": "shampoo.jpg"},
    {"name": "coconut (oil) 200ml", "price": 110, "unit": "200ml", "img": "coconut.jpg"},
    {"name": "Goodnight (Aggarbati) 1 pkt", "price": 100, "unit": "1 pkt", "img": "goodnight.jpg"},
    {"name": "MUNG (dal) 1kg", "price": 110, "unit": "1kg", "img": "milk.jpg"},
    {"name": "MASSOR (dal) 1kg", "price": 90, "unit": "1kg", "img": "milk.jpg"},
    {"name": "khdamung (dal) 1kg", "price": 120, "unit": "1kg", "img": "milk.jpg"},
    {"name": "Matchbox 1 pic", "price": 10, "unit": "1 pic", "img": "matchbox.jpg"},
    {"name": "haldi 200g", "price": 60, "unit": "200g", "img": "milk.jpg"},
    {"name": "mirchi 200g", "price": 70, "unit": "200g", "img": "milk.jpg"},
    {"name": "dhaniya 200g", "price": 60, "unit": "200g", "img": "milk.jpg"},
    {"name": "kalimirchi 50g", "price": 50, "unit": "50g", "img": "milk.jpg"},
    {"name": "khda zira 100g", "price": 45, "unit": "100g", "img": "milk.jpg"},
    {"name": "poha 1kg", "price": 50, "unit": "1kg", "img": "milk.jpg"},
    {"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
    {"name": "Suji 1kg", "price": 50, "unit": "1kg", "img": "milk.jpg"},
    {"name": "soyabin (badi) 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
    {"name": "basan 1kg", "price": 120, "unit": "1kg", "img": "milk.jpg"},
    {"name": "desi chana 1kg", "price": 80, "unit": "1kg", "img": "milk.jpg"},
    {"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
{"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
{"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
{"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},
{"name": "falidana 250g", "price": 30, "unit": "250g", "img": "milk.jpg"},


]

@app.route('/search', methods=['GET'])
def search_product():
    query = request.args.get('q', '').lower()
    # Filter products based on search query
    results = [p for p in products if query in p['name'].lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
