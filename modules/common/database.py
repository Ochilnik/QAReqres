import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/mnt/d/My_Projects/Python/QAReqres' + r'/chinook.db')
        self.cursor = self.connection.cursor()


    def test_query(self):
        query = "PRAGMA table_info(invoice_items)"
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

