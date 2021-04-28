<template>
  <div class="container py-5">
    <div v-if="cart.cart.length>=1 ">
      <h3>Your cart</h3>

      <div class="row py-5">
        <div class="col-2 font-weight-bold">Product photo</div>
        <div class="col-3 font-weight-bold">Product name</div>
        <div class="col-2 font-weight-bold">Unit Price</div>
        <div class="col-2 font-weight-bold">Quantity</div>
        <div class="col-2 font-weight-bold">Value</div>
      </div>

      <div class="row pb-5" v-for="product in cart.cart" :key="product.details.id" :product="product">
        <div class="col-2 align-self-center"><img :src="getImgUrl(product.details.id)" v-bind:alt="product.name" /></div>
        <div class="col-3 align-self-center">
          <router-link class="card-text" :to="{ name: 'productDetail' , params: {id: product.details.id}}">
            {{ product.details.producer }} {{ product.details.name }}
          </router-link>
        </div>
        <div class="col-2 align-self-center">{{ product.details.price.toLocaleString().replace(',', ' ') }} zł</div>

        <div class="col-2 align-self-center">
          <i class="bi-dash" v-on:click="decreaseQuantity(product.details.id)" style="cursor: pointer"></i>
          <span class="border p-2 rounded">{{ product.quantity }}</span>
          <i class="bi-plus" v-on:click="increaseQuantity(product.details.id)" style="cursor: pointer"></i>
        </div>

        <div class="col-2 align-self-center">{{ (product.details.price * product.quantity).toLocaleString().replace(',', ' ') }} zł</div>
        <div class="col-1 align-self-center">
          <i class="bi-trash" v-on:click="removeFromCart(product.details.id)" style="cursor: pointer" title="Remove from cart"></i>
        </div>
      </div>

      <hr>

      <div class="row justify-content-end py-5">
        <div class="col-3  font-weight-bold">
          Total value:
        </div>
        <div class="col-3">
          {{totalCost.toLocaleString().replace(',', ' ')}} zł
        </div>
      </div>

      <div class="row py-5">
      <div class="col-10">
        <router-link class="btn btn-outline-secondary" :to="{ name: 'home' }">Continue shopping</router-link>
      </div>
      <div class="col-2">
        <router-link class="btn btn-success rounded btn-lg" :to="{ name: 'order' }">Checkout</router-link>
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
import {useToast} from "vue-toastification";

export default {
  name: "Cart",
  setup() {
    const toast = useToast();
      return {toast}
  },
  data() {
    return {
      cart: Store.state
    }
  },
  methods: {
    getImgUrl(id) {
      return require('../data/images/'+id+'.png')
    },
    removeFromCart(id){
      Store.removeFromCart(id)
      this.toast.error("Product was removed from cart", {
        timeout: 1500,
      });
    },
    increaseQuantity(product) {
      Store.increaseQuantity(product)
    },
    decreaseQuantity(product) {
      Store.decreaseQuantity(product)
    }
  },
  computed: {
    totalCost() {
      return Store.state.cart.reduce((accum, product) => {
            return accum + product.details.price * product.quantity
        }, 0)
    }
  },
}
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 100%;
}

</style>