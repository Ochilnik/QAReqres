import pytest
from modules.common.database import Database

#Debug test. Obtaining information about a database table
@pytest.mark.detab
def test_describe_table():
    table = 'invoices'
    db = Database()
    describes = db.test_query(table)
    print(describes)

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

#Test for check SELECT all customers from table customers
@pytest.mark.database
def test_check_all_customers():
    db = Database()
    customers = db.get_all_customers()
    assert customers[51][4] == '202 Hoxton Street'

#Test for check SELECT customer's address from table customers
@pytest.mark.database
def test_check_customer():
    name = 'Martha'
    db = Database()
    customer = db.get_customer_address(name)
    assert customer[0][1] == name
    assert customer[0][3] == '194A Chain Lake Drive'
    assert customer[0][4] == 'Halifax'
    assert customer[0][6] == 'Canada'

#Test for check SELECT all items from table invoice_items
@pytest.mark.database
def test_all_invoice_items():
    db = Database()
    items = db.get_invoice_items()
    assert items[2238][0] == 2239

#Test for check UPDATE field quantity table invoice_items
@pytest.mark.database
def test_invoice_qnt_update():
    itemid = 2222
    qnt = 255
    db = Database()
    qnt_origin = db.select_invoice_quantity(itemid)[0][0]
    db.update_invoice_quantity(itemid, qnt)
    assert db.select_invoice_quantity(itemid)[0][0] == qnt
    db.update_invoice_quantity(itemid, qnt_origin)

#Test
@pytest.mark.database
def test_invoice_insert():
    invoice_id = 2222
    customer_id = 222
    date = '2024-06-06'
    address = 'Baker St. 2B'
    city = 'London'
    db = Database()
    db.insert_invoice(invoice_id, customer_id, date, address, city)
    print(db.select_invoice(invoice_id))
    #assert water_qnt[0][0] == 30

