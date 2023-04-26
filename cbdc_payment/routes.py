from flask import Flask, Blueprint, render_template

blueprint = Blueprint("routes", __name__)


@blueprint.route("/")
def index():
    return render_template("index.html")


@blueprint.route("/about-us")
def about_us():
    return render_template("about_us.html")


@blueprint.route("/contact-us")
def contact_us():
    return render_template("contact_us.html")


@blueprint.route("/payments/payment-links")
def payment_links():
    return render_template("payment_links.html")


@blueprint.route("/payments/checkout-demo")
def checkout_demo():
    return render_template("checkout_demo.html")


@blueprint.route("/payments/pay-bills")
def pay_bills():
    return render_template("pay_bills.html")
