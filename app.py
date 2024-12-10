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

    if request.method == 'POST' and 'update_customer' in request.form:
        customer_id = request.form['customer_id']
        name = request.form['name']
        cursor.execute("UPDATE Customer SET Name = %s WHERE CustomerID = %s", (name, customer_id))
        conn.commit()

    if request.method == 'POST' and 'delete_customer' in request.form:
        customer_id = request.form['customer_id']
        cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))
        conn.commit()

    cursor.execute("SELECT * FROM Customer")
    customers = cursor.fetchall()
    conn.close()

    return render_template('customers.html', customers=customers)

# Route: Rental Management
@app.route('/rentals', methods=['GET', 'POST'])
def rentals():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

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

    if request.method == 'POST' and 'update_rental' in request.form:
        agreement_id = request.form['agreement_id']
        return_date = request.form['return_date']
        cursor.execute("UPDATE RentalAgreement SET ReturnDate = %s WHERE AgreementID = %s", 
                       (return_date, agreement_id))
        conn.commit()

    if request.method == 'POST' and 'delete_rental' in request.form:
        agreement_id = request.form['agreement_id']
        cursor.execute("DELETE FROM RentalAgreement WHERE AgreementID = %s", (agreement_id,))
        conn.commit()

    cursor.execute("SELECT * FROM RentalAgreement")
    rentals = cursor.fetchall()
    conn.close()

    return render_template('rentals.html', rentals=rentals)

# Route: Billing Management
@app.route('/billing', methods=['GET', 'POST'])
def billing():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST' and 'add_billing' in request.form:
        total_amount = request.form['total_amount']
        discount = request.form['discount_amount']
        tax = request.form['tax_amount']
        status = request.form['status']
        agreement_id = request.form['agreement_id']
        cursor.execute("INSERT INTO Billing (Total_Amount, Discount_Amount, Tax_Amount, Status, AgreementID) VALUES (%s, %s, %s, %s, %s)", 
                       (total_amount, discount, tax, status, agreement_id))
        conn.commit()

    if request.method == 'POST' and 'update_billing' in request.form:
        bill_id = request.form['bill_id']
        status = request.form['status']
        cursor.execute("UPDATE Billing SET Status = %s WHERE BillID = %s", 
                       (status, bill_id))
        conn.commit()

    if request.method == 'POST' and 'delete_billing' in request.form:
        bill_id = request.form['bill_id']
        cursor.execute("DELETE FROM Billing WHERE BillID = %s", (bill_id,))
        conn.commit()

    cursor.execute("SELECT * FROM Billing")
    bills = cursor.fetchall()
    conn.close()

    return render_template('billing.html', bills=bills)

# Route: Reservation Management
@app.route('/reservations', methods=['GET', 'POST'])
def reservations():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST' and 'add_reservation' in request.form:
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        car_class = request.form['car_class']
        status = request.form['status']
        customer_id = request.form['customer_id']
        cursor.execute("INSERT INTO Reservation (StartDate, EndDate, CarClass, Status, CustomerID) VALUES (%s, %s, %s, %s, %s)", 
                       (start_date, end_date, car_class, status, customer_id))
        conn.commit()

    if request.method == 'POST' and 'update_reservation' in request.form:
        reservation_id = request.form['reservation_id']
        status = request.form['status']
        cursor.execute("UPDATE Reservation SET Status = %s WHERE ReservationID = %s", 
                       (status, reservation_id))
        conn.commit()

    if request.method == 'POST' and 'delete_reservation' in request.form:
        reservation_id = request.form['reservation_id']
        cursor.execute("DELETE FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        conn.commit()

    cursor.execute("SELECT * FROM Reservation")
    reservations = cursor.fetchall()
    conn.close()

    return render_template('reservations.html', reservations=reservations)

# Route: Car Management
@app.route('/cars', methods=['GET', 'POST'])
def cars():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST' and 'add_car' in request.form:
        vin = request.form['vin']
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        car_class = request.form['class']
        daily_rate = request.form['daily_rate']
        weekly_rate = request.form['weekly_rate']
        branch_id = request.form['branch_id']
        cursor.execute("INSERT INTO Car (VIN, Make, Model, Year, Class, DailyRate, WeeklyRate, BranchID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       (vin, make, model, year, car_class, daily_rate, weekly_rate, branch_id))
        conn.commit()

    if request.method == 'POST' and 'update_car' in request.form:
        vin = request.form['vin']
        daily_rate = request.form['daily_rate']
        cursor.execute("UPDATE Car SET DailyRate = %s WHERE VIN = %s", 
                       (daily_rate, vin))
        conn.commit()

    if request.method == 'POST' and 'delete_car' in request.form:
        vin = request.form['vin']
        cursor.execute("DELETE FROM Car WHERE VIN = %s", (vin,))
        conn.commit()

    cursor.execute("SELECT * FROM Car")
    cars = cursor.fetchall()
    conn.close()

    return render_template('cars.html', cars=cars)

# Route: Car Availability
@app.route('/car_availability', methods=['GET', 'POST'])
def car_availability():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Filter cars by availability
    if request.method == 'POST' and 'check_availability' in request.form:
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        cursor.execute("""
            SELECT Car.VIN, Car.Make, Car.Model, Car.Year, Car.Class, Car.DailyRate, Car.WeeklyRate
            FROM Car
            LEFT JOIN RentalAgreement ON Car.VIN = RentalAgreement.VIN
            AND ((RentalAgreement.PickupDate BETWEEN %s AND %s)
            OR (RentalAgreement.ReturnDate BETWEEN %s AND %s))
            WHERE RentalAgreement.VIN IS NULL
        """, (start_date, end_date, start_date, end_date))
        available_cars = cursor.fetchall()
    else:
        # Default to show all cars
        cursor.execute("SELECT VIN, Make, Model, Year, Class, DailyRate, WeeklyRate FROM Car")
        available_cars = cursor.fetchall()

    conn.close()
    return render_template('car_availability.html', available_cars=available_cars)

# Route: Branch Management
@app.route('/branch', methods=['GET', 'POST'])
def branch():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Handle Create (Add Branch)
    if request.method == 'POST' and 'add_branch' in request.form:
        branch_id = request.form['branch_id']
        address = request.form['address']
        cursor.execute("INSERT INTO Branch (BranchID, Address) VALUES (%s, %s)", 
                       (branch_id, address))
        conn.commit()

    # Handle Update
    if request.method == 'POST' and 'update_branch' in request.form:
        branch_id = request.form['branch_id']
        address = request.form['address']
        cursor.execute("UPDATE Branch SET Address = %s WHERE BranchID = %s", 
                       (address, branch_id))
        conn.commit()

    # Handle Delete
    if request.method == 'POST' and 'delete_branch' in request.form:
        branch_id = request.form['branch_id']
        cursor.execute("DELETE FROM Branch WHERE BranchID = %s", (branch_id,))
        conn.commit()

    # Retrieve all branches
    cursor.execute("SELECT * FROM Branch")
    branches = cursor.fetchall()
    conn.close()

    return render_template('branch.html', branches=branches)


if __name__ == '__main__':
    app.run(debug=True)
