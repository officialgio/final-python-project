from sqlalchemy import create_engine, Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Waiter(Base):
    __tablename__ = "waiter"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    tax_number = Column(String)

class CustomerTicket(Base):
    __tablename__ = "customer_ticket"
    id = Column(Integer, primary_key=True)
    arrival = Column(DateTime, default=datetime.now)
    departed = Column(DateTime)
    table_id = Column(Integer)
    waiter_id = Column(Integer, ForeignKey("waiter.id"))
    waiter = relationship("Waiter", back_populates="customer_tickets")

class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    description = Column(String)
    price = Column(Numeric)

class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    menu_item_id = Column(Integer, ForeignKey("menu.id"))
    menu_item = relationship("Menu", back_populates="orders")
    customer_ticket_id = Column(Integer, ForeignKey("customer_ticket.id"))
    customer_ticket = relationship("CustomerTicket", back_populates="orders")

Waiter.customer_tickets = relationship("CustomerTicket", back_populates="waiter")
Menu.orders = relationship("Order", back_populates="menu_item")
CustomerTicket.orders = relationship("Order", back_populates="customer_ticket")
