import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/mnt/DATA/My_Projects/Python/QAReqres' + r'/chinook.db')
        self.cursor = self.connection.cursor()


    def test_query(self, table):
        query = f"PRAGMA table_info('{table}')"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record        
    
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_customers(self):
        query = "SELECT customerid, FirstName, LastName, Company, Address, \
            City, State, Country FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_customer_address(self, name):
        query = f"SELECT customerid, FirstName, LastName, Address, \
            City, State, Country FROM customers WHERE FirstName = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_invoice_items(self):
        query = "SELECT * FROM invoice_items"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    def update_invoice_quantity(self, id, qnt):
        query = f"UPDATE invoice_items SET Quantity = {qnt} WHERE InvoiceLineId = {id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_invoice_quantity(self, id):
        query = f"SELECT Quantity FROM invoice_items WHERE InvoiceLineId = {id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_invoice(self, invoice_id, customer_id, invoice_date, billing_address, \
                       billing_city):
        query = f"INSERT OR REPLACE INTO invoices (invoiceid, customerid, \
              invoicedate, billingaddress, billingcity) \
            VALUES ({invoice_id}, {customer_id}, '{invoice_date}', '{billing_address}', \
                '{billing_city}')"
        self.cursor.execute(query)
        self.connection.commit()

    def select_invoice(self, invoice_id):
        query = f"SELECT * FROM invoices WHERE invoiceid = '{invoice_id}'"
        self.cursor.execute(query)
        self.connection.commit()