<template>

  <header>
    <Header />
  </header>

  <main>
    <div class="container">
      <router-view />
    </div>
  </main>

  <footer>
    <Footer />
  </footer>

</template>

<script>

import Header from "./components/Header";
import Footer from "./components/Footer";

export default {
  name: 'App',
  components: {
    Header,
    Footer,
  }
}
</script>

<style>
</style>
