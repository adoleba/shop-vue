<template>
  <div class="row">
    <div v-for="product in products" :product="product" :key="product.id"
         class="col-sm-4 col-xs-12 text-center p-4 p-sm-2 p-lg-5">
      <div class="card no-border">
        <img :src="getImgUrl(product.id)" v-bind:alt="product.name" class="card-img-top">
        <div class="card-body">
          <router-link class="card-text" :to="{ name: 'productDetail' , params: {id: product.id}}">
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
import products from "../data/products";
import {Store} from "../store/store";
import {useToast} from "vue-toastification";

export default {
  name: 'HomePage',
  setup() {
    const toast = useToast();
    return {toast};
  },
  data() {
    return {
      products,
    };
  },
  methods: {
    getImgUrl(id) {
      return require('../data/images/' + id + '.png');
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
