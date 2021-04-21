export const Store = {
    cart: [],
    addToCart(product){
        const locationInCart = this.cart.findIndex(p => {
            return p.details.id === product.id
        })

        if (locationInCart === -1) {
            this.cart.push({
                details: product,
                quantity: 1
            })
            console.log('dupa dodana')
            console.log(this.cart.length)
        } else {
            this.cart[locationInCart].quantity++
        }
    },
}
