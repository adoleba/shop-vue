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
      <div v-for="product in products" :key="product" class="col-sm-4 col-xs-12 text-center p-4 p-sm-2 p-lg-5">
        <div class="card no-border">
          <img :src="getImgUrl(product.id)" v-bind:alt="product.name" class="card-img-top">
          <div class="card-body">
            <p class="card-text">{{ product.producer }} {{ product.name }}</p>
            <h5 class="card-title font-weight-bold">{{ product.price }}</h5>
            <a href="#" class="btn btn-success rounded">To cart</a>
          </div>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
import products from "../data/products";

export default {
  name: 'HomePage',
  methods: {
    getImgUrl(id) {
      return require('../data/images/'+id+'.png')
    }
  },
  data () {
    return {
      products,
    }
  },
};
</script>

<style scoped>

.no-border {
  border: none;
}
</style>
