# **NDVI Prediction App**

## **Project Overview**

The **NDVI Prediction App** is designed to enhance agricultural productivity by providing farmers with real-time NDVI (Normalized Difference Vegetation Index) data of their farms. The app allows users to register farms, view NDVI analysis for their crops, and make data-driven decisions to improve crop health. Additionally, it integrates weather information to help users manage their fields more effectively.

### **Features**
- **User Registration & Authentication**: Farmers can sign up, log in, and manage their farm data.
- **Farm Management**: Users can register farms, add farm details, and track farm-related NDVI readings.
- **NDVI Analysis**: Provides NDVI values and images for different dates, helping farmers monitor the health of their crops.
- **Weather Integration**: Displays real-time weather data relevant to the farm location.
- **Interactive Map**: Visualizes farms on a map using **Leaflet.js**, with NDVI values shown for each farm.

---

## **Tech Stack**
- **Backend**: Django, Django REST Framework (DRF)
- **Frontend**: HTML, CSS, JavaScript (integrated with Django templates)
- **Database**: PostgreSQL (or SQLite for local development)
- **Map Integration**: Leaflet.js for displaying farm locations and NDVI data on an interactive map.
- **APIs**:
  - **Sentinel Hub**: For retrieving NDVI data based on farm location.
  - **Weather API**: To fetch real-time weather information.

---

## **Setup and Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/ndvi-prediction-app.git
cd ndvi-prediction-app
```

### **2. Create a Virtual Environment and Install Dependencies**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### **3. Configure Environment Variables**

Create a `.env` file in the project’s root directory and add the following:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=your_database_url
SENTINEL_API_KEY=your_sentinel_hub_api_key
WEATHER_API_KEY=your_weather_api_key
```

### **4. Apply Migrations**

```bash
python manage.py migrate
```

### **5. Run the Development Server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## **API Endpoints**

- **/api/register/**: User registration
- **/api/login/**: User login
- **/api/farms/**: Manage farms (GET, POST, PUT, DELETE)
- **/api/ndvi/**: View NDVI analysis for farms
- **/api/weather/**: Get real-time weather data for a farm

---

## **Models**

### **1. User**
The app uses Django’s built-in `User` model for user authentication and management.

### **2. Farm**
```python
class Farm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='farms')
    name = models.CharField(max_length=255)
    location = models.PointField()  # Store geographical data
    size = models.FloatField()  # Farm size in hectares
```

### **3. NDVI Analysis**
```python
class NDVIAnalysis(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='ndvi_readings')
    ndvi_value = models.FloatField()
    ndvi_image = models.ImageField(upload_to='ndvi_images/')
    analysis_date = models.DateTimeField(default=datetime.now)
```

---

## **How to Contribute**

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b my-feature-branch`.
3. Make your changes and commit: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## **Contact**

If you have any questions or need further assistance, please reach out to the project maintainers:

- [Suman Malla] - Project Lead
- Email: mallasuman041@gmail.com

---

This `README.md` provides the basic structure of the project, its setup, and how developers can get started with it. Make sure to replace placeholders like `your-username` and `your-email@example.com` with your actual information before pushing it to GitHub.
