import sqlite3


class Database():
    
    # Connect to database chinook.db
    def __init__(self):
        self.connection = sqlite3.connect(r'/mnt/DATA/My_Projects/Python/QAReqres' + r'/chinook.db')
        self.cursor = self.connection.cursor()

    # Fetch structure of table
    def test_query(self, table):
        query = f"PRAGMA table_info('{table}')"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record        
    
    # Print SQLite version
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")
        return

    # Get selected coloumns in all records from tables customers
    def get_all_customers(self):
        query = "SELECT customerid, FirstName, LastName, Company, Address, \
            City, State, Country FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # Get address in records by FirstName from tables customers
    def get_customer_address(self, name):
        query = f"SELECT customerid, FirstName, LastName, Address, \
            City, State, Country FROM customers WHERE FirstName = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    # Get all coloumns in all records from tables invoice_items
    def get_invoice_items(self):
        query = "SELECT * FROM invoice_items"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    # UPDATE Quantity in table invoice_items by InvoiceLineId
    def update_invoice_quantity(self, id, qnt):
        query = f"UPDATE invoice_items SET Quantity = {qnt} WHERE InvoiceLineId = {id}"
        self.cursor.execute(query)
        self.connection.commit()
        return
    
    # SELECT Quantity from table invoice_items by InvoiceLineId
    def select_invoice_quantity(self, id):
        query = f"SELECT Quantity FROM invoice_items WHERE InvoiceLineId = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # INSERT / REPLACE a record in invoices table by InvoiceId
    def insert_invoice(self, invoice_id, customer_id, invoice_date, billing_address, \
                       billing_city, country, total):
        query = f"INSERT OR REPLACE INTO invoices (InvoiceId, CustomerId, \
              InvoiceDate, BillingAddress, BillingCity, BillingCountry, Total) \
            VALUES ({invoice_id}, {customer_id}, '{invoice_date}', '{billing_address}', \
                '{billing_city}', '{country}', {total})"
        self.cursor.execute(query)
        self.connection.commit()
        return
    
    # Get the number of entries in the table
    def select_count_table(self, table):
        query = f"SELECT count(*) FROM '{table}';"
        self.cursor.execute(query)
        count = self.cursor.fetchall()
        return count[0][0]
    
    # Retrieve a record from the invoice table by InvoiceId
    def select_record_invoices(self, id):
        query = f"SELECT * FROM invoices WHERE InvoiceId = '{id}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    # DELETE a record from the invoice table by InvoiceId
    def delete_record_invoices(self, id):
        query = f"DELETE FROM invoices WHERE InvoiceId ='{id}'"
        self.cursor.execute(query)
        self.connection.commit()
        return
    
