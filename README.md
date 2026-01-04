# Trav. - Travel Booking Platform

A Django-based travel booking platform for exploring and booking accommodations across various destinations in Odisha, India.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Dynamic Place Search**: Browse accommodations in different locations (Puri, Bhubaneswar, Chilka Lake, Konark, etc.)
- **Advanced Filtering System**:
  - Filter by property type (House, Hostel, Flat, Villa, Guest-Suite)
  - Filter by price range (Up to $50, $60, $70, $80, $90, $100, $100+)
  - Multiple filter combinations
  - Real-time filter counts
- **Property Listings**: Display of hotels/properties with detailed information
- **Responsive Design**: Mobile-friendly interface
- **Random Place Discovery**: Explore random destinations with one click
- **Rating System**: Visual star ratings for properties
- **Search Functionality**: Search accommodations by location

## 🛠️ Technologies Used

- **Backend**: Django 4.x / Python 3.x
- **Database**: SQLite (default) / PostgreSQL / MySQL (configurable)
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome
- **Styling**: Custom CSS

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/trav-booking-platform.git
cd trav-booking-platform
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install Django manually:
```bash
pip install django
```

## 🗄️ Database Setup

### Step 1: Create the Database Tables
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### Step 3: Add Sample Data
You can add hotels through the Django admin panel:
1. Start the server: `python manage.py runserver`
2. Visit: `http://127.0.0.1:8000/admin`
3. Login with superuser credentials
4. Add hotels with the following fields:
   - `place_name`: Location name (e.g., "Puri", "Bhubaneswar")
   - `property_type`: Type of property (House, Hostel, Flat, Villa, Guest-Suite)
   - `property_name`: Name/title of the property
   - `bedroom_count`: Number of bedrooms
   - `bathroom_count`: Number of bathrooms
   - `guest_count`: Maximum guest capacity
   - `price`: Price per day (in dollars)
   - `star_rating`: Rating (1-5)

## 🚀 Running the Project

### Development Server
```bash
python manage.py runserver
```
Visit: `http://127.0.0.1:8000`

### Access Admin Panel
Visit: `http://127.0.0.1:8000/admin`

## 📁 Project Structure

```
trav-booking-platform/
│
├── main/                          # Main app directory
│   ├── migrations/                # Database migrations
│   ├── static/                    # Static files
│   │   └── main/
│   │       ├── css/
│   │       │   └── style.css     # Main stylesheet
│   │       └── images/           # Image assets
│   ├── templates/                 # HTML templates
│   │   └── main/
│   │       ├── index.html        # Home page
│   │       ├── listing.html      # Listing page with filters
│   │       └── hotel.html        # Hotel detail page
│   ├── models.py                  # Database models
│   ├── views.py                   # View functions
│   ├── urls.py                    # URL routing
│   └── admin.py                   # Admin configuration
│
├── project_name/                  # Project settings directory
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
│
├── manage.py                      # Django management script
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## 📖 Usage

### Home Page
- Browse featured destinations
- Use the search bar to find accommodations
- Click on "Plan Random" to discover random destinations
- Explore trending places and exclusive offers

### Listing Page
Navigate to listings by:
- Clicking on destination cards on the home page
- Using the search functionality
- Accessing via URL: `/listing?place=Puri`

**Filtering Options**:
1. **Property Type**: Select one or multiple property types
2. **Price Range**: Select a maximum price range
3. **Clear Filters**: Reset all applied filters

**URL Parameters**:
- Place: `/listing?place=Puri`
- Property Type: `/listing?place=Puri&property_type=Villa`
- Price: `/listing?place=Puri&max_price=100`
- Combined: `/listing?place=Puri&property_type=Villa&property_type=House&max_price=80`

### Hotel Detail Page
Click on any property card to view detailed information (coming soon).

## 🎨 Customization

### Adding New Locations
1. Go to Django admin panel
2. Add hotels with the new `place_name`
3. Update `index.html` to add navigation links for the new place

### Styling
Edit `main/static/main/css/style.css` to customize the appearance.

### Adding New Filters
1. Update `views.py` to handle new filter parameters
2. Update `listing.html` to add new filter UI elements
3. Add filter logic in the view function

## 🔧 Configuration

### Settings
Edit `settings.py` for:
- Database configuration
- Static files settings
- Allowed hosts
- Debug mode

### Static Files
In production, collect static files:
```bash
python manage.py collectstatic
```

## 🐛 Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic
```

### Database Errors
```bash
python manage.py makemigrations
python manage.py migrate
```

### Port Already in Use
```bash
python manage.py runserver 8080
```

## 📝 Models

### Hotels Model
```python
class Hotels(models.Model):
    place_name = models.CharField(max_length=100)
    property_type = models.CharField(max_length=50)
    property_name = models.CharField(max_length=200)
    bedroom_count = models.IntegerField()
    bathroom_count = models.IntegerField()
    guest_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    star_rating = models.IntegerField()
```

## 🚧 Future Enhancements

- [ ] User authentication and registration
- [ ] Booking system
- [ ] Payment gateway integration
- [ ] Review and rating system
- [ ] Wishlist functionality
- [ ] Email notifications
- [ ] Advanced search with date ranges
- [ ] Property owner dashboard
- [ ] Multi-language support
- [ ] Map integration
- [ ] Image gallery for properties

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Font Awesome for icons
- Django community for excellent documentation
- All contributors who help improve this project


