"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Flask_test import app

@app.route('/')
@app.route('/main')
def main():
    """Renders the main page."""
    return render_template(
        'index.html',
        title='Main',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='How to get in touch with us.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
