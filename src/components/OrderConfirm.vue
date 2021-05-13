<template>
    <div class="container">

      <div class="row justify-content-center py-4">
        <div class="col-8 text-center">
          <h5 class="font-weight-bold">Order summary</h5>
        </div>
      </div>

      <div class="row justify-content-center p-1 p-md-4">
        <div class="col-8 border rounded p-1 p-md-4">

          <div class="row justify-content-center justify-content-md-start p-4">
            <div class="col-sm col-md-4">To pay: </div>
            <div class="col-sm col-md-8"><span class="font-weight-bold">{{ (totalCost).toLocaleString().replace(',', ' ').replace('.', ',') }} zł</span></div>
          </div>

          <div class="row px-4">
            <div class="col-sm col-md-4">Delivery: </div>
            <div class="col-sm col-md-8">{{ deliveryMethod }}</div>
          </div>

          <hr />

          <div class="row p-4">
            <div class="col"><span class="font-weight-bold">Your Shipping Data</span> </div>
          </div>

          <div v-if="invoice">
            <div class="row px-4 py-1">
              <div class="col-sm col-md-4">Company Name:</div>
              <div class="col-sm col-md-8"> {{shippingData['companyName']}}</div>
            </div>

            <div class="row px-4 py-1">
              <div class="col-sm col-md-4">Nip Number:</div>
              <div class="col-sm col-md-8"> {{shippingData['nip']}}</div>
            </div>

          </div>

          <div class="row px-4 py-1">
            <div class="col-sm col-md-4">Name:</div>
            <div class="col-sm col-md-8"> {{shippingData['firstName']}} {{shippingData['lastName']}}</div>
          </div>

          <div class="row px-4 py-1">
            <div class="col-sm col-md-4">Email:</div>
            <div class="col-sm col-md-8"> {{shippingData['email']}}</div>
          </div>

          <div class="row px-4 py-1">
            <div class="col-sm col-md-4">Address:</div>
            <div class="col-sm col-md-8"> {{shippingData['street']}} {{shippingData['streetNumber']}}
              <span v-if="shippingData['apartmentNumber']">/{{shippingData['apartmentNumber']}}</span><br>
              {{shippingData['postalCode']}} {{shippingData['city']}}
            </div>
          </div>

          <div class="row px-4 py-1">
            <div class="col-sm col-md-4">Comments:</div>
            <div class="col-sm col-md-8">{{shippingData['comments']}}</div>
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
      totalCost: Store.state.totalCost,
      deliveryMethod: Store.state.deliveryMethod,
      invoice: Store.state.invoice,
    }
  },
}
</script>

<style scoped>

</style>