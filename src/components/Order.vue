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

  <div class="row pb-4" id="test">
    <div class="col-6">
      <div class="p-5 border rounded">

        <div class="form-row form-group">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="customerType" id="privatePerson" value="privatePerson" v-model='validate.customerKind' @change="customerData">
            <label class="form-check-label" for="privatePerson">Private Person</label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio" name="customerType" id="company" value="company" v-model='validate.customerKind' @change="customerData">
            <label class="form-check-label" for="company">Company</label>
          </div>
          <span v-if="v$.customerKind.$error">
            {{ v$.customerKind.$errors[0].$message }}
          </span>
        </div>

        <div id="companyData">
          <div class="form-group">
            <label for="companyName">Company Name</label>
            <input id="companyName" type="text" class="form-control" v-model="validate.companyName" />
            <span v-if="v$.companyName.$error">Value is required </span>
          </div>
          <div class="form-group">
            <label for="nip">NIP number</label>
            <input id="nip" type="text" class="form-control" v-model="validate.nip"/>
            <span v-if="v$.nip.$error">Value is required </span>
          </div>
        </div>

        <div id="privatePersonData">
          <div class="form-row">
            <div class="form-group col-6">
              <label for="firstName">First Name</label>
              <input id="firstName" type="text" class="form-control" v-model="validate.firstName"/>
              <span v-if="v$.firstName.$error">Value is required </span>
            </div>
            <div class="form-group col-6">
              <label for="lastName">Last Name</label>
              <input id="lastName" type="text" class="form-control" v-model="validate.lastName"/>
              <span v-if="v$.lastName.$error">Value is required </span>
            </div>
          </div>
        </div>

        <div id="commonShippingData" style="display: none">
          <div class="form-group">
            <label for="email">Email</label>
            <input id="email" type="text" class="form-control" v-model="validate.email"/>
             <span v-if="v$.email.$error">
               {{ v$.email.$errors[0].$message }}
             </span>
          </div>

          <div class="form-group">
            <label for="street">Street</label>
            <input id="street" type="text" class="form-control" v-model="validate.street"/>
            <span v-if="v$.street.$error">
               {{ v$.street.$errors[0].$message }}
             </span>
          </div>

          <div class="form-row">
            <div class="form-group col-6">
              <label for="streetNumber">Street number</label>
              <input id="streetNumber" type="text" class="form-control" v-model="validate.streetNumber"/>
              <span v-if="v$.streetNumber.$error">
               {{ v$.streetNumber.$errors[0].$message }}
             </span>
            </div>
            <div class="form-group col-6">
              <label for="apartmentNumber">Apartment number</label>
              <input id="apartmentNumber" type="text" class="form-control" v-model="shippingData['apartmentNumber']"/>
            </div>
          </div>

          <div class="form-row">
            <div class="form-group col-4">
              <label for="postalCode">Postal code</label>
              <input id="postalCode" type="text" class="form-control" v-model="validate.postalCode"/>
              <span v-if="v$.postalCode.$error">
               {{ v$.postalCode.$errors[0].$message }}
             </span>
            </div>
            <div class="form-group col-8">
              <label for="city">City</label>
              <input id="city" type="text" class="form-control" v-model="validate.city"/>
              <span v-if="v$.city.$error">
               {{ v$.city.$errors[0].$message }}
             </span>
            </div>
          </div>

          <div class="form-group">
            <label for="comments">Comments</label>
            <textarea id="comments" class="form-control" v-model="shippingData['comments']"/>
          </div>

        </div>

      </div>
    </div>

    <div class="col-5 offset-1">

      <div class="border rounded p-3 mb-5">
        <div class="p-4">
          <div v-for="carrier in carriers" :key="carrier" class="form-row form-group">
              <div  class="form-check col-7 pl-3">
                <input class="form-check-input" type="radio" name='delivery' id="delivery" v-bind:value='carrier.name' v-model='validate.deliveryMethod' @change="addDeliveryCost">
                <label class="form-check-label" for="delivery">{{ carrier.name }}</label>
              </div>
              <div class="col-5">{{carrier.price.toLocaleString().replace('.', ',')}} zł</div>
          </div>
          <span v-if="v$.deliveryMethod.$error">
            {{ v$.deliveryMethod.$errors[0].$message }}
          </span>
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
                <input class="form-check-input" type="checkbox" id="terms_accepted" v-model="validate.validTermAccepted" @change="agreeTerms">
              </div>
            </div>
            <div class="col-10">Etiam sit amet velit ullamcorper dui finibus ultrices porta at justo</div>
            <span v-if="v$.validTermAccepted.$error">You have to accept terms </span>
          </div>
          <div class="row px-3 py-1">
            <div class="col-1">
              <div class="form-check">
                <input class="form-check-input" type="checkbox" id="marketing_accepted" v-model="marketingAccepted" @change="agreeMarketing">
              </div>
            </div>
            <div class="col-10">Suspendisse et magna tempus nisi pretium aliquet in in sapien</div>
          </div>

          <div class="row px-4 pt-4 justify-content-center">
            <button class="btn btn-success rounded btn-lg" v-on:click="saveShippingValues()">Confirm and pay</button>
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
import { required, email, minLength, requiredIf } from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { reactive, computed } from "vue";
import { isTermChecked } from "../data/validators";

