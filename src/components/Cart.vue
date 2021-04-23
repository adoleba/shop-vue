<template>
  <div class="container py-5">
    <div v-if="cart.cart.length>=1 ">
      <h3>Your cart</h3>

      <div class="row py-5">
        <div class="col-2 font-weight-bold">Product photo</div>
        <div class="col-4 font-weight-bold">Product name</div>
        <div class="col-2 font-weight-bold">Unit Price</div>
        <div class="col-2 font-weight-bold">Quantity</div>
        <div class="col-2 font-weight-bold">Value</div>
      </div>

      <div class="row pb-5" v-for="product in cart.cart" :key="product">
        <div class="col-2 align-self-center"><img :src="getImgUrl(product.details.id)" v-bind:alt="product.name" /></div>
        <div class="col-4 align-self-center">{{ product.details.producer }} {{ product.details.name }}</div>
        <div class="col-2 align-self-center">{{ product.details.price }} zł</div>
        <div class="col-2 align-self-center">{{ product.quantity }}</div>
        <div class="col-2 align-self-center">{{ product.details.price * product.quantity }} zł</div>
      </div>

      <hr>

      <div class="row justify-content-end py-5">
        <div class="col-2  font-weight-bold">
          Total value:
        </div>
        <div class="col-2">
          {{totalCost}} zł
        </div>
      </div>

      <div class="row py-5">
      <div class="col-10">
        <router-link class="btn btn-outline-secondary" :to="{ name: 'home' }">Continue shopping</router-link>
      </div>
      <div class="col-2">
        <button class="btn btn-success rounded btn-lg">Checkout</button>
      </div>
      </div>
    </div>

    <div v-else>
      <div class="container py-5 my-2 text-center">
        <h3 class="pb-5 mt-5">Your cart is empty</h3>
        <router-link class="btn btn-success rounded btn-lg" :to="{ name: 'home' }">Go to shopping</router-link>

        <h4 class="py-5 my-5">You can also read <router-link class="font-weight-bold" :to="{ name: 'about' }">about us</router-link>
          or <router-link class="font-weight-bold" :to="{ name: 'contact' }">contact us</router-link></h4>
      </div>
    </div>
  </div>
</template>

<script>
import {Store} from "../store/store";

export default {
  name: "Cart",
  data() {
    return {
      cart: Store.state
    }
  },
  methods: {
    getImgUrl(id) {
      return require('../data/images/'+id+'.png')
    },
  },
  computed: {
    totalCost() {
      return Store.state.cart.reduce((accum, product) => {
            return accum + product.details.price * product.quantity
        }, 0)
    }
  }

}
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 100%;
}

</style>