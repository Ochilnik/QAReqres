import pytest
from modules.common.database import Database

@pytest.mark.dbquery
def test_database_query():
    db = Database()
    print(db.test_query())

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_customers():
    db = Database()
    customers = db.get_all_customers()
    assert customers[51][4] == '202 Hoxton Street'

@pytest.mark.database
def test_check_customer():
    name = 'Martha'
    db = Database()
    customer = db.get_customer_address(name)
#    print(customer[0][1])
    assert customer[0][1] == name
    assert customer[0][3] == '194A Chain Lake Drive'
    assert customer[0][4] == 'Halifax'
    assert customer[0][6] == 'Canada'

@pytest.mark.database
def test_all_invoice_items():
    db = Database()
    items = db.get_invoice_items()
    assert items[2238][0] == 2239

@pytest.mark.database
def test_invoice_qnt_update():
    itemid = 22
    qnt = 25
    db = Database()
    db.update_invoice_quantity(itemid, qnt)
    assert db.select_invoice_quantity(itemid)[0][0] == 25

