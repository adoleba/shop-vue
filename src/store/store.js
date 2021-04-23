import { reactive } from 'vue'

export const Store = {
    state: reactive({
        cart: [],
    }),
    addToCart(product) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === product.id
        })

        if (locationInCart === -1) {
            this.state.cart.push({
                details: product,
                id: product.id,
                quantity: 1
            })
        } else {
            this.state.cart[locationInCart].quantity++
        }
    },
    removeFromCart(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === id
        })
        this.state.cart.splice(locationInCart, 1)
        console.log(locationInCart)
    },
    increaseQuantity(product) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === product.id
        })
        this.state.cart[locationInCart].quantity++
    },
    decreaseQuantity(product) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === product.id
        })
        this.state.cart[locationInCart].quantity--
    }
}
