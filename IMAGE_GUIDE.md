# Image Guide for BrettenWood Projects Website

## 📁 Image Directory Structure

All images should be placed in the `static/images/` directory:

```
static/
└── images/
    ├── logo.png                    # Company logo (navbar)
    ├── jojo-logo.png              # Jojo brand logo
    ├── eco-logo.png               # Eco brand logo
    ├── jojo-1000.png              # 1000L Jojo tank image
    ├── jojo-2500.webp             # 2500L Jojo tank image
    ├── jojo-5200.webp             # 5000L Jojo tank image
    ├── eco-1000.jpg               # 1000L Eco tank image
    ├── eco-2500.png               # 2500L Eco tank image
    ├── eco-5000.png               # 5000L Eco tank image
    └── portfolio/                 # Portfolio images folder
        ├── job1.jpg               # Portfolio project 1
        ├── job2.jpg               # Portfolio project 2
        ├── job3.jpg               # Portfolio project 3
        └── ...                    # More portfolio images
```

## 🖼️ Image Requirements

### Company Logo (`logo.png`)
- **Size**: 40px height (width auto-scales)
- **Format**: PNG with transparent background preferred
- **Usage**: Appears in the navigation bar
- **Fallback**: Water icon if image fails to load

### Brand Logos
- **Jojo Logo** (`jojo-logo.png`): 30px height, PNG format
- **Eco Logo** (`eco-logo.png`): 30px height, PNG format
- **Usage**: Displayed above tank system sections

### Tank System Images
- **Size**: Maximum 150px height, any width
- **Format**: PNG, JPG, or WebP
- **Quality**: High resolution for crisp display
- **Background**: Transparent or white background preferred

#### Current Tank Images Needed:
1. `jojo-1000.png` - 1000L Jojo tank
2. `jojo-2500.webp` - 2500L Jojo tank  
3. `jojo-5200.webp` - 5000L Jojo tank
4. `eco-1000.jpg` - 1000L Eco tank
5. `eco-2500.png` - 2500L Eco tank
6. `eco-5000.png` - 5000L Eco tank

### Portfolio Images
- **Size**: Minimum 800px width for good quality
- **Format**: JPG preferred for photos
- **Naming**: Use descriptive names (e.g., `durban-north-5000l.jpg`)

## 📝 How to Add Images

### 1. Adding Company Logo
1. Save your logo as `static/images/logo.png`
2. The website will automatically display it in the navigation
3. If no logo is found, it shows a water icon instead

### 2. Adding Brand Logos
1. Save Jojo logo as `static/images/jojo-logo.png`
2. Save Eco logo as `static/images/eco-logo.png`
3. They will appear above their respective tank sections

### 3. Adding Tank Images
1. Save tank images with the exact filenames listed above
2. Place them in `static/images/` directory
3. The website will automatically display them on the systems page
4. If an image is missing, a water icon placeholder appears

### 4. Adding Portfolio Images
1. Create `static/images/portfolio/` directory if it doesn't exist
2. Add your project photos with descriptive names
3. Update the portfolio template to reference your images

## 🔧 Updating Portfolio Images

To add real portfolio images, edit `templates/portfolio.html`:

```html
<!-- Replace placeholder with actual image -->
<div class="portfolio-image-container">
    <img src="{{ url_for('static', filename='images/portfolio/your-image.jpg') }}" 
         alt="Project Description" class="img-fluid portfolio-image">
</div>
```

## 📱 Image Optimization Tips

### For Web Performance:
1. **Compress images** before uploading (use tools like TinyPNG)
2. **Use appropriate formats**:
   - PNG for logos and graphics with transparency
   - JPG for photographs
   - WebP for modern browsers (smaller file sizes)
3. **Optimize dimensions** - don't upload huge images if they'll be displayed small

### Recommended Image Sizes:
- **Logo**: 200x200px maximum
- **Tank images**: 400x300px maximum  
- **Portfolio images**: 1200x800px maximum
- **Brand logos**: 200x100px maximum

## 🎨 Image Editing Guidelines

### For Tank Images:
- Clean, professional product shots
- Consistent lighting and background
- Show the tank from a clear angle
- Include any visible branding/labels

### For Portfolio Images:
- Before/after installation shots
- Wide shots showing the complete system
- Detail shots of connections and components
- Clean, well-lit photography

## 🔄 Updating Tank Systems

If you need to add more tank sizes or change specifications, edit `app.py`:

```python
TANK_SYSTEMS = {
    'new_tank_id': {
        'name': 'Tank Name',
        'brand': 'Jojo' or 'Eco',
        'capacity': 'Capacity in Litres',
        'pump': 'Pump specifications',
        'pump_specs': 'Technical specs',
        'includes': ['List', 'of', 'included', 'items'],
        'price': 'Contact for Quote',
        'image': 'filename.jpg'
    }
}
```

## 🚀 Quick Start

1. **Create the images directory**:
   ```bash
   mkdir -p static/images/portfolio
   ```

2. **Add your company logo** as `static/images/logo.png`

3. **Add tank images** with the exact filenames listed above

4. **Test the website** - images should appear automatically

5. **Add portfolio images** and update the portfolio template

## ❓ Troubleshooting

### Image Not Showing?
1. Check the filename matches exactly (case-sensitive)
2. Ensure the image is in the correct directory
3. Verify the image format is supported (PNG, JPG, WebP)
4. Check browser console for error messages

### Image Too Large/Small?
1. The CSS automatically scales images appropriately
2. For better performance, resize images before uploading
3. Check the CSS classes for size constraints

### Need Different Image Sizes?
Edit the CSS in `static/css/style.css` or the template files to adjust image dimensions.

## 📞 Support

If you need help adding images or customizing the image display, refer to the main README.md file or contact the development team.
