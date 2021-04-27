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
    <div class="col-6 border rounded p-3">
      <div class="p-4">

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
                <input class="form-check-input" type="radio" name="delivery" id="delivery" value="carrier.value">
                <label class="form-check-label" for="delivery">{{ carrier.name }}</label>
              </div>
              <div class="col-5">{{carrier.price}} zł</div>
          </div>
        </div>
      </div>

      <div class="border rounded p-3">
        <h6 class="font-weight-bold">Order summary</h6>
      </div>

    </div>

  </div>

</div>
</template>

<script>
import carriers from "../data/delivery";

export default {
  name: "Order",

  data() {
    return {
      carriers: carriers,
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
    }
  }
}
</script>

<style scoped>

</style>