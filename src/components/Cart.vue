<template>
  <div class="container py-5">
    <h3>Your cart</h3>

    <div class="row py-5">
      <div class="col-2 font-weight-bold">Product photo</div>
      <div class="col-4 font-weight-bold">Product name</div>
      <div class="col-2 font-weight-bold">Unit Price</div>
      <div class="col-2 font-weight-bold">Quantity</div>
      <div class="col-2 font-weight-bold">Value</div>
    </div>

    <div class="row pb-5">
      <div class="col-2">Product photo</div>
      <div class="col-4">Product name</div>
      <div class="col-2">Unit Price</div>
      <div class="col-2">Quantity</div>
      <div class="col-2">Value</div>
    </div>

    <hr>

    <div class="row justify-content-end py-5">
      <div class="col-2  font-weight-bold">
        Total value:
      </div>
      <div class="col-2">
        Value
      </div>
    </div>

    <div class="row py-5">
    <div class="col-10">
      <router-link class="btn btn-outline-secondary" :to="{ name: 'home' }">Continue shopping</router-link>
    </div>
    <div class="col-2">
      <button class="btn btn-success rounded btn-lg">Checkout</button>
    </div>
  </div>

  </div>

</template>

<script>
export default {
  name: "Cart"
}
</script>

<style scoped>

</style>