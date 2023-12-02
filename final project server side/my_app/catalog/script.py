from sqlalchemy.orm import sessionmaker
from my_app import db
from models import *

# Create a Session
Session = sessionmaker(bind=db.engine)
session = Session()

# Create Waiters
waiter1 = Waiter(first_name='John', last_name='Doe', tax_number='123')
waiter2 = Waiter(first_name='Jane', last_name='Smith', tax_number='456')

# Add Waiters to the session
session.add_all([waiter1, waiter2])
session.commit()

# Create Menu Items
menu_item1 = Menu(item_name='Burger', description='Delicious burger', price=10.99)
menu_item2 = Menu(item_name='Pizza', description='Margherita pizza', price=12.99)

# Add Menu Items to the session
session.add_all([menu_item1, menu_item2])
session.commit()

# Create Customer Ticket
customer_ticket = CustomerTicket(arrival='2023-01-01 12:00:00', departed='2023-01-01 13:30:00', table_id=1, waiter_id=1)

# Add Customer Ticket to the session
session.add(customer_ticket)
session.commit()

# Create Orders for the Customer Ticket
order1 = Order(customer_ticket_id=customer_ticket.id, menu_item_id=menu_item1.id, quantity=2)
order2 = Order(customer_ticket_id=customer_ticket.id, menu_item_id=menu_item2.id, quantity=1)

# Add Orders to the session
session.add_all([order1, order2])
session.commit()

# Close the session
session.close()