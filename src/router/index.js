import { createWebHistory, createRouter } from "vue-router";
import HomePage from "../components/HomePage"
import About from "../components/About";
import Contact from "../components/Contact";
import Cart from "../components/Cart";
import ProductDetail from "../components/ProductDetail";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  }, {
    path: "/about",
    name: "about",
    component: About,
  }, {
    path: "/contact",
    name: "contact",
    component: Contact,
  }, {
    path: "/cart",
    name: "cart",
    component: Cart,
  }, {
    path: "/products/:id",
    name: "productDetail",
    component: ProductDetail,
    props: true,
 },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;