<template>
    <div class="container">

      <div class="row justify-content-center py-4">
        <div class="col-8 text-center">
          <h5 class="font-weight-bold">Order summary</h5>
        </div>
      </div>

      <div class="row justify-content-center p-4">
        <div class="col-8 border rounded p-4">

          <div class="row p-4">
            <div class="col-4">To pay: </div>
            <div class="col-8"><span class="font-weight-bold">Cost</span></div>
          </div>

          <div class="row px-4">
            <div class="col-4">Delivery: </div>
            <div class="col-8">Delivery</div>
          </div>

          <hr />

          <div class="row p-4">
            <div class="col"><span class="font-weight-bold">Your Shipping Data</span> </div>
          </div>

            <div v-for="entry in shippingData" :key="entry">
              <div v-if="entry.companyName" class="row px-4 py-1">
                <div class="col-4">Company Name:</div>
                <div class="col-8"> {{entry.companyName}}</div>
              </div>

              <div v-if="entry.nip" class="row px-4 py-1">
                <div class="col-4">Nip Number:</div>
                <div class="col-8"> {{entry.nip}}</div>
              </div>

              <div v-if="entry.firstName" class="row px-4 py-1">
                <div class="col-4">Name:</div>
                <div class="col-8"> {{entry.firstName}} {{entry.lastName}}</div>
              </div>

              <div class="row px-4 py-1">
                <div class="col-4">Email:</div>
                <div class="col-8"> {{entry.email}}</div>
              </div>

              <div class="row px-4 py-1">
                <div class="col-4">Address:</div>
                <div class="col-8"> {{entry.street}} {{entry.streetNumber}}
                  <span v-if="entry.apartmentNumber">/{{entry.apartmentNumber}}</span><br>
                  {{entry.postalCode}} {{entry.city}}
                </div>
              </div>

              <div class="row px-4 py-1">
                <div class="col-4">Comments:</div>
                <div class="col-8"> {{entry.comments}}</div>
              </div>

          </div>

          <div class="row p-4 justify-content-center">
            <button class="btn btn-success rounded btn-lg">Order and pay</button>
          </div>

        </div>
      </div>

  </div>
</template>

<script>
import {Store} from "../store/store";

export default {
  name: "OrderConfirm",
    data() {
    return {
      shippingData: Store.state.shippingData,
    }
  },
}
</script>

<style scoped>

</style>