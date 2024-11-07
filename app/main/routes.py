from flask import Blueprint, request, redirect, jsonify, render_template
from .models import URL
from app import db, limiter
from .utils import is_valid_url, generate_short_code

main = Blueprint('main', __name__)


@main.route('/shorten', methods=['POST'])
@limiter.limit("100/minute")
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    url_entry = URL(original_url=original_url, short_code=short_code)
    db.session.add(url_entry)
    db.session.commit()

    return jsonify({"short_url": f"/{short_code}"}), 201


@main.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()
    url_entry.clicks += 1
    db.session.commit()
    return redirect(url_entry.original_url)


@main.route('/stats/<short_code>', methods=['GET'])
def get_url_stats(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first_or_404()
    return jsonify({"clicks": url_entry.clicks, "original_url": url_entry.original_url})
