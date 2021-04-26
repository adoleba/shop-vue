<template>
  <div class="container">
    <div class="row">

      <div class="col-6 justify-content-center">
        <img :src="getImgUrl(product.id)" v-bind:alt="product.name" class="card-img-top">
      </div>

      <div class="col-6 justify-content-center py-5 pl-5">
        <h1 class="pb-5">{{product.producer}} {{product.name}}</h1>
        <div class="row">
          <div class="col"><p class="font-weight-bold">Memory</p></div>
          <div class="col-9">{{ product.memory }}</div>
        </div>
        <div class="row">
          <div class="col"><p class="font-weight-bold">Screen</p></div>
          <div class="col-9">{{ product.screen }}</div>
        </div>
        <div class="row">
          <div class="col"><p class="font-weight-bold">Disk</p></div>
          <div class="col-9">{{ product.disk }}</div>
        </div>
        <div class="row">
          <div class="col"><p class="font-weight-bold">Processor</p></div>
          <div class="col-9">{{ product.processor }}</div>
        </div>

        <div class="row pl-3 pt-3">
          <h3 class="font-weight-bold">{{ product.price }} zł</h3>
        </div>

        <div class="row pb-5 pt-3">
          <div class="col-3">
            <input type="number" class="form-control" value="1" min="1" max="10" id="quantity"/>
          </div>
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

