from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, CartOrder, ProductImages, ProductReview, Wishlist, Address


def default(request):
    
    categories = Category.objects.all()
    # address = Address.objects.get(user=request.user)
     
    
    
    return{
        'categories': categories,
        # 'address': address,
    }