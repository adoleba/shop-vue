<template>
  <div class="row">
    <div v-for="product in products" :product="product" :key="product.id"
         class="col-sm-4 col-xs-12 text-center p-4 p-sm-2 p-lg-5">
      <div class="card no-border">
        <img :src="getImgUrl(product.img_url)" v-bind:alt="product.name" class="card-img-top">
        <div class="card-body">
          <router-link class="card-text" :to="{ name: 'productDetail' , params:
            {product: slugify(product.producer+'-'+product.name), id: product.product_id}}">
            {{ product.producer }} {{ product.name }}
          </router-link>
          <h5 class="card-title font-weight-bold">{{ product.price.toLocaleString().replace(',', ' ') }} zł</h5>
          <button class="btn btn-success rounded" v-on:click="addToCart(product)">Add to cart</button>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

import {Store} from "../store/store";
import {useToast} from "vue-toastification";

export default {
  name: 'HomePage',
  setup() {
    const toast = useToast();
    const slugify = require('slugify');
    return {toast, slugify};
  },
  data (){
    return {
      products: [],
    };
  },

  methods: {
    getImgUrl(product) {
      return require('../../public/' + product);
    },
    addToCart(product) {
      Store.addToCart(product);
      this.toast.success("Product was added to cart", {
        timeout: 1500,
      });
    },
  },
  async created() {
    this.products = await Store.getProductsFromApi();
  }

};

</script>

<style scoped>

.no-border {
  border: none;
}
</style>
