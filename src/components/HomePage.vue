<template>
  <div class="container py-5 py-sm-2 py-lg-5">
    <div class="row">
      <div class="col-md-12 col-sm-12 col-xs-12">
        <h1 class="font-weight-bold text-center">Donec non magna</h1>
        <p class="text-center px-5 pb-4">
          Vivamus ornare fermentum lorem quis egestas. Praesent id sapien bibendum, ullamcorper nibh
          quis, porttitor sapien. Cras rhoncus elementum elementum
        </p>
      </div>
    </div>

    <div class="row">
      <div v-for="product in products" :product="product" :key="product.id" class="col-sm-4 col-xs-12 text-center p-4 p-sm-2 p-lg-5">
        <div class="card no-border">
          <img :src="getImgUrl(product.id)" v-bind:alt="product.name" class="card-img-top">
          <div class="card-body">
            <router-link class="card-text" :to="{ name: 'productDetail' , params: {id: product.id}}">
              {{ product.producer }} {{ product.name }}
            </router-link>
            <h5 class="card-title font-weight-bold">{{ product.price }} zł</h5>
            <button class="btn btn-success rounded" v-on:click="addToCart(product)">Add to cart</button>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import products from "../data/products";
import { Store } from "../store/store";
import { useToast } from "vue-toastification";

export default {
  name: 'HomePage',
  setup() {
    const toast = useToast();
      return {toast}
  },
  data () {
    return {
      products,
    };
  },
  methods: {
    getImgUrl(id) {
      return require('../data/images/'+id+'.png')
    },
    addToCart(product){
      Store.addToCart(product)
      this.toast.success("Product was added to cart", {
        timeout: 1500,
      });
    },
  },

};

</script>

<style scoped>

.no-border {
  border: none;
}
</style>
