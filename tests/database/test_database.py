import pytest
from modules.common.database import Database

# Debug test. Obtaining information about a database table
@pytest.mark.datab
def test_describe_table():
    table = 'invoices'
    db = Database()
    describes = db.test_query(table)
    print(describes)

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

# Test SELECT all customers from table customers
@pytest.mark.database
def test_check_all_customers():
    db = Database()
    customers = db.get_all_customers()
    assert customers[51][4] == '202 Hoxton Street'

# Test SELECT customer's address from table customers by name
@pytest.mark.database
def test_check_customer():
    name = 'Martha'
    db = Database()
    customer = db.get_customer_address(name)
    assert customer[0][1] == name
    assert customer[0][3] == '194A Chain Lake Drive'
    assert customer[0][4] == 'Halifax'
    assert customer[0][6] == 'Canada'

#Test SELECT all items from table invoice_items
@pytest.mark.database
def test_all_invoice_items():
    db = Database()
    items = db.get_invoice_items()
    assert items[2238][0] == 2239

#Test UPDATE field quantity in table invoice_items
@pytest.mark.database
def test_invoice_qnt_update():
    itemid = 2222
    qnt = 255
    db = Database()
    qnt_origin = db.select_invoice_quantity(itemid)[0][0]
    db.update_invoice_quantity(itemid, qnt)
    assert db.select_invoice_quantity(itemid)[0][0] == qnt
    db.update_invoice_quantity(itemid, qnt_origin)

#Test INSERT one more record in table invoices
@pytest.mark.database
def test_invoice_insert():
    db = Database() 
    invoice_id = db.select_count_table('invoices') + 1
    customer_id = 444
    date = '2024-06-07'
    address = 'Andii St., 2B'
    city = 'Kyiv'
    country = 'Ukraine'
    total = 99.99
    db.insert_invoice(invoice_id, customer_id, date, address, city, country, total)
    items = db.select_record_invoices(invoice_id)
    assert items[0][0] == invoice_id
    assert items[0][1] == customer_id
    assert items[0][2] == date
    assert items[0][3] == address
    assert items[0][4] == city
    assert items[0][6] == country
    assert items[0][8] == total
    db.delete_record_invoices(invoice_id)

#Test DELETE one record in table invoices
@pytest.mark.database
def test_invoice_delete():
    db = Database() 
    invoice_id = db.select_count_table('invoices') + 1
    customer_id = 444
    date = '2024-06-07'
    address = 'Andii St., 2B'
    city = 'Kyiv'
    country = 'Ukraine'
    total = 99.99
    db.insert_invoice(invoice_id, customer_id, date, address, city, country, total)
    db.delete_record_invoices(invoice_id)
    items = db.select_record_invoices(invoice_id)
    assert items == []
