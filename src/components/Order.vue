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
            <input class="form-check-input" type="radio" name="customerType" id="privatePerson" value="privatePerson" v-model='customerKind' @change="customerData">
            <label class="form-check-label" for="privatePerson">Private Person</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="customerType" id="company" value="company" v-model='customerKind' @change="customerData">
            <label class="form-check-label" for="company">Company</label>
          </div>
        </div>

        <div id="companyData" style="display: none">
          <div class="form-group">
            <label for="companyName">Company Name</label>
            <input id="companyName" type="text" class="form-control" v-model="shippingData['companyName']" />
          </div>
          <div class="form-group">
            <label for="nip">NIP number</label>
            <input id="nip" type="text" class="form-control" v-model="shippingData['nip']"/>
          </div>
        </div>

        <div id="privatePersonData" style="display: none">
          <div class="form-row">
            <div class="form-group col-6">
              <label for="firstName">First Name</label>
              <input id="firstName" type="text" class="form-control" v-model="shippingData['firstName']"/>
            </div>
            <div class="form-group col-6">
              <label for="lastName">Last Name</label>
              <input id="lastName" type="text" class="form-control" v-model="shippingData['lastName']"/>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="text" class="form-control" v-model="shippingData['email']"/>
        </div>

        <div class="form-group">
          <label for="street">Street</label>
          <input id="street" type="text" class="form-control" v-model="shippingData['street']"/>
        </div>

        <div class="form-row">
          <div class="form-group col-6">
            <label for="streetNumber">Street number</label>
            <input id="streetNumber" type="text" class="form-control" v-model="shippingData['streetNumber']"/>
          </div>
          <div class="form-group col-6">
            <label for="apartmentNumber">Apartment number</label>
            <input id="apartmentNumber" type="text" class="form-control" v-model="shippingData['apartmentNumber']"/>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-4">
            <label for="postalCode">Postal code</label>
            <input id="postalCode" type="text" class="form-control" v-model="shippingData['postalCode']"/>
          </div>
          <div class="form-group col-8">
            <label for="city">City</label>
            <input id="city" type="text" class="form-control" v-model="shippingData['city']"/>
          </div>
        </div>

        <div class="form-group">
          <label for="comments">Comments</label>
          <textarea id="comments" class="form-control" v-model="shippingData['comments']"/>
        </div>

      </div>
    </div>

    <div class="col-5 offset-1">

      <div class="border rounded p-3 mb-5">
        <div class="p-4">
          <div v-for="carrier in carriers" :key="carrier" class="form-row form-group">
              <div  class="form-check col-7 pl-3">
                <input class="form-check-input" type="radio" name='delivery' id="delivery" v-bind:value='carrier.name' @change="addDeliveryCost">
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
              <div class="col-5">{{ productsValue.toLocaleString().replace(',', ' ') }} zł</div>
          </div>

          <div v-if="deliveryCost !== 0" class="row pt-3">
            <div  class="col-7">Shipping cost: </div>
              <div class="col-5">{{ deliveryCost.toLocaleString().replace('.', ',') }} zł</div>
          </div>

          <div class="row pt-3">
            <div  class="col-7">
                <span class="font-weight-bolder">Total value:</span>
              </div>
              <div class="col-5 font-weight-bold">{{ (totalCost).toLocaleString().replace(',', ' ').replace('.', ',') }} zł</div>
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
            <router-link class="btn btn-success rounded btn-lg" :to="{ name: 'orderConfirm' }" v-on:click="shippingValues()">Confirm and pay</router-link>
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
      shippingData: Store.state.shippingData,
      customerKind: Store.state.customerKind,
    }
  },

  methods: {
    customerData(){
      const privatePersonData = document.getElementById('privatePersonData')
      const companyData = document.getElementById('companyData')

      if (document.getElementById('privatePerson').checked === true) {
        privatePersonData.style.display = 'block';
        companyData.style.display = 'none';
        Store.state.shippingData['companyName'] = '';
        Store.state.shippingData['nip'] = '';
        Store.state.customerKind = 'privatePerson';
      }
      if (document.getElementById('company').checked === true) {
        privatePersonData.style.display = 'none';
        companyData.style.display = 'block';
        Store.state.shippingData['firstName'] = '';
        Store.state.shippingData['lastName'] = '';
        Store.state.customerKind = 'company';
      }
    },
    addDeliveryCost(event) {
      const deliveryKind = event.target.value
      const carrier = this.carriers.find(carrier => carrier.name === deliveryKind);
      this.deliveryCost = carrier.price
      Store.state.deliveryMethod = carrier.name
    },
    shippingValues() {
      const values = {
        'companyName': document.querySelector("input[id=companyName]").value,
        'nip': document.querySelector("input[id=nip]").value,
        'firstName': document.querySelector("input[id=firstName]").value,
        'lastName': document.querySelector("input[id=lastName]").value,
        'email': document.querySelector("input[id=email]").value,
        'street': document.querySelector("input[id=street]").value,
        'streetNumber': document.querySelector("input[id=streetNumber]").value,
        'apartmentNumber': document.querySelector("input[id=apartmentNumber]").value,
        'postalCode': document.querySelector("input[id=postalCode]").value,
        'city': document.querySelector("input[id=city]").value,
        'comments': document.querySelector("textarea[id=comments]").value,
      }
      if (Store.state.shippingData.length === 0) {
        Store.state.shippingData.push(values)
      }
    },

  },
  computed: {
    productsValue() {
      return Store.productsValue()
    },
    totalCost() {
      const totalCost = Store.productsValue() + +this.deliveryCost
      Store.state.totalCost = totalCost
      return totalCost
    },

  },
}
</script>

<style scoped>

</style>