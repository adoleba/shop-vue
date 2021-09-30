<template>
  <div class="container py-1 py-md-5">
    <div v-if="cart.cart.length>=1 ">
      <h3>Your cart</h3>

      <div class="row py-2 py-md-5">
        <div class="col-2 d-none d-md-block font-weight-bold">Product photo</div>
        <div class="col-3 d-none d-md-block font-weight-bold">Product name</div>
        <div class="col-2 d-none d-md-block font-weight-bold">Unit Price</div>
        <div class="col-2 d-none d-md-block font-weight-bold">Quantity</div>
        <div class="col-2 d-none d-md-block font-weight-bold">Value</div>
      </div>

      <div class="row pb-5" v-for="product in cart.cart" :key="product.details.id" :product="product">

        <div class="d-md-none">
          <div class="row">
            <div class="col-6 align-self-center">
              <img :src="getImgUrl(product.details.img_url)" v-bind:alt="product.name"/>
            </div>
            <div class="col-6 align-self-center">
              <span class="font-weight-bold">Product: </span><br/>
              <router-link class="card-text" :to="{ name: 'productDetail' ,
                 params: {product: slugify(product.details.producer+'-'+product.details.name), id: product.details.product_id}}">
                {{ product.details.producer }} {{ product.details.name }}
              </router-link>
              <div class="align-self-center">
                <span class="font-weight-bold">Unity price: </span><br/>{{ product.details.price.toLocaleString().replace(',', ' ') }} zł
              </div>
              <div class="align-self-center py-2"><span class="font-weight-bold">Quantity: </span></div>
              <div class="row">
                <div class="col-8 col-sm-4 py-2">
                  <i class="bi-dash" v-on:click="decreaseQuantity(product.details.product_id)" style="cursor: pointer"></i>
                  <span class="border p-2 rounded">{{ product.quantity }}</span>
                  <i class="bi-plus" v-on:click="increaseQuantity(product.details.product_id)" style="cursor: pointer"></i>
                </div>
                <div class="col-4 text-lg-left align-self-center py-2">
                  <i class="bi-trash" v-on:click="removeFromCart(product.details.product_id)" style="cursor: pointer"
                     title="Remove from cart"></i>
                </div>
              </div>
              <div class="align-self-center">
                <span class="font-weight-bold">Value: </span><br/>{{ (product.details.price * product.quantity).toLocaleString().replace(',', ' ') }} zł
              </div>
            </div>
          </div>
        </div>

        <div class="col-2 align-self-center d-none d-md-block">
          <img :src="getImgUrl(product.details.img_url)" v-bind:alt="product.name"/>
        </div>
        <div class="col-3 align-self-center d-none d-md-block">
          <router-link class="card-text" :to="{ name: 'productDetail' ,
            params: {product: slugify(product.details.producer+'-'+product.details.name),id: product.details.product_id}}">
            {{ product.details.producer }} {{ product.details.name }}
          </router-link>
        </div>
        <div class="col-2 align-self-center d-none d-md-block">
          {{ product.details.price.toLocaleString().replace(',', ' ') }} zł
        </div>

        <div class="col-2 align-self-center d-none d-md-block">
          <i class="bi-dash" v-on:click="decreaseQuantity(product.details.product_id)" style="cursor: pointer"></i>
          <span class="border p-2 rounded">{{ product.quantity }}</span>
          <i class="bi-plus" v-on:click="increaseQuantity(product.details.product_id)" style="cursor: pointer"></i>
        </div>

        <div class="col-2 align-self-center d-none d-md-block">
          {{ (product.details.price * product.quantity).toLocaleString().replace(',', ' ') }} zł
        </div>
        <div class="col-1 text-lg-left align-self-center d-none d-md-block">
          <i class="bi-trash" v-on:click="removeFromCart(product.details.product_id)" style="cursor: pointer"
             title="Remove from cart"></i>
        </div>
      </div>

      <hr>

      <div class="row justify-content-md-end py-1 py-md-5">
        <div class="col-6 col-md-3 font-weight-bold">
          Total value:
        </div>
        <div class="col-6 col-md-3 col-3">
          {{ productsValue.toLocaleString().replace(',', ' ') }} zł
        </div>
      </div>

      <div class="row py-5">
        <div class="col-sm col-md-10">
          <router-link class="btn btn-outline-secondary" :to="{ name: 'home' }">Continue shopping</router-link>
        </div>
        <div class="col-sm col-sm-2 pt-4 pt-sm-0">
          <router-link class="btn btn-success rounded" :to="{ name: 'order' }">Checkout</router-link>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="container py-1 py-md-5 my-2 text-center">
        <h3 class="pb-5 mt-5">Your cart is empty</h3>
        <router-link class="btn btn-success rounded btn-lg" :to="{ name: 'home' }">Go to shopping</router-link>

        <h4 class="py-5 my-5">You can also read
          <router-link class="font-weight-bold" :to="{ name: 'about' }">about us</router-link>
          or
          <router-link class="font-weight-bold" :to="{ name: 'contact' }">contact us</router-link>
        </h4>
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
    return {toast};
  },
  data() {
    const slugify = require('slugify');
    return {
      cart: Store.state,
      slugify,
    };
  },
  methods: {
    getImgUrl(product) {
      return require('../../public/' + product);
    },
    removeFromCart(id) {
      Store.removeFromCart(id);
      this.toast.error("Product was removed from cart", {
        timeout: 1500,
      });
    },
    increaseQuantity(product) {
      Store.increaseQuantity(product);
    },
    decreaseQuantity(product) {
      Store.decreaseQuantity(product);
    },
  },
  computed: {
    productsValue() {
      return Store.productsValue();
    },
  },
};
</script>

<style scoped>
img {
  max-width: 100%;
  max-height: 100%;
}

</style>