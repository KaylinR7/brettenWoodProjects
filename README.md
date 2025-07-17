# BrettenWood Projects Website

A professional Flask website for BrettenWood Projects, specializing in water backup systems and house maintenance in KwaZulu-Natal, South Africa.

## Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Modern UI/UX**: Clean black and white theme with smooth animations
- **Tank Systems**: Detailed information about 1000L, 2500L, and 5000L Jojo tank systems
- **Portfolio**: Showcase of completed installations and projects
- **Reviews System**: Customer review submission with 1-5 star ratings
- **Contact Form**: Comprehensive contact form with service area selection
- **Mobile-First**: Fully responsive design optimized for mobile devices

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Font Awesome
- **Animations**: AOS (Animate On Scroll)
- **Data Storage**: JSON files for reviews

## Installation

1. Clone or download the project files
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
BrettenWood/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/                 # Data storage directory
│   └── reviews.json      # Customer reviews (auto-created)
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── systems.html      # Tank systems page
│   ├── portfolio.html    # Portfolio page
│   ├── reviews.html      # Reviews page
│   └── contact.html      # Contact page
└── static/              # Static files
    ├── css/
    │   └── style.css     # Custom styles
    ├── js/
    │   └── main.js       # Custom JavaScript
    └── images/           # Image assets
```

## Pages

1. **Home** (`/`) - Landing page with company information and services overview
2. **Tank Systems** (`/systems`) - Detailed information about available tank systems
3. **Portfolio** (`/portfolio`) - Gallery of completed projects and customer testimonials
4. **Reviews** (`/reviews`) - Customer reviews and review submission form
5. **Contact** (`/contact`) - Contact form and company information

## Tank Systems

The website showcases both **Jojo** and **Eco** tank systems in three capacities:

### Jojo Tank Systems
- **1000L Jojo System**: Contact for Quote - Perfect for small homes
- **2500L Jojo System**: Contact for Quote - Ideal for medium-sized families
- **5000L Jojo System**: Contact for Quote - Best for large homes and commercial use

### Eco Tank Systems
- **1000L Eco System**: Contact for Quote - Environmentally friendly option for small homes
- **2500L Eco System**: Contact for Quote - Cost-effective solution for families
- **5000L Eco System**: Contact for Quote - Large capacity eco-friendly system

Each system includes:
- Tank (Jojo or Eco brand)
- Grundfos Pump
- Pressure Switch
- Non-return Valve
- Tank Stand
- Installation Kit
- Professional Installation

**Note**: Prices may change based on current market conditions and specific installation requirements.

## Service Areas

BrettenWood Projects serves all areas of KwaZulu-Natal, including:
- Durban Metro
- South Coast
- North Coast
- Inland Areas

## Features

### Responsive Design
- Mobile-first approach
- Bootstrap 5 framework
- Custom responsive breakpoints
- Touch-friendly interface

### Animations
- AOS (Animate On Scroll) library
- Custom CSS animations
- Smooth transitions
- Interactive hover effects

### Reviews System
- 1-5 star rating system
- Customer review submission
- Review display with ratings
- JSON-based storage

### Contact System
- Comprehensive contact form
- Service area selection
- Urgency level selection
- Form validation
- Flash message feedback

## Customization

### Colors
The website uses a black and white theme as requested:
- Primary Black: `#000000`
- Primary White: `#ffffff`
- Light Gray: `#f8f9fa`
- Dark Gray: `#343a40`

### Adding Images
The website supports company logos, tank images, and portfolio photos:

1. **Company Logo**: Save as `static/images/logo.png` (40px height)
2. **Brand Logos**:
   - Jojo logo: `static/images/jojo-logo.png`
   - Eco logo: `static/images/eco-logo.png`
3. **Tank Images**: Place in `static/images/` with these exact names:
   - `jojo-1000.png`, `jojo-2500.webp`, `jojo-5200.webp`
   - `eco-1000.jpg`, `eco-2500.png`, `eco-5000.png`
4. **Portfolio Images**: Place in `static/images/portfolio/` directory

See `IMAGE_GUIDE.md` for detailed instructions and requirements.

### Modifying Tank Systems
To update tank systems, prices, or specifications:
1. Edit the `TANK_SYSTEMS` dictionary in `app.py`
2. Update pricing, specifications, or add new systems

## Deployment

For production deployment:
1. Set `app.debug = False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Set up proper database for reviews (instead of JSON)
4. Configure email sending for contact form
5. Add SSL certificate for HTTPS

## Support

For technical support or customization requests, contact the development team.

## License

This project is proprietary software developed for BrettenWood Projects.
