# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about-us")
def about_us():
    return render_template("about_us.html")


@app.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/payments/payment-links")
def payment_links():
    return render_template("payment_links.html")


@app.route("/payments/checkout-demo")
def checkout_demo():
    return render_template("checkout_demo.html")


@app.route("/payments/pay-bills")
def pay_bills():
    return render_template("pay_bills.html")


@app.route("/merchant-login")
def merchant_login():
    return render_template("merchant_login.html")


@app.route("/customer-login")
def customer_login():
    return render_template("customer_login.html")


if __name__ == "__main__":
    app.run(debug=True, port=5500)
