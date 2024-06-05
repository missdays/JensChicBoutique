from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = request.session.get('wishlist', [])
    
    if product_id not in wishlist:
        wishlist.append(product_id)
        request.session['wishlist'] = wishlist

    return redirect('wishlist:view_wishlist')