export default {
  name: "Order",

  mounted() {
    this.customerForm()
  },

  data() {
    return {
      carriers: carriers,
      cart: Store.state,
      deliveryCost: Store.state.deliveryCost,
      shippingData: Store.state.shippingData,
      customerKind: Store.state.customerKind,
      termsAccepted: Store.state.termsAccepted,
      marketingAccepted: Store.state.marketingAccepted,
    }
  },
  setup() {
    const validate = reactive({
      customerKind: Store.state.customerKind === undefined ? '' : Store.state.customerKind,
      firstName: Store.state.shippingData['firstName'] === undefined ? '' : Store.state.shippingData['firstName'],
      lastName: Store.state.shippingData['lastName'] === undefined ? '' : Store.state.shippingData['lastName'],
      companyName: Store.state.shippingData['companyName'] === undefined ? '' : Store.state.shippingData['companyName'],
      nip: Store.state.shippingData['nip'] === undefined ? '' : Store.state.shippingData['nip'],
      email: Store.state.shippingData['email'] === undefined ? '' : Store.state.shippingData['email'],
      street: Store.state.shippingData['street'] === undefined ? '' : Store.state.shippingData['street'],
      streetNumber: Store.state.shippingData['streetNumber'] === undefined ? '' : Store.state.shippingData['streetNumber'],
      postalCode: Store.state.shippingData['postalCode'] === undefined ? '' : Store.state.shippingData['postalCode'],
      city: Store.state.shippingData['city'] === undefined ? '' : Store.state.shippingData['city'],
      deliveryMethod: Store.state.deliveryMethod === undefined ? '' : Store.state.deliveryMethod,
      validTermAccepted: document.querySelector("input[id=terms_accepted]") === null ? Store.state.termsAccepted : this.termsAccepted,
    })

    const rules = computed(() => {
      return {
        customerKind: { required },
        firstName: { required: requiredIf(function () {return document.getElementById('privatePerson').checked}) },
        lastName: { required: requiredIf(function () {return document.getElementById('privatePerson').checked}) },
        companyName: { required: requiredIf(function () {return document.getElementById('company').checked}) },
        nip: { required: requiredIf(function () {return document.getElementById('company').checked}) },
        email: { required, email },
        street: { required, minLength: minLength(3) },
        streetNumber: { required },
        postalCode: { required, minLength: minLength(5) },
        city: { required, minLength: minLength(3) },
        deliveryMethod: { required },
        validTermAccepted: { isTermChecked }
      }
    })
    const v$ = useVuelidate(rules, validate)
    return { validate, v$ }
  },
  methods: {
    customerData() {
      const privatePersonData = document.getElementById('privatePersonData')
      const companyData = document.getElementById('companyData')
      const commonShippingData = document.getElementById('commonShippingData')

      if (document.getElementById('privatePerson').checked === true) {
        privatePersonData.style.display = 'block';
        commonShippingData.style.display = 'block';
        companyData.style.display = 'none';
        this.shippingData['companyName'] = '';
        Store.state.shippingData['companyName'] = '';
        this.shippingData['nip'] = '';
        Store.state.shippingData['nip'] = '';
        this.customerKind = 'privatePerson';
        Store.state.customerKind = 'privatePerson';
        console.log(Store.state.shippingData['companyName'])
      }
      if (document.getElementById('company').checked === true) {
        privatePersonData.style.display = 'none';
        companyData.style.display = 'block';
        commonShippingData.style.display = 'block';
        this.shippingData['firstName'] = '';
        Store.state.shippingData['firstName'] = '';
        this.shippingData['lastName'] = '';
        Store.state.shippingData['lastName'] = '';
        this.customerKind = 'company';
        Store.state.customerKind = 'company';
      }
    },
    addDeliveryCost(event) {
      const deliveryKind = event.target.value
      const carrier = this.carriers.find(carrier => carrier.name === deliveryKind);
      this.deliveryCost = carrier.price
      Store.state.deliveryMethod = carrier.name
      Store.state.deliveryCost = carrier.price
    },
    agreeTerms(event) {
      const agreedTerms = event.target.checked
      Store.state.termsAccepted = agreedTerms
      this.termsAccepted = agreedTerms
    },

    agreeMarketing(event) {
      const agreedMarketing = event.target.checked
      Store.state.marketingAccepted = agreedMarketing
    },

    saveShippingValues() {
      this.v$.$validate()

      if (!this.v$.$error) {
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

        Object.assign(Store.state.shippingData, values)
        this.$router.push({name: 'orderConfirm'})

      }
    },

    customerForm: function () {
      const privatePersonData = document.getElementById('privatePersonData')
      const companyData = document.getElementById('companyData')
      privatePersonData.classList.add('hiddenForm')
      companyData.classList.add('hiddenForm')

      if (Store.state.customerKind === 'privatePerson') {
        document.getElementById('privatePersonData').style.display = 'block';
        document.getElementById('commonShippingData').style.display = 'block'
        Store.state.shippingData['companyName'] = '';
        Store.state.shippingData['nip'] = '';

      }
      if (Store.state.customerKind === 'company') {
        document.getElementById('companyData').style.display = 'block';
        document.getElementById('commonShippingData').style.display = 'block'
        Store.state.shippingData['firstName'] = '';
        Store.state.shippingData['lastName'] = '';
      }
    },
  },

  computed: {
    productsValue() {
      return Store.productsValue()
    },
    totalCost() {
      const totalCost = Store.productsValue() + +Store.state.deliveryCost
      Store.state.totalCost = totalCost
      return totalCost
    },
  },
}
</script>

<style scoped>

.hiddenForm {
  display: none;
}

</style>