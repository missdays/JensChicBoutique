from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def view_wishlist(request):
    wishlist = request.session.get('wishlist', [])
    wishlist_items = Product.objects.filter(id__in=wishlist)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = request.session.get('wishlist', [])
    
    if product_id not in wishlist:
        wishlist.append(product_id)
        request.session['wishlist'] = wishlist

    return redirect('wishlist:view_wishlist')