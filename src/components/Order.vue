<template>
<div class="container">

  <div class="row py-4">
    <div class="col-6 px-3">
      <h6 class="font-weight-bold">Shipping data</h6>
    </div>
    <div class="col-5 px-3 offset-1">
      <h6 class="font-weight-bold">Delivery method</h6>
    </div>
  </div>

  <div class="row pb-4">
    <div class="col-6">
      <div class="p-5 border rounded">

        <div class="form-row form-group">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="customerType" id="privatePerson" value="privatePerson" checked @change="customerData">
            <label class="form-check-label" for="privatePerson">Private Person</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="customerType" id="company" value="company" @change="customerData">
            <label class="form-check-label" for="company">Company</label>
          </div>
        </div>

        <div id="companyData" style="display: none">
          <div class="form-group">
            <label for="companyName">Company Name</label>
            <input id="companyName" type="text" class="form-control" />
          </div>
          <div class="form-group">
            <label for="nip">NIP number</label>
            <input id="nip" type="text" class="form-control" />
          </div>
        </div>

        <div id="privatePersonData">
          <div class="form-row">
            <div class="form-group col-6">
              <label for="firstname">First Name</label>
              <input id="firstname" type="text" class="form-control" />
            </div>
            <div class="form-group col-6">
              <label for="lastname">Last Name</label>
              <input id="lastname" type="text" class="form-control" />
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="text" class="form-control" />
        </div>

        <div class="form-group">
          <label for="street">Street</label>
          <input id="street" type="text" class="form-control" />
        </div>

        <div class="form-row">
          <div class="form-group col-6">
            <label for="streetNumber">Street number</label>
            <input id="streetNumber" type="text" class="form-control" />
          </div>
          <div class="form-group col-6">
            <label for="apartmentNumber">Apartment number</label>
            <input id="apartmentNumber" type="text" class="form-control" />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-4">
            <label for="postalCode">Postal code</label>
            <input id="postalCode" type="text" class="form-control" />
          </div>
          <div class="form-group col-8">
            <label for="city">City</label>
            <input id="city" type="text" class="form-control" />
          </div>
        </div>

      </div>
    </div>

    <div class="col-5 offset-1">

      <div class="border rounded p-3 mb-5">
        <div class="p-4">
          <div v-for="carrier in carriers" :key="carrier" class="form-row form-group">
              <div  class="form-check col-7 pl-3">
                <input class="form-check-input" type="radio" name="delivery" id="delivery" v-bind:value='carrier.price' @change="addDeliveryCost">
                <label class="form-check-label" for="delivery">{{ carrier.name }}</label>
              </div>
              <div class="col-5">{{carrier.price.toLocaleString().replace('.', ',')}} zł</div>
          </div>
        </div>
      </div>

      <div class="pb-3">
        <h6 class="font-weight-bold">Order summary</h6>
      </div>

      <div class="border rounded p-3">
        <div class="p-4">
          <div v-for="product in cart.cart" :key="product.details.id" :product="product" class="form-row form-group">
              <div  class="col-7">
                {{ product.details.producer }} {{ product.details.name }}
              </div>
              <div class="col-5">{{product.quantity }} szt x {{ product.details.price.toLocaleString().replace(',', ' ') }} zł</div>
          </div>
          <hr>

          <div class="row pt-3">
            <div  class="col-7">Products value: </div>
              <div class="col-5">{{ totalCost.toLocaleString().replace(',', ' ') }} zł</div>
          </div>

          <div v-if="deliveryCost !== 0" class="row pt-3">
            <div  class="col-7">Shipping cost: </div>
              <div class="col-5">{{ deliveryCost.toLocaleString().replace('.', ',') }} zł</div>
          </div>

          <div class="row pt-3">
            <div  class="col-7">
                <span class="font-weight-bolder">Total value:</span>
              </div>
              <div class="col-5 font-weight-bold">{{ (totalCost + +deliveryCost).toLocaleString().replace(',', ' ').replace('.', ',') }} zł</div>
          </div>
        </div>

        <div class="form-group">
          <div class="row px-3 py-1">
            <div class="col-1">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" id="terms">
              </div>
            </div>
            <div class="col-10">Etiam sit amet velit ullamcorper dui finibus ultrices porta at justo</div>
          </div>
          <div class="row px-3 py-1">
            <div class="col-1">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" id="marketing">
              </div>
            </div>
            <div class="col-10">Suspendisse et magna tempus nisi pretium aliquet in in sapien</div>
          </div>

          <div class="row px-4 pt-4 justify-content-center">
              <button class="btn btn-success btn-lg rounded">Confirm and pay</button>
          </div>

        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import carriers from "../data/delivery";
import {Store} from "../store/store";

export default {
  name: "Order",

  data() {
    return {
      carriers: carriers,
      cart: Store.state,
      deliveryCost: 0,
    }
  },

  methods: {
    customerData(){
      const privatePersonData = document.getElementById('privatePersonData')
      const companyData = document.getElementById('companyData')

      if (document.getElementById('privatePerson').checked === true) {
        privatePersonData.style.display = 'block';
        companyData.style.display = 'none';
      }
      if (document.getElementById('company').checked === true) {
        privatePersonData.style.display = 'none';
        companyData.style.display = 'block';
      }
    },
    addDeliveryCost(event) {
      this.deliveryCost = event.target.value
    }

  },
  computed: {
    totalCost() {
      return Store.state.cart.reduce((accum, product) => {
            return accum + product.details.price * product.quantity
        }, 0)
    },
  },
}
</script>

<style scoped>

</style>