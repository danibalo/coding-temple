from sqlalchemy import create_engine,String
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column, Mapped
from typing import Optional
from datetime import datetime
engine = create_engine("sqlite:///contacts.db", echo=False)
class Base(DeclarativeBase):
    pass
class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    phone: Mapped[Optional[str]] = mapped_column(String(10))
    favorite: Mapped[bool] = mapped_column(default=False)
    def __repr__(self):
        return f"name: {self.first_name} {self.last_name}, email= {self.email} phone:{self.phone} favorite: {self.favorite}"
Base.metadata.create_all(engine)
def add_contact(first_name, last_name, email, phone=None):
    with Session(engine) as session:
        contact  = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone)
        session.add(contact)
        session.commit()
        session.refresh(contact)
        print(f"Created: {contact} (id = {contact.id})")
# print("\n ====Creating Contact====")
# add_contact("David", "James", "david24@gmail.com", "4088990500")
# add_contact("James","Susan","jamessus@yahoo.com", "2024567888")
# add_contact("Jessica", "Young", "jessiYo@gmail.com","2024567899")
# add_contact("Hames", "Rodregioz","hamesjesi@gmail.com","2025674400")
def list_contacts():
    with Session(engine) as session:
        return session.query(Contact).order_by(Contact.last_name).all()
def find_contact(email):
    with Session(engine) as session:
        return session.query(Contact).filter_by(email=email).first()
def update_phone(email, new_phone):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).first()
        if contact is None:
            print(f"Contact with email{email} not found!")
            return
        contact.phone = new_phone
        session.commit()
        print(f" Phone changed : {contact}")
def toggle_favorite(email):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).first()
        if contact is None:
            print(f" Contact not found")
            return
        contact.favorite = not contact.favorite
        session.commit()
        print(f"Favorite status changed: {contact.favorite}")
def delete_contact(email):
    with Session(engine) as session:
        contact = session.query(Contact).filter_by(email=email).first()
        if contact is None:
            print(f" Contact not found")
            return
        session.delete(contact)
        session.commit()
        print(f"Contact with email {email} is deleted")
print("==== Contact List ====")
for contact in list_contacts():
    print(f"{contact}")
print("==== Finding contact with email address ===")
print(find_contact("david24@gmail.com"))
print("===Phone Change==")
update_phone("hamesjesi@gmail.com", "4335679900" )
print("===Toggle Favorite===")
toggle_favorite("jamessus@yahoo.com")
print("====remove contact===")
delete_contact("jessiYo@gmail.com")
for contact in list_contacts():
    print(f"{contact}")



