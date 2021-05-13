<template>
  <div class="container">
    <div class="row text-center text-md-left">

      <div class="col-12 col-md-6 justify-content-center">
        <img :src="getImgUrl(product.id)" v-bind:alt="product.name" class="card-img-top">
      </div>

      <div class="col-12 col-md-6 justify-content-center py-5 pl-5">
        <h1 class="pb-5">{{product.producer}} {{product.name}}</h1>
        <div class="row">
          <div class="col"><p><span class="font-weight-bold">Memory: </span>{{ product.memory }}</p></div>
        </div>
        <div class="row">
          <div class="col"><p><span class="font-weight-bold">Screen: </span>{{ product.screen }}</p></div>
        </div>
        <div class="row">
          <div class="col"><p><span class="font-weight-bold">Disk: </span>{{ product.disk }}</p></div>
        </div>
        <div class="row">
          <div class="col"><p><span class="font-weight-bold">Processor: </span>{{ product.processor }}</p></div>
        </div>

        <div class="row justify-content-center justify-content-md-start pl-3 pt-3">
          <h3 class="font-weight-bold">{{ product.price.toLocaleString().replace(',', ' ') }} zł</h3>
        </div>

        <div class="row pt-3">
          <div class="col">
            <input type="number" class="col-form-label" style="max-width: 120px;" value="1" min="1" max="10" id="quantity"/>
          </div>
        </div>
        <div class="row pb-5 pt-3">
          <div class="col">
            <button class="btn btn-success rounded" v-on:click="addToCart(product)">Add to cart</button>
          </div>
        </div>

        <div class="row">
          <p>{{ product.description }}</p>
        </div>
      </div>

    </div>
  </div>

</template>

<script>

import products from "../data/products";
import {Store} from "../store/store";
import {useToast} from "vue-toastification";

export default {
  name: "ProductDetail",
  setup() {
    const toast = useToast();
      return {toast}
  },
  data() {
    return {
      products: products,
    }
  },
  methods: {
    getImgUrl(id) {
      return require('../data/images/'+id+'.png')
    },
    getQuantity(){
      return document.querySelector("input[id=quantity]").value
    },
    addToCart(product){
      Store.addToCart(product, this.getQuantity())
      this.toast.success("Product was added to cart", {
        timeout: 1500,
      });
    },
  },
  created() {
    const ID = Number(this.$route.params.id);
    const product = this.products.find(product => product.id === ID);
    this.product = product;
  }
}
</script>

<style scoped>

</style>

