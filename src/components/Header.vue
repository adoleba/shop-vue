<template>
      <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-5 mb-3 bg-white border-bottom shadow-sm">
        <h5 class="my-0 mr-md-auto font-weight-normal">Shop name</h5>
        <nav class="my-2 my-md-0 mr-md-3">
          <router-link class="p-2 text-dark" :to="{ name: 'home' }">Home</router-link>
          <router-link class="p-2 text-dark" :to="{ name: 'about' }">About us</router-link>
          <router-link class="p-2 text-dark" :to="{ name: 'contact' }">Contact</router-link>
        </nav>
        <router-link class="btn btn-success rounded" :to="{ name: 'cart' }"><i class="bi-cart"></i> Cart ( {{totalCartQuantity}} )</router-link>
      </div>
</template>

<script>
import {Store} from "../store/store";

export default {
  name: "Header",
  computed: {
    totalCartQuantity() {
      return Store.state.cart.reduce((accum, product) => {
            return accum + product.quantity
        }, 0)
    }
  },
}
</script>

<style scoped>

</style>