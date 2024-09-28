function addProductToBasket(productId) {
    const productCount = $('#product_count').val();
    $.get('/cart/add-to-basket?product_id=' + productId + '&count=' + productCount).then(res => {
        Swal.fire({
            title: res.title,
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirmButtonText,
            allowOutsideClick: false
        }).then(confirm => {
            if (res.status === 'not_auth') {
                window.location.href = '/login'
            }
        }).then(confirm => {
            if (res.status === 'success') {
                window.location.href = '/basket'
            }
        });
    });
}

function removeProductFromBasket(detailId) {
    $.get('/remove-order?detail_id=' + detailId).then(res => {
        console.log(res);
    });
}