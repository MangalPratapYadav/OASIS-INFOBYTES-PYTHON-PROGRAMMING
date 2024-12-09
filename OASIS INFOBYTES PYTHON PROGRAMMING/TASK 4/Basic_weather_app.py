from tkinter import *
from tkinter import ttk
import requests

cities = [
    "Anantapur", "Chittoor", "East Godavari", "Ahmedabad", "Amreli", "Bharuch", "Kheda (Nadiad)", "Vadodara", "Valsad", "Surendranagar", 
    "Surat", "Rajkot", "Patan", "Navsari", "Narmada", "Morbi", "Mehsana", "Junagadh", "Jamnagar", "Gir Somnath", "Dahod", "Dang", 
    "Devbhoomi Dwarka", "Gandhinagar", "Botad", "Bhavn", "Bilaspur", "Chamba", "Hamirpur", "Kangra", "Kinnaur", "Kullu", "Lahaul and Spiti", 
    "Mandi", "Shimla", "Sirmaur", "Solan", "Una", "Bokaro", "Chatra", "Deoghar", "Dhanbad", "Dumka", "Garhwa", "Giridih", "Godda", "Gumla", 
    "Hazaribagh", "Jamtara", "Khunti", "Koderma", "Latehar", "Lohardaga", "Pakur", "Palamu", "Ramgarh", "Ranchi", "Sahibganj", 
    "Seraikela Kharsawan", "Simdega", "West Singhbhum", "Bagalkot", "Bangalore Rural", "Bangalore Urban", "Belgaum", "Bellary", "Bidar", 
    "Vijayapura", "Chamarajanagar", "Chikmagalur", "Chitradurga", "Dakshina Kannada", "Davanagere", "Dharwad", "Gadag", "Gulbarga", "Hassan", 
    "Haveri", "Kodagu", "Kolar", "Koppal", "Mandya", "Mysore", "Raichur", "Ramanagara", "Shimoga", "Tumkur", "Udupi", "Uttara Kannada", "Yadgir", 
    "Alappuzha", "Ernakulam", "Idukki", "Kannur", "Kasaragod", "Kollam", "Kottayam", "Kozhikode", "Malappuram", "Palakkad", "Pathanamthitta", 
    "Thiruvananthapuram", "Thrissur", "Wayanad", "Agar Malwa", "Alirajpur", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind", 
    "Bhopal", "Burhanpur", "Chhatarpur", "Chhindwara", "Damoh", "Datia", "Dewas", "Dhar", "Dindori", "Guna", "Gwalior", "Harda", "Hoshangabad", 
    "Indore", "Jabalpur", "Jhabua", "Katni", "Khandwa", "Khargone", "Mandla", "Mandsaur", "Morena", "Narsinghpur", "Neemuch", "Panna", "Raisen", 
    "Rajgarh", "Ratlam", "Rewa", "Sagar", "Satna", "Sehore", "Seoni", "Kota", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur", "Ajmer", 
    "Alwar", "Banswara", "Baran", "Barmer", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa", "Dholpur", "Dungarpur", 
    "Hanumangarh", "Jaipur", "Jaisalmer", "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Nagaur", "Pali", "Pratapgarh", "Rajsamand", 
    "Sawai Madhopur", "Sikar", "Sirohi", "Sri Ganganagar", "Tonk", "Udaipur", "East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim", 
    "Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kallakurichi", "Kanchipuram", 
    "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai", "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai", 
    "Ramanathapuram", "Ranipet", "Salem", "Sivaganga", "Tenkasi", "Thanjavur", "Theni", "Thoothukudi", "Tiruchirappalli", "Tirunelveli", 
    "Tirupattur", "Tiruppur", "Tiruvallur", "Tiruvannamalai", "Vellore", "Viluppuram", "Virudhunagar", "Dhalai", "Gomati", "Khowai", 
    "North Tripura", "Sepahijala", "South Tripura", "Unakoti", "West Tripura", "Agra", "Aligarh", "Ambedkar Nagar", "Amethi", "Amroha", "Auraiya", 
    "Ayodhya", "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Balrampur", "Banda", "Barabanki", "Bareilly", "Basti", "Bhadohi", "Bijnor", "Budaun", 
    "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria", "Etah", "Etawah", "Farrukhabad", "Fatehpur", "Firozabad", "Gautam Buddha Nagar", 
    "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur", "Hapur", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj", 
    "Kanpur Dehat", "Kanpur Nagar", "Kasganj", "Kaushambi", "Kushinagar", "Lakhimpur Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", 
    "Mainpuri", "Mathura", "Mau", "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "Prayagraj", "Raebareli", 
    "Rampur", "Saharanpur", "Sambhal", "Sant Kabir Nagar", "Shahjahanpur", "Shamli", "Shravasti", "Siddharthnagar", "Sitapur", "Sonbhadra", 
    "Sultanpur", "Unnao", "Varanasi", "Almora", "Bageshwar", "Chamoli", "Champawat", "Dehradun", "Haridwar", "Nainital", "Pauri Garhwal", 
    "Pithoragarh", "Rudraprayag", "Tehri Garhwal", "Udham Singh Nagar", "Uttarkashi", "Alipurduar", "Bankura", "Birbhum", "Cooch Behar", 
    "Dakshin Dinajpur", "Darjeeling", "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Kalimpong", "Kolkata", "Malda", "Murshidabad", "Nadia", 
    "North 24 Parganas", "Paschim Bardhaman", "Paschim Medinipur", "Purba Bardhaman", "Purba Medinipur", "Purulia", "South 24 Parganas", 
    "Uttar Dinajpur", "Nicobar", "North and Middle Andaman", "South Andaman", "Chandigarh", "Dadra and Nagar Haveli", "Daman", "Diu", "Lakshadweep", 
    "Kargil", "Leh", "Central Delhi", "East Delhi", "New Delhi", "North Delhi", "North East Delhi", "North West Delhi", "Shahdara", "South Delhi", 
    "South East Delhi", "South West Delhi", "West Delhi"
]
def filter_cities(event):
    typed_text = com.get().lower()
    matching_cities = [city for city in cities if typed_text in city.lower()]
    if not matching_cities:  # Display a message when no matches found
        matching_cities = ["No matching cities found"]
    com['values'] = matching_cities

