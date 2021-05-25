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

    <div class="row justify-content-center navbar navbar-expand-lg navbar-light">
      <ul class="navbar-nav">
        <li>
          <router-link :to="{ name: 'home' }" class="nav-item nav-link">All</router-link>
        </li>
        <li>
          <router-link :to="{ name: 'category', params: {categoryName: 'ultrabook'}}" class="nav-item active nav-link">
            Ultrabooks
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'category', params: {categoryName: 'laptop'}}" class="nav-item active nav-link">
            Laptops
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'category', params: {categoryName: '2in1'} }" class="nav-item active nav-link">2 in
            1
          </router-link>
        </li>
      </ul>
    </div>

    <hr>

    <router-view :key="$route.path"></router-view>

  </div>
</template>

<script>
export default {
  name: "Index",
};
</script>

<style scoped>

a.router-link-active {
  font-weight: 700;
  cursor: default;
}
</style>