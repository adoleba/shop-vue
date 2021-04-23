import { reactive } from 'vue'

export const Store = {
    state: reactive({
        cart: [],
    }),
    addToCart(product){
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
        console.log(this.state.cart[0].quantity)
    },
    removeFromCart(id){
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.id === id
        })
            this.state.cart.splice(locationInCart, 1)
        console.log(locationInCart)
    }
}