def get_weather():
    city = com.get()
    if city == "No matching cities found":
        result_label.config(text="Please select a valid city from the list.")
        return
    api_key = '253682c0bd759acfb4255d4aa08c3dd7'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        country_code = data['sys']['country']
        city_with_country = f"{city}, {country_code}"
        
        result_label.config(text=f"City: {city_with_country}\n\nTemperature: {temperature_celsius:.2f} °C / {temperature_fahrenheit:.2f} °F\nHumidity: {humidity}%\nWeather Condition: {weather_condition}\nWind Speed: {wind_speed} m/s\nPressure: {pressure} hPa")
    except requests.exceptions.RequestException as e:
        result_label.config(text=f"Error: {e}")
    except KeyError as e:
        result_label.config(text="Error: Data format incorrect, please try again.")

def clear_search():
    com.set("")
    result_label.config(text="")

# GUI setup
win = Tk()
win.title("Weather App")
win.config(bg="#e3f2fd")  # Light blue background
win.geometry("750x500")  # Larger window size

# Add title label
name_label = Label(win, text="Weather App", font=("Arial", 36, "bold"), fg="#0288d1", bg="#e3f2fd")
name_label.place(x=180, y=20)

# Combobox for city selection with a scrollbar
com = ttk.Combobox(win, values=cities, font=("Arial", 12), width=40, state="normal")
com.place(x=180, y=100)
com.bind("<KeyRelease>", filter_cities)

# Button to trigger weather information retrieval
done_button = Button(win, text="Get Weather", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=get_weather)
done_button.place(x=290, y=200)

# Clear button to reset search
clear_button = Button(win, text="Clear Search", font=("Arial", 12, "bold"), bg="#0288d1", fg="white", command=clear_search)
clear_button.place(x=180, y=250)

# Label to display results
result_label = Label(win, text="", font=("Arial", 12), wraplength=600, justify="left", bg="#e3f2fd", fg="#0288d1")
result_label.place(x=50, y=300)

win.mainloop()