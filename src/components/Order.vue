<template>
<div class="container">

  <div class="row pb-4">
    <div class=" col-md col-lg-6">
      <h6 class="font-weight-bold py-4">Shipping data</h6>

      <div class="p-3 p-md-5 border rounded">
        <div class="form-row">
          <div class="form-group col-sm col-md-6">
            <label for="firstName">First Name</label>
            <input id="firstName" type="text" class="form-control" :class="{'input-error': v$.firstName.$error}" v-model="validate.firstName"/>
            <span v-if="v$.firstName.$error" class="error-message">{{ v$.firstName.$errors[0].$message }}</span>
          </div>
          <div class="form-group col-sm col-md-6">
            <label for="lastName">Last Name</label>
            <input id="lastName" type="text" class="form-control" :class="{'input-error': v$.lastName.$error}" v-model="validate.lastName"/>
            <span v-if="v$.lastName.$error" class="error-message">{{ v$.lastName.$errors[0].$message }}</span>
          </div>
        </div>

        <div class="form-group">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" id="invoice" v-model='invoice' @change="invoiceForm">
            <div>I need an invoice</div>
          </div>

          <div id="companyData" style="display: none">
            <div class="form-group pt-2">
              <label for="companyName">Company Name</label>
              <input id="companyName" type="text" class="form-control" :class="{'input-error': v$.companyName.$error}" v-model="validate.companyName" />
              <span v-if="v$.companyName.$error" class="error-message">Value is required</span>
            </div>
            <div class="form-group">
              <label for="nip">NIP number</label>
              <input id="nip" type="text" class="form-control" :class="{'input-error': v$.nip.$error}" v-model="validate.nip"/>
              <span v-if="v$.nip.$error" class="error-message">Value is required</span>
            </div>
          </div>
        </div>

        <div class="form-group">
          <label for="email">Email</label>
          <input id="email" type="text" class="form-control" :class="{'input-error': v$.email.$error}" v-model="validate.email"/>
          <span v-if="v$.email.$error" class="error-message">{{ v$.email.$errors[0].$message }}</span>
        </div>

        <div class="form-group">
          <label for="street">Street</label>
          <input id="street" type="text" class="form-control" :class="{'input-error': v$.street.$error}" v-model="validate.street"/>
          <span v-if="v$.street.$error" class="error-message">{{ v$.street.$errors[0].$message }}</span>
        </div>

        <div class="form-row">
          <div class="form-group col-sm col-md-6">
            <label for="streetNumber">Street No.</label>
            <input id="streetNumber" type="text" class="form-control" :class="{'input-error': v$.streetNumber.$error}" v-model="validate.streetNumber"/>
            <span v-if="v$.streetNumber.$error" class="error-message">{{ v$.streetNumber.$errors[0].$message }}</span>
          </div>
          <div class="form-group col col-md-6">
            <label for="apartmentNumber">Apartment No.</label>
            <input id="apartmentNumber" type="text" class="form-control" v-model="shippingData['apartmentNumber']"/>
          </div>
        </div>

        <div class="form-row">
          <div class="form-group col-sm col-sm-4">
            <label for="postalCode">Zipcode</label>
            <input id="postalCode" type="text" class="form-control" :class="{'input-error': v$.postalCode.$error}" v-model="validate.postalCode"/>
            <span v-if="v$.postalCode.$error" class="error-message">{{ v$.postalCode.$errors[0].$message }}</span>
          </div>
          <div class="form-group col-sm col-sm-8">
            <label for="city">City</label>
            <input id="city" type="text" class="form-control" :class="{'input-error': v$.city.$error}" v-model="validate.city"/>
            <span v-if="v$.city.$error" class="error-message">{{ v$.city.$errors[0].$message }}</span>
          </div>
        </div>

        <div class="form-group">
          <label for="comments">Comments</label>
          <textarea id="comments" class="form-control" v-model="shippingData['comments']"/>
        </div>
      </div>
    </div>

    <div class="col-md col-lg-5 offset-lg-1">
      <h6 class="font-weight-bold py-4">Delivery method</h6>

      <div class="border rounded p-3 mb-5">
        <div class="p-4">
          <div v-for="carrier in carriers" :key="carrier" class="form-row form-group">
              <div class="form-check col-7 pl-3">
                <input class="form-check-input"
                       :class="{'input-error': v$.deliveryMethod.$error}"
                       type="radio" name='delivery'
                       id="delivery"
                       v-bind:value='carrier.name'
                       v-model='validate.deliveryMethod'
                       @change="addDeliveryCost">
                <label class="form-check-label" for="delivery">{{ carrier.name }}</label>
              </div>
              <div class="col-5">{{carrier.price.toLocaleString().replace('.', ',')}} zł</div>
          </div>
          <span v-if="v$.deliveryMethod.$error" class="error-message">{{ v$.deliveryMethod.$errors[0].$message }}</span>
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
                <input class="form-check-input"
                       :class="{'input-error': v$.deliveryMethod.$error}"
                       type="checkbox" id="terms_accepted"
                       v-model="validate.validTermAccepted"
                       @change="agreeTerms">
              </div>
            </div>
            <div class="col-10">Etiam sit amet velit ullamcorper dui finibus ultrices porta at justo</div>
            <span v-if="v$.validTermAccepted.$error" class="error-message">You have to accept terms </span>
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
import {required, email, minLength, requiredIf} from "@vuelidate/validators";
import { useVuelidate } from "@vuelidate/core";
import { reactive, computed } from "vue";
import {isInvoiceChecked, isTermChecked} from "../data/validators";

export default {
  name: "Order",

  mounted() {
    this.displayInvoiceData()
  },

  data() {
    return {
      carriers: carriers,
      cart: Store.state,
      invoice: Store.state.invoice,
      deliveryCost: Store.state.deliveryCost,
      shippingData: Store.state.shippingData,
      termsAccepted: Store.state.termsAccepted,
      marketingAccepted: Store.state.marketingAccepted,
    }
  },
  setup() {
    const validate = reactive({
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
        firstName: { required, minLength: minLength(3) },
        lastName: { required, minLength: minLength(3) },
        companyName: { required: requiredIf(isInvoiceChecked)},
        nip: { required: requiredIf(isInvoiceChecked)},
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
        'invoice': document.querySelector("input[id=invoice]").checked,
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

    invoiceForm() {
      const companyData = document.getElementById('companyData')

      if (document.getElementById('invoice').checked) {
        companyData.style.display = 'block'
        Store.state.invoice = true
      } else {
        companyData.style.display = 'none'
        Store.state.invoice = false
      }
    },

    displayInvoiceData: function () {
      const companyData = document.getElementById('companyData')
      if (Store.state.invoice === true) {
        companyData.style.display = 'block';
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

.error-message {
  color: darkred;
}

.input-error{
  box-shadow: 0 0 0 1px darkred;
}

</style>