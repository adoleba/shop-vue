<template>
  <div class="row">

    <div v-if="!products.length">
      <div class="container px-sm-5">
          <div class="col-md-12 col-sm-12 col-xs-12">
            <div class="text-center p-0 p-md-5">
              <p>There are no products in category</p>
            </div>
          </div>
      </div>
    </div>

    <div v-for="product in products" :key="product.id" :products="products"
         class="col-sm-4 col-xs-12 text-center p-4 p-sm-2 p-lg-5">
      <div class="card no-border">
        <img :src="getImgUrl(product.img_url)" v-bind:alt="product.name" class="card-img-top">
        <div class="card-body">
          <router-link class="card-text" :to="{ name: 'productDetail' , params:
          {product: slugify(product.producer+'-'+product.name), id: product.id}}">
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
import {useToast} from "vue-toastification";
import {Store} from "../store/store";
import axios from "axios";

export default {
  name: "CategoryProducts",
  props: ['categoryName'],
  setup() {
    const toast = useToast();
    const slugify = require('slugify');
    return {toast, slugify};
  },
  data() {
    return {
      products: [],
    };
  },

  mounted () {
    const categoryName = this.$route.params.categoryName;
    axios.get('http://localhost:8000/api/products/').then(response => {
      this.products = response.data.filter(product => product.category === categoryName);
    });
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
};
</script>

<style scoped>

.no-border {
  border: none;
}

</style>