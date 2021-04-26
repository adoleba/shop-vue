import { createApp } from 'vue';
import App from './App.vue';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import Toast, { POSITION } from "vue-toastification";
import "vue-toastification/dist/index.css";
import router from "./router";
require('bootstrap-icons/font/bootstrap-icons.css');


createApp(App).use(router).use(Toast, {position: POSITION.TOP_CENTER}).mount('#app')
