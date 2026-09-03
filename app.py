import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Tuhade Designs - Photo link naal
designs = [
    {"id":1, "title":"30x40 Modern 2BHK - 2D", "sqft":"1200", "bhk":"2BHK", "type":"2D", "price":199, "img":"https://i.imgur.com/8Km9tLL.jpg"},
    {"id":2, "title":"30x40 Modern 2BHK - 3D Front", "sqft":"1200", "bhk":"2BHK", "type":"3D", "price":299, "img":"https://i.imgur.com/Q6a2z7b.jpg"},
    {"id":3, "title":"30x50 Punjabi Haveli - Blueprint", "sqft":"1500", "bhk":"3BHK", "type":"Blueprint", "price":399, "img":"https://i.imgur.com/m6pL2iL.jpg"},
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ghar Banoyo</title>
<style>
body{font-family:Arial; background:#f2f2f2; padding:10px;}
.card{background:white; border-radius:12px; padding:12px; margin:12px; width:320px; display:inline-block; box-shadow:0 2px 10px #ccc;}
.card img{width:100%; border-radius:8px; height:200px; object-fit:cover;}
.btn{background:black; color:white; padding:10px 15px; border:none; border-radius:6px; width:100%; font-size:16px;}
.qr{width:200px !important; height:200px !important;}
</style>
</head>
<body>
<h1>🏠 Ghar Banoyo - Blueprints</h1>
<p>Direct Download - No Subscription - UPI: <b>deepbuttar805@okhdfcbank</b></p>

{% for d in designs %}
<div class="card">
<img src="{{d.img}}">
<h3>{{d.title}}</h3>
<p>📐 {{d.sqft}} SqFt | 🛏️ {{d.bhk}} | 📁 {{d.type}}</p>
<p>Price: <b>Rs.{{d.price}}</b></p>
<a href="/pay/{{d.id}}"><button class="btn">Pay Rs.{{d.price}} & Download</button></a>
</div>
{% endfor %}

</body>
</html>
"""

PAY_HTML = """
<body style="text-align:center; font-family:Arial; padding:20px;">
<h1>Pay Rs.{{d.price}} - {{d.title}}</h1>
<div style="background:white; padding:20px; border-radius:15px; max-width:400px; margin:auto; box-shadow:0 4px 15px #ccc;">
<img src="https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa=deepbuttar805@okhdfcbank%26am={{d.price}}%26tn={{d.title}}" style="width:280px; border:1px solid #000;">
<p><b>UPI:</b> deepbuttar805@okhdfcbank<br><b>Name:</b> Dilpreet Singh</p>
<p>Scan karke pay karo - fer download shuru</p>
<a href="/download/{{d.id}}"><button style="background:green; color:white; padding:12px 20px; border:none; border-radius:8px;">I Paid - Download Now</button></a>
<br><br><a href="/">Back</a>
</div>
</body>
"""

@app.route('/')
def home():
    return render_template_string(HTML, designs=designs)

@app.route('/pay/<int:id>')
def pay(id):
    d = next((x for x in designs if x["id"]==id), None)
    return render_template_string(PAY_HTML, d=d)

@app.route('/download/<int:id>')
def download(id):
    d = next((x for x in designs if x["id"]==id), None)
    return f"<h1>Downloading {d['title']} - {d['img']} <br><br><a href='/'>Back to Home</a></h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
