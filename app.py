from flask import Flask, render_template, request, redirect
import mysql.connector
from db_config import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Route: Customer Management
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Handle Create (Add Customer)
    if request.method == 'POST' and 'add_customer' in request.form:
        name = request.form['name']
        gender = request.form['gender']
        occupation = request.form['occupation']
        dob = request.form['dob']
        address = request.form['address']
        email = request.form['email']
        cursor.execute("INSERT INTO Customer (Name, Gender, Occupation, DOB, Address, Email) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (name, gender, occupation, dob, address, email))
        conn.commit()

    # Handle Update
    if request.method == 'POST' and 'update_customer' in request.form:
        customer_id = request.form['customer_id']
        name = request.form['name']
        cursor.execute("UPDATE Customer SET Name = %s WHERE CustomerID = %s", (name, customer_id))
        conn.commit()

    # Handle Delete
    if request.method == 'POST' and 'delete_customer' in request.form:
        customer_id = request.form['customer_id']
        cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))
        conn.commit()

    # Retrieve all customers
    cursor.execute("SELECT * FROM Customer")
    customers = cursor.fetchall()
    conn.close()

    return render_template('customers.html', customers=customers)

# Route: Rental Agreements
@app.route('/rentals', methods=['GET', 'POST'])
def rentals():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Handle Create (Add Rental Agreement)
    if request.method == 'POST' and 'add_rental' in request.form:
        customer_id = request.form['customer_id']
        vin = request.form['vin']
        reservation_id = request.form['reservation_id']
        pickup_date = request.form['pickup_date']
        return_date = request.form['return_date']
        rental_cost = request.form['rental_cost']
        cursor.execute("INSERT INTO RentalAgreement (CustomerID, VIN, ReservationID, PickupDate, ReturnDate, RentalCost) VALUES (%s, %s, %s, %s, %s, %s)", 
                       (customer_id, vin, reservation_id, pickup_date, return_date, rental_cost))
        conn.commit()

    # Handle Update
    if request.method == 'POST' and 'update_rental' in request.form:
        agreement_id = request.form['agreement_id']
        return_date = request.form['return_date']
        cursor.execute("UPDATE RentalAgreement SET ReturnDate = %s WHERE AgreementID = %s", 
                       (return_date, agreement_id))
        conn.commit()

    # Handle Delete
    if request.method == 'POST' and 'delete_rental' in request.form:
        agreement_id = request.form['agreement_id']
        cursor.execute("DELETE FROM RentalAgreement WHERE AgreementID = %s", (agreement_id,))
        conn.commit()

    # Retrieve all rental agreements
    cursor.execute("SELECT * FROM RentalAgreement")
    rentals = cursor.fetchall()
    conn.close()

    return render_template('rentals.html', rentals=rentals)

# Route: Billing Management
@app.route('/billing', methods=['GET', 'POST'])
def billing():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Handle Create (Add Billing)
    if request.method == 'POST' and 'add_billing' in request.form:
        total_amount = request.form['total_Amount']
        discount = request.form['discount_amount']
        tax = request.form['tax_amount']
        status = request.form['Status']
        agreement_id = request.form['agreement_id']
        cursor.execute("INSERT INTO Billing (Total_Amount, Discount_Amount, Tax_Amount, Status, AgreementID) VALUES (%s, %s, %s, %s, %s)", 
               (total_amount, discount, tax, status, agreement_id))

        conn.commit()

    # Handle Update
    if request.method == 'POST' and 'update_billing' in request.form:
        bill_id = request.form['bill_id']
        status = request.form['status']
        cursor.execute("UPDATE Billing SET Status = %s WHERE BillID = %s", 
                       (status, bill_id))
        conn.commit()

    # Handle Delete
    if request.method == 'POST' and 'delete_billing' in request.form:
        bill_id = request.form['bill_id']
        cursor.execute("DELETE FROM Billing WHERE BillID = %s", (bill_id,))
        conn.commit()

    # Retrieve all bills
    cursor.execute("SELECT * FROM Billing")
    bills = cursor.fetchall()
    conn.close()

    return render_template('billing.html', bills=bills)

if __name__ == '__main__':
    app.run(debug=True)
