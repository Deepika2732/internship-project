import requests
import smtplib

def umbrellaReminder():
    city = "kodad"
    print(f"Fetching weather info from wttr.in for {city}...")

    try:
        # Using wttr.in (no API key needed)
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url)
        weather_info = response.text.strip()
        
        print(f"🌤️ Weather Info: {weather_info}")

        # Extract the full weather condition
        weather_condition = weather_info.split('+')[0].strip()

        # Check if reminder is needed
        if weather_condition in ["Rain", "Showers", "Drizzle", "Thunderstorm", "Cloudy", "Overcast", "Partly cloudy"]:
            smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_object.starttls()
            
            # Log in with your Gmail and App Password
            smtp_object.login("deepthiramabommakanti@gmail.com", "gthw krnr vawc cjkt")

            subject = "🌧️ Umbrella Reminder"
            body = f"Weather in {city} is {weather_info}.\nDon't forget your umbrella!"
            message = f"Subject: {subject}\n\n{body}".encode('utf-8')

            # Send the email
            smtp_object.sendmail("deepthiramabommakanti@gmail.com", "aakanksha.kandibanda@gmail.com", message)
            smtp_object.quit()
            print("✅ Email sent!")
        else:
            print("🌞 Weather is clear. No umbrella needed.")

    except Exception as e:
        print("⚠️ Something went wrong:", e)

umbrellaReminder()
