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
    },
    increaseQuantity(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === id
        })
        this.state.cart[locationInCart].quantity++
    },
    decreaseQuantity(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === id
        })
        if (this.state.cart[locationInCart].quantity===1) {
            this.state.cart.splice(locationInCart, 1)
        } else {
            this.state.cart[locationInCart].quantity--
        }
    }
}
