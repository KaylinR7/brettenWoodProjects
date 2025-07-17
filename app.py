from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime
import glob

app = Flask(__name__)
app.secret_key = 'brettenwood_secret_key_2025'

# Ensure data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Initialize reviews file if it doesn't exist
reviews_file = 'data/reviews.json'
if not os.path.exists(reviews_file):
    with open(reviews_file, 'w') as f:
        json.dump([], f)

def load_reviews():
    """Load reviews from JSON file"""
    try:
        with open(reviews_file, 'r') as f:
            return json.load(f)
    except:
        return []

def save_review(review_data):
    """Save a new review to JSON file"""
    reviews = load_reviews()
    review_data['id'] = len(reviews) + 1
    review_data['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    reviews.append(review_data)
    with open(reviews_file, 'w') as f:
        json.dump(reviews, f, indent=2)

def load_portfolio_descriptions():
    """Load custom descriptions from JSON file"""
    descriptions_file = 'data/portfolio_descriptions.json'
    if os.path.exists(descriptions_file):
        try:
            with open(descriptions_file, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}

def get_portfolio_images():
    """Automatically get all portfolio images from the portfolio folder"""
    portfolio_dir = 'static/images/portfolio'
    if not os.path.exists(portfolio_dir):
        return []

    # Load custom descriptions
    custom_descriptions = load_portfolio_descriptions()

    # Supported image formats
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.gif']
    portfolio_images = []

    for extension in image_extensions:
        # Get both lowercase and uppercase, but avoid duplicates
        files = glob.glob(os.path.join(portfolio_dir, extension))
        files.extend(glob.glob(os.path.join(portfolio_dir, extension.upper())))
        portfolio_images.extend(files)

    # Convert to just filenames, remove duplicates, and sort
    portfolio_images = list(set([os.path.basename(img) for img in portfolio_images]))
    portfolio_images.sort()

    # Create portfolio data with automatic titles and custom descriptions
    portfolio_data = []
    for i, image in enumerate(portfolio_images, 1):
        # Generate automatic title from filename
        title = os.path.splitext(image)[0].replace('_', ' ').replace('-', ' ').title()
        if title.lower().startswith('job'):
            title = f"Project {title[3:].strip() or i}"

        # Use custom description if available, otherwise generate automatic one
        image_key = os.path.splitext(image)[0]  # filename without extension
        if image_key in custom_descriptions:
            description = custom_descriptions[image_key]['description']
            category = custom_descriptions[image_key].get('category', 'residential')
            custom_title = custom_descriptions[image_key].get('title', title)
        else:
            description = f"Professional water backup system installation - {title}"
            category = 'residential' if i % 3 != 0 else 'commercial'  # Mix categories
            custom_title = title

        portfolio_data.append({
            'image': image,
            'title': custom_title,
            'description': description,
            'category': category
        })

    return portfolio_data

# Tank systems data
TANK_SYSTEMS = {
    'jojo_1000L': {
        'name': '1000L Jojo Tank System',
        'brand': 'Jojo',
        'capacity': '1000 Litres',
        'pump': 'Grundfos SB 3-45 A Submersible Pump',
        'pump_specs': '0.75kW, 45L/min flow rate',
        'includes': ['1000L Jojo Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit'],
        'price': 'Contact for Quote',
        'image': 'jojo-1000.png'
    },
    'jojo_2500L': {
        'name': '2500L Jojo Tank System',
        'brand': 'Jojo',
        'capacity': '2500 Litres',
        'pump': 'Grundfos SB 3-45 A Submersible Pump',
        'pump_specs': '1.1kW, 60L/min flow rate',
        'includes': ['2500L Jojo Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit', 'Level Indicator'],
        'price': 'Contact for Quote',
        'image': 'jojo-2500.webp'
    },
    'jojo_5000L': {
        'name': '5000L Jojo Tank System',
        'brand': 'Jojo',
        'capacity': '5000 Litres',
        'pump': 'Grundfos SB 5-45 A Submersible Pump',
        'pump_specs': '1.5kW, 75L/min flow rate',
        'includes': ['5000L Jojo Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit', 'Level Indicator', 'Overflow Kit'],
        'price': 'Contact for Quote',
        'image': 'jojo-5200.webp'
    },
    'eco_1000L': {
        'name': '1000L Eco Tank System',
        'brand': 'Eco',
        'capacity': '1000 Litres',
        'pump': 'Grundfos SB 3-45 A Submersible Pump',
        'pump_specs': '0.75kW, 45L/min flow rate',
        'includes': ['1000L Eco Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit'],
        'price': 'Contact for Quote',
        'image': 'eco-1000.jpg'
    },
    'eco_2500L': {
        'name': '2500L Eco Tank System',
        'brand': 'Eco',
        'capacity': '2500 Litres',
        'pump': 'Grundfos SB 3-45 A Submersible Pump',
        'pump_specs': '1.1kW, 60L/min flow rate',
        'includes': ['2500L Eco Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit', 'Level Indicator'],
        'price': 'Contact for Quote',
        'image': 'eco-2500.png'
    },
    'eco_5000L': {
        'name': '5000L Eco Tank System',
        'brand': 'Eco',
        'capacity': '5000 Litres',
        'pump': 'Grundfos SB 5-45 A Submersible Pump',
        'pump_specs': '1.5kW, 75L/min flow rate',
        'includes': ['5000L Eco Tank', 'Grundfos Pump', 'Pressure Switch', 'Non-return Valve', 'Tank Stand', 'Installation Kit', 'Level Indicator', 'Overflow Kit'],
        'price': 'Contact for Quote',
        'image': 'eco-5000.png'
    }
}

@app.route('/')
def home():
    """Home page with about us section"""
    return render_template('home.html')

@app.route('/systems')
def systems():
    """Tank systems page"""
    return render_template('systems.html', tank_systems=TANK_SYSTEMS)

@app.route('/portfolio')
def portfolio():
    """Portfolio page showing previous jobs"""
    portfolio_images = get_portfolio_images()
    return render_template('portfolio.html', portfolio_images=portfolio_images)

@app.route('/reviews')
def reviews():
    """Reviews page"""
    reviews_data = load_reviews()
    return render_template('reviews.html', reviews=reviews_data)

@app.route('/submit_review', methods=['POST'])
def submit_review():
    """Handle review submission"""
    try:
        review_data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'rating': int(request.form.get('rating')),
            'title': request.form.get('title'),
            'review': request.form.get('review')
        }
        
        # Basic validation
        if not all([review_data['name'], review_data['rating'], review_data['review']]):
            flash('Please fill in all required fields.', 'error')
            return redirect(url_for('reviews'))
        
        save_review(review_data)
        flash('Thank you for your review! It has been submitted successfully.', 'success')
        return redirect(url_for('reviews'))
    
    except Exception as e:
        flash('An error occurred while submitting your review. Please try again.', 'error')
        return redirect(url_for('reviews'))

@app.route('/contact')
def contact():
    """Contact page"""
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission"""
    try:
        # In a real application, you would send an email or save to database
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    except Exception as e:
        flash('An error occurred while sending your message. Please try again.', 'error')
        return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
