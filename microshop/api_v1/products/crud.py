from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from microshop.core.models import Product
from .schemas import ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(statement=stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, id: int) -> Product | None:
    return await session.get(Product, id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product: Product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product
