import { createWebHistory, createRouter } from "vue-router";
import HomePage from "../components/HomePage";
import Index from "../components/Index";
import About from "../components/About";
import Contact from "../components/Contact";
import Cart from "../components/Cart";
import ProductDetail from "../components/ProductDetail";
import Order from "../components/Order";
import OrderConfirm from "../components/OrderConfirm";
import CategoryProducts from "../components/CategoryProducts";

const routes = [
    {
    path: "/",
    name: "index",
    component: Index,
      children: [
          {
            path: "/",
            name: "home",
            component: HomePage,
          },
          {
          path: "/category/:categoryName",
          name: "category",
          component: CategoryProducts,
          props: true
        },
      ]},
  {
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
    path: "/order",
    name: "order",
    component: Order,
  }, {
    path: "/order/confirm",
    name: "orderConfirm",
    component: OrderConfirm,
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