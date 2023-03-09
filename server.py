from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from new_booking import create_new_booking
from forms import MonthForm, BookingForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET_KEY"
Bootstrap(app)


# TODO: Read previous booking data, calculate availability, and load to page
# TODO: Add functionality to change displayed calendar month. MonthForm is a placeholder. Using a form should work...
#  but there is definitely a better way that doesn't involve reloading everything.
# TODO: Take form data from BookingForm and create a new booking
# TODO: load current month and year as default calendar and restrict options to next 12 months
@app.route('/', methods=["GET", "POST"])
def index():
    booking = BookingForm()
    month = MonthForm()
    calendar = [[day for day in range(7)] for week in range(7)]
    # Old code from new_booking when it was a script. Use in booking form.
    # email = input("email?: ")
    # date = input("first night?(yyyymmdd): ")
    # dur = int(input("how many nights?: "))
    # new_booking = {date: {"room06": [email, dur]}}
    return render_template("index.html", booking=booking, month=month, calendar=calendar)


if __name__ == "__main__":
    app.run(debug=True)
