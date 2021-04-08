import { createWebHistory, createRouter } from "vue-router";
import HomePage from "../components/HomePage"
import About from "../components/About";
import Contact from "../components/Contact";
import Cart from "../components/Cart";

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
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;