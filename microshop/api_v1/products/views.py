from fastapi import APIRouter, Path, HTTPException, status, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import ProductCreate, Product
from microshop.core.models import db_helper
from . import crud

router: APIRouter = APIRouter()


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product_id: Annotated[int, Path(ge=1, lt=1_000_000)],
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    product = await crud.get_product(session=session, id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product (ID: {product_id}) not found.",
    )
