from django.shortcuts import render


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)

