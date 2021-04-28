import { reactive } from 'vue'

export const Store = {
    state: reactive({
        cart: [],
    }),
    addToCart(product, addedQuantity=1) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === product.id
        })
        console.log(addedQuantity)
        if (locationInCart === -1) {
            this.state.cart.push({
                details: product,
                quantity: +addedQuantity
            })
        } else {
            this.state.cart[locationInCart].quantity += +addedQuantity
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
