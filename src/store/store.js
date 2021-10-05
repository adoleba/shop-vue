import { reactive } from 'vue'
import axios from "axios";

export const Store = {
    state: reactive({
        cart: [],
        shippingData: [],
        deliveryMethod: '',
        deliveryCost: 0,
        totalCost: '',
        invoice: false,
        termsAccepted: false,
        marketingAccepted: false,
        products: [],
    }),
    addToCart(product, addedQuantity=1) {
        if (JSON.parse(localStorage.getItem('cart')) === null) {
            this.state.cart = []
        } else {
            this.state.cart = JSON.parse(localStorage.getItem('cart'))
        }
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.product_id === product.product_id
        })

        if (locationInCart === -1) {
            this.state.cart.push({
                details: product,
                quantity: +addedQuantity
            })
        } else {
            this.state.cart[locationInCart].quantity += +addedQuantity
        }
        localStorage.setItem('cart', JSON.stringify(Store.state.cart))

    },
    removeFromCart(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.product_id === id
        })
        this.state.cart.splice(locationInCart, 1)
    },
    clearCart() {
        this.state.cart.push({
                details: [],
                quantity: 0
            });
        this.state = reactive({
            cart: [],
            shippingData: [],
            deliveryMethod: '',
            deliveryCost: 0,
            totalCost: '',
            invoice: false,
            termsAccepted: false,
            marketingAccepted: false,
      });
    },
    increaseQuantity(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.product_id === id
        })
        this.state.cart[locationInCart].quantity++
    },
    decreaseQuantity(id) {
        const locationInCart = this.state.cart.findIndex(p => {
            return p.details.product_id === id
        })
        if (this.state.cart[locationInCart].quantity===1) {
            this.state.cart.splice(locationInCart, 1)
        } else {
            this.state.cart[locationInCart].quantity--
        }
    },
    productsValue() {
      return Store.state.cart.reduce((accum, product) => {
            return accum + product.details.price * product.quantity
        }, 0)
    },
    totalCartQuantity() {
        if (localStorage.getItem('cart') === null) {
            return 0
        } else {
            const localStorageAsObject = JSON.parse(localStorage.getItem('cart'));
            return localStorageAsObject.reduce((accum, product) => {
                return accum + product.quantity;
                }, 0);
        }
    },
    async getProductsFromApi() {
        const response = await axios.get('http://localhost:8000/api/products/');
        Store.state.products = response.data;
        return response.data;
        },

}
