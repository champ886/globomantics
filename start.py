
from flask import Flask, render_template, request
from database import Database 


# Create flask object and instantiate database object
app = Flask(__name__)

# Path to database (db.json)
#path = "/home/vagrant/globomantics/db.json"
#path = "/home/vagrant/globomantics/db.yml"
path = "/home/vagrant/globomantics/db.xml"
db = Database(path) 


@app.route("/", methods=["GET", "POST"])
def index():
    """
    This is a view function which responds to requests for the top-level
    URL. It serves as the "Controller" in MVC as it accesses both the 
    model and the view
    """

    # The button click within the view kicks off a POST request ...
    if request.method == "POST":

        # This collects the user input from the view. The controller's
        #job is to process this info, which includes using methods from
        # the "model" to get the information we need (in this case,
        # The acount balance).
        acct_id = request.form["acctid"]
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"balance for {acct_id}: {acct_balance}")

    else:
        # During a normal GET request, no need to perform any calculations
        acct_balance ="N/A"

    # This is the "view", which is jinja2 templated HTML data that is
    # presented to the user. The user interacts with this webpage and provides
    # information that the controller then processes.
    # The controller passes the account balance into the view so it can
    # be displayed back to the user.
    return render_template("index.html", acct_balance=acct_balance)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)