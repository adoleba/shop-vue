<template>

  <header>
    <Header />
  </header>

  <main>
    <div class="container">
      <router-view />
    </div>
  </main>

</template>

<script>

import Header from "./components/Header";

export default {
  name: 'App',
  components: {
    Header,
  }
}
</script>

<style>
</style>
