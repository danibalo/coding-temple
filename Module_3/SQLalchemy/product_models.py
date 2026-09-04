from sqlalchemy import create_engine, String
from sqlalchemy.orm import Mapped, DeclarativeBase, Session, mapped_column
from typing import Optional
engine = create_engine("sqlite:///product_catalog.db", echo=True)
class Base(DeclarativeBase):
    pass
class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False,unique=True)
    description: Mapped[Optional[str]] = mapped_column(String(200))
    def __repr__(self):
        return f"Category(id={self.id} name={self.name})"
class Product(Base):
    __tablename__ = "product"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    instock: Mapped[bool] = mapped_column(default=True)
    def __repr__(self):
        return f"Product(id={self.id},name={self.name},price={self.price},instock={self.instock})"
Base.metadata.create_all(engine)
print('Tables are created')

#INSERT DATA
with Session(engine) as session:
    categories = [
        Category(name="electronics", description="All electronics are in this category"),
        Category(name="Cleaners", description="All cleaners and detergents are in this category"),
        Category(name="Tools", description="All tools and kits are available in this category")]
    # session.add_all(categories)
    # session.commit()

    products = [Product(name="Samsung S20", price=999.9),
        Product(name="Monitor display", price=575),
        Product(name="HDMI cable", price=75, instock=False),
        Product(name="Tide", price=19),
        Product(name="Hydrolic Painter", price=255),
        Product(name="Dove", price=25)]
    # session.add_all(products)
    # session.commit()
    print("Datas are inserted")
    category = session.query(Category).all()
    for cat in category:
        print(f"{cat}")
    products = session.query(Product).all()
    for prod in products:
        print(f"{prod}")
    price_under_50 = session.query(Product).filter(Product.price < 50).all()
    for price in price_under_50:
        print(f"{price}")
    
