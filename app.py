from flask import Flask, render_template, request

from datetime import date, timedelta
from weather import get_city_weather


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():

    if request.method == 'POST':

        city_name = request.form.get('city_name')

        todays_date = date.today().strftime("%Y-%m-%d")
        seven_days_later = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")


        weather_data = get_city_weather(city_name, todays_date, seven_days_later)
        # weather_data = get_city_weather(city_name=city_name)
        found_city = True if weather_data is not None else False

        return render_template('weather.html', weather_data=weather_data, found_city=found_city)

    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)