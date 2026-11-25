from django.shortcuts import get_object_or_404


def by_pk(request, pk):
    # ruleid: robusta-py-idor-django-get-object
    invoice = Invoice.objects.get(pk=pk)
    return invoice


def by_id(request, pk):
    # ruleid: robusta-py-idor-django-get-object
    invoice = Invoice.objects.get(id=pk)
    return invoice


def by_filter(request, pk):
    # ruleid: robusta-py-idor-django-get-object
    invoice = Invoice.objects.filter(pk=pk).first()
    return invoice


def by_shortcut(request, pk):
    # ruleid: robusta-py-idor-django-get-object
    invoice = get_object_or_404(Invoice, pk=pk)
    return invoice


class InvoiceView(APIView):
    def get(self, request, pk):
        # ruleid: robusta-py-idor-django-get-object
        invoice = Invoice.objects.get(pk=pk)
        return Response(invoice)


def scoped(request, pk):
    # ok: robusta-py-idor-django-get-object
    invoice = Invoice.objects.get(pk=pk, owner=request.user)
    return invoice


def checked(request, pk):
    # ok: robusta-py-idor-django-get-object
    invoice = Invoice.objects.get(pk=pk)
    if invoice.owner != request.user:
        raise PermissionDenied
    return invoice


class CheckedView(APIView):
    def get(self, request, pk):
        # ok: robusta-py-idor-django-get-object
        invoice = Invoice.objects.get(pk=pk)
        self.check_object_permissions(request, invoice)
        return Response(invoice)


def cleanup_job(pk):
    # ok: robusta-py-idor-django-get-object
    invoice = Invoice.objects.get(pk=pk)
    invoice.delete()
