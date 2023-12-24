from fastapi import APIRouter
from .products.views import router as products_router

router: APIRouter = APIRouter(tags=["API_V1"])
router.include_router(
    products_router,
    prefix="/api/v1/products",
)
